file = open('day 6/input.txt', 'r')
lines = file.readlines()
file.close()

guard = [0, 0]
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == '^':
            guard = [i, j]
lines[guard[0]] = lines[guard[0]].replace('^', '.')
# print(f"Guard: {guard}")
# print(f"Lines: {lines}")    

def guard_navigation(guard, lines, added_obstacle=None):
    pos_i, pos_j = guard
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    go = 'up'
    next_dir = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    distinct = set() 
    visited_with_direction = set() 
    
    distinct.add((pos_i, pos_j))
    visited_with_direction.add((pos_i, pos_j, go))


    if added_obstacle:
        i, j = added_obstacle
        lines = [list(row) for row in lines]  
        lines[i][j] = '#'
        lines = [''.join(row) for row in lines] 

    for _ in range(10000):
        if pos_i + directions[go][0] < 0 or pos_i + directions[go][0] >= len(lines) or pos_j + directions[go][1] < 0 or pos_j + directions[go][1] >= len(lines[0]):
            break

        next_i = pos_i + directions[go][0]
        next_j = pos_j + directions[go][1]

        if lines[next_i][next_j] == '#':
            go = next_dir[go]
            next_i = pos_i + directions[go][0]
            next_j = pos_j + directions[go][1]
        

        if lines[next_i][next_j] == '.':
            pos_i, pos_j = next_i, next_j
            distinct.add((pos_i, pos_j))
            if (pos_i, pos_j, go) in visited_with_direction:
                return True 
            visited_with_direction.add((pos_i, pos_j, go))

    return False  # No loop found

def find_loop_positions(guard, lines):
    loop_positions = []

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.': 
                if guard_navigation(guard, lines, added_obstacle=(i, j)):
                    print(f"Loop found when obstacle at {i}, {j}")
                    loop_positions.append((i, j))

    return len(loop_positions)

loop_positions = find_loop_positions(guard, lines)
print("Positions that cause a loop:", loop_positions)
