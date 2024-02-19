# https://school.programmers.co.kr/learn/courses/30/lessons/81301
# 14분 14초

def solution(s):
    answer = 0
    # 숫자 0~9까지 돌아가며 만약 영단어 zero가 s에 있다면 숫자형으로 바꾼다.
    # if-else문을 작성한다.
    if 'zero' in s:
        s = s.replace('zero', '0')
    if 'one' in s:
        s = s.replace('one', '1')
    if 'two' in s:
        s = s.replace('two', '2')
    if 'three' in s:
        s = s.replace('three', '3')
    if 'four' in s:
        s = s.replace('four', '4')
    if 'five' in s:
        s = s.replace('five', '5')
    if 'six' in s:
        s = s.replace('six', '6')
    if 'seven' in s:
        s = s.replace('seven', '7')
    if 'eight' in s:
        s = s.replace('eight', '8')
    if 'nine' in s:
        s = s.replace('nine', '9')
    answer = int(s)
    return answer