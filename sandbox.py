source_grid = [
    [0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1]

]

shadow_grid = [[-1] * len(source_grid[0]) for i in range(len(source_grid))]

print shadow_grid
