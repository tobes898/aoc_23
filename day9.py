import aoc_tools as at

at.setup()
# data = at.load_test_input()
data = at.load_input(day=9, year=2023)




def build_sequence(start, p2):
    res_seq = calc_diff(start, p2)
    if p2:
        return start[0] - res_seq[0]
    else:
        return res_seq[-1] + start[-1]    

def calc_diff(seq, p2):
    res = []
    diffs = set()
    for i in range(len(seq) - 1):
        a = seq[i]
        b = seq[i+1]
        diffs.add(b-a)
        res.append(b-a)

    #base case of all zeros reached
    # return seq with extra zero
    if len(diffs) == 1 and 0 in diffs:
        if p2:
            res.insert(0, 0)
        else:
            res.append(0)
        return res
    
    # add the value of  the last value of prev sequnce
    # and the last val of current seq and return
    prev_seq = calc_diff(res, p2)
    if p2:
        val = res[0] - prev_seq[0]
        res.insert(0, val)
    else:
        res.append(prev_seq[-1] + res[-1]) 
    return res


#test calc diff
res_p1 = 0
res_p2 = 0
for line in data:
    start = [int(n) for n in line.split()]
    res_p1 += build_sequence(start, False)
    res_p2 += build_sequence(start, True)
print(res_p1)
print(res_p2)