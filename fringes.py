import heapq

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def enqueue(self, this):
        self.items.insert(0, this)

    def dequeue(self):
        return self.items.pop()
    
    def contain(self, this):
        return this in self.items

    def size(self):
        return len(self.items)
    
class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, this):
        self.items.append(this)
        
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items)==0
    
    def contain(self, this):
        return this in self.items
    
    def peek(self):
        return self.items[-1]
    
class PriorityQueue():
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
         return len(self.items)==0
     
    def enqueue(self, this):
        self.items.append(this)
        self.items.sort()
        
    def dequeue(self):
        return self.items.pop(0)
    
    def contain(self, this):
        return this in [it[1] for it in self.items]
    
    def getPriority(self, key):
        for w, v in self.items:
            if v == key:
                return w
        raise 'KeyError'
    
    def updatePriority(self, v, w):
        p_w = self.getPriority(v)
        self.items.remove((p_w, v))
        self.items.append((w, v))
        self.items.sort()
        


class PriorityQueueHQ:
    def __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.count, item))
        self.count += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        self.push(item, priority)
        
    def tostring(self):
        return str(self.heap)
    
class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
        
    def __str__(self):
        return f"State: {self.state}, Path Cost: {self.path_cost}, Path: {self.getPath()}"
        
    def getState(self):
        return self.state

    def getPath(self):
        node, path_back = self, []
        while node:
            if node.action:
                path_back.append(node.action)
            node = node.parent
        return list(reversed(path_back))