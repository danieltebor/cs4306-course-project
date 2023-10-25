#pragma once

#include <vector>

#include "eight_puzzle_node.hpp"

typedef struct {
    std::vector<Node> path_to_goal;
    unsigned int num_nodes_visited;
    long long time_taken_ms;
} SearchResult;

// Frees a SearchResult from memory.
SearchResult breadth_first_search(const Node start_node);
SearchResult multithreaded_breadth_first_search(const Node start_node);
SearchResult a_star_search(const Node start_node);