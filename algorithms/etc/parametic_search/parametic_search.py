# 떡볶이 떡 만들기

N, M = list(map(int, input().split()))

rice_cake = sorted(list(map(int, input().split())), reverse=True)

# rice_cake를 정렬했을 때 max_cut는 N번째 떡의 길이보다 작아야 한다.
max_cut = max(rice_cake)

# N번째까지의 떡들에서 max_cut만큼 뺀 나머지 떡들의 합이 M보다 크거나 같아야 한다.
# max_cut에서 1씩 줄여나갈 때 조건을 만족하는 max_cut을 반환한다.
for i in range(rice_cake[0], 0, -1):
    sum = 0
    for j in range(0, N):
        if rice_cake[j] >= i:
            sum += (max_cut - rice_cake[j])
        else:
            continue
    if sum >= M:
        print(i)
        break


