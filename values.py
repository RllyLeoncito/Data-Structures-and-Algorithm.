import numpy as np
import math

def read_problems(file):
    try:
        with open(file, 'r') as f:
            problems = [line.strip() for line in f.readlines()]
        return problems
    except FileNotFoundError:
        print(f"Error: File '{file}' not found.")
        return []

def solve_problem(problem, x_values):
    try:
        answers = []
        for x in x_values:
            result = eval(problem.replace('x', str(x)))
            answers.append(result)
        return answers
    except Exception as e:
        print(f"Error solving problem '{problem}': {e}")
        return []

def main():
    problems = read_problems('problems.txt')
    if not problems:
        return

    x_values = list(range(1, 51))
    all_answers = []

    for problem in problems:
        answers = solve_problem(problem, x_values)
        all_answers.append(answers)

    return all_answers

if __name__ == '__main__':
    # Re-run the main function
    answers = main()
    
    # Write the answers to output.txt
    with open('output.txt', 'w') as file:
        for i, answer in enumerate(answers, start=1):
            file.write(f"Problem {i} answers:\n")
            for j, value in enumerate(answer, start=1):
                file.write(f"x={j}, y={value}\n")
            file.write('\n')
    
    print("Answers saved to output.txt")
