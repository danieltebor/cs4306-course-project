#include <iostream>
#include <atomic>
#include <chrono>
#include <deque>
#include <memory>
#include <mutex>
#include <queue>
#include <stack>
#include <thread>
#include <unordered_set>

#include "eight_puzzle.hpp"
#include "node_set_functions.hpp"
#include "priority_queue_functions.hpp"
#include "search_alg.hpp"

// Each search algorithm populates a SearchResult struct.
void populate_search_result(SearchResult& result,
                            const unsigned int num_nodes_visited,
                            const long long time_taken_ms,
                            const std::shared_ptr<const Node>& goal_node) {
    result.num_nodes_visited = num_nodes_visited;
    result.time_taken_ms = time_taken_ms;

    // Check if goal reached.
    if (goal_node == nullptr) {
        return;
    }

    // Trace back from goal node to start node to get the path.
    std::shared_ptr<const Node> current_node = goal_node;
    while (current_node != nullptr) {
        // Copy node into path to goal vector.
        result.path_to_goal.push_back(*current_node);
        // Move to parent.
        current_node = current_node->parent;
    }
}

SearchResult breadth_first_search(const Node start_node) {
    // Record start time for algorithm execution.
    auto start_time = std::chrono::high_resolution_clock::now();

    std::deque<std::shared_ptr<const Node>> nodes_to_visit;
    std::unordered_set<std::shared_ptr<const Node>, NodeHash, NodeEqual> nodes_visited(MAX_NODES / 10, NodeHash(), NodeEqual());
    std::shared_ptr<const Node> goal_node;

    // Enqueue start node.
    nodes_to_visit.push_back(std::make_shared<const Node>(start_node));
    
    // Visit every node in the queue. When a node is extended in the loop,
    // the children are enqueued. This causes the nodes to be visited in a BFS order.
    while (!nodes_to_visit.empty()) {
        const std::shared_ptr<const Node> current_node = nodes_to_visit.front();
        nodes_to_visit.pop_front();
        
        nodes_visited.insert(current_node);

        // Check if current node is the goal state.
        if (check_states_are_equivalent(current_node->state, goal_state)) {
            goal_node = current_node;
            break;
        }
        
        // Extend current node and enqueue children.
        // 3rd parameter is false as a heuristic is not used in BFS.
        std::vector<std::shared_ptr<const Node>> child_nodes = extend_node(
                current_node,
                nodes_visited,
                false
            );
        
        // Enqueue children nodes.
        for (const auto& child_node : child_nodes) {
            nodes_to_visit.push_back(child_node);
        }
    }

    // Record end time for algorithm execution.
    auto end_time = std::chrono::high_resolution_clock::now();
    // Calculate time taken in milliseconds.
    auto cpu_time_taken_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    // Fill out fields in the SearchResult struct.
    
    SearchResult result;
    populate_search_result(result, nodes_visited.size(), cpu_time_taken_ms, goal_node);
    return result;
}

