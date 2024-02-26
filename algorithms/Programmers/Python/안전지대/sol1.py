# https://school.programmers.co.kr/learn/courses/30/lessons/120866#
# first try: 1hour 10 minutes (test case 1 returned to be wrong)

board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
answer = 0
n = len(board[0])

# [0,0]부터 [n,n]까지의 좌표로 표현
# try, except 구문을 이용해서 가장자리에 있는 지뢰에 대한 판별을 진행한다.
# 안전지역은 0, 지뢰가 있는 지역은 1, 지뢰가 없는 위험지역은 2로 표시한다.
x = 0
y = 0
for line in board:
    for region in line:
        if region == 1:
            # 지뢰가 있을 경우, board[x][y]를 기준으로 board[x+1][y], board[x+1][y+1], board[x+1][y-1], board[x][y+1], board[x][y-1], board[x-1][y], board[x-1][y+1], board[x-1][y-1]가 0이면 2로 변환한다. 가장자리에 있어서 위의 값들 중 위치상 구할 수 없는 값이 있거나 값이 1이면 그대로 놔둔다.
            try:
                if board[x+1][y] == 0:
                    board[x+1][y] = 2
                if board[x+1][y] == 2:
                    board[x+1][y] = 2
                if board[x+1][y] == 1:
                    board[x+1][y] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x+1][y+1] == 0:
                    board[x+1][y+1] = 2
                if board[x+1][y+1] == 2:
                    board[x+1][y+1] = 2
                if board[x+1][y+1] == 1:
                    board[x+1][y+1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x+1][y-1] == 0:
                    board[x+1][y-1] = 2
                if board[x+1][y-1] == 2:
                    board[x+1][y-1] = 2
                if board[x+1][y-1] == 1:
                    board[x+1][y-1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x][y+1] == 0:
                    board[x][y+1] = 2
                if board[x][y+1] == 2:
                    board[x][y+1] = 2
                if board[x][y+1] == 1:
                    board[x][y+1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x][y-1] == 0:
                    board[x][y-1] = 2
                if board[x][y-1] == 2:
                    board[x][y-1] = 2
                if board[x][y-1] == 1:
                    board[x][y-1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x-1][y] == 0:
                    board[x-1][y] = 2
                if board[x-1][y] == 2:
                    board[x-1][y] = 2
                if board[x-1][y] == 1:
                    board[x-1][y] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x-1][y+1] == 0:
                    board[x-1][y+1] = 2
                if board[x-1][y+1] == 2:
                    board[x-1][y+1] = 2
                if board[x-1][y+1] == 1:
                    board[x-1][y+1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1

            try:
                if board[x-1][y-1] == 0:
                    board[x-1][y-1] = 2
                if board[x-1][y-1] == 2:
                    board[x-1][y-1] = 2
                if board[x-1][y-1] == 1:
                    board[x-1][y-1] = 1
            except:  # 위치상 구할 수 없는 값일 때
                board[x][y] = 1
            if y == n-1:
                y = 0
            else:
                y += 1

        else:   # if region is 1 or 2
            if y == n-1:
                y = 0
            else:
                y += 1
            continue
    x += 1

counts = 0     
print(board)
for line in board:
    for region in line:
        if region == 0:
            counts += 1

print(counts)