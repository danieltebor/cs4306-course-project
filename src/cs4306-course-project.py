import cppyy
import matplotlib.pyplot as plt

# Load libcs4306-course-project.dll
cppyy.include('./src/eight_puzzle_node.hpp')
cppyy.include('./src/eight_puzzle.hpp')
cppyy.include('./src/search_alg.hpp')
lib = cppyy.load_library('./lib/libcs4306-course-project.dll')

num_times_to_run = 100

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
    
fig, axises = plt.subplots()

axises.plot(a_star_num_nodes_visited_results, a_star_time_taken_ms_results, label='A*')
axises.plot(bfs_nodes_visited_results, bfs_time_taken_ms_results, label='BFS')
axises.plot(multithreaded_bfs_nodes_visited_results, multithreaded_bfs_time_taken_ms_results, label='Multithreaded BFS')

axises.set_xlabel('Number of Nodes Visited')
axises.set_ylabel('Time Taken (ms)')

axises.set_title('Number of Nodes Visited vs Time Taken')

axises.legend()

axises.text('')