# https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 17:56 ~ 
def solution(distance, rocks, n):
    rocks.sort(reverse=False) 
    min_distance = []
    for i in range(len(rocks)-1):
        for j in range(i+1, len(rocks)):
            removed_list = [rock for rock in rocks]
            removed_list.remove(removed_list[j])
            removed_list.remove(removed_list[i])
            
            distance_2 = []
            removed_list.append(distance)
            
            for k in range(len(removed_list)):
                if k == 0:
                    distance_2.append(removed_list[k])
                else:
                    distance_2.append(removed_list[k] - removed_list[k-1])
            min_distance.append(min(distance_2))
        
    return max(min_distance)

solution(25, [2,14,11,21,17], 2)