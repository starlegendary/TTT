import numpy as np
size = (3,3)
board = np.zeros(size)
history = [[]]*(size[0]*size[1])
time = 0
print(history)
class player:
    def __init__(self,name = None, agent = None):
        self.name  = name
        self.agent = agent
class prop:
    def __init__(self,name = None, space = None):
        self.name  = name
        self.space = space

def place(player,board,space):
    global time
    board[space[0]][space[1]] = player.name
    time = time + 1
    history[time].append(prop(player.name, space))

def future(board):
    space = np.where(board == 0)
    return list(zip(space[0],space[1]))
a = player( 1,None)
b = player(-1,None)
place(a,board,(1,1))
place(b,board,(0,1))
print(history)