total = 0
with open('input.txt', 'r') as f:
    for line in f:
        round = line.strip().split(' ')
        if round[0] == 'A':
            if round[1] == 'X':
                total += 3
            if round[1] == 'Y':
                total += 4
            if round[1] == 'Z':
                total += 8
        if round[0] == 'B':
            if round[1] == 'X':
                total += 1
            if round[1] == 'Y':
                total += 5
            if round[1] == 'Z':
                total += 9
        if round[0] == 'C':
            if round[1] == 'X':
                total += 2
            if round[1] == 'Y':
                total += 6
            if round[1] == 'Z':
                total += 7
print(total)