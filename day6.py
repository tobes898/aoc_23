import aoc_tools

# data = aoc_tools.load_test_input()
aoc_tools.setup()
data = aoc_tools.load_input(day=6, year=2023)

#time
tmp = data[0][data[0].index(':') + 1:].split()
time = [int(x) for x in tmp]

#distance
tmp = data[1][data[1].index(':') + 1:].split()
distance = [int(x) for x in tmp]

#time
timep2 = int(data[0][data[0].index(':') + 1:].replace(' ',''))
# timep2 = [int(x) for x in tmp]
print(timep2)
#distance
distancep2 = int(data[1][data[1].index(':') + 1:].replace(' ',''))



res = 1
test = []
for i in range(len(time)):
    ways_to_win = 0
    time_to_beat = distance[i]
    speed = None
    for j in range(1, time[i], 1):
        if not speed:
            speed = 1
        else:
            speed += 1
        
        time_left = time[i] - j
        race_dist = time_left * speed
        if race_dist > time_to_beat:
            ways_to_win += 1
    res *= ways_to_win

print(res)

res2 = 1

ways_to_win = 0
time_to_beat = distancep2
speed = None
for j in range(1, timep2, 1):
    if not speed:
        speed = 1
    else:
        speed += 1
    
    time_left = timep2 - j
    race_dist = time_left * speed
    if race_dist > time_to_beat:
        ways_to_win += 1
res2 = ways_to_win

print(res2)