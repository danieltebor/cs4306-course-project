#include "priority_queue_functions.hpp"

// Comparison Function for Node struct.
bool NodeCompare::operator()(const std::shared_ptr<const Node>& lhs, const std::shared_ptr<const Node>& rhs) const {
    return (lhs->heuristic + lhs->depth) > (rhs->heuristic + rhs->depth);
}