# https://school.programmers.co.kr/learn/courses/30/lessons/134240
# 16분 40초

def solution(food):
    f_answer = ''
    answer = ''
    # 홀수일 때와 짝수일 때를 나누어서 생각
    # 가운데가 0이기 때문에 0을 기준으로 대칭인 숫자들의 문자열을 추후에 합친다.
    i = 0
    for f in food[1:]:
        i += 1
        if f == 1:
            continue
        if f % 2 == 0:
            repeat = ''
            repeat += (str(i) * (f // 2))
            f_answer += repeat
        else:
            repeat = ''
            repeat += (str(i) * (f // 2))
            f_answer += repeat
    answer = f_answer + '0' + f_answer[::-1]
    
    return answer