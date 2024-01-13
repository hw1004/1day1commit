# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    # 가장 큰 가로 길이와 세로 길이를 기억한다.
    max_width = 0
    max_height = 0
    for card in sizes:
        if max_width < card[0]:
            max_width = card[0]
        if max_height < card[1]:
            max_height = card[1] 
    
    # 가장 큰 가로 길이와 세로 길이 중 더 큰 값을 찾는다.
    # 만약 가로의 최댓값이 세로의 최댓갑보다 크다면 가로보다 세로가 큰 값들의
    # 가로와 세로의 값을 바꾼다.
    # 그 후에 세로의 최댓값을 다시 구하고 가로의 최댓값과 곱한다.
    if max_width >= max_height:
        for card in sizes:
            if card[0] < card[1]:
                width = card[0]
                height = card[1]
                card[0] = height
                card[1] = width
        re_max_height = 0
        for card in sizes:
            if re_max_height < card[1]:
                re_max_height = card[1]
        return max_width * re_max_height
    # 반대의 경우도 똑같이 진행한다.
    if max_height >= max_width:
        for card in sizes:
            if card[1] < card[0]:
                width = card[0]
                height = card[1]
                card[0] = height
                card[1] = width
        re_max_width = 0
        for card in sizes:
            if re_max_width < card[0]:
                re_max_width = card[0]
        return max_height * re_max_width