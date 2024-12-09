file = open('day 1/input.txt', 'r')
lines = file.readlines()
file.close()
lines = [line.split() for line in lines]
l1 = []
l2 = []
for line in lines:
    l1.append(int(line[0]))
    l2.append(int(line[1]))
sum = 0
for i in l1:
    sum+=i*l2.count(i)
print(sum)