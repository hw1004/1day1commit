# https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 첫번째 시도 못 풀었음
edges= [[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]]
answer = []
# 시작하는 정점은 [a,b]에서 a에는 이는데 b에는 없는 숫자
start = 0
a = []
b = []
for edge in edges:
    a.append(edge[0])
    b.append(edge[1])
for i in a:
    # 원소가 1개일 경우 막대그래프일 수도 있기 때문에 1이 아닌 경우
    if (a.count(i) != 1) and (i not in b):
        start = i
# 막대 그래프 => [a,b]에서 a,b를 합쳐도 유일한 값이 있으면 막대 그래프
all = []
for edge in edges:
    all.append(edge[0])
    all.append(edge[1])
all = sorted(all)
bar_count = 0
idx = 0
for i in all:
    if (idx == 0) and all[idx+1] != i:
        bar_count += 1
    elif (idx == len(all)-1) and all[idx-1] != i:
        bar_count += 1
    elif (all[idx-1] != i) and (all[idx+1] != i):
        bar_count += 1
    end = i
    idx += 1
# 막대그래프 있는 요소 삭제

other = 0
for edge in edges:
    if (edge[0] == end):
        other = edge[1]
        edges.remove(edge)
    elif (edge[1] == end):
        other = edge[0]
        edges.remove(edge)
    elif (edge[0] == other):
        other = edge[1]
        edges.remove(edge)
    elif (edge[1] == other):
        other = edge[0]
        edges.remove(edge)
    else:
        continue
    
# 시작하는 정점이 포함된 리스트는 remove
new_edges = []
for edge in edges:
    if edge[0] == start:
        continue
    else:
        new_edges.append(edge)
        
a = []
b = []
for edge in new_edges:
    a.append(edge[0])
    b.append(edge[1])
# 도넛 모양은 [n,n] 형식이거나 시작점과 끝점이 같은 list가 있으면 도넛
# 단, n=1 일때의 8자 모양 그래프와 구분해야 함
donut_count = 0
eight_count = 0
donut_remove = []
i = 0
donut_count_temp = 0
for edge in new_edges:
    if edge[0] == edge[1]:
        donut_count += 1
        donut_remove.append(edge)
        i += 1
    elif (edge[0] in b) and (b.count(edge[0]) == 1):
        edge_0 = edge[0]
        edge_1 = edge[1]
        for edge in new_edges:                   
            if edge[0] == edge_1:
                edge_1 = edge[1]
                for edge in new_edges:
                    if edge[0] == edge_1:
                        edge_1 = edge[1]
                    if edge[1] == edge_0:
                        donut_count_temp += 1
if donut_count_temp % 2 == 0:
    i += 1
elif donut_count_temp % 2 != 0:
    donut_count += 1
    donut_remove.append(edge)
    i += 1

# 도넛모양을 이루는 donut_remove 안의 원소들을 new_edges에서 remove
for donut in donut_remove:
    if donut in new_edges:
        new_edges.remove(donut)
    else:
        continue
print(new_edges)
print([start, donut_count, bar_count])