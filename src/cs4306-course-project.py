import cppyy

# Load libcs4306-course-project.dll
cppyy.include('./src/eight_puzzle_node.hpp')
cppyy.include('./src/eight_puzzle.hpp')
cppyy.include('./src/search_alg.hpp')
lib = cppyy.load_library('./lib/libcs4306-course-project.dll')

node = cppyy.gbl.generate_random_start_node()

result_a_star_search = cppyy.gbl.a_star_search(node)
result_breadth_first_search = cppyy.gbl.breadth_first_search(node)
result_multithreaded_breadth_first_search = cppyy.gbl.multithreaded_breadth_first_search(node)

print(result_a_star_search.path_to_goal.size())