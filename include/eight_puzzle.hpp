#pragma once

#include <memory>
#include <unordered_set>
#include <vector>

#include "eight_puzzle_node.hpp"
#include "node_set_functions.hpp"

// The max number of nodes is 9! since the state is a 3x3 grid with 9 tiles.
#define MAX_NODES 362880

// Goal state.
extern const unsigned int goal_state[3][3];

// Generate a node with a random starting state.
const Node generate_random_start_node();

// Return all possible children of a node, rejecting nodes with a previously visited state.
std::vector<std::shared_ptr<const Node>> extend_node(const std::shared_ptr<const Node>& node,
                                                     const std::unordered_set<std::shared_ptr<const Node>, NodeHash, NodeEqual>& nodes_visited,
                                                     bool should_use_heuristic);