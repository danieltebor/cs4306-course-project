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