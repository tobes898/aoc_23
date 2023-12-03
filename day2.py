import aoc_tools


aoc_tools.setup()
data = aoc_tools.load_input(2, 2023)

# data = aoc_tools.load_test_input()


# remove game n: from input
# indexes will be handled by index in list + 1

# replace all semicolons and commas
res = 0
res2 = 0
maxes = {'red':12, 'green':13, 'blue':14}
cleaned_1 = []
for line in data:
    # no game:
    tmp = line[line.index(':')+1:].strip()
    tmp = tmp.replace(';', '')
    tmp = tmp.replace(',', '')
    cleaned_1.append(tmp)

for index, line in enumerate(cleaned_1):
    tmp = line.split(' ')
    tracker = {'red': 0, 'green': 0, 'blue': 0}
    i = 0
    flag = False
    while i < len(tmp) - 1:
        num = int(tmp[i])
        color = tmp[i+1]
        tracker[color] = max(num, tracker[color])
        if num > maxes[color]:
            flag = True
            # break
        i += 2
    if not flag:
        res += index + 1
    power = 1
    for value in tracker.values():
        power *= value
    res2 += power

print(res)
print(res2)