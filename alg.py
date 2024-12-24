maze1 = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]


def display_maze(maze):
    for row in maze:
        print("  ".join(str(cell) for cell in row))


def check_zero(param):
    if param==0:
        return True
    else:
        return False
class node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.path=[]
def get_nighbors(point, maze):
    neighbors = []
    x = point[0] 
    y = point[1]
    max_col = len(maze)
    max_row = len(maze[0])
    if(x+1<max_row and y<max_col):
        if(check_zero(maze[x+1][y])):
            neighbors.append((x+1,y))
    if(x<max_row and y+1<max_col):
        if(check_zero(maze[x][y+1])):
            neighbors.append((x,y+1))
    if(x-1>=0 and y<max_col):
        if(check_zero(maze[x-1][y])):
            neighbors.append((x-1,y))
    if(x<max_row and y-1>=0):
        if(check_zero(maze[x][y-1])):
            neighbors.append((x,y-1))
    return neighbors
    
        
        
def create_grph(maze):
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if(maze[i][j] == 0):
                graph[(i,j)]= get_nighbors((i,j),maze)
    return graph


def dfs(start, end, graph:dict):
    stack = [start]
    path = []
    visited = set()
    while len(stack)>0:
        current_node = stack.pop()
        if(current_node.x==end.x and current_node.y==end.y):
            return path+[(current_node.x,current_node.y)]
        else:
            path=current_node.path+[(current_node.x,current_node.y)]
            neighbors = list(map(lambda nn:node(nn[0],nn[1]),reversed(graph.get((current_node.x,current_node.y),[]))))
            for neighbor in neighbors:           
                 if (neighbor.x, neighbor.y) not in visited:
                     visited.add((neighbor.x, neighbor.y))
                     neighbor.path = path.copy()
                     stack.append(neighbor) 
    return None    


def bfs(start, end, graph: dict):
    que = [start]
    visited = set()
    start.path = [] 
    while len(que) > 0:
        current_node = que.pop(0)
        if (current_node.x, current_node.y) == (end.x, end.y):
            return current_node.path + [(current_node.x, current_node.y)]
        if (current_node.x, current_node.y) not in visited:
            visited.add((current_node.x, current_node.y))
            neighbors = list(map(lambda nn: node(nn[0], nn[1]), graph.get((current_node.x, current_node.y), [])))
            for neighbor in neighbors:
                if (neighbor.x, neighbor.y) not in visited and neighbor not in que:
                    neighbor.path = current_node.path + [(current_node.x, current_node.y)]
                    que.append(neighbor)
    return None

def solve_with_bfs(start,end,maze):
    return bfs(start,end,create_grph(maze))

def solve_with_dfs(start,end,maze):
   return dfs(start,end,create_grph(maze))
def display_path(maze,path):
    if(path==None):
        print('path not found')
        return
    for p in path:
        maze[p[0]][p[1]] = "_"
    display_maze(maze)


