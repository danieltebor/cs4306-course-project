import cppyy
import matplotlib.pyplot as plt
import numpy as np

# Load libcs4306-course-project.dll
cppyy.include('./src/eight_puzzle_node.hpp')
cppyy.include('./src/eight_puzzle.hpp')
cppyy.include('./src/search_alg.hpp')
lib = cppyy.load_library('./lib/libcs4306-course-project.dll')

num_times_to_run = 10

a_star_num_moves_to_goal_avg = 0
a_star_num_nodes_visited_results = []
a_star_time_taken_ms_results = []

bfs_num_moves_to_goal_avg = 0
bfs_nodes_visited_results = []
bfs_time_taken_ms_results = []

multithreaded_bfs_num_moves_to_goal_avg = 0
multithreaded_bfs_nodes_visited_results = []
multithreaded_bfs_time_taken_ms_results = []

print(f'Running algs {num_times_to_run} times')
for i in range(0, num_times_to_run):
    print(f'Running {i} of {num_times_to_run} times')
    
    node = cppyy.gbl.generate_random_start_node()
    
    a_star_result = cppyy.gbl.a_star_search(node)
    a_star_num_moves_to_goal_avg += (a_star_result.path_to_goal.size() - a_star_num_moves_to_goal_avg) / (i + 1)
    a_star_num_nodes_visited_results.append(a_star_result.num_nodes_visited)
    a_star_time_taken_ms_results.append(a_star_result.time_taken_ms)

    bfs_result = cppyy.gbl.breadth_first_search(node)
    bfs_num_moves_to_goal_avg += (bfs_result.path_to_goal.size() - bfs_num_moves_to_goal_avg) / (i + 1)
    bfs_nodes_visited_results.append(bfs_result.num_nodes_visited)
    bfs_time_taken_ms_results.append(bfs_result.time_taken_ms)

    multithreaded_bfs_result = cppyy.gbl.multithreaded_breadth_first_search(node)
    multithreaded_bfs_num_moves_to_goal_avg += (multithreaded_bfs_result.path_to_goal.size() - multithreaded_bfs_num_moves_to_goal_avg) / (i + 1)
    multithreaded_bfs_nodes_visited_results.append(multithreaded_bfs_result.num_nodes_visited)
    multithreaded_bfs_time_taken_ms_results.append(multithreaded_bfs_result.time_taken_ms)
    
plt.plot(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, 'o', label='A*')
plt.plot(bfs_nodes_visited_results, bfs_time_taken_ms_results, 'o', label='BFS')
plt.plot(multithreaded_bfs_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, 'o', label='Multithreaded BFS')

plt.xlabel('Number of Nodes Visited')
plt.ylabel('Time Taken (ms)')

plt.title('Number of Nodes Visited vs Time Taken')

plt.legend()

a_star_slope, a_star_intercept = np.polyfit(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, 1)
a_star_line_of_best_fit = a_star_slope * np.array(a_star_num_nodes_visited_results) + a_star_intercept
plt.plot(a_star_num_nodes_visited_results, a_star_line_of_best_fit, '-', label='A*')

bfs_slope, bfs_intercept = np.polyfit(bfs_nodes_visited_results, bfs_time_taken_ms_results, 1)
bfs_line_of_best_fit = bfs_slope * np.array(bfs_nodes_visited_results) + bfs_intercept
plt.plot(bfs_nodes_visited_results, bfs_line_of_best_fit, '-', label='BFS')

multithreaded_bfs_slope, multithreaded_bfs_intercept = np.polyfit(multithreaded_bfs_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, 1)
multithreaded_bfs_line_of_best_fit = multithreaded_bfs_slope * np.array(multithreaded_bfs_nodes_visited_results) + multithreaded_bfs_intercept
plt.plot(multithreaded_bfs_nodes_visited_results, multithreaded_bfs_line_of_best_fit, '-', label='Multithreaded BFS')

plt.figtext(0.0, -0.0, f'Avg Moves to Goal (A*): {(int)(a_star_num_moves_to_goal_avg + 0.5)}')
plt.figtext(0.0, -0.1, f'Avg Moves to Goal (BFS): {(int)(bfs_num_moves_to_goal_avg + 0.5)}')
plt.figtext(0.0, -0.2, f'Avg Moves to Goal (Multithreaded BFS): {(int)(multithreaded_bfs_num_moves_to_goal_avg + 0.5)}')

plt.show()