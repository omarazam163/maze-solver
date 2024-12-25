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
    i = point[0] 
    j = point[1]
    max_col = len(maze[0])
    max_row = len(maze)
    if(i-1>=0 and j>=0): #up
        if(check_zero(maze[i-1][j])):
            neighbors.append((i-1,j))
    if(i>=0 and j-1>=0):  #left
        if(check_zero(maze[i][j-1])):
            neighbors.append((i,j-1))
    if(i+1<max_row and j<max_col): #down
        if(check_zero(maze[i+1][j])):
            neighbors.append((i+1,j))
    if(i<max_row and j+1<max_col):  # right 
        if(check_zero(maze[i][j+1])):
            neighbors.append((i,j+1))
    return neighbors
    
        
def create_grph(maze):
    graph = {}
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if(maze[i][j] == 0):
                graph[(i,j)]= get_nighbors((i,j),maze)
    return graph


def dfs(start, end, graph: dict):
    stack = [start]
    visited = set()
    start.path = [] 
    while len(stack) > 0:
        current_node = stack.pop()
        if (current_node.x, current_node.y) == (end.x, end.y):
            return current_node.path + [(current_node.x, current_node.y)]
        if (current_node.x, current_node.y) not in visited:
            visited.add((current_node.x, current_node.y))
            neighbors = list(map(lambda nn: node(nn[0], nn[1]), reversed(graph.get((current_node.x, current_node.y), []))))
            for neighbor in neighbors:
                if (neighbor.x, neighbor.y) not in visited and neighbor not in stack:
                    neighbor.path = current_node.path + [(current_node.x, current_node.y)]
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


