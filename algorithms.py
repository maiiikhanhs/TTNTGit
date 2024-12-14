import heapq
import time
import pygame
from maze import draw_maze
from config import FPS

# BFS with visualization
def bfs_visual(maze, start, end, screen):
    rows, cols = len(maze), len(maze[0])
    queue = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}
    start_time = time.time()

    while queue:
        current = queue.pop(0)
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            elapsed_time = time.time() - start_time
            return path[::-1], len(visited), elapsed_time

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
                queue.append((r, c))
                visited.add((r, c))
                parent[(r, c)] = current
        draw_maze(screen, maze, visited, [], current, start, end)
        pygame.time.delay(50)

    elapsed_time = time.time() - start_time
    return [], len(visited), elapsed_time

# DFS with visualization
def dfs_visual(maze, start, end, screen):
    rows, cols = len(maze), len(maze[0])
    stack = [start]
    visited = set()
    visited.add(start)
    parent = {start: None}
    start_time = time.time()

    while stack:
        current = stack.pop()
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            elapsed_time = time.time() - start_time
            return path[::-1], len(visited), elapsed_time

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = current[0] + dr, current[1] + dc
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0 and (r, c) not in visited:
                stack.append((r, c))
                visited.add((r, c))
                parent[(r, c)] = current
        draw_maze(screen, maze, visited, [], current, start, end)
        pygame.time.delay(50)

    elapsed_time = time.time() - start_time
    return [], len(visited), elapsed_time

# A* with visualization
def a_star_visual(maze, start, end, screen):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    rows, cols = len(maze), len(maze[0])
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {start: None}
    g_score = {start: 0}
    visited = set()
    start_time = time.time()

    while open_set:
        _, current = heapq.heappop(open_set)
        visited.add(current)

        if current == end:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            elapsed_time = time.time() - start_time
            return path[::-1], len(visited), elapsed_time

        for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            r, c = current[0] + dr, current[1] + dc
            neighbor = (r, c)
            if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 0:
                tentative_g_score = g_score[current] + 1
                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    heapq.heappush(open_set, (tentative_g_score + heuristic(neighbor, end), neighbor))
        draw_maze(screen, maze, visited, [], current, start, end)
        pygame.time.delay(50)

    elapsed_time = time.time() - start_time
    return [], len(visited), elapsed_time
