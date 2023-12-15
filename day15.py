import aoc_tools as at
at.setup()

file = open('test_input.txt')

for line in file:
    data= line.strip().split(',')

def helper(string):
    hash_val = 0
    for s in string:
        hash_val += ord(s)
        hash_val *= 17
        hash_val %= 256
    return hash_val


res = 0

for item in data:
    res += helper(item)

print(res)



test = 'abcd'

print(test[:len(test)-1])
print(test[-1])

test2 = 'abc=3'
idx = test2.index('=')
label = test2[:idx]
print(label)

# p2
boxes = [{} for _ in range(256)]

for item in data:
    
    if item.find('=') == -1:
        label = item[:len(item) - 1]
        box_n = helper(label)
        if boxes[box_n]:
            if label in boxes[box_n]:
                del boxes[box_n][label]
        # add code here for removal

    else:
        idx = item.index('=')
        label = item[:idx]
        fl = item[-1]
        # code for add
        box_n = helper(label)
        boxes[box_n][label] = fl


res2 = 0

for i in range(len(boxes)):
    if boxes[i]:
        j = 1
        for val in boxes[i].values():
            res2 += ((i+1) * j * int(val))
            j +=1

print(res2)