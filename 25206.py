# 너의 평점은

import sys

point_list = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

results = []
points =  []

for _ in range(20):
    n = sys.stdin.readline().strip()
    _, point, rank = n.split()
    
    if rank != 'P':
        results.append(float(point) * point_list[rank])
        points.append(float(point))
    
print(round(sum(results) / sum(points), 6))
    