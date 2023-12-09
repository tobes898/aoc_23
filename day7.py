import aoc_tools

aoc_tools.setup()

# data = aoc_tools.load_test_input()
data = aoc_tools.load_input(day=7, year=2023)


letter_map = {'A':14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
def hand_strength(hand) -> int:
    tracker = {}
    for card in hand:
        if card not in tracker:
            tracker[card] = 1
        else:
            tracker[card] += 1

    # determine relative strength
    two_flag = False
    three_flag = False
    for key in tracker:
        val = int(tracker[key])
        if val == 5:
            return 6
        elif val == 4:
            return 5
        elif val == 3:
            three_flag = True
        elif val == 2:
            two_flag = True

    if three_flag and two_flag:
        return 4
    elif three_flag:
        return 3
    elif two_flag:
        return 2
    # high card    
    return 0


def compare_hands(h1, h2) -> bool:
    
    for i in range(5):
        h1_card = h1[i]
        h2_card = h2[i]

        if h1_card in letter_map:
            h1_card = letter_map[h1_card]
        else:
            h1_card = int(h1_card)
        if h2_card in letter_map:
            h2_card = letter_map[h2_card]
        else:
            h2_card = int(h2_card)


        if h1_card > h2_card:
            return True
        elif h2_card > h1_card:
            return False
    
def bubble_sort(bucket):
    flag = True
    tmp = []
    tmp_val = ''
    while flag:
        flag = False
        for i in range(len(bucket)-1):
            h1 = bucket[i].split()[0]
            h2 = bucket[i+1].split()[0]
            if compare_hands(h1, h2):
                tmp_val = bucket[i+1]
                bucket[i+1] = bucket[i]
                bucket[i] = tmp_val
                flag = True
    return bucket


buckets = [[] for i in range(7)]

for line in data:
    hand, wager = line.split()
    buckets[hand_strength(hand)].append(line)

order = []
for bucket in buckets:
    tmp = bubble_sort(bucket)
    for x in tmp:
        order.append(x)

res = 0
for i, val in enumerate(order):
    hand, wager = val.split()
    res += (int(wager) * (i + 1))

print(res)


test_bucket = [['32T3K 765', 'KK677 28', 'KTJJT 220']]
