#pragma once

#include "eight_puzzle_node.hpp"

// Comparison Function for Node struct.
struct NodeCompare {
    bool operator()(const std::shared_ptr<const Node>& lhs, const std::shared_ptr<const Node>& rhs) const;
};