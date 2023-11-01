import os

import cppyy
import matplotlib.pyplot as plt
import numpy as np

# Load lib_eight_puzzle_solver.dll
cppyy.include('./include/eight_puzzle_solver_includes.hpp')
lib = cppyy.load_library('./lib/lib_eight_puzzle_solver.dll')

num_times_to_run = 0
while True:
    num_times_to_run = input('Enter a number of times to run the algorithms: ')
    try:
        num_times_to_run = int(num_times_to_run)
        break
    except:
        print('Invalid input. Please enter an integer.')

a_star_num_moves_to_goal_results = []
a_star_num_nodes_visited_results = []
a_star_time_taken_ms_results = []

bfs_num_moves_to_goal_results = []
bfs_num_nodes_visited_results = []
bfs_time_taken_ms_results = []

multithreaded_bfs_num_moves_to_goal_results= []
multithreaded_bfs_num_nodes_visited_results = []
multithreaded_bfs_time_taken_ms_results = []

# Run the algorithms and collect results
print(f'Running algs {num_times_to_run} times')
for i in range(0, num_times_to_run):
    print(f'Running {i + 1} of {num_times_to_run} times')
    
    node = cppyy.gbl.generate_random_start_node()
    
    a_star_result = cppyy.gbl.a_star_search(node)
    a_star_num_moves_to_goal_results.append(a_star_result.path_to_goal.size())
    a_star_num_nodes_visited_results.append(a_star_result.num_nodes_visited)
    a_star_time_taken_ms_results.append(a_star_result.time_taken_ms)

    bfs_result = cppyy.gbl.breadth_first_search(node)
    bfs_num_moves_to_goal_results.append(bfs_result.path_to_goal.size())
    bfs_num_nodes_visited_results.append(bfs_result.num_nodes_visited)
    bfs_time_taken_ms_results.append(bfs_result.time_taken_ms)

    multithreaded_bfs_result = cppyy.gbl.multithreaded_breadth_first_search(node)
    multithreaded_bfs_num_moves_to_goal_results.append(multithreaded_bfs_result.path_to_goal.size())
    multithreaded_bfs_num_nodes_visited_results.append(multithreaded_bfs_result.num_nodes_visited)
    multithreaded_bfs_time_taken_ms_results.append(multithreaded_bfs_result.time_taken_ms)

os.makedirs('./out/figs', exist_ok=True)

# Plot Nodes Visited vs Runtime (ms).
plt.title('Nodes Visited vs Runtime (ms)')
plt.xlabel('Nodes Visited')
plt.ylabel('Runtime (ms)')

plt.plot(multithreaded_bfs_num_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, 's', label='Multithreaded BFS', color='green', markersize=3, alpha=0.33)
plt.plot(bfs_num_nodes_visited_results, bfs_time_taken_ms_results, 'o', label='BFS', color='red', markersize=3, alpha=0.33)
plt.plot(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, '^', label='A*', color='blue', markersize=3, alpha=0.33)

plt.legend()

plt.savefig('./out/figs/nodes-visited-vs-runtime.png')
plt.show()


# Plot Moves to Goal vs Nodes Visited.
plt.title('Moves to Goal vs Nodes Visited')
plt.xlabel('Moves to Goal')
plt.ylabel('Nodes Visited')

plt.plot(multithreaded_bfs_num_moves_to_goal_results, multithreaded_bfs_num_nodes_visited_results, 's', label='Multithreaded BFS', color='green', markersize=3, alpha=0.33)
plt.plot(bfs_num_moves_to_goal_results, bfs_num_nodes_visited_results, 'o', label='BFS', color='red', markersize=3, alpha=0.33)
plt.plot(a_star_num_moves_to_goal_results, a_star_num_nodes_visited_results, '^', label='A*', color='blue', markersize=3, alpha=0.33)

plt.legend()

plt.subplots_adjust(left=0.15)

plt.savefig('./out/figs/moves-to-goal-vs-nodes-visited.png')
plt.show()


# Plot Moves to Goal vs Runtime (ms).
plt.title('Moves to Goal vs Runtime (ms)')
plt.xlabel('Moves to Goal')
plt.ylabel('Runtime (ms)')

plt.plot(multithreaded_bfs_num_moves_to_goal_results, multithreaded_bfs_time_taken_ms_results, 's', label='Multithreaded BFS', color='green', markersize=3, alpha=0.33)
plt.plot(bfs_num_moves_to_goal_results, bfs_time_taken_ms_results, 'o', label='BFS', color='red', markersize=3, alpha=0.33)
plt.plot(a_star_num_moves_to_goal_results, a_star_time_taken_ms_results, '^', label='A*', color='blue', markersize=3, alpha=0.33)

plt.legend()

plt.savefig('./out/figs/moves-to-goal-vs-runtime.png')
plt.show()


# Plot Avg Number of Moves to Goal.
plt.title('Avg Number of Moves to Goal (Lower is Better)')

labels = ['A*', 'BFS', 'Multithreaded BFS']
colors = ['blue', 'red', 'green']
x_pos = np.arange(len(labels))
num_moves_avgs = [
    np.average(a_star_num_moves_to_goal_results),
    np.average(bfs_num_moves_to_goal_results),
    np.average(multithreaded_bfs_num_moves_to_goal_results),
]

plt.bar(x_pos, num_moves_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Moves to Goal')

plt.savefig('./out/figs/avg-moves-to-goal.png')
plt.show()


# Plot Avg Number of Nodes Visited.
plt.title('Avg Number of Nodes Visited (Lower is Better)')

num_nodes_visited_avgs = [
    np.average(a_star_num_nodes_visited_results),
    np.average(bfs_num_nodes_visited_results),
    np.average(multithreaded_bfs_num_nodes_visited_results),
]

plt.bar(x_pos, num_nodes_visited_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Nodes Visited')
plt.subplots_adjust(left=0.15)

plt.savefig('./out/figs/avg-num-nodes-visited.png')
plt.show()


# Plot Avg Runtime (ms).
plt.title('Avg Runtime (ms) (Lower is Better)')

time_taken_avgs = [
    np.average(a_star_time_taken_ms_results),
    np.average(bfs_time_taken_ms_results),
    np.average(multithreaded_bfs_time_taken_ms_results),
]

plt.bar(x_pos, time_taken_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Runtime (ms)')

plt.savefig('./out/figs/avg-runtime.png')
plt.show()