# 첫 번째 줄에 N,K가 공백을 기준으로 구분되어 입력됩니다.
inputs = input()

N = int(inputs.split()[0])
K = int(inputs.split()[1])

# 두 번째 줄에 배열 A의 원소들이 공백을 기준으로 구분되어 입력됩니다. 
# 모든 원소는 10,000,000보다 작은 자연수입니다.

A = list(map(int, input().split()))

# 세 번째 줄에ㅔ 배열 B의 원소들이 공백을 기준으로 구분되어 입력됩니다.
# 모든 원소는 10,000,000보다 작은 자연수입니다.

B = list(map(int, input().split()))

# 최대 K번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력합니다.
# A에서 가장 작은 자연수 K개를 B에서 가장 큰 자연수 K개와 바꾸기
sorted_a = list(map(int, sorted(A)))
sorted_b = list(map(int, sorted(B)))

for i in range(K):
    sorted_a[i] = sorted_b[-i-1]
    
# 바뀐 A의 합
first_sum = sum(sorted_a)
# B에서 가장 작은 자연수 K개를 A에서 가장 큰 자연수 K개와 바꾸기
for i in range(K):
    B[i] = A[-i-1]
    
# 바뀐 B의 합
second_sum = sum(B)

print(max(first_sum, second_sum))

    