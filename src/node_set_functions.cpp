#include "node_set_functions.hpp"

// Hashing function for Node struct.
std::size_t NodeHash::operator()(const std::shared_ptr<const Node>& node) const {
    std::size_t hash = 0;
    std::size_t base = 1;
    for (unsigned int i = 0; i < 3; i++) {
        for (unsigned int j = 0; j < 3; j++) {
            hash += node->state[i][j] * base;
            base *= 9;
        }
    }
    return hash;
}

// Equality function for Node struct.
bool NodeEqual::operator()(const std::shared_ptr<const Node>& node1, const std::shared_ptr<const Node>& node2) const {
    return check_states_are_equivalent(node1->state, node2->state);
}

// Search for a node in an unordered set of shared_ptr<Node>.
const std::shared_ptr<const Node> node_set_search(const std::shared_ptr<const Node>& node,
                                                  const std::unordered_set<std::shared_ptr<const Node>, NodeHash, NodeEqual>& nodes_visited) {
    auto found_node = nodes_visited.find(node);
    if (found_node != nodes_visited.end()) {
        return *found_node;
    }
    return nullptr;
}