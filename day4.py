import aoc_tools

aoc_tools.setup()
data = aoc_tools.load_input(4, 2023)
# data = aoc_tools.load_test_input()


cleaned_data = []
res = 0
for line in data:
    count = 0
    line = line[line.index(':') + 2:].strip(' ')
    tmp = line.split('|')
    row = []
    for item in tmp:
        row.append(item.split())
    
    cleaned_data.append(row)

print(cleaned_data)
res = 0
for line in cleaned_data:
    win = line[0]
    real = line[1]

    count = 0
    for val in real:
        if val in win:
            if count == 0:
                count +=1
            else:
                count += count
    
    res += count
print(res)

res = 1

copies = []
for i in range(len(cleaned_data)):
    tmp = cleaned_data[i]
    win = tmp[0]
    real = tmp[1]
    count = 0
    for val in real:
        if val in win:
            count += 1
    copies.append([i+1, count, 1])

print(copies)

for card, count, copy in copies:
    for i in range(count):
        copies[card + i][2] += copy

res2 = 0
for card, count, copy in copies:
    res2 += copy

print(res2)