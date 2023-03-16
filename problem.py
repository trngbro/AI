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
    
    def load_from_file(self, filename) -> None:
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
    
    def __str__(self) -> str:
        for i in self.arr:
            s = ""
            for j in i:
                s += j
            print(s)
              
    def animate(self, actions) -> None:
        cur = self.P
        self.__str__()
        for i in actions:
            os.system("cls")
            os.system("clear")
            self.__str__()
            self.arr[cur[0]][cur[1]] = " "
            if i == "Stop":
                break
            if i == "N": 
                cur[0] -= 1
                self.arr[cur[0]][cur[1]] = "P"
            if i == "S": 
                cur[0] += 1
                self.arr[cur[0]][cur[1]] = "P"
            if i == "W": 
                cur[1] -= 1
                self.arr[cur[0]][cur[1]] = "P"
            if i == "E": 
                cur[1] += 1
                self.arr[cur[0]][cur[1]] = "P"
            enter = input("Press Enter")
            
import random

class EightQueenProblem:

    def __init__(self):
        self.state = None
        self.n = 8
            
    def read_board(self, file_name):
        with open(file_name, "r") as f:
            lines = f.readlines()
            self.initial_state = [[1 if c == "Q" else 0 for c in line.strip()] for line in lines]


    def print_board(self, state):
        for row in range(len(state)):
            for col in range(len(state)):
                if state[row] == col:
                    print("Q ", end="")
                else:
                    print("0 ", end="")
            print()



    def h(self, state):
        n = len(state)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    count += 1
        return count

    def hill_climbing_search(self):
        if self.state is None:
            self.state = [random.randint(0, self.n - 1) for i in range(self.n)]
        while True:
            h = self.h(self.state)
            neighbors = []
            for col in range(self.n):
                for row in range(self.n):
                    if self.state[col] != row:
                        neighbor = list(self.state)
                        neighbor[col] = row
                        neighbors.append(neighbor)
            if not neighbors:
                break
            neighbor_h = [self.h(n) for n in neighbors]
            if min(neighbor_h) >= h:
                break
            self.state = neighbors[neighbor_h.index(min(neighbor_h))]
        return self.state
            
problem = EightQueenProblem()
state = [0, 2, 4, 1, 6, 3, 7, 5]
h_value = problem.h(state)
print("Heuristic value:", h_value)
problem = EightQueenProblem()
problem.read_board("input/eight_queens01.txt")
best_state = problem.hill_climbing_search()
problem.print_board(best_state)