file = open('day 5/input.txt', 'r')
lines = file.readlines()
file.close()

rules=[]
sequences=[]
for line in lines:
    if '|' in line:
        line = line.split('|')
        line[-1] = line[-1].strip('\n')
        line = [int(i) for i in line]
        rules.append((line[0], line[1]))
    elif ',' in line:
        line = line.split(',')
        line[-1] = line[-1].strip('\n')
        line = [int(i) for i in line]
        sequences.append(line)

def check_sequence(sequence, rules):
    for i in range(len(sequence)):
        for j in rules:
            if sequence[i] == j[0]:
                if j[1] in sequence[:i]:
                    return False
            if sequence[i] == j[1]:
                if j[0] in sequence[i+1:]:
                    return False
    return True

def find_middle(array):
    if len(array)%2==0:
        return array[len(array)//2-1]
    else:
        return array[len(array)//2]
    
from collections import deque, defaultdict

def fix_sequence(sequence, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    all_elements = set()

    for x, y in rules:
        graph[x].append(y)
        in_degree[y] += 1
        if x not in in_degree:
            in_degree[x] = 0
        all_elements.add(x)
        all_elements.add(y)

    queue = deque([node for node in all_elements if in_degree[node] == 0])
    topological_order = []

    while queue:
        node = queue.popleft()
        topological_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topological_order) != len(all_elements):
        raise ValueError("There exists a cycle in the precedence rules (invalid input)")

    element_position = {element: index for index, element in enumerate(topological_order)}

    sorted_sequence = sorted(sequence, key=lambda x: element_position.get(x, float('inf')))
    
    return sorted_sequence

count=0
print('----')
for sequence in sequences:
    if not check_sequence(sequence, rules):
        print(sequence," -> ",fix_sequence(sequence, rules))
        sequence = fix_sequence(sequence, rules)
        count+=find_middle(sequence)
print("----")
print(count)