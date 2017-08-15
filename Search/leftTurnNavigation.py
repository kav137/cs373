# ----------
# User Instructions:
#
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's
# optimal path to the position specified in goal;
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a
# right turn.

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

forward = [[-1, 0],  # go up
           [0, -1],  # go left
           [1, 0],  # go down
           [0, 1]]  # go right
forward_name = ['up', 'left', 'down', 'right']
# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']
init = [4, 3, 0]  # given in the form [row,col,direction]
# direction = 0: up
#             1: left
#             2: down
#             3: right
goal = [2, 0]  # given in the form [row,col]
cost = [2, 1, 20]  # cost has 3 values, corresponding to making


# a right turn, no turn, and a left turn


def optimum_policy2D(grid, init, goal, cost):
    target_x, target_y = goal
    found = False

    rows_total = len(grid)
    cols_total = len(grid[0])

    policy2D = [[' '] * cols_total for row in range(rows_total)]
    actions_grid = [[[] for col in range(cols_total)] for row in range(rows_total)]  # storage for actions we perform
    m_costs_grid = [[999] * cols_total for row in range(rows_total)]  # movement
    h_costs_grid = [[999] * cols_total for row in range(rows_total)]  # heuristic

    # fill the heuristics grid
    h_open_cells = [[0, target_x, target_y]]
    while len(h_open_cells) > 0:
        count, h_x, h_y = h_open_cells.pop()
        if h_costs_grid[h_x][h_y] > count:
            h_costs_grid[h_x][h_y] = count
            for i in range(len(forward)):
                x_delta, y_delta = forward[i]
                x2 = h_x + x_delta
                y2 = h_y + y_delta
                if 0 <= x2 < rows_total and 0 <= y2 < cols_total and grid[x2][y2] != 1:
                    h_open_cells.append([count + 1, x2, y2])

    for r in h_costs_grid:
        print r
    print '********'

    init_x, init_y, init_theta = init

    # there are three type of costs: movement (m_cost); h_costs_grid (h_cost); total (t_cost)
    # t_cost is used for comparison
    init_m_cost = 0
    init_h_cost = h_costs_grid[init_x][init_y]
    init_t_cost = init_m_cost + init_h_cost

    m_costs_grid[init_x][init_y] = init_m_cost
    open_cells = [[init_t_cost, init_m_cost, init_x, init_y, init_theta, None, None]]

    while len(open_cells) > 0 and not found:
        open_cells.sort()
        open_cells.reverse()

        cell = open_cells.pop()
        t_cost1, m_cost1, x1, y1, theta1, prev_action_name, prev_movement = cell

        (actions_grid[x1][y1]).append([prev_action_name, prev_movement])

        if x1 == target_x and y1 == target_y:
            found = True

        else:
            for i in range(len(action)):
                current_action = action[i]
                current_action_name = action_name[i]

                theta2 = (theta1 + current_action) % len(forward)
                movement_to_apply = forward[theta2]

                x2 = x1 + movement_to_apply[0]
                y2 = y1 + movement_to_apply[1]

                if 0 <= x2 < rows_total and 0 <= y2 < cols_total and grid[x2][y2] != 1:
                    m_cost2 = m_cost1 + cost[i]
                    m_costs_grid[x2][y2] = m_cost2
                    t_cost2 = m_cost2 + h_costs_grid[x2][y2]
                    open_cells.append([t_cost2, m_cost2, x2, y2, theta2, current_action_name, movement_to_apply])

    # building path
    next_action, next_reverse_movement = actions_grid[target_x][target_y].pop()
    policy2D[target_x][target_y] = '*'
    x1 = target_x
    y1 = target_y
    while next_reverse_movement:
        x_delta, y_delta = next_reverse_movement
        x1 -= x_delta
        y1 -= y_delta
        policy2D[x1][y1] = next_action
        next_action, next_reverse_movement = actions_grid[x1][y1].pop()

    return [actions_grid, m_costs_grid, policy2D]


result = optimum_policy2D(grid, init, goal, cost)

for res_grid in result:
    for row in res_grid:
        print row
    print '***********'

    # EXAMPLE OUTPUT:
    # calling optimum_policy2D with the given parameters should return
    # [[' ', ' ', ' ', 'R', '#', 'R'],
    #  [' ', ' ', ' ', '#', ' ', '#'],
    #  ['*', '#', '#', '#', '#', 'R'],
    #  [' ', ' ', ' ', '#', ' ', ' '],
    #  [' ', ' ', ' ', '#', ' ', ' ']]
    # ----------
