input = []
with open('input.txt', 'r') as f:
    for line in f:
        input.append(line.strip())

total = 0
sumArr = []
for x in input:
    if x != '':
        total += int(x)
    else:
        sumArr.append(total)
        total = 0

#Part 1 Answer
print(max(sumArr))

#Part 2 Answer
sumArr.sort(reverse=True)
sumArr = sumArr[:3]
print(sum(sumArr))