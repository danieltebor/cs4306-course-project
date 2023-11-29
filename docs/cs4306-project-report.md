# Parallel Algorithms Analysis

**Group Members:**
- Daniel Tebor
- Merrick McPherson

*Course CS4306*

*Kennesaw State University - College of Computing and Software Engineering*


# Introduction and Project Overview

In the ever-evolving landscape of computational algorithms, the pursuit of optimizing search processes is a critical endeavor. This project delves into the intricate realm of search algorithm optimization, specifically exploring the potential performance enhancements achieved through parallelizing search algorithms as opposed to the traditional approach of augmenting them with heuristic techniques.

Our primary focus lies in unraveling the comparative advantages and nuances of these two distinct methodologies. By dissecting the search process and introducing parallelization techniques, we aim to uncover the efficiency gains and computational advantages that may be harnessed. Concurrently, we will contrast this approach with the application of heuristics, seeking to determine the most effective strategy for enhancing search algorithms in various contexts.

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
(Your content here)

# Results
(Your content here)

# Conclusion
(Your content here)

