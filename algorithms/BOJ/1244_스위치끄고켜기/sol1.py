

switch = int(input())
onoff = [int(i) for i in input().split()]
student = int(input())
cases = []
for testcase in range(student):
    cases.append([int(i) for i in input().split()])

# 학생이 받은 수를 기준으로 스위치 상태 변경
for testcase in range(student):
    
    if cases[testcase][0] == 1:    # 남학생
        for i in range(1, switch+1):
            
            if i % cases[testcase][1] == 0:
                if onoff[i-1] == 0:
                    onoff[i-1] = 1
                else:
                    onoff[i-1] = 0
    
    elif cases[testcase][0] == 2:    # 여학생
        # 양 옆 대칭으로 탐색
        case = cases[testcase][1] - 1
        
        if onoff[case] == 0:
            onoff[case] = 1
        else:
            onoff[case] = 0
            
        for i in range(1, switch):
            
            if onoff[case-i] == onoff[case+i]:
                if onoff[case-i] == 0:
                    onoff[case-i] = 1
                    onoff[case+i] = 1
                elif onoff[case-i] == 1:
                    onoff[case-i] = 0
                    onoff[case+i] = 0
            else:
                break
            
            if case-i <= 0 or case+i >= switch-1:
                break
        
            
print(' '.join([str(i) for i in onoff]))
            
            
        
        