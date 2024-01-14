# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    part_string_length = len(p)
    count_part = 0
    for i in range(len(t) - part_string_length + 1):
        if int(t[i:i+part_string_length]) <= int(p):
            count_part += 1
    return count_part