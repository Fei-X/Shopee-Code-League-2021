def one(lst, total, position):
    return total, position
def two(lst, total, position):
    if position:
        lst = lst[::-1]
    max_ = 0
    current = 0
    for i in range(len(lst)):
        current += lst[i]
        if current > max_:
            max_ = current
    return total + max_, position

def thr(lst, total, position):
    return total + sum(lst), 1-position

def bf_case(bf_table,day):
    bf_lst = []
    for i in range(len(bf_table)): 
        bf_lst.append(one(data[day],bf_table[i][0],bf_table[i][1]))
        bf_lst.append(two(data[day],bf_table[i][0],bf_table[i][1]))
        bf_lst.append(thr(data[day],bf_table[i][0],bf_table[i][1]))
    return bf_lst

def bf_optimize(bfTable):
    max_left = max([item[0] for item in bf_table if item[1] == 0])
    max_right = max([item[0] for item in bf_table if item[1] == 1])
    return [(max_left,0),[max_right,1]]

import sys
num_line = int(sys.stdin.readline())
for _ in range(num_line):
    s = sys.stdin.readline().split()
    N, M = int(s[0]), int(s[1])
    data = []
    for i in range(N):
        s = sys.stdin.readline()
        data.append([int(t) for t in s.split(' ')])
    bf_table = [(0,0)]
    for day in range(N):
        bf_table = bf_case(bf_table,day)
        bf_table = bf_optimize(bf_table)
    print(max([item[0] for item in bf_table]))
# print(data)

