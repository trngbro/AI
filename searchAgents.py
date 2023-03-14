from fringes import *
from problem import *

a = SingleFoodSearchProblem()
a.load_from_file("pacman_single01.txt")

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
    
ucs = UCS()
e,p = ucs.search(a, a.P, a.G)
print(p)
# av =[1,2]
# ab = str(av)
# print(int(ab[4])+int(ab[1]))
