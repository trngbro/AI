from fringes import *
from problem import *

problem = EightQueenProblem()
problem.read_board("input/eight_queens04.txt")
best_state = problem.hill_climbing_search()
problem.print_board(best_state)