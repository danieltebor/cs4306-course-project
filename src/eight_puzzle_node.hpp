#pragma once

#include <memory>

// Struct to represent a node in the search tree.
typedef struct Node Node;

struct Node {
    std::shared_ptr<const Node> parent = nullptr; // Pointer to parent node
    unsigned int state[3][3]; // Board state
    unsigned int depth; // Depth of node in search tree
    unsigned int heuristic; // Heuristic value of node
};

// Checks if two nodes are equivalent.
bool check_states_are_equivalent(const unsigned int state1[3][3], const unsigned int state2[3][3]);