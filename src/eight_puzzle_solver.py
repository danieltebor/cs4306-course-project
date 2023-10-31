import cppyy
import tkinter as tk
from tkinter import ttk

# Load lib_eight_puzzle_solver.dll
cppyy.include('./include/eight_puzzle_solver_includes.hpp')
lib = cppyy.load_library('./lib/lib_eight_puzzle_solver.dll')

# Create the main window
window = tk.Tk()
window.title('Eight Puzzle Solver')

# Create a dropdown menu to select algorithm.
selected_algorithm = tk.StringVar()
selected_algorithm.set('A*')
algorithm_selector = ttk.Combobox(window, textvariable=selected_algorithm)
algorithm_selector['values'] = ('A*', 'BFS', 'Multithreaded BFS')
algorithm_selector.grid(column=0, row=0)

# Create result labels with default text
moves_to_goal_label = tk.Label(window, text='Moves to Goal: -')
moves_to_goal_label.grid(column=0, row=1, sticky=tk.W)
nodes_visited_label = tk.Label(window, text='Nodes Visited: -')
nodes_visited_label.grid(column=0, row=2, sticky=tk.W)
runtime_ms_label = tk.Label(window, text='Runtime (MS): -')
runtime_ms_label.grid(column=0, row=3, sticky=tk.W)

# Create a 3x3 grid of labels with empty strings
state_table_frame = tk.Frame(window)
state_table_frame.grid(column=0, row=5, columnspan=5, sticky=tk.W)

state_labels = [[tk.Label(state_table_frame, text=' ', relief='solid', width=4, height=2) for _ in range(3)] for _ in range(3)]
for y in range(3):
    for x in range(3):
        state_labels[y][x].grid(column=x + 1, row=y)

def set_state_labels(state: cppyy.gbl.std.array[cppyy.gbl.std.array[int, 3], 3]):
    global state_labels

    for y in range(3):
        for x in range(3):
            state_labels[y][x].config(text=str(state[y][x]))

# Create previous and next buttons
current_result = None
current_state_idx = 0

def traverse_previous_move():
    global current_result
    global current_state_idx

    if current_state_idx == current_result.path_to_goal.size() - 1:
        next_button.config(state=tk.NORMAL)

    current_state_idx -= 1
    if current_state_idx == 0:
        previous_button.config(state=tk.DISABLED)

    set_state_labels(state=current_result.path_to_goal[current_state_idx].state)

def traverse_next_move():
    global current_result
    global current_state_idx

    if current_state_idx == 0:
        previous_button.config(state=tk.NORMAL)

    current_state_idx += 1
    if current_state_idx == current_result.path_to_goal.size() - 1:
        next_button.config(state=tk.DISABLED)

    set_state_labels(state=current_result.path_to_goal[current_state_idx].state)

previous_button = tk.Button(state_table_frame, text='←', command=traverse_previous_move, state=tk.DISABLED)
previous_button.grid(column=0, row=0, rowspan=3)
next_button = tk.Button(state_table_frame, text='→', command=traverse_next_move, state=tk.DISABLED)
next_button.grid(column=4, row=0, rowspan=3)

# Create a button to run the selected algorithm
def run_algorithm() -> cppyy.gbl.SearchResult:
    global current_result
    global current_state_idx

    # Lock buttons
    run_button.config(state=tk.DISABLED)
    previous_button.config(state=tk.DISABLED)
    next_button.config(state=tk.DISABLED)

    node = cppyy.gbl.generate_random_start_node()

    result = None
    algorithm = selected_algorithm.get()
    if algorithm == 'A*':
        result = cppyy.gbl.a_star_search(node)
    elif algorithm == 'BFS':
        result = cppyy.gbl.breadth_first_search(node)
    elif algorithm == 'Multithreaded BFS':
        result = cppyy.gbl.multithreaded_breadth_first_search(node)

    # Update the labels with the result
    moves_to_goal_label.config(text=f'Moves to Goal: {result.path_to_goal.size()}')
    nodes_visited_label.config(text=f'Nodes Visited: {result.num_nodes_visited}')
    runtime_ms_label.config(text=f'Runtime (MS): {result.time_taken_ms}')

    # Update the state labels
    current_result = result
    current_state_idx = 0
    set_state_labels(state=result.path_to_goal[0].state)

    # Unlock run button
    run_button.config(state=tk.NORMAL)
    next_button.config(state=tk.NORMAL)

run_button = tk.Button(window, text='Run', command=run_algorithm)
run_button.grid(column=1, row=0)

# Start the main loop
window.mainloop()