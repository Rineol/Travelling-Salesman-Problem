import sys
import math
import time
sys.setrecursionlimit(1000000)

lol = 0
points = {}
tmp_order = []
visited = []
opt_order = []
visited_number = 0
tmp_distance = 0
opt_distance = 0
start = 0
matrix = []
ids = []


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


def tsp_start(n, tmp_order, opt_order, visited):
    for i in range(n):
        tmp_order += [0]
        opt_order += [0]
        visited += [0]
    return tmp_order, opt_order, visited


def distance(n1, n2):
    d = (math.sqrt((math.pow((points[n2][0]-points[n1][0]), 2)+math.pow((points[n2][1]-points[n1][1]), 2))))
    return d


def distances_matrix(points, ids):
    lenght = len(points)
    matrix = []
    for i in range(lenght):
        matrix += [[]]
        for j in range(lenght):
            matrix[i] += [0]
            # print(ids)
            k = ids[i]
            l = ids[j]
            matrix[i][j] = distance(k, l)
    # for i in matrix:
    #     print(i)
    return matrix


def tsp(start, n, matrix, tmp_order, visited, visited_number, opt_order, points):
    act_time = time.clock()
    global first_search
    global tmp_distance
    global opt_distance
    #print('fs: ', first_search)
    #print("visited: ", visited)
    #print(tmp_order)
    tmp_order[visited_number] = start
    visited_number += 1
    #print(visited_number)
    if visited_number != n:
        if act_time > 57:
            return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points
        visited[start] = 1
        for i in range(n):
            if visited[i] == 0 and i != start:
                tmp_distance += matrix[start][i]
                if first_search:
                    if tmp_distance < opt_distance:
                        tsp(i, n, matrix, tmp_order, visited, visited_number, opt_order, points)
                else:
                    if act_time > 57:
                        return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points
                    tsp(i, n, matrix, tmp_order, visited, visited_number, opt_order, points)
                tmp_distance -= matrix[start][i]
        visited[start] = 0
    else:
        tmp_distance += matrix[start][0]
        if first_search == 0:
            opt_distance = tmp_distance
            #print("opt po temp: ", opt_distance)
            first_search = 1
            #print("fs: ", first_search)
            for j in range(n):
                opt_order[j] = tmp_order[j]
            if act_time > 57:
                return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points
        else:
            if tmp_distance < opt_distance:
                if act_time > 57:
                    return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points
                opt_distance = tmp_distance
                for j in range(n):
                    opt_order[j] = tmp_order[j]
                if act_time > 57:
                    return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points
                #print(act_time)

        tmp_distance -= matrix[start][0]
    visited_number -= 1
    #print(act_time)
    return n, matrix, tmp_order, visited, visited_number, opt_order, first_search, points



points, ids = process_input()
first_search = 0
#print(ids)
n = len(points)
mat = distances_matrix(points, ids)
#print(mat)
tmp_order, opt_order, visited = tsp_start(n, tmp_order, opt_order, visited)
(tsp(start, n, mat, tmp_order, visited, visited_number, opt_order, points))
#print(opt_order)
for k in range(n):
    print(ids[opt_order[k]])
