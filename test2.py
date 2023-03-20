from fringes import *
from problem import *
from searchAgents import *


problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single02.txt")
actions = modifyAstar(problem,euclidean)
problem.animate(actions)

problem = MultiFoodSearchProblem()
problem.load_from_file("input/pacman_multi01.txt")
actions = modifyAstar(problem,food_heuristic)
problem.animate(actions)

problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single01.txt")
actions = astar(problem,euclidean)
problem.animate(actions)

problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single02.txt")
actions = gbfs(problem,manhattan)
problem.animate(actions)