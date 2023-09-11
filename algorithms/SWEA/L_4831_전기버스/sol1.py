T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K = int(input())
    N = int(input())
    M = int(input())
    
    number = [int(num) for num in input().split()]
    
        
    
    counts = 0
    move = 0
    
    while move <= N:
        ranges = []
        for num in number:
            if num in range(counts, counts+K+1):
                ranges.append(num)
        counts = max(ranges)
            
    