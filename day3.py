import aoc_tools

aoc_tools.setup()
data = aoc_tools.load_input(3, 2023)
# data = aoc_tools.load_test_input()

schematic = []

for row in data:
    col = []
    for item in row:
        col.append(item)
    schematic.append(col)

# print(schematic)

# need way to track numbers found
# need way to search for symbols that are not periods near numbers *can be diagonal*
# search:
# x + 1 ; x - 1; 
# y + 1; y - 1; 
# (x + 1, y + 1); (x - 1, y + 1); 
# (x + 1, y - 1); (x - 1 ; y - 1)
# only search if number at cord

# 1) find all numbers in row
# 2) when numeric found save in list i,j to be used for search
def search(coords, arr):
    # valid result if char found is not numeric or '.'
    symbol_flag = False
    gear_flag = (False,[])
    for y, x in coords:
        x1 = x + 1
        x2 = x - 1
        y1 = y + 1
        y2 = y - 1
        
        # x + 1  
        if x1 <len(arr[0]):
            symbol_flag = not arr[y][x1].isnumeric() and arr[y][x1] != '.'
            if symbol_flag:
                if arr[y][x1] == '*':
                    gear_flag = (True, (y, x1))
                break
            if y1 < len(arr):
                # y + 1
                symbol_flag = not arr[y1][x].isnumeric() and arr[y1][x] != '.'
                if symbol_flag:
                    if arr[y1][x] == "*":
                        gear_flag = (True, (y1, x))
                    break
                # (x + 1, y + 1)
                symbol_flag = not arr[y1][x1].isnumeric() and arr[y1][x1] != '.'
                if symbol_flag:
                    if arr[y1][x1] == "*":
                        gear_flag = (True, (y1, x1))
                    break

            if y2 > - 1:
                # y - 1
                symbol_flag = not arr[y2][x].isnumeric() and arr[y2][x] != '.'
                if symbol_flag:
                    if arr[y2][x] == "*":
                        gear_flag = (True, (y2, x))
                    break
                # x + 1; y - 1
                symbol_flag = not arr[y2][x1].isnumeric() and arr[y2][x1] != '.'
                if symbol_flag:
                    if arr[y2][x1] == "*":
                        gear_flag = (True, (y2, x1))
                    break
        # x - 1
        if x2 > -1:
            symbol_flag = not arr[y][x2].isnumeric() and arr[y][x2] != '.'
            if symbol_flag:
                if arr[y][x2] == "*":
                    gear_flag = (True, (y, x2))
                break
            
            if y1 < len(arr):
                # y + 1
                symbol_flag = not arr[y1][x].isnumeric() and arr[y1][x] != '.'
                if symbol_flag:
                    if arr[y1][x] == "*":
                        gear_flag = (True, (y1, x))
                    break
                # (x - 1, y + 1)
                symbol_flag = not arr[y1][x2].isnumeric() and arr[y1][x2] != '.'
                if symbol_flag:
                    if arr[y1][x2] == "*":
                        gear_flag = (True, (y1,x2))
                    break

            if y2 > - 1:
                # y - 1
                symbol_flag = not arr[y2][x].isnumeric() and arr[y2][x] != '.'
                if symbol_flag:
                    if arr[y2][x] == "*":
                        gear_flag = (True, (y2, x))
                    break
                # x - 1; y - 1
                symbol_flag = not arr[y2][x2].isnumeric() and arr[y2][x2] != '.'
                if symbol_flag:
                    if arr[y2][x2] == "*":
                        gear_flag = (True, (y2, x2))
                    break

    return symbol_flag, gear_flag

overall_num = []
for i in range(len(data)):
    r_num = []
    coords = []
    number = ""
    for j in range(len(data[0])):
        if data[i][j].isnumeric():
            number += data[i][j]
            coords.append([i,j])
        else:
            if number:
                r_num.append((number, coords))
            number = ""
            coords = []
    
    if number:
        r_num.append((number, coords))
    overall_num.append(r_num)

# num, coords = overall_num[0][1]

# print(search(coords, data))

# print(overall_num)
res = 0
gear_map = {} # (coords) : [nums]
for row in overall_num:
    for num, coords in row:

        valid, gear_info = search(coords, data)
        if valid:
            res += int(num)

        gear_found, coords = gear_info
        if gear_found:
            if coords not in gear_map:
                gear_map[coords] = [num]
            else:
                gear_map[coords].append(num)

print(f"p1: {res}")
res2 = 0
for key in gear_map.keys():
    if len(gear_map[key]) == 2:
        tmp = 1
        for val in gear_map[key]:
            tmp *= int(val)
        res2 += tmp

print(f"p2: {res2}") 


# when number finds * increment key by one
# any key that has 2 is then values to put together

# search arounds star if numeric found add that coord to list and increment key by one
# all keys == 2, loop through number/coord list and find the numbers and put together for solution


