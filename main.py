size = (3,3)
board = np.zeros(size)
history = {}

class player:
    def __init__(self,name = None, agent = None):
        self.name  = name
        self.agent = agent
class prop:
    def __init__(self,name = None, space = None):
        self.name  = name
        self.space = space

def place(player,board,space):
    board[space[0]][space[1]] = player.name
def action(move,player,board,space,time):
    move(player,board,space)
    history[time] = prop(player.name, space)

a = player( 1,None)
b = player(-1,None)

def future(board,time):
    