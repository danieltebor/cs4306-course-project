// Search for a node in an unordered set of shared_ptr<Node>.
template <typename SetType>
const std::shared_ptr<const Node> node_set_search(const std::shared_ptr<const Node>& node,
                                                  const SetType& nodes_visited) {
    auto found_node = nodes_visited.find(node);
    if (found_node != nodes_visited.end()) {
        return *found_node;
    }
    return nullptr;
}