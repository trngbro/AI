from fringes import *
from problem import *
from searchAgents import *


problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single01.txt")
actions = astar(problem,euclidean)
problem.animate(actions)

problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single02.txt")
actions = gbfs(problem,manhattan)
problem.animate(actions)