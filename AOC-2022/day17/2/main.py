with open('input.txt') as infile:
    pushes = infile.readlines()[0].strip()

# height: 3068
pushes = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

rock_types = [
    [
        '####'
    ],
    [
        '.#.',
        '###',
        '.#.',
    ],
    [
        '..#',
        '..#',
        '###',
    ],
    [
        '#',
        '#',
        '#',
        '#',
    ],
    [
        '##',
        '##',
    ]
]

rocks = 0
push_index = 0
rock_index = 0
x_pos = 2
y_pos = 0

gw = 7
gh = (2022+5) * 4  # this should be more than enough space
grid = [[0 for _ in range(gh)] for _ in range(gw)]
for x in range(gw):
    grid[x][0] = 1


prev_height = 0


def height():
    for y in range(gh - 1, -1, -1):
        for x in range(gw):
            if grid[x][y] == 1:
                return y + 1
    return 1


def print_grid():
    for y in range(height(), -1, -1):
        for x in range(gw):
            print('#' if grid[x][y] == 1 else '.', end='')
        print()
    print()


def test_move(dx, dy):
    rock = rock_types[rock_index % len(rock_types)]
    for x in range(len(rock[0])):
        for y in range(len(rock)):
            if rock[len(rock) - 1 - y][x] == '#':
                if x_pos + x + dx >= gw or x_pos + x + dx < 0 \
                        or y_pos + (len(rock)-1 + y) + dy >= gh or y_pos + y + dy < 0 \
                        or grid[x_pos + x + dx][y_pos + y + dy] != 0:
                    return False
    return True


def place():
    global rocks
    rock = rock_types[rock_index % len(rock_types)]
    for x in range(len(rock[0])):
        for y in range(len(rock)):
            if rock[len(rock) - 1 - y][x] == '#':
                grid[x_pos + x][y_pos + y] = 1
    rocks += 1


x_pos = 2
y_pos = height() + 3
modulo = len(rock_types) * len(pushes)
total = 2022
print(f'modulo: {modulo}')
base_times = total // modulo
rest = total % modulo
print(f'base_times: {base_times}')
print(f'rest: {rest}')


while True:
    while True:
        d = 1 if pushes[push_index % len(pushes)] == '>' else -1
        push_index += 1
        if test_move(d, 0):
            x_pos += d
        if test_move(0, -1):
            y_pos -= 1
        else:
            break
    place()
    rock_index += 1
    x_pos = 2
    y_pos = height() + 3
    if rocks % (modulo // 5) == 0:
        #print(rocks / 2022)
        pass
    print(push_index % len(pushes), len(pushes) - 1)
    if push_index % len(pushes) == len(pushes) - 1:
        print(height(), rock_index % len(rock_types))
# test data heights at modulo:
# 308
# 609
# 915
# 1218
# 1521
# 1822
# 2128
# 2428
base_height = height() - 1
print(f'base_height: {base_height}')
while rocks < modulo + rest + 1:
    while True:
        d = 1 if pushes[push_index % len(pushes)] == '>' else -1
        push_index += 1
        if test_move(d, 0):
            x_pos += d
        if test_move(0, -1):
            y_pos -= 1
        else:
            break
    place()
    rock_index += 1
    x_pos = 2
    y_pos = height() + 3
    if rocks % (modulo // 5) == 0:
        print(rocks / 2022)
rest_height = height() - base_height
print(f'rest_height: {rest_height}')
print(f'height: {height() - 1}')
# height: 3137
