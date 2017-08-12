# ----------
# User Instructions:
#
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal.
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0]]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1  # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def compute_value(grid, goal, cost):
    value_grid = [[0] * len(grid[0]) for row in range(len(grid))]
    closed_grid = [[False] * len(grid[0]) for row in range(len(grid))]

    count = 0
    open = [goal]

    rows_total = len(grid)
    cols_total = len(grid[0])

    while len(open) > 0:
        new_open = []
        for i in range(len(open)):
            cell = open.pop()
            row = cell[0]
            col = cell[1]
            closed_grid[row][col] = True
            value_grid[row][col] = count
            for move in delta:
                row_delta, col_delta = move
                new_row = row - row_delta
                new_col = col - col_delta
                if 0 <= new_row < rows_total and 0 <= new_col < cols_total and grid[new_row][new_col] != 1 and not (
                        closed_grid[new_row][new_col]):
                    new_open.append([new_row, new_col])

        count += cost
        open = new_open

    for row in range(len(value_grid)):
        for col in range(len(value_grid[0])):
            if grid[row][col] == 1 or (value_grid[row][col] == 0 and not (row == goal[0] and col == goal[1])):
                value_grid[row][col] = 99

    return value_grid


res = compute_value(grid, goal, cost)
for row in res:
    print row
