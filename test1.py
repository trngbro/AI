from fringes import *
from problem import *
from searchAgents import *

##BFS
a = SingleFoodSearchProblem()
a.load_from_file("input/pacman_single01.txt")
a.animate(BFS(a))

##DFS
b = SingleFoodSearchProblem()
b.load_from_file("input/pacman_single02.txt")
b.animate(DFS(b))

##UCS
c = SingleFoodSearchProblem()
c.load_from_file("input/pacman_single03.txt")
c.animate(UCS(c))

##BFS Multi
d = MultiFoodSearchProblem()
d.load_from_file("input/pacman_multi02.txt")
d.animate(BFS_Multi(d))

##DFS Multi
e = MultiFoodSearchProblem()
e.load_from_file("input/pacman_multi01.txt")
e.animate(DFS_Multi(e))

##UCS Multi
f = MultiFoodSearchProblem()
f.load_from_file("input/pacman_multi03.txt")
f.animate(UCS_Multi(f))