import matplotlib.pyplot as plt
import numpy as np

# Read problems from file
def read_problems(file):
    try:
        with open(file, 'r') as f:
            problems = [line.strip() for line in f.readlines()]
        return problems
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []

# Solve a single problem for given x values
def solve_problem(expression, x_values):
    try:
        return [eval(expression) for x in x_values]
    except Exception as e:
        print(f"Error solving problem: {e}")
        return []

# Plot the graph of a given problem
def plot_graph(x_values, y_values, problem_number):
    plt.plot(x_values, y_values)
    plt.title(f"Problem {problem_number}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# Main function
def main():
    # Read problems from file
    problems = read_problems("problems.txt")
    if not problems:
        return
    
    # Create a list of x values from 1 to 50
    x_values = np.arange(1, 51)
    
    while True:
        print("Choose a problem to solve and graph (1-10), or enter 0 to exit:")
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Exiting program.")
                break
            elif 1 <= choice <= len(problems):
                problem_expression = problems[choice - 1]
                y_values = solve_problem(problem_expression, x_values)
                plot_graph(x_values, y_values, choice)
            else:
                print("Invalid choice. Please enter a number between 1 and 10.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
