from fringes import *
from problem import *

problem = EightQueenProblem()
state = [7, 7, 7, 7, 7, 7, 7, 7]
h_value = problem.h(state)
print("Heuristic value:", h_value)
problem = EightQueenProblem()
problem.read_board("input/eight_queens04.txt")
best_state = problem.hill_climbing_search()
problem.print_board(best_state)