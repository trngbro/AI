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

# # # p = BFS(a)
# # # a.animate(p)

# p2 = BFS(a)
# a.animate(p2)


def BFS_Multi(map: MultiFoodSearchProblem)-> list:
    # def search(self,map: MultiFoodSearchProblem, map.state: list, map.G: list):
        # check xem scr co trung map.G k, trung thi delete
    if map.state in map.G:
        map.G.remove(map.state)
    q = Queue()  
    # path2 dung de cong path vao 
    path2 = []
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
        path = getPathMulti(map.state, i, parents)
        parents = {str(map.state): i}
        path2 += path
        map.state = i
    path2.append("Stop")       
    return path2

def DFS_Multi(map: MultiFoodSearchProblem) -> list:
    parents = {str(map.P): -1}
    path2 = []
    for g in map.G:
        stack = []
        visited =[]
        stack = [map.state]
        while stack:
            cur = stack.pop()
            if cur == g:
                path = getPathMulti(map.state, g, parents)
                map.state = g
                path2 += path
                
            if cur not in visited:
                visited.append(cur)
                successors = map.successor(cur)
                for v in successors:
                    if v not in visited:
                        parents[str(v)] = cur
                        stack.append(v)
    path2.append("Stop")
    return path2

def UCS_Multi(map: MultiFoodSearchProblem) -> list:
    parents = {str(map.P): -1}
    path2 = []
    for g in map.G:
        pq = PriorityQueue()
        pq.enqueue((0, map.state))
        expanded = []
        while not pq.isEmpty():
            cur_w, cur = pq.dequeue()
            expanded.append(cur)
        
            if cur == g: 
                path = getPathMulti(map.state ,g , parents)
                path2 += path
                map.state = g
                
            successors = map.successor(cur)
            for v in successors:
                if v not in expanded and not pq.contain(v):
                    parents[str(v)] = cur
                    pq.enqueue((cur_w + 1, v))
                elif pq.contain(v) and pq.getPriority(v) > cur_w + 1:
                    pq.updatePriority(v, cur_w + 1)
                    parents[str(v)] = cur

    path2.append("Stop")
    return path2

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

# a = MultiFoodSearchProblem()
# a.load_from_file("input/pacman_multi02.txt")
# # a.__str__()
# p =DFS_Multi(a)
# a.animate(p)
# #print(p)


def euclidean(state: list, map: SingleFoodSearchProblem):
    return ((state[0] - map.G[0])**2 + (state[1] - map.G[1])**2)**0.5

def manhattan(state: list, map: SingleFoodSearchProblem):
    return abs(state[0] + map.G[0]) + abs(state[1] - map.G[1])

def fn_manhattan(x: list, y: list):
    return abs(x[0] + y[0]) + abs(x[1] - y[1])

# pacman = SingleFoodSearchProblem()
# pacman.load_from_file("input/pacman_single01.txt")

# print(euclidean(pacman))
# print(manhattan(pacman))

def food_heuristic(state: MultiFoodSearchProblem):
    foods = state.G
    if(len(foods)==0): return 0
    distances = ([fn_manhattan(state.P, food) for food in foods])
    return sum(distances)
    
# a = MultiFoodSearchProblem()
# a.load_from_file("input/pacman_multi02.txt")
# print(food_heuristic(a))

def gbfs(problem:SingleFoodSearchProblem):
    start_state = problem.P
    visited = set()
    frontier = PriorityQueueHQ()
    frontier.push(start_state, euclidean(start_state, problem))
    
    while not frontier.isEmpty():
        state = frontier.pop()
        
        if problem.isGoalState(state):
            return frontier
        
        if tuple(state) not in visited:
            visited.add(tuple(state))
            successors = problem.successor(state)
            
            for successor in successors:
                if tuple(successor) not in visited:
                    frontier.push(successor, euclidean(successor, problem))
    
    return None



# problem = SingleFoodSearchProblem()
# problem.load_from_file("input/pacman_single01.txt")
# actions = gbfs(problem)
# print(actions.tostring())


def astar(problem:SingleFoodSearchProblem):
    start_node = Node(state=problem.P, action=None, path_cost=0)

    frontier = PriorityQueueHQ()
    frontier.push(start_node, euclidean(problem.P, problem))

    explored = set()

    while not frontier.isEmpty():
        node = frontier.pop()

        if problem.isGoalState(node.state):
            return node.getPath()

        explored.add(tuple(node.state))
        for child_state in problem.successor(node.state):
            if tuple(child_state) not in explored:
                child_node = Node(state=child_state, action='',
                                  path_cost=euclidean(node.state, problem), parent=node)
                f_value = child_node.path_cost + euclidean(child_state, problem)
                frontier.push(child_node, f_value)

    return None

problem = SingleFoodSearchProblem()
problem.load_from_file("input/pacman_single01.txt")
actions = astar(problem)
print(actions)