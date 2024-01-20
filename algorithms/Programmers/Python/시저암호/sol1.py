# https://school.programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    # 알파벳
    lower_alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    # s 안의 알파벳들에 대해 n만큼 옮긴 결과값을 반환한다.
    answer = ''
    for alphabet in s:
        if alphabet == ' ':
            answer += ' '
        if alphabet in lower_alphabet:
            index_a = lower_alphabet.index(alphabet)
            answer += lower_alphabet[index_a + n]
        if alphabet in upper_alphabet:
            index_a = upper_alphabet.index(alphabet)
            answer += upper_alphabet[index_a + n]
    return answer