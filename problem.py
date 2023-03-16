import os
import numpy as np

class EightQueenProblem:
    def __init__(self):
        self.state = []

    def read_input(self, file_path):
        with open(file_path, 'r') as f:
            for line in f:
                row = [0 if c == '0' else 1 for c in line.split()]
                self.state.append(row)

    def print_board(self):
        for row in self.state:
            print(' '.join(['Q' if c == 1 else '0' for c in row]))

    def h(self, state):
        def under_attack(row, col):
            return any(state[i][col] or
                       state[row][i] or
                       state[row+i][col+i] or
                       state[row+i][col-i]
                       for i in range(8))

        attacked = 0
        for row, col in enumerate(state):
            if under_attack(row, col):
                attacked += 1
        return attacked
            
class SingleFoodSearchProblem:
    arr = [] #mang 2 chieu
    P = [] #diem P
    G = [] #goal
    def __init__(self) -> None:
        pass
    
    def successor(self,node):
        i = node[0]
        j = node[1]
        a = []
        b = []
        if i != 0: a.append([i-1,j])
        if i != len(self.arr) -1 : a.append([i+1,j])
        if j != 0: a.append([i,j-1])
        if j != len(self.arr[0]) -1 : a.append([i,j+1])

        [b.append(i) for i in a if self.arr[i[0]][i[1]] != "%"]
        return b
    
    def successor_2(self, node):
        i, j = node
        successors = []
        if i > 0 and self.arr[i-1][j] != "%":
            successors.append((i-1, j))
        if i < len(self.arr)-1 and self.arr[i+1][j] != "%":
            successors.append((i+1, j))
        if j > 0 and self.arr[i][j-1] != "%":
            successors.append((i, j-1))
        if j < len(self.arr[0])-1 and self.arr[i][j+1] != "%":
            successors.append((i, j+1))
        return successors
        
    
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                i = 0
                for line in g:
                    a = []
                    for j in range(0,len(line)):
                        if line[j] != "\n": a.append(line[j])
                        if line[j] == "P": 
                            self.P.append(i)
                            self.P.append(j)
                        if line[j] == ".": 
                            self.G.append(i)
                            self.G.append(j)
                    self.arr.append(a)
                    i+=1
        #print 
        for i in self.arr:
            print(i)
        print(self.P)
        print(self.G)



