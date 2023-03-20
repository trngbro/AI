import os
import random

class SingleFoodSearchProblem:
    
    def __init__(self):
        self.map = [] #map
        self.P = [] #Initial state
        self.G = [] #Goal
        self.state = [] 
    
    def isGoal(self, state):
        return state == self.G
    
    def successor(self,state):
        i = state[0]
        j = state[1]
        a = []
        b = []
        if i != 0: a.append([i-1,j])
        if i != len(self.map) -1 : a.append([i+1,j])
        if j != 0: a.append([i,j-1])
        if j != len(self.map[0]) -1 : a.append([i,j+1])
        [b.append(i) for i in a if self.map[i[0]][i[1]] != "%"]
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
                            self.P = [i,j]
                            self.state = self.P
                        if line[j] == ".": 
                            self.G = [i,j]
                    self.map.append(a)
                    i+=1
    
    def __str__(self) -> str:
        for i in self.map:
            s = ""
            for j in i:
                s += j
            print(s)
              
    def animate(self, actions) -> None:
        cur = self.P
        for i in actions:
            os.system("cls")
            os.system("clear")
            self.__str__()
            self.map[cur[0]][cur[1]] = " "
            if i == "Stop":
                break
            if i == "N": 
                cur[0] -= 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "S": 
                cur[0] += 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "W": 
                cur[1] -= 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "E": 
                cur[1] += 1
                self.map[cur[0]][cur[1]] = "P"
            enter = input("Press Enter")
            
class MultiFoodSearchProblem:
    def __init__(self):
        self.map = [] 
        self.P = [] 
        self.G = [] 
        self.state = []
               
    def successor(self,state):
        i = state[0]
        j = state[1]
        a = []
        b = []
        if i != 0: a.append([i-1,j])
        if i != len(self.map) -1 : a.append([i+1,j])
        if j != 0: a.append([i,j-1])
        if j != len(self.map[0]) -1 : a.append([i,j+1])
        [b.append(i) for i in a if self.map[i[0]][i[1]] != "%"]
        return b
    
    def isGoal(self,state):
        return state in self.G  
    
    def load_from_file(self, filename):
        if os.path.exists(filename):
            with open(filename) as g:
                i = 0
                for line in g:
                    a = []
                    for j in range(0,len(line)):
                        if line[j] != "\n": a.append(line[j])
                        if line[j] == "P": 
                            self.P=[i,j]
                            self.state = self.P
                        if line[j] == ".": 
                            self.G.append([i,j])
                    self.map.append(a)
                    i+=1
    
    def __str__(self) -> str:
        for i in self.map:
            s = ""
            for j in i:
                s += j
            print(s)

    def animate(self, actions) -> None:
        cur = self.P
        for i in actions:
            os.system("cls")
            os.system("clear")
            self.__str__()
            self.map[cur[0]][cur[1]] = " "
            if i == "Stop":
                break
            if i == "N": 
                cur[0] -= 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "S": 
                cur[0] += 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "W": 
                cur[1] -= 1
                self.map[cur[0]][cur[1]] = "P"
            if i == "E": 
                cur[1] += 1
                self.map[cur[0]][cur[1]] = "P"
            enter = input("Press Enter")

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
            '''Mở xem chi tiết từng bước đạt được'''
            self.print_board(self.state)
            print("\n\n")
        return self.state