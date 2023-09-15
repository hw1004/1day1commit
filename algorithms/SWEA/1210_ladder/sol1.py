import sys
sys.stdin = open('C:/Users/USER/Github/1day1commit/algorithms/SWEA/1210_ladder/input.txt')

T = 10

for tc in range(1, T+1):
    matrix = []
    
    test_number = int(input())
    
    first_row = list(map(int, input().split()))
    matrix.append(first_row)
    
    for _ in range(len(first_row)-1):
        matrix.append(list(map(int, input().split())))
    
    end = [0, 0]
    # endpoint를 먼저 찾기
    for row in range(len(matrix)):
        if 2 in matrix[row]:
            end[1] = matrix[row].index(2)
            end[0] = row
            
    # direction 1, 2, 3을 위, 왼, 오이라고 하자.
    direction = 1 
    change = 0  # change가 짝수일 때는 direction = 1
    # row = 0이 나올 때까지 위로 track
    while end[0] != 0:
        if end[1] == len(matrix)-1:
            if matrix[end[0]][end[1]-1] == 1 and change % 2 == 0:
                change += 1
                direction = 2
            elif matrix[end[0]][end[1]-1] == 1 and change % 2 == 1:
                change += 1
                direction = 1
            elif matrix[end[0]][end[1]-1] == 0 and change % 2 == 0:
                direction = 1
        elif end[1] == 0:
            if matrix[end[0]][end[1]+1] == 1 and change % 2 == 0:
                change += 1
                direction = 3
            elif matrix[end[0]][end[1]+1] == 1 and change % 2 == 1:
                change += 1
                direction = 1
            elif matrix[end[0]][end[1]+1] == 0 and change % 2 == 0:
                direction = 1
            
        else: 
            if matrix[end[0]][end[1]-1] == 1 and matrix[end[0]][end[1]+1] == 0 and direction == 1:
                change += 1
                direction = 2
            elif matrix[end[0]][end[1]-1] == 0 and matrix[end[0]][end[1]+1] == 1 and direction == 1:
                change += 1
                direction = 3
            elif matrix[end[0]][end[1]-1] == 0 and matrix[end[0]][end[1]+1] == 1 and change % 2 == 1:
                change += 1
                direction = 1
            elif matrix[end[0]][end[1]-1] == 1 and matrix[end[0]][end[1]+1] == 0 and change % 2 == 1:
                change += 1
                direction = 1
        
        
        if direction == 1:
            end[0] -= 1
        elif direction == 2:
            end[1] -= 1
        elif direction == 3:
            end[1] += 1

    print(f'#{tc} {end[1]}')