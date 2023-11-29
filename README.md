# cs4306-course-project
Course Project for Algorithm Analysis at KSU. This project investigates different algorithms to solve the Eight Puzzle Problem including parallel and heuristic algorithms.

## Eight Puzzle Problem Analysis
A detailed analysis of the algorithms used to solve the Eight Puzzle Problem can be found [here](/docs/cs4306-project-report.md).
A PowerPoint presentation of the algorithms used and the results can also be [downloaded](https://github.com/danieltebor/cs4306-course-project/raw/main/docs/cs4306-course-project-presentation.pptx).

## Project Setup
This project uses CMake to build the C++ code and Python to run the GUI and requires some setup. The following instructions are for Windows, Linux, and MacOS.

### Dependencies
In order to build the project, you will need to install the following dependencies:
- [CMake](https://cmake.org/download/)
- [C++ Compiler](https://gcc.gnu.org/install/)
- [Python 3](https://www.python.org/downloads/)
- [Python 3 Pip](https://pip.pypa.io/en/stable/installation/)
- [Python 3 Tkinter](https://tkdocs.com/tutorial/install.html)

### Configure Project
To build the project, required Python packages must be installed and the project must be configured using CMake. To do this run the following command in the project root:

#### Windows
```bash
configure.bat
```
#### Linux & MacOS
```bash
./configure.sh
```

### Building and Running
To build and run the project, run the following commands in the project root:

#### Windows
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

#### Linux & MacOS
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
