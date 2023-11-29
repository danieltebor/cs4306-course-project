# Parallel Algorithms Analysis

**Group Members:**
- Daniel Tebor
- Merrick McPherson

*Course CS4306*

*Kennesaw State University - College of Computing and Software Engineering*


# Introduction and Project Overview

In the ever-evolving landscape of computational algorithms, the pursuit of optimizing search processes is a critical endeavor. This project delves into the intricate realm of search algorithm optimization, specifically exploring the potential performance enhancements achieved through parallelizing search algorithms as opposed to the traditional approach of augmenting them with heuristic techniques.

Our primary focus lies in unraveling the comparative advantages and nuances of these two distinct methodologies. By dissecting the search process and introducing parallelization techniques, we aim to uncover the efficiency gains and computational advantages that may be harnessed. Moreover, we will contrast this approach with the application of heuristics, seeking to determine the most effective strategy for enhancing search algorithms in various contexts.

This comprehensive report unfolds with a detailed exploration of our aims and objectives, providing a roadmap for our investigation. We pivot to the puzzle problem chosen as the litmus test for algorithmic performance, offering insights into the intricacies of the challenges posed and the overarching goals each algorithm aspires to achieve.

Moreover, we embark on a concise overview of the literature and online resources that have steered our project, highlighting the foundational knowledge and cutting-edge insights that shaped our analytical framework. Drawing from a diverse range of scholarly contributions and practical implementations, our approach is fortified by a synthesis of the latest advancements in the field.

The subsequent sections of this report navigate through the meticulously chosen methodologies employed in the study. From the inception of the project to the final implementation of algorithms, we detail the systematic approach taken to study, analyze, and program these intricate search algorithms. The narrative then seamlessly transitions to an exposition of the empirical results, providing a comprehensive account of how these algorithms performed under various conditions and scenarios.

Concluding this exploration is a succinct yet insightful reflection on the outcomes, encapsulated in a conclusive section. Here, we synthesize the findings, discuss their implications, and present a holistic understanding of the optimized search algorithms' efficacy in light of our objectives.

By traversing this project, readers will gain not only a nuanced understanding of parallelized search algorithms and heuristic-enhanced counterparts but also a profound insight into the dynamic interplay between theory and implementation in the realm of computational optimization.

# Aims and Objectives

The primary objective of this project is to conduct a thorough performance evaluation of three distinct algorithms, namely Breadth First Search (BFS), Multithreaded Breadth First Search, and the A* (pronounced A-star) algorithm, in the context of solving the well-known 8-puzzle problem. The 8-puzzle problem, a classic and widely studied puzzle, involves a 3x3 grid with eight numbered tiles and one empty tile. The challenge is to rearrange these tiles by sliding them into the empty space, ultimately reaching a predefined goal state where the numbered tiles are in the correct order.

In our project, we have specifically configured the 8-puzzle to consist of 8 numbered tiles and one empty blank space tile. This puzzle serves as an ideal testbed for evaluating the efficiency and effectiveness of the selected algorithms in solving real-world combinatorial problems.

The algorithms under scrutiny each bring unique characteristics to the table. Breadth First Search is a systematic and reliable search algorithm that exhaustively explores all possible paths to find the shortest solution. The Multithreaded Breadth First Search, a parallelized adaptation of BFS, harnesses the computational power of multiple CPU cores to expedite the search process. Finally, the A* algorithm, known for its popularity and efficiency in pathfinding, employs heuristics to guide its search, striking a balance between optimality and computational efficiency.

Our evaluation metrics encompass a comprehensive set of criteria, including runtimes, moves to goal, nodes visited, space complexity, and time complexity. Through a meticulous analysis of these metrics, we aim to provide a nuanced and holistic performance review of each algorithm. By scrutinizing their performance across various dimensions, we seek to discern the strengths and weaknesses of these algorithms under the specific constraints posed by the 8-puzzle problem.

This investigation is not only instrumental in gauging the capabilities of these algorithms but also contributes valuable insights into their practical applicability in solving complex problems. As we navigate through the subsequent sections of this report, we invite readers to join us in unraveling the intricate dynamics of algorithmic performance, with a specific focus on the challenges posed by the 8-puzzle problem.


# Brief Literature Review

## Background

The foundation of this project has been significantly influenced by the collective experiences and expertise of the team members, Daniel and Merrick.

### Daniel's Experience

In a previous AI class, Daniel played a pivotal role in the development of a comprehensive code base for algorithm analysis. His prior work serves as the cornerstone for the current project, providing valuable insights and a robust starting point for the exploration of optimized search algorithms. Leveraging his expertise, Daniel has contributed to shaping the methodology and approach undertaken in this endeavor.

### Merrick's Experience

Merrick brings a wealth of knowledge in parallel programming, acquired through a different class. His background in this specialized area has been instrumental in guiding the project towards efficient parallelization of search algorithms. Merrick's insights have played a crucial role in optimizing the utilization of multiple CPU cores, thereby enhancing the overall computational efficiency of the algorithms under examination.

## External References

In addition to the team's internal expertise, the project has been enriched by consulting external resources that have significantly informed its direction.

### Textbook Reference

- **"Distributed Computing: Principles and Applications" by M. L. Liu:**
  This textbook has served as a foundational resource, offering comprehensive insights and principles in the domain of distributed and parallel computing. The principles extracted from this source have been instrumental in shaping the theoretical framework of the project. Concepts and methodologies discussed in the book have guided the team in developing a nuanced understanding of the complexities involved in parallelizing search algorithms.

