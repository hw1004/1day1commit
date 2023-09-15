T = int(input())

for tc in range(1, T+1):
    cut = list(map(str, input()))
    
    lines = 0
    
    cut_point = []
    
    # '('를 만날 때와 ')'를 만날 때
    # 마지막 원소를 list에서 없애는 pop의 속성을 이용
    for i in range(len(cut)):
        if cut[i] == '(':
            cut_point.append('(')
        elif cut[i] == ')':
            if cut[i-1] == ')':
                cut_point.pop()
                lines += 1
            else:
                cut_point.pop()
                lines += len(cut_point)
    
    print(f'#{tc} {lines}')
    
    
    # 또 다른 풀이로는 replace를 이용하여 레이저를 다른 기호로 변경하고 계산