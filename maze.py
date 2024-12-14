import pygame
import numpy as np
from config import WHITE, BLACK, YELLOW, BLUE, GREEN, RED, CELL_SIZE

# Hàm vẽ mê cung và kết quả
def draw_maze(screen, maze, visited, path, current, start, end):
    rows, cols = len(maze), len(maze[0])
    screen.fill(WHITE)

    for r in range(rows):
        for c in range(cols):
            color = WHITE if maze[r][c] == 0 else BLACK
            pygame.draw.rect(screen, color, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for r, c in visited:
        pygame.draw.rect(screen, YELLOW, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    for r, c in path:
        pygame.draw.rect(screen, BLUE, (c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    pygame.draw.rect(screen, GREEN, (current[1] * CELL_SIZE, current[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (start[1] * CELL_SIZE, start[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (end[1] * CELL_SIZE, end[0] * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    pygame.display.flip()

# Hàm tạo mê cung
def generate_maze(rows, cols):
    maze = np.random.choice([0, 1], size=(rows, cols), p=[0.7, 0.3])
    maze[0][0] = 0
    maze[rows - 1][cols - 1] = 0
    return maze, (0, 0), (rows - 1, cols - 1)
