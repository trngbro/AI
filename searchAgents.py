from fringes import *
from problem import *

##Ex1
#Single

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
    parents = {str(map.P): -1}
    if map.isGoal(map.P):
        path = getPath(map.G, parents)
        return path
    
    q = Queue()  
    q.enqueue(map.P)
    expanded = []
    path = []
    
    while not q.isEmpty():
        cur = q.dequeue()
        expanded.append(cur)
        successors = map.successor(cur)
        for v in successors:                
            if v not in expanded and not q.contain(v):
                if map.isGoal(v):
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
        if map.isGoal(cur):
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
    
        if map.isGoal(cur): 
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


##Multi


def BFS_Multi(map: MultiFoodSearchProblem)-> list:
    if map.isGoal(map.P):
        map.G.remove(map.P)
        
    q = Queue()  
    path = []
    parents = {str(map.P): -1}
    for i in map.G:
        expanded = []
        q.enqueue(map.state)
        while not q.isEmpty():
            cur = q.dequeue()
            expanded.append(cur)
            successors = map.successor(cur)
            for v in successors:                
                if v not in expanded and not q.contain(v):
                    parents[str(v)] = cur 
                    q.enqueue(v)                
        
        path += getPathMulti(map.state, i, parents)
        parents = {str(map.state): i}
        map.state = i
    path.append("Stop")       
    return path

def DFS_Multi(map: MultiFoodSearchProblem) -> list:
    parents = {str(map.P): -1}
    path = []
    for g in map.G:
        stack = []
        visited =[]
        stack = [map.state]
        while stack:
            cur = stack.pop()
            if cur == g:
                path += getPathMulti(map.state, g, parents)
                map.state = g
                
            if cur not in visited:
                visited.append(cur)
                successors = map.successor(cur)
                for v in successors:
                    if v not in visited:
                        parents[str(v)] = cur
                        stack.append(v)
    path.append("Stop")
    return path

def UCS_Multi(map: MultiFoodSearchProblem) -> list:
    parents = {str(map.P): -1}
    path = []
    for g in map.G:
        pq = PriorityQueue()
        pq.enqueue((0, map.state))
        expanded = []
        while not pq.isEmpty():
            cur_w, cur = pq.dequeue()
            expanded.append(cur)
        
            if cur == g: 
                path += getPathMulti(map.state ,g , parents)
                map.state = g
                
            successors = map.successor(cur)
            for v in successors:
                if v not in expanded and not pq.contain(v):
                    parents[str(v)] = cur
                    pq.enqueue((cur_w + 1, v))
                elif pq.contain(v) and pq.getPriority(v) > cur_w + 1:
                    pq.updatePriority(v, cur_w + 1)
                    parents[str(v)] = cur

    path.append("Stop")
    return path

def getPathMulti(src: list, dst: list, parents: dict):
    path = []
    pathConvert= []
    x = dst
    while x != src:
        path.append(x)
        x = parents[str(x)]
    path.reverse()
    path.insert(0, src)
    
    for i in range(0,len(path)-1):
        if path[i][0] > path[i+1][0]: pathConvert.append("N")
        elif path[i][0] < path[i+1][0]: pathConvert.append("S")
        elif path[i][1] > path[i+1][1]: pathConvert.append("W")
        else: pathConvert.append("E")
    return pathConvert


##Ex2

#YC2-1
def euclidean(state: list, map: SingleFoodSearchProblem):
    return ((state[0] - map.G[0])**2 + (state[1] - map.G[1])**2)**0.5

def manhattan(state: list, map: SingleFoodSearchProblem):
    return abs(state[0] + map.G[0]) + abs(state[1] - map.G[1])

#YC2-2
def food_heuristic(state: list, map: MultiFoodSearchProblem):
    foods = map.G
    if(len(foods)==0): return 0
    distances = ([fn_manhattan(state, food) for food in foods])
    return sum(distances)

def fn_manhattan(x: list, y: list):
    return abs(x[0] + y[0]) + abs(x[1] - y[1])

#YC2-3
#A*
def astar(problem : SingleFoodSearchProblem, fn_heuristic) -> list:
    expanded = []
    parents = {str(problem.P): -1}
    pq = PriorityQueue()
    pq.enqueue((fn_heuristic(problem.P,problem),0 ,problem.P))
    
    while not pq.isEmpty():
        h,c, cur = pq.dequeue()
        expanded.append(cur)
        if problem.isGoal(cur):
            return getPath(problem.G, parents)
        for s in problem.successor(cur):
            if s not in expanded:
                sc = c+1
                pq.enqueue((fn_heuristic(s,problem)+sc,sc ,s))
                parents[str(s)] = cur
    
    return None  
    
#YC2-4
#Modify A* 

def modifyAstar(problem, fn_heuristic) -> list:
    expanded = []
    parents = {str(problem.P): -1}
    pq = PriorityQueue()
    pq.enqueue((fn_heuristic(problem.P,problem),0 ,problem.P))
    
    while not pq.isEmpty():
        h,c, cur = pq.dequeue()
        expanded.append(cur)
        if problem.isGoal(cur):
            return getPath(problem.G, parents)
        for s in problem.successor(cur):
            if s not in expanded:
                sc = c+1
                pq.enqueue((fn_heuristic(s,problem)+sc,sc ,s))
                parents[str(s)] = cur
    
    return None

#yc2-5
def gbfs(problem : SingleFoodSearchProblem, fn_heuristic) -> list:
    visited = [problem.P]
    parents = {str(problem.P): -1}
    pq = PriorityQueue()
    pq.enqueue((fn_heuristic(problem.P,problem), problem.P))
    
    while not pq.isEmpty():
        h, cur = pq.dequeue()
        if problem.isGoal(cur):
            return getPath(problem.G, parents)
        for s in problem.successor(cur):
            if s not in visited:
                visited.append(s)
                pq.enqueue((fn_heuristic(s,problem),s))
                parents[str(s)] = cur
    
    return None       