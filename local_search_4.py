import math
from time import process_time
import time


points = {}
ids = []
lol = 0
tmp_order = []
visited = []
opt_order = []
visited_number = 0
tmp_distance = 0
opt_distance = 0
start = 0
dlugosc = 0
matrix = []
list = []
k = 0
i = 0


def process_input():
    ids = []
    while True:
        try:
            line = input()
            b = line
        except EOFError:
            return points, ids
        a = line.find(str(b))
        if a != -1:
            lol = 0
            #print(line)
        if line == '':
            return points, ids
        b = line.split(' ')
        points[int(b[0])] = [float(b[1]), float(b[2])]
        ids += [int(b[0])]


def distance(n1, n2):
    d = (math.sqrt((math.pow((points[n2][0]-points[n1][0]), 2)+math.pow((points[n2][1]-points[n1][1]), 2))))
    return d


def list_distance(route):
    s = 0
    dist = 0
    long = len(route)
    for s in range(long):
        if s < long - 1:
            dist += distance(route[s], route[s+1])
        else:
            dist += distance(route[s], route[0])
    return dist


def swap_n_find(route):
    long = len(ids)
    shortest_route = ids
    all_distance = list_distance(shortest_route)
    shortest_distance = all_distance
    improved = True
    st = time.clock()
    while improved:
        improved = False
        for i in range(1, long - 1):
            for k in range(i+1, long - 1):
                if process_time() - st > 58:
                    return shortest_route
                if k - i == 1:
                    continue
                new_route = ids[:]
                part1 = ids[i: k + 1]
                part2 = part1[::-1]
                new_route[i:k + 1] = part2
                new_distance = list_distance(new_route)
                print(new_route)
                print(new_distance)
                if new_distance < shortest_distance:
                    improved = True
                    shortest_route = new_route
                    shortest_distance = new_distance
                    #print("Czas: ", process_time() - st)
    return shortest_route


points, ids = process_input()
shortest = swap_n_find(ids)
for i in range(len(shortest)):
    print(shortest[i])


