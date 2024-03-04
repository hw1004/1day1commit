# https://school.programmers.co.kr/learn/courses/30/lessons/12941
# 가장 작은 원소와 가장 큰 원소를 곱한 것을 더한 것이 최솟값임 (증명을 통해 알 수 있음)

def solution(A,B):
    answer = 0
    A.sort(reverse=False)
    B.sort(reverse=True)
    # 가장 작은 원소와 가장 큰 원소를 곱한 것을 더한 것이 최솟값임
    for i in range(len(A)):
        answer += (A[i] * B[i])
    return answer