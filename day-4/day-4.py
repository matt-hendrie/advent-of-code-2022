count = 0
count_2 = 0
with open('input.txt', 'r') as f:
    for line in f:
        pair_1 = line.strip().split(",")[0].replace("-"," ")
        pair_2 = line.strip().split(",")[1].replace("-"," ")
        #check if pair_2 is in range of pair 1
        if int(pair_1.split()[0]) <= int(pair_2.split()[0]) <= int(pair_2.split()[1]) <= int(pair_1.split()[1]):
            count += 1
        elif int(pair_2.split()[0]) <= int(pair_1.split()[0]) <= int(pair_1.split()[1]) <= int(pair_2.split()[1]):
            count += 1
        for x in range(int(pair_1.split()[0]), int(pair_1.split()[1])+1):
            if x in range(int(pair_2.split()[0]), int(pair_2.split()[1])+1):
                count_2 += 1
                break
print(count, count_2)