SearchResult multithreaded_breadth_first_search(const Node start_node) {
    // Record start time for algorithm execution.
    auto start_time = std::chrono::high_resolution_clock::now();

    std::deque<std::shared_ptr<const Node>> nodes_to_visit;
    std::unordered_set<std::shared_ptr<const Node>, NodeHash, NodeEqual> nodes_visited(MAX_NODES / 10, NodeHash(), NodeEqual());
    std::shared_ptr<const Node> goal_node;

    // Enqueue start node.
    nodes_to_visit.push_back(std::make_shared<const Node>(start_node));

    // Visit every node in the queue. When a node is extended in the loop,
    // the children are enqueued. Once the number of nodes_to_visit becomes
    // >= to the number of available cpu threads, break.
    while (!nodes_to_visit.size() < std::thread::hardware_concurrency()) {
        const std::shared_ptr<const Node> current_node = nodes_to_visit.front();
        nodes_to_visit.pop_front();
        nodes_visited.insert(current_node);

        // Check if current node is the goal state.
        if (check_states_are_equivalent(current_node->state, goal_state)) {
            goal_node = current_node;
            break;
        }
        
        // Extend current node and enqueue children.
        // 3rd parameter is false as a heuristic is not used in BFS.
        std::vector<std::shared_ptr<const Node>> child_nodes = extend_node(
                current_node,
                nodes_visited,
                false
            );

        // Enqueue children nodes.
        for (const auto& child_node : child_nodes) {
            nodes_to_visit.push_back(child_node);
        }
    }

    // If goal has not been found yet, continue to multithreaded section.
    if (goal_node == nullptr) {
        // Distrubute nodes_to_visit into multiple queues.
        std::vector<std::deque<std::shared_ptr<const Node>>> nodes_to_visit_queues(std::thread::hardware_concurrency());
        for (int i = 0; i < nodes_to_visit.size(); i++) {
            nodes_to_visit_queues[i % nodes_to_visit_queues.size()].push_back(nodes_to_visit[i]);
        }

        // Create threads to visit nodes.
        std::vector<std::thread> threads;
        threads.reserve(nodes_to_visit_queues.size());

        std::mutex nodes_visited_mutex;
        std::mutex goal_node_mutex;
        std::atomic<bool> goal_is_found(false);

        // Create a new thread for each queue of nodes that need to be visited.
        for (auto& queue : nodes_to_visit_queues) {
            threads.push_back(std::thread([&queue, &nodes_visited, &goal_node, &nodes_visited_mutex, &goal_node_mutex, &goal_is_found] {
                std::deque<std::shared_ptr<const Node>> nodes_to_visit(queue);

                // Visit every node in the queue. When a node is extended in the loop,
                // the children are enqueued. This causes the nodes to be visited in an asyncronous BFS order.
                while (!nodes_to_visit.empty() && !goal_is_found) {
                    const std::shared_ptr<const Node> current_node = nodes_to_visit.front();
                    nodes_to_visit.pop_front();

                    {
                        // Lock nodes_visited to ensure thread safety.
                        std::lock_guard<std::mutex> lock(nodes_visited_mutex);
                        nodes_visited.insert(current_node);
                    }

                    // Check if current node is the goal state.
                    if (check_states_are_equivalent(current_node->state, goal_state)) {
                        {
                            // Lock goal_node to ensure thread safety.
                            std::lock_guard<std::mutex> lock(goal_node_mutex);
                            goal_node = current_node;
                            goal_is_found = true;
                        }
                    }

                    // Extend current node and enqueue children.
                    // 3rd parameter is false as a heuristic is not used in BFS.
                    std::vector<std::shared_ptr<const Node>> child_nodes = extend_node(
                            current_node,
                            nodes_visited,
                            false
                        );

                    // Enqueue children nodes.
                    for (const auto& child_node : child_nodes) {
                        nodes_to_visit.push_back(child_node);
                    }
                }
            }));
        }

        // Start the threads.
        std::cout << "num threads: " << threads.size() << std::endl;
        for (auto& thread : threads) {
            thread.join();
        }
    }

    // Record end time for algorithm execution.
    auto end_time = std::chrono::high_resolution_clock::now();
    // Calculate time taken in milliseconds.
    auto cpu_time_taken_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    // Fill out fields in the SearchResult struct.
    SearchResult result;
    populate_search_result(result, nodes_visited.size(), cpu_time_taken_ms, goal_node);
    return result;
}

SearchResult a_star_search(const Node start_node) {
    // Record start time for algorithm execution.
    auto start_time = std::chrono::high_resolution_clock::now();
    
    std::priority_queue<std::shared_ptr<const Node>, std::vector<std::shared_ptr<const Node>>, NodeCompare> nodes_to_visit;
    std::unordered_set<std::shared_ptr<const Node>, NodeHash, NodeEqual> nodes_visited(MAX_NODES / 10, NodeHash(), NodeEqual());
    std::shared_ptr<const Node> goal_node;

    // Enqueue start node.
    nodes_to_visit.push(std::make_shared<const Node>(start_node));
    
    // Visit every node in the priority queue. When a node is extended in the loop,
    // the children are enqued and internally sorted so that those with the lowest
    // depth + heuristic value come first. This causes the nodes to be visited in a A* order.
    while (!nodes_to_visit.empty()) {
        const std::shared_ptr<const Node> current_node = nodes_to_visit.top();
        nodes_to_visit.pop();
        nodes_visited.insert(current_node);

        // Check if current node is the goal state.
        if (check_states_are_equivalent(current_node->state, goal_state)) {
            goal_node = current_node;
            break;
        }
        
        // Extend current node and enqueue children.
        // 3rd parameter is true as a heuristic is used in A*.
        std::vector<std::shared_ptr<const Node>> child_nodes = extend_node(
                current_node,
                nodes_visited,
                true
            );

        // Enqueue children nodes.
        for (const auto& child_node : child_nodes) {
            nodes_to_visit.push(child_node);
        }
    }

    // Record end time for algorithm execution.
    auto end_time = std::chrono::high_resolution_clock::now();
    // Calculate time taken in milliseconds.
    auto cpu_time_taken_ms = std::chrono::duration_cast<std::chrono::milliseconds>(end_time - start_time).count();

    // Fill out fields in the SearchResult struct.
    SearchResult result;
    populate_search_result(result, nodes_visited.size(), cpu_time_taken_ms, goal_node);
    return result;
}