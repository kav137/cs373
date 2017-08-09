# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

# KAV: 1) we have to add a mechanism of sorting which would allow to expand cells with the smallest value first
#       2) cost is not equal to the delta of step
grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]

init = [0, 0]
goal = [len(grid) - 1, len(grid[0]) - 1]
cost = 1

delta = [[-1, 0],  # go up
         [0, -1],  # go left
         [1, 0],  # go down
         [0, 1]]  # go right

delta_name = ['^', '<', 'v', '>']


def search(grid, init, goal, cost):
    expand = [[0, init[0], init[1]]]
    expand_next = []
    path = False

    while path is False:
        for cell_to_expand in expand:
            cell_path, cell_y, cell_x = cell_to_expand
            grid[cell_y][cell_x] = -1
            for movement in delta:
                movement_y, movement_x = movement
                target_cell_y, target_cell_x = [cell_y + movement_y, cell_x + movement_x]
                if (len(grid) > target_cell_y >= 0 and len(grid[0]) > target_cell_x >= 0
                    and grid[target_cell_y][target_cell_x] == 0):
                    expand_next.append([cell_path + cost, target_cell_y, target_cell_x])
                    grid[target_cell_y][target_cell_x] = -1

        if len(expand_next) == 0:
            path = 'fail'
            # exit(0) this line is not accepted when using cs373's course validation

        for result in expand_next:
            length, x, y = result
            if x == goal[0] and y == goal[1]:
                path = result

        expand = expand_next
        expand_next = []

    return path


print search(grid, init, goal, cost)
