# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 효율성 검사에서 시간 초과가 나타났다.
def solution(s):
    answer = True
    
    # s의 길이만큼 반복하면서 "()"을 기준으로 split을 진행한다.
    # 만약 최종적으로 빈 문자열 ""이 반환되면 True이다.
    # 만약 빈 문자열이 아니면 False이다.
    for _ in range(len(s)):
        s = s.split("()")
        # split하여 list 형식이기 때문에 str 형식으로 만든다.
        s_c = ""
        for i in s:
            s_c += i
        s = s_c
        if s == "":
            return True
    if len(s) != 0:
        return False