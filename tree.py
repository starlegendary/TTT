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
    def future(self): return np.where(allboard[self.now] == 0)[0]

def mark(time): return 1 if time % 2 == 0  else -1
def rand(name): return random.choice(allnode[name].future())

def nextmove(name,agent):
    nextname = name + str(agent(name))
    allnode[nextname]  = node(name,nextname)
    allboard[nextname] = allboard[name]
    allboard[nextname][int(nextname[-1])] = mark(len(nextname))
    return nextname

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
def allrand(name,agent):
    while len(name) != size**2:
        name = nextmove(name,agent)
        print(name)
        print(allboard[name])
        winning = winner(allboard[name])
        if winning != None: return winning
    return 'Tie'
print(allrand('',rand))
