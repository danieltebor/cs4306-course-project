// Add Nilsson's sequence score heuristic
inline unsigned int calc_nilsson_sequence_score(const Node node) {
    const unsigned int x_clockwise_order[8] = {0, 1, 2, 2, 2, 1, 0, 0};
    const unsigned int y_clockwise_order[8] = {0, 0, 0, 1, 2, 2, 2, 0};
    unsigned int score = 0;

    // Add one to score if center not 0.
    if (node.state[1][1] != 0) {
        score++;
    }

    // Build state clockwise.
    unsigned int goal_state_clockwise[8];
    unsigned int node_state_clockwise[8];

    for (unsigned int i = 0; i < 8; i++) {
        goal_state_clockwise[i] = goal_state[y_clockwise_order[i]][x_clockwise_order[i]];
        node_state_clockwise[i] = node.state[y_clockwise_order[i]][x_clockwise_order[i]];
    }

    // Check if each tile clockwise matches 
    for (unsigned int i = 0; i < 7; i++) {
        if (node_state_clockwise[i] != goal_state_clockwise[i]) {
            score += 2;
        }
    }

    return score * 3;
}

// Calculates a heuristic value by finding the 
// Manhatten distance of a tile from its position in the goal state.
inline unsigned int calc_manhatten_distance(unsigned int tile_value, unsigned int x, unsigned int y) {
    unsigned int goal_x, goal_y;

    // Find goal position of tile.
    for (unsigned int y = 0; y < 3; y++) {
        for (unsigned int x = 0; x < 3; x++) {
            if (goal_state[y][x] == tile_value) {
                goal_x = x;
                goal_y = y;
            }
        }
    }

    // Calculate manhatten distance.
    unsigned int x_diff = (goal_x > x) ? goal_x - x : x - goal_x;
    unsigned int y_diff = (goal_y > y) ? goal_y - y : y - goal_y;
    return x_diff + y_diff;
}

// Calculates a heuristic value by calculating the sum of
// the Manhatten distances of all tiles in the state compared to the goal.
inline unsigned int calc_summed_manhatten_distances(const Node node) {
    unsigned int total_distances = 0;

    // Traverse state.
    for (unsigned int y = 0; y < 3; y++) {
        for (unsigned int x = 0; x < 3; x++) {
            unsigned int tile_value = node.state[y][x];
            if (tile_value != 0) {
                total_distances += calc_manhatten_distance(tile_value, x, y);
            }
        }
    }

    return total_distances;
}

// Return all possible children of a node, rejecting nodes with a previously visited state.
template <typename SetType>
std::vector<std::shared_ptr<const Node>> extend_node(const std::shared_ptr<const Node>& node,
                                                     const SetType& nodes_visited,
                                                     bool should_use_heuristic) {
    // Find blank tile.
    unsigned int blank_x = 0, blank_y = 0;
    bool blank_tile_found = false;

    for (unsigned int y = 0; y < 3; y++) {
        for (unsigned int x = 0; x < 3; x++) {
            if (node->state[y][x] == 0) {
                blank_x = x;
                blank_y = y;
                blank_tile_found = true;
                break;
            }
        }

        if (blank_tile_found) {
            break;
        }
    }

    std::vector<std::shared_ptr<const Node>> child_nodes;
    child_nodes.reserve(4);

    for (unsigned int i = 0; i < 4; i++) {
        // Dynamically allocate using shared_ptrs so that node persists outside of function scope.
        const std::shared_ptr<Node> child_node = std::make_shared<Node>();
        // Copy state into child_node's state.
        for (unsigned int y = 0; y < 3; y++) {
            for (unsigned int x = 0; x < 3; x++) {
                child_node->state[y][x] = node->state[y][x];
            }
        }
        
        if (i == 0 && blank_x > 0) {
            // Swap blank tile with tile to the left of it.
            unsigned int left_tile = child_node->state[blank_y][blank_x - 1];
            child_node->state[blank_y][blank_x - 1] = 0;
            child_node->state[blank_y][blank_x] = left_tile;
        }
        else if (i == 1 && blank_y < 2) {
            // Swap blank tile with tile below it.
            unsigned int below_tile = child_node->state[blank_y + 1][blank_x];
            child_node->state[blank_y + 1][blank_x] = 0;
            child_node->state[blank_y][blank_x] = below_tile;
        }
        else if (i == 2 && blank_x < 2) {
            // Swap blank tile with tile to the right of it.
            unsigned int right_tile = child_node->state[blank_y][blank_x + 1];
            child_node->state[blank_y][blank_x + 1] = 0;
            child_node->state[blank_y][blank_x] = right_tile;
        }
        else if (i == 3 && blank_y > 0) {
            // Swap blank tile with tile above it.
            unsigned int above_tile = child_node->state[blank_y - 1][blank_x];
            child_node->state[blank_y - 1][blank_x] = 0;
            child_node->state[blank_y][blank_x] = above_tile;
        }
        else {
            continue;
        }

        // Populate blank fields in child_node.
        child_node->parent = node;
        child_node->depth = node->depth + 1;
        child_node->heuristic = should_use_heuristic
            ? calc_nilsson_sequence_score(*child_node) + calc_summed_manhatten_distances(*child_node)
            : 0;

        // Add child_node to child_nodes if it's state does not already exist.
        if (node_set_search(child_node, nodes_visited) == NULL) {
            child_nodes.emplace_back(std::const_pointer_cast<const Node>(child_node));
        }
    }

    return child_nodes;
}