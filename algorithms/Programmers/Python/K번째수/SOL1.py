# https://school.programmers.co.kr/learn/courses/30/lessons/42748
# 5분 52초

def solution(array, commands):
    answer = []
    # commands를 for loop으로 돌면서 각각의 경우에 대한 return값을 answer에 append한다.
    for command in commands:
        c_array = array[(command[0] - 1):command[1]]
        c_array = sorted(c_array)
        c_result = c_array[command[2] - 1]
        answer.append(c_result)
    return answer