### Software Library

- **"oneAPI Threading Building Blocks" (a C++ library):**
  To facilitate the implementation of parallelization techniques and ensure optimal utilization of multi-core processing, the team has incorporated the "oneAPI Threading Building Blocks" C++ library. This library simplifies the intricacies of parallel programming, providing a robust foundation for developing efficient and scalable algorithms. The integration of this library aligns with best practices in parallel computing and enhances the project's ability to harness the computational power of modern hardware architectures.

## Synthesis of Literature

The combination of internal expertise and external references has laid a robust foundation for this project. The literature review has not only shaped the methodology but has also provided the team with a well-rounded perspective on the intricacies of parallel computing and algorithm optimization. As we delve deeper into the subsequent sections of this report, the synthesis of literature continues to guide our approach and analysis, ensuring a comprehensive exploration of the chosen search algorithms in the context of parallelization and heuristic enhancement.

# Methodologies
To facilitate the evaluation of the breadth-first search, multithreaded breadth-first search, and A* search, these algorithms had to be built from scratch. Each has a similar, but slightly different implementation. However, all are dependent on the mechanics of the 8-puzzle Problem.

## Representing 8-puzzle
Creating an 8-puzzle in a way in which a search algorithm can use it requires two things: the board to be representable in memory as a node, and for the current node to be extendable to reach the next available moves. Firstly, a node structure was configured. This Node contains a 3x3 grid, representing the state of the 8-puzzle board, with the number 0 representing the empty tile. The node also stores a pointer to its parent (the previous move) so that we can trace from the starting position of the board to the current position. In addition, the node also stores the current depth of the node (which starts at 0), which also describes how many moves it has taken thus far to reach the goal. Finally, the node stores a heuristic value. This value is only populated when A* is being utilized and is used to estimate the best next move.

### Extending the Current Node
To extend the current node, the first step is to find the position of the empty tile. This can be done by looping through the 3x3 grid until the position of the tile with "0" is found. From there we can try to move in all 4 directions, rejecting any moves that attempt to move outside the bounds of the board. For example, if the empty tile is in the top-right corner, it cannot move up or right since this would be outside the bounds of the grid, so those moves are rejected. Another requirement is that a child node's 3x3 grid cannot be identical to any previously visited tile. To ensure this, every visited node is stored in a hashed-set data structure. This allows for an average lookup time of O(1), making this process extremely efficient.

### Branching Factor
Since a generated child node cannot be the same as the previous move it is generated from, we can always subtract 1 from the possible moves at any given board state. Using this idea we can calculate a rough estimate of the the branching factor for each node. If the empty tile is in a corner, there is only one possible move it can make. If the empty tile is touching one of the sides, it has 2 possible moves. Finally, if the tile is in the middle it has 3 possible moves. There are 4 corners, 4 sides, and 1 center position, so we can calculate a rough branching factor by summing the possible moves at each position divided by the total number of positions: ((1 * 4) + (2 * 4) + 3) / 9. This results in a rough average branching factor of 1.67.

## Search Algorithm Implementations
Each of the search algorithms was written in C++ and utilizes the same algorithm for expanding the current node. The goal node was hard coded to the following value:
| 1 | 2 | 3 |
| - | - | - |
| 8 | 0 | 4 |
| 7 | 6 | 5 |

A random start node was then generated by scrambling the 3x3 grid of the goal node by doing 1000000 random moves.

### Breadth First Search
Breadth first search explores every possible state systematically. It does this depth-wise, meaning that it will explore all nodes of depth 0, then all nodes of depth 1, etc. until a goal node is found. This garuntees that the shortest possible path (number of moves) is found from the start to the goal. The steps for the algorithm are as follows and use C++ datatypes:
1. Initialize a

# Results
(Your content here)

# Conclusion

In conclusion, our exploration into parallel search algorithms and heuristic-based approaches for solving the 8-puzzle problem has provided valuable insights into the trade-offs and advantages associated with different strategies.

**A * for Speed:** A* emerges as the star performer when speed is the top priority. Its ability to swiftly navigate through the solution space makes it the preferred choice for scenarios where finding a quick resolution to the 8-puzzle problem is crucial. The efficiency of A* shines through, showcasing its prowess in rapidly converging towards solutions.

**BFS for Optimal Moves:** On the other hand, if the primary objective is to achieve optimal moves, Breadth-First Search (BFS) takes the lead. Its systematic exploration of the solution space ensures that the shortest path to the solution is identified. When the focus shifts from speed to the precision of moves, BFS stands out as the superior option.

**Multi-Threaded BFS:** However, our project delves deeper into the realm of optimization, introducing the concept of Multi-Threaded BFS. This innovative approach not only preserves the optimal moves of BFS but also introduces a parallel processing element that significantly enhances runtime efficiency. The multi-threaded BFS proves to be the optimal choice when the goal is to minimize the number of moves while simultaneously outperforming the traditional BFS in terms of runtime.

In the evolving landscape of search algorithms, our project underscores the importance of understanding the specific priorities and requirements of a problem before selecting an appropriate solution strategy. A* for speed, BFS for optimal moves, and Multi-Threaded BFS for a harmonious blend of both — our project contributes to the nuanced understanding of these algorithms, paving the way for informed decision-making in problem-solving scenarios. As we conclude this report, we acknowledge the dynamic nature of algorithmic research and anticipate that future endeavors will continue to refine and expand upon the foundations laid in this project.


