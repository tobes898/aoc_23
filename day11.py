import aoc_tools as at

at.setup()
starting_grid = at.load_test_input()



def expand_grid(grid, r_expand, c_expand):
    # cols first then rows as it would just be adding
    # the len of the row at that point
    e_grid = []

    #column expansion
    for i in range(len(grid)):
        row = []
        for j in range((len(grid[0]))):
            row.append(grid[i][j])
            if c_expand[j] == 0:
                # row.insert(j, '.')
                row.append('.')
        e_grid.append(row)

    # row expansion
    for i in range(len(grid)):
        if r_expand[i] == 0:
            e_grid.insert(i, ['.']*len(e_grid[0]))
    
    for line in e_grid:
        print(line)

# trackers to see if row or col is empty
r_empty_t = [0] * len(starting_grid)
c_empty_t = [0] * len(starting_grid[0])

for i in range(len(starting_grid)):
    for j in range((len(starting_grid[0]))):
        if starting_grid[i][j] == '#':
            r_empty_t[i] = 1
            c_empty_t[j] = 1



expand_grid(starting_grid, r_empty_t, c_empty_t)


