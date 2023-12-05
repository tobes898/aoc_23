import aoc_tools


data = aoc_tools.load_test_input()


i = 0
seeds = []
seed_to_soil = {}
soil_to_fert = {}
fert_to_water = {}
water_to_light = {}
light_to_temp = {}
temp_to_hum = {}
hum_to_loc = {}
seeds_p1 = data[i][data[0].index(':')+1:].split()
seeds = []
# part two
for i in range(0, len(seeds_p1), 2):
    start = int(seeds_p1[i])
    seed_range = int(seeds_p1[i + 1])
    for j in range(seed_range):
        seeds.append(start+j)     
i = 1


def determine_map(row, val_set, res):
    tmp = row.split()
    dest = int(tmp[0])
    src = int(tmp[1])
    r = int(tmp[2])
    for val in val_set:
        if int(val) >= src and int(val) <= src + r and val not in res:
            diff = int(val) - src
            res[val] = dest + diff
    return res


# while data[i] != '':
#     seed_to_soil = determine_map(data[i], seed_to_soil)
#     i += 1 

# # print(seed_to_soil)
# for seed in seeds:
#     if seed not in seed_to_soil:
#         seed_to_soil[seed] = seed
i = 1
while i < len(data) - 1:
    if 'seed-to-soil map' in data[i]:
        i += 1
        while data[i] != '':
            seed_to_soil = determine_map(data[i], seeds, seed_to_soil)
            i += 1 
        for seed in seeds:
            if seed not in seed_to_soil:
                seed_to_soil[seed] = int(seed)
        
    elif 'soil-to-fertilizer map' in data[i]:
        i += 1
        while data[i] != '':
            soil_to_fert = determine_map(data[i], seed_to_soil.values(), soil_to_fert)
            i+=1
        for soil in seed_to_soil.values():
            if soil not in soil_to_fert:
                soil_to_fert[soil] = soil
    elif 'fertilizer-to-water map' in data[i]:
        i += 1
        while data[i] != '':
            fert_to_water = determine_map(data[i], soil_to_fert.values(), fert_to_water)
            i+=1
        for fert in soil_to_fert.values():
            if fert not in fert_to_water:
                fert_to_water[fert] = fert

    elif 'water-to-light map' in data[i]:
        i += 1
        while data[i] != '':
            water_to_light = determine_map(data[i], fert_to_water.values(), water_to_light)
            i+=1
        for water in fert_to_water.values():
            if water not in water_to_light:
                water_to_light[water] = water
    elif 'light-to-temperature map' in data[i]:
        i += 1
        while data[i] != '':
            light_to_temp = determine_map(data[i], water_to_light.values(), light_to_temp)
            i+=1
        for light in water_to_light.values():
            if light not in light_to_temp:
                light_to_temp[light] = light
    elif 'temperature-to-humidity' in data[i]:
        i += 1
        while data[i] != '':
            temp_to_hum = determine_map(data[i], light_to_temp.values(), temp_to_hum)
            i+=1
        for temp in light_to_temp.values():
            if temp not in temp_to_hum:
                temp_to_hum[temp] = temp
    elif 'humidity-to-location' in data[i]:
        i += 1
        while data[i] != '' and i < len(data) -1:
            hum_to_loc = determine_map(data[i], temp_to_hum.values(), hum_to_loc)
            i+=1
        for hum in temp_to_hum.values():
            if hum not in hum_to_loc:
                hum_to_loc[hum] = hum
    i += 1

# print(seed_to_soil)
# print(soil_to_fert)
# print(fert_to_water) # issue
# print(water_to_light)
# print(light_to_temp)
# print(temp_to_hum)
# print(hum_to_loc)
# print(seeds)
res = min(hum_to_loc.values())
print(res)
# parse input
