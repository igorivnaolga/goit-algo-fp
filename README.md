## Task 1: Data Structures. Sorting. Working with a Singly Linked List

For implementing a singly linked list (you may use an example from the lecture notes), you must:

Write a function that reverses the singly linked list by modifying the node links;

Develop a sorting algorithm for the singly linked list, such as insertion sort or merge sort;

Write a function that merges two sorted singly linked lists into one sorted list.

## Task 2: Recursion. Creating the "Pythagoras Tree" Fractal Using Recursion

You need to write a Python program that uses recursion to create the "Pythagoras Tree" fractal.
The program should visualize the fractal, and the user should be able to specify the recursion depth.

## Task 3: Trees, Dijkstra’s Algorithm

Develop Dijkstra's algorithm to find the shortest paths in a weighted graph using a binary heap.
The task includes:

Creating a graph;

Using a heap to optimize vertex selection;

Computing the shortest paths from a starting vertex to all others.

## Task 4: Heap Visualization

The following code builds binary trees. Analyze the code to understand how it works.
Then, based on this code, write a function to visualize a binary heap.

👉🏻 Note: The purpose of the task is to create a tree structure from a heap.

## Task 5: Visualization of Binary Tree Traversals

Using the tree-building code from Task 4, you need to create a Python program that visualizes binary tree traversals: depth-first and breadth-first.

It should display each step with different node colors, using RGB hex codes (e.g., #1296F0);

Node colors should shift from dark to light shades, depending on the traversal order;

Each node should be assigned a unique color that visually reflects the traversal sequence.

👉🏻 Note: Use a stack and a queue, NOT recursion.

## Task 6: Greedy Algorithms and Dynamic Programming

Write a Python program that solves the maximum-calorie food selection problem within a limited budget using two approaches:

A greedy algorithm, and

Dynamic programming.

Each food item has a cost and calorie value. The data is given in a dictionary:

items = {
"pizza": {"cost": 50, "calories": 300},
"hamburger": {"cost": 40, "calories": 250},
"hot-dog": {"cost": 30, "calories": 200},
"pepsi": {"cost": 10, "calories": 100},
"cola": {"cost": 15, "calories": 220},
"potato": {"cost": 25, "calories": 350}
}
Implement greedy_algorithm() to select items maximizing calories per cost, without exceeding the budget.

Implement dynamic_programming() to find the optimal set of items maximizing calories under the given budget.

## Task 7: Using the Monte Carlo Method

Write a Python program that simulates a large number of dice rolls, computes the sum of the dice, and determines the probability of each possible sum.

Simulate rolling two dice many times;

For each roll, compute the sum of the two dice;

Count how often each possible sum (from 2 to 12) appears;

Use this data to calculate the empirical probability of each sum.

Create a table or graph showing the probabilities of each sum discovered using the Monte Carlo method.

Compare your results with the theoretical probabilities shown in a reference table.

## Conclusion Task 7

The simulation successfully confirms the correctness of analytical probability calculations by using the Monte Carlo method. As the number of simulations increases, the statistical error decreases, and the results converge with theoretical expectations. This validates both the methodology of simulation and the theoretical model of dice roll probabilities.
