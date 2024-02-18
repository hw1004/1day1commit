# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    word = ''
    for alphabet in s:
        if alphabet not in word:
            word += alphabet
            answer.append(-1)
        else:
            index_i = 0
            for i in word[::-1]:
                if i != alphabet:
                    index_i += 1
                else:
                    index_i += 1
                    break
            answer.append(index_i)
            word += alphabet
                    
    return answer