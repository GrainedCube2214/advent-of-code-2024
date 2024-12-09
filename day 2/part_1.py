file = open('day 2/input.txt', 'r')
lines = file.readlines()
file.close()
lines = [[int(num) for num in line.split()] for line in lines]

def issafe(report):
    if not (sorted(report) == report or sorted(report, reverse=True) == report): 
        # print('No consistent increase or decrease') 
        return False
    for i in range(len(report)-1):
        if abs(report[i]-report[i+1]) <= 3 and abs(report[i]-report[i+1])>=1:
            continue
        else:
            # print(f'Difference between two numbers {report[i]}, {report[i+1]} is not between 1 and 3')
            return False
    return True

count = 0
for line in lines:
    if issafe(line):
        count+=1
print(count)