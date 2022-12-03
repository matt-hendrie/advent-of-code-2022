import string

values = dict()
for index, letter in enumerate(string.ascii_letters):
    values[letter] = index + 1

total = 0
total_2 = 0
batch = []
with open('input.txt', 'r') as f:
    for line in f:
        line = line.strip()
        shared = ''.join(sorted(set.intersection(set(line[:len(line)//2]), set(line[len(line)//2:]))))
        total += sum(values[letter] for letter in shared)
        batch.append(set(line))
        if len(batch) == 3:
            matched = ''.join(sorted(set.intersection(*batch)))
            total_2 += sum(values[letter] for letter in matched)
            batch.clear()

print(total, total_2)
