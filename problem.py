import os
import numpy as np
class SingleFoodSearchProblem:
    arr = [] #mang 2 chieu
    P = [] #diem P
    G = [] #goal
    def __init__(self) -> None:
        pass
    
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
        print(self.arr[9][9])
        
a = SingleFoodSearchProblem()
a.load_from_file("pacman_single01.txt")



