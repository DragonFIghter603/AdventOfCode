with open('../input.txt') as infile:
    data = [row.strip() for row in infile.readlines()]

class Sensor:
    def __init__(self, p, b):
        self.pos = p
        self.beacon = b
        self.dist = abs(b[0]-p[0]) + abs(b[1]-p[1])


sensors = []

for d in data:
    _, _, px, py, _, _, _, _, bx, by = d.strip().split()
    p = int(px[2:-1]), int(py[2:-1])
    b = int(bx[2:-1]), int(by[2:])
    sensors.append(Sensor(p, b))

parcells = [((-10000, 1200000), 5007), ((-10000, 1230000), 9289), ((20000, 1230000), 5161), ((-10000, 1240000), 0), ((0, 1240000), 9289), ((10000, 1240000), 9949), ((20000, 1240000), 4993), ((-10000, 1250000), 0), ((0, 1250000), 9949), ((-10000, 1260000), 9949), ((1640000, 1950000), 9525), ((1650000, 1950000), 9048), ((1650000, 1960000), 952), ((1660000, 1960000), 9048), ((1660000, 1970000), 952), ((1670000, 1970000), 9048), ((1670000, 1980000), 952), ((1680000, 1980000), 9048), ((1680000, 1990000), 952), ((1690000, 1990000), 9048), ((1690000, 2000000), 952), ((1700000, 2000000), 9048), ((3340000, 2450000), 2737), ((3340000, 2460000), 9243), ((3350000, 2460000), 757), ((3350000, 2470000), 9243), ((3360000, 2470000), 757), ((3360000, 2480000), 9243), ((3370000, 2480000), 757), ((3370000, 2490000), 9243), ((3380000, 2490000), 757), ((3380000, 2500000), 9243), ((3390000, 2500000), 757), ((3390000, 2510000), 9243), ((3400000, 2510000), 757), ((3400000, 2520000), 9243), ((3410000, 2520000), 757), ((3410000, 2530000), 9243), ((3420000, 2530000), 757), ((3420000, 2540000), 9243), ((3430000, 2540000), 757), ((3430000, 2550000), 9243), ((3440000, 2550000), 757), ((3440000, 2560000), 9243), ((3450000, 2560000), 757), ((3450000, 2570000), 9243), ((3460000, 2570000), 757), ((3460000, 2580000), 9243), ((3470000, 2580000), 757), ((3470000, 2590000), 9243), ((3480000, 2590000), 757), ((3480000, 2600000), 9243), ((3490000, 2600000), 757), ((3490000, 2610000), 9243), ((3500000, 2610000), 757), ((3500000, 2620000), 9243), ((3510000, 2620000), 757), ((3510000, 2630000), 9243), ((3520000, 2630000), 757), ((3520000, 2640000), 9243), ((3530000, 2640000), 757), ((3530000, 2650000), 9243), ((3540000, 2650000), 757), ((3540000, 2660000), 9243), ((3550000, 2660000), 757), ((3550000, 2670000), 9243), ((3560000, 2670000), 757), ((3560000, 2680000), 9243), ((3570000, 2680000), 757), ((3570000, 2690000), 9243), ((3580000, 2690000), 757), ((3580000, 2700000), 9243), ((3590000, 2700000), 757), ((3590000, 2710000), 9243), ((3600000, 2710000), 757), ((3600000, 2720000), 9243), ((3610000, 2720000), 757), ((3610000, 2730000), 9243), ((3620000, 2730000), 757), ((3620000, 2740000), 9243), ((3630000, 2740000), 757), ((3630000, 2750000), 9243), ((3640000, 2750000), 757), ((3640000, 2760000), 9243), ((3650000, 2760000), 757), ((3650000, 2770000), 9243), ((3660000, 2770000), 757), ((3660000, 2780000), 9243), ((3670000, 2780000), 757), ((3670000, 2790000), 9243), ((3680000, 2790000), 757), ((3680000, 2800000), 9243), ((3690000, 2800000), 757), ((3690000, 2810000), 9243), ((3700000, 2810000), 757), ((3700000, 2820000), 9243), ((3710000, 2820000), 757), ((3710000, 2830000), 9243), ((3720000, 2830000), 757), ((3720000, 2840000), 9243), ((3730000, 2840000), 757), ((3730000, 2850000), 9243), ((3740000, 2850000), 757), ((3740000, 2860000), 9243), ((3750000, 2860000), 757), ((3750000, 2870000), 9243), ((3760000, 2870000), 757), ((3760000, 2880000), 9243), ((3770000, 2880000), 757), ((3770000, 2890000), 9243), ((3780000, 2890000), 757), ((3780000, 2900000), 9243), ((3790000, 2900000), 757), ((3790000, 2910000), 9243), ((3800000, 2910000), 5375), ((2010000, 3290000), 1515), ((2010000, 3300000), 9455), ((2030000, 3310000), 5961), ((2720000, 3360000), 8831), ((2720000, 3370000), 3395)]

for p, d in parcells:
    map = [[0 for y in range(40)] for x in range(40)]

    deepest = []

    for mx, y in enumerate(range(p[0] - 10000, p[0] + 10000, 500)):
        for my, x in enumerate(range(p[1] - 10000, p[1] + 10000, 500)):
            max_d = 0
            for sensor in sensors:
                d = abs(x - sensor.pos[0]) + abs(y - sensor.pos[1])
                max_d = max(max_d, (sensor.dist - d))
            map[mx][my] = max_d
            if max_d < 40:
                deepest.append(((x, y), max_d))

    for y in range(40):
        for x in range(40):
            c = chr(ord('a') + map[x][y] // 20000)
            if 0 < x < 39 and 0 < y < 39:
                if min(map[x - 1][y], map[x + 1][y], map[x][y - 1], map[x][y + 1]) > map[x][y]:
                    print(f'\x1b[1;31m{c}\x1b[0m', end='')
                elif max(map[x - 1][y], map[x + 1][y], map[x][y - 1], map[x][y + 1]) < map[x][y]:
                    print(f'\x1b[1;32m{c}\x1b[0m', end='')
                else:
                    print(c, end='')
            else:
                print(c, end='')
        print()
    print()
    input()