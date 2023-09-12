T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    point = input().split()
    K = int(point[0])
    N = int(point[1])
    M = int(point[2])
    
    number = [int(num) for num in input().split()]
    
    # 마지막에 도착할 수 없는 경우
    for i in range(len(number)-1):
        if int(number[i+1]) - int(number[i]) >= K+1 or int(number[0]) >= K+1:
            print(f'#{test_case} ' + '0')
            
            
    
    how_many = 0
    current = 0
    range_list = []
    while current < N-K:
        for num in range(current+1, current + K + 1):
            if num in number:
                range_list.append(num)
        if len(range_list) == 0:
            break
        current = max(range_list)
        how_many += 1
        range_list = []
    
    final_count = 0
    for i in range(len(number)-1):
        if int(number[i+1]) - int(number[i]) >= K+1 or int(number[0]) >= K+1:
            final_count += 1
    if final_count == 0:
        print(f'#{test_case} ' + str(how_many))
        
        
        
        
            
    