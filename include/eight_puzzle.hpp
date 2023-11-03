#pragma once

#include <memory>
#include <vector>

#include "eight_puzzle_node.hpp"
#include "node_set_functions.hpp"

// The max number of nodes is 9! / 2 since the state is a 3x3 grid with 9 tiles 
// but only half of the states are reachable given any start node.
#define MAX_NODES 181440

// Goal state.
extern const unsigned int goal_state[3][3];

// Generate a node with a random starting state.
const Node generate_random_start_node();

// Return all possible children of a node, rejecting nodes with a previously visited state.
template <typename SetType>
std::vector<std::shared_ptr<const Node>> extend_node(const std::shared_ptr<const Node>& node,
                                                     const SetType& nodes_visited,
                                                     bool should_use_heuristic);

#include "eight_puzzle.tpp"