import numpy as np
size = 3
board   = np.zeros(size**2)
boards  = {}
tree   = {}
class node:
    def __init__(self,now):
        self.before = None
        self.now    = now
        self.after  = None
        self.value  = None
    def afterward(self):
        self.after = list(map(lambda x: self.now + str(x),empty(self.now)))

def empty(name):
   return list(map(lambda x: str(x),np.where(boards[name] == 0)[0]))
def random
boards[''] = board
tree[''] = node('')
print(board)
tree[''].afterward()
print(tree[''].after)