import heapq
GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x, y = divmod(val - 1, 3)
                dist += abs(x - i) + abs(y - j)
    return dist

def neighbors(state):
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, val in enumerate(row) if val == 0][0]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state
def a_star(start):
    queue = [(manhattan(start), 0, start, [])]
    visited = set()
    
    while queue:
        _, cost, state, path = heapq.heappop(queue)
        if state == GOAL:
            return path + [state]
        
        visited.add(tuple(tuple(row) for row in state))
        for neighbor in neighbors(state):
            if tuple(tuple(row) for row in neighbor) not in visited:
                heapq.heappush(queue, (cost + 1 + manhattan(neighbor), cost + 1, neighbor, path + [state]))

initial_state = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
solution = a_star(initial_state)

for step in solution:
    for row in step:
        print(row)
    print()
