# 이진 탐색을 이용하여 구하기

# 중간점에서 오른쪽으로 옮기면서 이진 탐색

# 중간점의 값은 시간이 지날수록 최적화된 값이 된다.
# 얻을 수 있는 떡의 길이 합이 필요한 떡의 길이보다 크거나 같을 때마다
# 중간값 기록

N, M = list(map(int, input().split()))

array = list(map(int, input().split()))

start = 0
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += (x - mid)
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
