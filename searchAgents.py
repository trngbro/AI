from fringes import *
from problem import *

a = SingleFoodSearchProblem()
a.load_from_file("pacman_single01.txt")

class UCS():
    def search(self, map: SingleFoodSearchProblem, src: list, dst: list):
        pq = PriorityQueue()
        pq.enqueue((0, src))
        expanded = []
        path = []
        
        while not pq.isEmpty():
            cur_w, cur = pq.dequeue()
            expanded.append(cur)
        
            if cur == dst: return expanded, path
            
            successors = map.successor(cur)
            for v in successors:
                if v not in expanded and not pq.contain(v):
                    pq.enqueue((cur_w + 1, v))
                elif pq.contain(v) and pq.getPriority(v) > cur_w + 1:
                    pq.updatePriority(v, cur_w + 1)
        
        return expanded, path
    
    def getPath(self, src: list, dst: list, parents: dict):
        path = []
        x = dst
        while x != -1:
            path.append(x)
            x = parents[x]
        path.reverse()
        return path
ucs = UCS()
e,p = ucs.search(a, a.P, a.G)
print(e)
print(p)