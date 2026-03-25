import numpy as np

grid = np.zeros((3, 3))
gamma = 0.9

def reward(x, y):
    if (x, y) == (2, 2):
        return 10
    return -1

for _ in range(20):
    new_grid = grid.copy()
    for i in range(3):
        for j in range(3):
            actions = []
            
            for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < 3 and 0 <= nj < 3:
                    actions.append(reward(ni, nj) + gamma * grid[ni][nj])
            
            if actions:
                new_grid[i][j] = max(actions)
    
    grid = new_grid

print(grid)