import aoc_tools


aoc_tools.setup()
data = aoc_tools.load_input(1, 2023)

#p2

#this is needed (one = o1e) instead of 1 as in the string the start and end of the number string can be "double dipped" (eightwo)
num_map = {'one':"o1e", 'two': "t2o", 'three':"t3e", 'four': "f4r", 'five' : "f5e", 'six':"s6x", 'seven': "s7n", 'eight' : "e8t", 'nine': "n9e"}
num_trie = aoc_tools.Trie()
num_trie.insert('one')
num_trie.insert('two')
num_trie.insert('three')
num_trie.insert('four')
num_trie.insert('five')
num_trie.insert('six')
num_trie.insert('seven')
num_trie.insert('eight')
num_trie.insert('nine')

# p1

print(num_map.keys())
res = 0
for r in data:
    tmp = []
    
    for c in r:

        if c.isnumeric():
           tmp.append(c)
        # print(str(res) + ":" + tmp[0] + " " + tmp[len(tmp) - 1])
    res += int(tmp[0] + tmp[len(tmp) - 1])

print(f'Day 1 Part 1: {res}')


data_cleaned = []
for r in data:
    for key in num_map.keys():
        r = r.replace(key, num_map[key])
    data_cleaned.append(r)

res = 0
for r in data_cleaned:
    tmp = []
    
    for c in r:

        if c.isnumeric():
           tmp.append(c)
        # print(str(res) + ":" + tmp[0] + " " + tmp[len(tmp) - 1])
    res += int(tmp[0] + tmp[len(tmp) - 1])

print(f'Day 1 Part 2: {res}')

# print(data_cleaned[3])
#p2








