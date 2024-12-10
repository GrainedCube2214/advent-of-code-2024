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

def guard_navigation(guard, lines):
    pos_i, pos_j = guard
    directions = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}
    go = 'up'
    next_dir = {'up': 'right', 'right': 'down', 'down': 'left', 'left': 'up'}
    distinct = set()
    distinct.add((pos_i, pos_j))
    while True:
        if pos_i+directions[go][0] < 0 or pos_i+directions[go][0] >= len(lines) or pos_j+directions[go][1] < 0 or pos_j+directions[go][1] >= len(lines[0]):
            break
        if lines[pos_i+directions[go][0]][pos_j+directions[go][1]] == '.':
            pos_i += directions[go][0]
            pos_j += directions[go][1]
            distinct.add((pos_i, pos_j))
        elif lines[pos_i+directions[go][0]][pos_j+directions[go][1]] == '#':
            print(f"wall found at {pos_i+directions[go][0]}, {pos_j+directions[go][1]}, moving {next_dir[go]}")
            go = next_dir[go]
            pos_i += directions[go][0]
            pos_j += directions[go][1]
            distinct.add((pos_i, pos_j))
        # if new position is out of bounds, break the loop
        print(f"current position: {pos_i}, {pos_j}")
    print("\n======\n")
    return len(distinct)


print(guard_navigation(guard, lines))