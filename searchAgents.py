from fringes import *

class Graph:
    def __init__(self):
        self.AL = dict() # adjacency list
        self.V = 0
        self.E = 0
        self.H = dict()

    def __str__(self):
        res = 'V: %d, E: %d\n'%(self.V, self.E)
        for u, neighbors in self.AL.items():
            line = '%d: %s\n'%(u, str(neighbors))
            res += line
        for u, h in self.H.items():
            line = 'h(%d) = %d\n'%(u, h)
        return res

    def print(self):
        print(str(self))

    def load_from_file(self, filename):
        # Read file
        # if os.path.exists(filename):
        #   with open(filename) as g:
        #     self.V, self.E = [int(it) for it in g.readline().split()]
        #     for i in range(self.E):
        #       line = g.readline()
        #       u, v, w = [int(it) for it in line.strip().split()]
        #       if u not in self.AL:
        #         self.AL[u] = []
        #       self.AL[u].append((v, w))
        #     for i in range(self.V):
        #       line = g.readline()
        #       u, h = [int(it) for it in line.strip().split()]
        #       self.H[u] = h
        return None

class SearchStrategy:
    def search(self, g:Graph, src:int, dst:int) -> tuple:
        expanded = []
        path = []
        return expanded, path
    
    def get_path(self, src:int, dst:int, parents:dict) -> list:
        path = []
        x = dst
        while x != -1:
            path.append(x)
            x = parents[x]
        path.reverse()
        return path
    
class BFS(SearchStrategy):
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        if(src==dst):
            expanded = []
            path = [src]
            return expanded, path
        q = Queue()
        q.enqueue(src)
        expanded = []
        parents = dict()
        parents[src] = -1
        
        while not q.isEmpty():
            cur = q.dequeue()
            expanded.append(cur)

            successors = g.getSuccessor()
            # Continues
       
class DFS(SearchStrategy):
    def search(self, g: Graph, src: int, dst: int) -> tuple:
        if(src==dst):
            expanded = []
            path = [src]
            return expanded, path
        return super().search(g, src, dst)