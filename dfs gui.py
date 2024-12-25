import pygame
import sys
from alg import solve_with_dfs, solve_with_bfs,node
pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 60
ROWS, COLS = 10, 10

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

maze = [
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
]

start = None
end = None


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver")

def draw_maze():
    for row in range(ROWS):
        for col in range(COLS):
            color = WHITE if maze[row][col] == 0 else BLACK
            if start and (row, col) == (start.x, start.y):
                color = RED
            elif end and (row, col) == (end.x, end.y):
                color = GREEN
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def draw_path(path):
    for position in path:
        x, y = position[1], position[0]
        pygame.draw.rect(screen, GREEN, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def main():
    global start, end
    running = True
    solved = False
    path = []

    while running:
        screen.fill(WHITE)
        draw_maze()

        if solved and path:
            draw_path(path)
        
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                col, row = x // CELL_SIZE, y // CELL_SIZE
                if maze[row][col] == 0:
                    if not start:
                        start = node(row, col)
                    elif not end:
                        end = node(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and start and end: 
                    path = solve_with_dfs(node(start.x, start.y),node(end.x, end.y), maze)
                    solved = True
                    if not path:
                        print("no solution found")
                if event.key == pygame.K_b and start and end: 
                    path = solve_with_bfs(node(start.x, start.y),node(end.x, end.y), maze)
                    solved = True
                    if not path:
                        print("no solution found")
                elif event.key == pygame.K_r: 
                    solved = False
                    path = []
                    start = None
                    end = None
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()