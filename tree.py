import numpy as np
import random
size = 3
board   = np.zeros(size**2)
allboard  = {}
allnode   = {}

class node:
    def __init__(self,before,now):
        self.before = before
        self.now    = now
        self.value  = None
        self.visit  = None
    def future(self): return np.where(allboard[self.now] == 0)[0]
    def value(self):
        winner(allboard[self.now])
def mark(time): return 1 if time % 2 == 0  else -1
def rand(name): return random.choice(allnode[name].future())
def isleaf(name): return len(name) == size**2
def isroot(name): return len(name) == 0
def nextmove(name,move):
    nextname = name + move
    allnode[nextname]  = node(name,nextname)
    allboard[nextname] = allboard[name]
    allboard[nextname][int(nextname[-1])] = mark(len(nextname))
    return nextname
#function that take choice as input and return winning or losing, the value of state = weight of the learning process
class agent:
    def __init__(self,mark,first):
        self.mark   = None
        self.first  = None
        self.memory =
        self.policy = 
    def
def winner(board):
    result = []
    sth = np.reshape(board,(size,size))
    for i in range(size):
      result.append(np.sum(sth[i,:]))
      result.append(np.sum(sth[:,i]))
    result.append(0)
    for i in range(size):
        result[-1] += sth[i,i]
    result.append(0)
    for i in range(size):
        result[-1] += sth[i,size-1-i]
    result = max(result, key=abs)
    if   result ==  size : return 1
    elif result == -size : return -1
    return None
allboard[''] = board
allnode[''] = node(None,'')
#a = nextrand(b)
def forward(name,agentA, agentB):
    while not isleaf(name):
        if   len(name)%2 == 0:  name = nextmove(name, str(agentA(name)))
        elif len(name)%2 == 1:  name = nextmove(name, str(agentB(name)))
        print(name)
        print(allboard[name])
        winning = winner(allboard[name])
        if winning != None: break
    return name, winning
def backward(name, agent):
    while not isroot(name):
        
        name = name[:-1]
print(forward('',rand,rand))
