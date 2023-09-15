T = int(input())

for tc in range(1, T+1):
    N = int(input())
    
    info = list(map(int, input().split()))
    
    benefit = 0
    max_value = info[-1] 
    # 뒤에서부터 탐색
    for i in range(len(info)-1, -1, -1):
        if max_value > info[i]:
            benefit += max_value-info[i]
        else:
            max_value = info[i]
    
    print(f'#{tc} {benefit}')
            
        
 
        