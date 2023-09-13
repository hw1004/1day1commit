import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # N: 전체 행렬 크기, M: 파리채 크기
    N, M = map(int, input().split())

    # matrix = []
    # for _ in range(N):
    #     matrix.append(list(map(int, input().split())))
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_kill = 0
    for row in range(N-M+1):
        for column in range(N-M+1):
            one_kill = 0
            for i in range(M):
                for j in range(M):
                    one_kill += matrix[row+i][column+j]
            if one_kill > max_kill:
                max_kill = one_kill
                
    print(f'#{tc} {max_kill}')
