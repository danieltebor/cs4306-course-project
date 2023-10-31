# cs4306-course-project
Course Project for Algorithm Analysis at KSU. This project investigates different algorithms to solve the Eight Puzzle Problem.

## Dependencies
In order to build the project, you will need to install the following dependencies:
- [CMake](https://cmake.org/download/)
- [C++ Compiler](https://gcc.gnu.org/install/)
- [Python 3](https://www.python.org/downloads/)
- [Python 3 Pip](https://pip.pypa.io/en/stable/installation/)
- [Python 3 Tkinter](https://tkdocs.com/tutorial/install.html)

## Configure Project
To build the project, required Python packages must be installed and the project must be configured using CMake. To do this run the following command in the project root:
### Windows
```bash
configure.bat
```
### Linux & MacOS
```bash
./configure.sh
```

## Building and Running
To build and run the project, run the following commands in the project root:

### Windows
Build the project
```bash
build.bat
```

Run the Eight Puzzle Solver
```bash
eight_puzzle_solver.bat
```

Run the Algorithm Analyzer
```bash
analyze_search_algs.bat
```

### Linux & MacOS
Build the project
```bash
./build.sh
```

Run the Eight Puzzle Solver
```bash
./eight_puzzle_solver.sh
```

Run the Algorithm Analyzer
```bash
./analyze_search_algs.sh
```

## Results
![Nodes Visited vs Runtime (ms)](/assets/nodes-visited-vs-runtime.png)
![Avg Moves to Goal](/assets/avg-moves-to-goal.png)
![Avg Nodes Visited](/assets/avg-num-nodes-visited.png)
![Avg Runtime (ms)](/assets/avg-runtime-ms.png)
