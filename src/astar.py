import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    cost = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        neighbors = [
            (current[0]+1, current[1]),
            (current[0]-1, current[1]),
            (current[0], current[1]+1),
            (current[0], current[1]-1)
        ]

        for n in neighbors:
            x, y = n
            if 0 <= x < grid.rows and 0 <= y < grid.cols:
                if grid.is_obstacle(n):
                    continue

                new_cost = cost[current] + 1
                if n not in cost or new_cost < cost[n]:
                    cost[n] = new_cost
                    priority = new_cost + heuristic(goal, n)
                    heapq.heappush(open_list, (priority, n))
                    came_from[n] = current

    path = []
    cur = goal
    while cur != start:
        path.append(cur)
        cur = came_from.get(cur, start)
    path.append(start)
    path.reverse()
    return path
