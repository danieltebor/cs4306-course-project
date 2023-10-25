import cppyy
import matplotlib.pyplot as plt
import numpy as np

# Load libcs4306-course-project.dll
cppyy.include('./include/eight_puzzle_node.hpp')
cppyy.include('./include/eight_puzzle.hpp')
cppyy.include('./include/search_alg.hpp')
lib = cppyy.load_library('./lib/libcs4306-course-project.dll')

num_times_to_run = 100000

a_star_num_moves_to_goal_avg = 0
a_star_num_nodes_visited_results = []
a_star_time_taken_ms_results = []

bfs_num_moves_to_goal_avg = 0
bfs_num_nodes_visited_results = []
bfs_time_taken_ms_results = []

multithreaded_bfs_num_moves_to_goal_avg = 0
multithreaded_bfs_num_nodes_visited_results = []
multithreaded_bfs_time_taken_ms_results = []

print(f'Running algs {num_times_to_run} times')
for i in range(0, num_times_to_run):
    print(f'Running {i + 1} of {num_times_to_run} times')
    
    node = cppyy.gbl.generate_random_start_node()
    
    a_star_result = cppyy.gbl.a_star_search(node)
    a_star_num_moves_to_goal_avg += (a_star_result.path_to_goal.size() - a_star_num_moves_to_goal_avg) / (i + 1)
    a_star_num_nodes_visited_results.append(a_star_result.num_nodes_visited)
    a_star_time_taken_ms_results.append(a_star_result.time_taken_ms)

    bfs_result = cppyy.gbl.breadth_first_search(node)
    bfs_num_moves_to_goal_avg += (bfs_result.path_to_goal.size() - bfs_num_moves_to_goal_avg) / (i + 1)
    bfs_num_nodes_visited_results.append(bfs_result.num_nodes_visited)
    bfs_time_taken_ms_results.append(bfs_result.time_taken_ms)

    multithreaded_bfs_result = cppyy.gbl.multithreaded_breadth_first_search(node)
    multithreaded_bfs_num_moves_to_goal_avg += (multithreaded_bfs_result.path_to_goal.size() - multithreaded_bfs_num_moves_to_goal_avg) / (i + 1)
    multithreaded_bfs_num_nodes_visited_results.append(multithreaded_bfs_result.num_nodes_visited)
    multithreaded_bfs_time_taken_ms_results.append(multithreaded_bfs_result.time_taken_ms)

plt.title('Nodes Visited vs Runtime (ms)')
plt.xlabel('Nodes Visited')
plt.ylabel('Runtime (ms)')

plt.plot(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, 'o', label='A*', color='blue', markersize=5)
plt.plot(bfs_num_nodes_visited_results, bfs_time_taken_ms_results, 'o', label='BFS', color='red', markersize=5)
plt.plot(multithreaded_bfs_num_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, 'o', label='Multithreaded BFS', color='green', markersize=5)

plt.legend()

a_star_slope, a_star_intercept = np.polyfit(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, 1)
a_star_line_of_best_fit = a_star_slope * np.array(a_star_num_nodes_visited_results) + a_star_intercept
plt.plot(a_star_num_nodes_visited_results, a_star_line_of_best_fit, '-', label='A*', color='blue')

bfs_slope, bfs_intercept = np.polyfit(bfs_num_nodes_visited_results, bfs_time_taken_ms_results, 1)
bfs_line_of_best_fit = bfs_slope * np.array(bfs_num_nodes_visited_results) + bfs_intercept
plt.plot(bfs_num_nodes_visited_results, bfs_line_of_best_fit, '-', label='BFS', color='red')

multithreaded_bfs_slope, multithreaded_bfs_intercept = np.polyfit(multithreaded_bfs_num_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, 1)
multithreaded_bfs_line_of_best_fit = multithreaded_bfs_slope * np.array(multithreaded_bfs_num_nodes_visited_results) + multithreaded_bfs_intercept
plt.plot(multithreaded_bfs_num_nodes_visited_results, multithreaded_bfs_line_of_best_fit, '-', label='Multithreaded BFS', color='green')

plt.savefig('./out/figs/nodes-visited-vs-runtime.png')
plt.show()


plt.title('Avg Number of Moves to Goal (Lower is Better)')

labels = ['A*', 'BFS', 'Multithreaded BFS']
colors = ['blue', 'red', 'green']
x_pos = np.arange(len(labels))
num_moves_avgs = [
    a_star_num_moves_to_goal_avg,
    bfs_num_moves_to_goal_avg,
    multithreaded_bfs_num_moves_to_goal_avg,
]

plt.bar(x_pos, num_moves_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Moves to Goal')

plt.savefig('./out/figs/avg-moves-to-goal.png')
plt.show()


plt.title('Avg Number of Nodes Visited (Lower is Better)')

num_nodes_visited_avgs = [
    np.average(a_star_num_nodes_visited_results),
    np.average(bfs_num_nodes_visited_results),
    np.average(multithreaded_bfs_num_nodes_visited_results),
]

plt.bar(x_pos, num_nodes_visited_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Nodes Visited')

plt.savefig('./out/figs/avg-num-nodes-visited.png')
plt.show()


plt.title('Avg Runtime (ms) (Lower is Better)')

time_taken_avgs = [
    np.average(a_star_time_taken_ms_results),
    np.average(bfs_time_taken_ms_results),
    np.average(multithreaded_bfs_time_taken_ms_results),
]

plt.bar(x_pos, time_taken_avgs, align='center', alpha=0.5, color=colors)
plt.xticks(x_pos, labels)
plt.ylabel('Runtime (ms)')

plt.savefig('./out/figs/avg-runtime-ms.png')
plt.show()