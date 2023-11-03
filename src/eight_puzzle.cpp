#include <cstdlib>
#include <limits>

#include "eight_puzzle.hpp"
#include "node_set_functions.hpp"

// Goal state.
const unsigned int goal_state[3][3] = {
    {1, 2, 3},
    {8, 0, 4},
    {7, 6, 5}
};

// Generate a node with a random starting state.
const Node generate_random_start_node() {
    Node node;
    
    // Copy goal state into node.
    unsigned int blank_x, blank_y;
    for (int y = 0; y < 3; y++) {
        for (int x = 0; x < 3; x++) {
            node.state[y][x] = goal_state[y][x];
            if (node.state[y][x] == 0) {
                blank_x = x;
                blank_y = y;
            }
        }
    }

    srand(time(NULL));

    // Randomly scramble the state. This garuntees the state can be solved.
    for (unsigned int i = 0; i < 1000000; i++) {
        // Generate a random move 0-3.
        unsigned int move = rand() % 4;

        if (move == 0 && blank_x > 0) {
            // Swap blank tile with tile to the left of it.
            unsigned int left_tile = node.state[blank_y][blank_x - 1];
            node.state[blank_y][blank_x - 1] = 0;
            node.state[blank_y][blank_x] = left_tile;
            blank_x--;
        }
        else if (move == 1 && blank_y < 2) {
            // Swap blank tile with tile below it.
            unsigned int below_tile = node.state[blank_y + 1][blank_x];
            node.state[blank_y + 1][blank_x] = 0;
            node.state[blank_y][blank_x] = below_tile;
            blank_y++;
        }
        else if (move == 2 && blank_x < 2) {
            // Swap blank tile with tile to the right of it.
            unsigned int right_tile = node.state[blank_y][blank_x + 1];
            node.state[blank_y][blank_x + 1] = 0;
            node.state[blank_y][blank_x] = right_tile;
            blank_x++;
        }
        else if (move == 3 && blank_y > 0) {
            // Swap blank tile with tile above it.
            unsigned int above_tile = node.state[blank_y - 1][blank_x];
            node.state[blank_y - 1][blank_x] = 0;
            node.state[blank_y][blank_x] = above_tile;
            blank_y--;
        }
        else {
            i--;
        }
    }

    // Populate rest of node.
    node.depth = 0;
    node.heuristic = std::numeric_limits<unsigned int>::max();

    return (const Node) node;
}