# Data-Structures-and-Algorithm.


The code was made to solve and graph of the mathematical expression in problems.txt.
Reading Problems from File: The function read_problems reads mathematical expressions from a file line by line and returns them as a list.

Solving a Single Problem: The function solve_problem takes a mathematical expression and a list of x-values. It substitutes each x-value into the expression and evaluates it to get corresponding y-values.

Plotting Graphs: The function plot_graph takes x-values and y-values and creates a plot using matplotlib library.

Main Function: The main function is the entry point of the program. It reads problems from the file, prompts the user to choose a problem to solve, and then displays the graph of the chosen problem.

It repeatedly prompts the user to input a problem number to solve and graph until the user enters 0 to exit.
It calls solve_problem to get y-values for the chosen problem expression.
It then calls plot_graph to plot the graph of the chosen problem.
Re-running the Main Function: After the initial execution of the main function, there's an additional part of the code which runs the main function again, collecting all the answers, and then writes them to an output file named "output.txt".

It calls the main function to get answers for all problems.
It writes the answers to "output.txt", including which problem each set of answers corresponds to.
