#pragma once

#include <memory>
#include <unordered_set>

#include "eight_puzzle_node.hpp"

// Hashing function for Node struct.
struct NodeHash {
    std::size_t operator()(const std::shared_ptr<const Node>& node) const;
};

// Equality function for Node struct.
struct NodeEqual {
    bool operator()(const std::shared_ptr<const Node>& node1, const std::shared_ptr<const Node>& node2) const;
};

// Search for a node in an unordered set of shared_ptr<Node>.
template <typename SetType>
const std::shared_ptr<const Node> node_set_search(const std::shared_ptr<const Node>& node,
                                                  const SetType& nodes_visited);

#include "node_set_functions.tpp"