T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    
    p = []
    for _ in range(N):
        color = input()
        p.append(color.split())
        
    point = []
    for num in p:
        part = []
        for n in num:
            part.append(int(n))
        point.append(part)

    
    # r1,c1 또는 r2,c2가 다른 사각형의 r1,c1 또는 r2,c2 사이에 존재하면 겹친다.
    # 색이 반대여야 한다.
    duplicate = 0
    for i in range(len(point)):
        for j in range(len(point)):
            if point[i][0] <= point[j][2] and point[i][1] >= point[j][3] and point[i][4] != point[j][4]:
                duplicate += (point[j][2] - point[i][0] + 1) * (point[i][1] - point[j][3] + 1)
            elif point[i][0] == point[i][1] and point[j][2] == point[j][3] and point[i][4] != point[j][4]:
                duplicate += (point[j][2] - point[i][0] + 1) * (point[i][1] - point[j][3] + 1)
                
    print(f'#{testcase} ' + str(duplicate))
            