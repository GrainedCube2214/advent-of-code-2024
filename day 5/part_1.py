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

count=0
for sequence in sequences:
    if check_sequence(sequence, rules):
        count+=find_middle(sequence)
print(count)