import numpy as np
import random
size = 3
board   = np.zeros(size**2)
allboard  = {}
tree   = {}
class node:
    def __init__(self,before,now):
        self.before = before
        self.now    = now
        self.value  = None
    def future(self):
        return list(map(lambda x: self.now + str(x),empty(self.now)))

def empty(name):
    return list(map(lambda x: str(x),np.where(allboard[name] == 0)[0]))
def mark(time): return 1 if time % 2 == 0  else -1

def nextrand(name):
    nextname = random.choice(tree[name].future())
    tree[nextname]  = node(name,nextname)
    allboard[nextname] = allboard[name].copy()
    allboard[nextname][int(nextname[-1])] = mark(len(nextname))
    return nextname
def win(num):
    if   num ==  3 : return 1
    elif num == -3 : return -1
    return None
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
    return win(max(result, key=abs)) #maximum absolute value
allboard[''] = board
tree[''] = node(None,'')
print(board)
a = nextrand('')
print(board)
b = nextrand(a)
print(winner(allboard[b]))
c = nextrand(b)
print(winner(allboard[c]))