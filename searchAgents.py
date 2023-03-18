from fringes import *
from problem import *

#get Path
def getPath(dst: list, parents: dict) -> list:
    path = []
    pathConvert= []
    x = dst
    
    while x != -1:
        path.append(x)
        x = parents[str(x)]
    path.reverse()
    
    for i in range(0,len(path)-1):
        if path[i][0] > path[i+1][0]: pathConvert.append("N")
        elif path[i][0] < path[i+1][0]: pathConvert.append("S")
        elif path[i][1] > path[i+1][1]: pathConvert.append("W")
        else: pathConvert.append("E")
    pathConvert.append("Stop")
    
    return pathConvert
    
#BFS function
def BFS(map: SingleFoodSearchProblem) -> list:
    if map.P == map.G:
        expanded = []
        path = [map.P]
        return path
    
    q = Queue()  
    q.enqueue(map.P)
    expanded = []
    path = []
    parents = {str(map.P): -1}
    
    while not q.isEmpty():
        cur = q.dequeue()
        expanded.append(cur)
        successors = map.successor(cur)
        for v in successors:                
            if v not in expanded and not q.contain(v):
                if v == map.G:
                    parents[str(v)] = cur
                    path = getPath(map.G, parents)
                    return path
                parents[str(v)] = cur
                q.enqueue(v)
                
    path = getPath(map.G, parents)
    return path
    
#DFS function
def DFS(map: SingleFoodSearchProblem) -> list:
    visited = []
    parents = {str(map.P): -1}
    stack = [map.P]
    
    while stack:
        cur = stack.pop()
        if cur == map.G:
            path = getPath(map.G, parents)
            return path
        if cur not in visited:
            visited.append(cur)
            successors = map.successor(cur)
            for v in successors:
                if v not in visited:
                    parents[str(v)] = cur
                    stack.append(v)
                    
    path = getPath(map.G, parents)
    return path


#UCS function
def UCS(map: SingleFoodSearchProblem) -> list:
    pq = PriorityQueue()
    pq.enqueue((0, map.P))
    expanded = []
    parents = {str(map.P): -1}
    path = []
    
    while not pq.isEmpty():
        cur_w, cur = pq.dequeue()
        expanded.append(cur)
    
        if cur == map.G: 
            path = getPath(map.G, parents)
            return path
        
        successors = map.successor(cur)
        for v in successors:
            if v not in expanded and not pq.contain(v):
                parents[str(v)] = cur
                pq.enqueue((cur_w + 1, v))
            elif pq.contain(v) and pq.getPriority(v) > cur_w + 1:
                pq.updatePriority(v, cur_w + 1)
                parents[str(v)] = cur

    path = getPath(map.G, parents)
    return path



# a = SingleFoodSearchProblem()
# a.load_from_file("input/pacman_single02.txt")

# # p = BFS(a)
# # a.animate(p)

# p2 = BFS(a)
# a.animate(p2)



def euclidean(state: list, map: SingleFoodSearchProblem):
    return ((state[0] - map.G[0])**2 + (state[1] - map.G[1])**2)**0.5

def manhattan(state: list, map: SingleFoodSearchProblem):
    return abs(state[0] + map.G[0]) + abs(state[1] - map.G[1])

pacman = SingleFoodSearchProblem()
pacman.load_from_file("input/pacman_single01.txt")

print(euclidean([4,5], pacman))
# print(manhattan(pacman))

def fn_heuristic(start, goal):
    return ((start[0]-goal[0])**2 + (start[1]-goal[1])**2)**0.5

def gbfs(problem: SingleFoodSearchProblem):
    start = problem.P
    goal = problem.G

    fringes = PriorityQueueHQ()
    fringes.push([start], fn_heuristic(start, goal))

    visited = set()

    while not fringes.isEmpty():
        path = fringes.pop()
        node = path[-1]

        if node == goal:
            return path[1:]

        if tuple(node) in visited:
            continue

        visited.add(tuple(node))

        for successor in problem.successor(node):
            if successor[0] not in visited:
                new_path = path[:]
                new_path.append(successor[1])
                fringes.push(new_path, fn_heuristic(successor[0], goal))

    return []  # Failed to find a path



# problem = SingleFoodSearchProblem()
# problem.load_from_file("input/pacman_single01.txt")
# actions = gbfs(problem)
# print(actions)