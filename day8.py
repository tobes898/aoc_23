import aoc_tools as at
from itertools import count
at.setup()
# data = at.load_test_input()
data = at.load_input(day=8, year=2023)

t_seq = [c for c in data[0]]
seq = []
for i in t_seq:
    seq.append(0 if i == 'L' else 1)
seq_c = 0
seq_l = len(seq)
# move to instruction set
data = data[2:]


i_lookup = {}
# key = (left val, right val)

for line in data:
    tmp = line.split()
    key = tmp[0]
    left_val = tmp[2].replace('(','').replace(',','')
    right_val = tmp[3].replace(')','')
    i_lookup[key] = [left_val, right_val]

# reach end of seq 

seq_c = 0
res = 0
#loop terminates when ZZZ is reached
# set curr node to start key
c_node = list(i_lookup.keys())[0]



res = 0
for step in count():
    if c_node == 'ZZZ':
        res = step
        break
    curr_seq = seq[step % seq_l]
    c_node = i_lookup[c_node][curr_seq]


# while c_node != 'ZZZ':
#     # add to steps req
#     res+=1 
#     curr_seq = seq[seq_c % seq_l]
#     c_node = i_lookup[c_node][curr_seq]
#     seq_c += 1
#     print(c_node)

print(res)