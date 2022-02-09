# AI-Algorithms

This repository documents several algorithms I wrote as part of Introduction to Artificial Intelligence course I took at Bar-Ilan University. The algorithm implementations were written as part of my solution to Pacman-AI exercise that was written by Berkeley University http://ai.berkeley.edu.


### Search Problem

A Search Problem is defined by:
1. s_start - a start state.
2. actions(s) - a set of actions to be taken from state s.
3. successors(s, a) - a set of successor states from state s by taking action a.
4. is_goal(s) - a function that tell if given state s is a goal state.
5. cost(s, a, t) - a function that calculate the cost of taking action a from state s to state t.

A State-Space is defined as a graph of states (nodes) and actions (edges) that describes all the possible paths from the start state.

Given that, we can use algorithms for searching trees/graphs to solve search problems.


### Search Algorithms

1. **DFS** - Depth First Search algorithm deepens in the search-graph until it is no longer possible, then backtrack and deepens in another way, until there are no more paths left.
2. **BFS** - Breadth First Search algorithm expand every node in depth i before it expands to depth i+1.
3. **UCS** - Uniform Cost Search algorithm searches the node of least total cost first.
4. **A*** - A-Star Search algorithm searches the node that has the lowest combined cost and heuristic first.


### Files

1. containers.py - a utility file that contains implementations of basic data-structures.
2. searchAlgorithms.py - implementations of search algorithms.

