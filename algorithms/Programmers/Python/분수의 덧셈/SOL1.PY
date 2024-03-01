# https://school.programmers.co.kr/learn/courses/30/lessons/120808
# 22 min 38 sec

def solution(numer1, denom1, numer2, denom2):
    # 두 분수를 더한 분수를 나타내기
    numer = (numer1*denom2 + numer2*denom1)
    denom = (denom1*denom2)
    
    # 약분을 진행한다.
    # 0에서 1000 사이의 숫자들이다. 따라서 동일한 숫자로 나누어떨어지면 그 숫자로 둘 다 나눈다.
    # 같은 수로 두번 나눠질 수도 있다.
    for i in range(1, 2000001):
        if ((numer % i == 0) and (denom % i == 0)):
            if (numer // i) >= (denom // i):
                repeat = int(denom // i)
            else:
                repeat = int(numer // i)
            for _ in range(0, repeat):
                if ((numer % i == 0) and (denom % i == 0)):
                    numer /= i
                    denom /= i
    answer = []
    answer.append(numer)
    answer.append(denom)
    
    
    return answers