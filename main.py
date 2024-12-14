import pygame
from maze import generate_maze, draw_maze
from algorithms import bfs_visual, dfs_visual, a_star_visual
from config import FPS, CELL_SIZE

# Hàm chính
def main():
    pygame.init()
    print("Xin chào đây là dự án của Nhóm 8")
    rows, cols = 20, 20
    maze, start, end = generate_maze(rows, cols)

    screen = pygame.display.set_mode((cols * CELL_SIZE, rows * CELL_SIZE))
    pygame.display.set_caption("Maze Solver Visualization")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    path, visited, elapsed_time = bfs_visual(maze, start, end, screen)
                    print(f"BFS - Time: {elapsed_time:.4f}s, Visited Nodes: {visited}, Path Length: {len(path)}")

                if event.key == pygame.K_2:
                    path, visited, elapsed_time = dfs_visual(maze, start, end, screen)
                    print(f"DFS - Time: {elapsed_time:.4f}s, Visited Nodes: {visited}, Path Length: {len(path)}")

                if event.key == pygame.K_3:
                    path, visited, elapsed_time = a_star_visual(maze, start, end, screen)
                    print(f"A* - Time: {elapsed_time:.4f}s, Visited Nodes: {visited}, Path Length: {len(path)}")

        draw_maze(screen, maze, [], [], start, start, end)
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
