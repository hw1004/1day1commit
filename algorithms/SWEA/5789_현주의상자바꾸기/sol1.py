T = int(input())

for tc in range(1, T+1):
    N, Q = map(int, input().split())   # [5, 2]
    
    boxes = [0] * N
    
    for i in range(1, Q+1):
        L, R = map(int, input().split())   # [1, 3], [2, 4]
        
        for box in range(L-1, R):
            boxes[box] = i
    
    answer = ''
    for box in boxes:
        answer += str(box) + ' '
    answer = answer[:-1]
    print(f'#{tc} ' + answer)
        