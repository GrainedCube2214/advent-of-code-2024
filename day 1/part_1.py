file = open('day 1/input.txt', 'r')
lines = file.readlines()
file.close()
lines = [line.split() for line in lines]
l1 = []
l2 = []
for line in lines:
    l1.append(int(line[0]))
    l2.append(int(line[1]))
l1.sort()
l2.sort()
sum = 0
for i in range(len(l1)):
    sum+= abs(l1[i]-l2[i])
print(sum)