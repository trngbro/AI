from fringes import *
from problem import *
from typing import Tuple, List

class BFS():
    def search(self,map: SingleFoodSearchProblem, src: list, dst: list):
        if src == dst:
            expanded = []
            path = [src]
            return expanded,path
        q = Queue()  
        q.enqueue(src)
        expanded = []
        path = []
        # parents = dict()
        parents = {str(src): -1}
        while not q.isEmpty():
            cur = q.dequeue()
            expanded.append(cur)
            successors = map.successor(cur)
            for v in successors:                
                if v not in expanded and not q.contain(v):
                    if v == dst:
                        parents[str(v)] = cur
                        path = self.getPath(src, dst, parents)
                        return expanded,path
                    parents[str(v)] = cur
                    q.enqueue(v)
        path = self.getpath(src, dst, parents)
        return expanded,path
    
    def getPath(self, src: list, dst: list, parents: dict):
        path = []
        path2= []
        x = dst
        while x != -1:
            path.append(x)
            x = parents[str(x)]
        path.reverse()
        
        for i in range(0,len(path)-1):
            if path[i][0] > path[i+1][0]: path2.append("N")
            elif path[i][0] < path[i+1][0]: path2.append("S")
            elif path[i][1] > path[i+1][1]: path2.append("W")
            else: path2.append("E")
        return path2

# a = SingleFoodSearchProblem()
# a.load_from_file("pacman_single01.txt")
# bfs = BFS()
# e, p = bfs.search(a,a.P,a.G)
# print(p)

class UCS():
    def search(self, map: SingleFoodSearchProblem, src: list, dst: list):
        pq = PriorityQueue()
        pq.enqueue((0, src))
        expanded = []
        parents = {str(src): -1}
        path = []
        
        while not pq.isEmpty():
            cur_w, cur = pq.dequeue()
            expanded.append(cur)
        
            if cur == dst: 
                path = self.getPath(src, dst, parents)
                return expanded, path
            
            successors = map.successor(cur)
            for v in successors:
                if v not in expanded and not pq.contain(v):
                    parents[str(v)] = cur
                    pq.enqueue((cur_w + 1, v))
                elif pq.contain(v) and pq.getPriority(v) > cur_w + 1:
                    pq.updatePriority(v, cur_w + 1)
                    parents[str(v)] = cur
               

        path = self.getPath(src, dst, parents)
        return expanded, path
    
    def getPath(self, src: list, dst: list, parents: dict):
        path = []
        pathConvert= []
        x = dst
        while x != -1:
            path.append(x)
            x = parents[str(x)]
        path.reverse()
        
        for i in range(0,len(path)-2):
            if path[i][0] > path[i+1][0]: pathConvert.append("N")
            elif path[i][0] < path[i+1][0]: pathConvert.append("S")
            elif path[i][1] > path[i+1][1]: pathConvert.append("W")
            else: pathConvert.append("E")
        pathConvert.append("Stop")
        return pathConvert
    
# a = SingleFoodSearchProblem()
# a.load_from_file("pacman_single01.txt")
# ucs = UCS()
# e,p = ucs.search(a, a.P, a.G)
# print(p)



class DFS():
    def search(self, map: SingleFoodSearchProblem, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], List[str]]:
        visited = set()
        parents = {}
        stack = [start]
        
        while stack:
            cur = stack.pop()
            if cur == goal:
                path = self.getPath(start, goal, parents)
                return visited, path
            if tuple(cur) not in visited:
                visited.add(tuple(cur))
                successors = map.successor(cur)
                for v in successors:
                    if tuple(v) not in visited:
                        parents[tuple(v)] = tuple(cur)
                        stack.append(v)

        path = self.getPath(start, goal, parents)
        return visited, path
    
    def getPath(self, src: Tuple[int, int], dst: Tuple[int, int], parents: dict):
        path = []
        pathConvert= []
        x = dst
        while x != src:
            path.append(x)
            x = parents[x]
        path.reverse()
        
        for i in range(0,len(path)-1):
            if path[i][0] > path[i+1][0]: pathConvert.append("N")
            elif path[i][0] < path[i+1][0]: pathConvert.append("S")
            elif path[i][1] > path[i+1][1]: pathConvert.append("W")
            else: pathConvert.append("E")
        pathConvert.append("Stop")
        return pathConvert


a = SingleFoodSearchProblem()
a.load_from_file("pacman_single01.txt")

dfs = DFS()
visited, path = dfs.search(a, tuple(a.P), tuple(a.G))
print(path)