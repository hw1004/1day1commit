T = int(input())

for tc in range(1, T+1):
    cut = input()
    
    lines = 0
    start = 0
    end = 0
    
    i = 0
    while i < len(cut):
        if cut[i] == '(' and cut[i+1] == ')':
            lines += start - end
            i += 2
        elif cut[i] == '(':
            start += 1
            i += 1
        elif cut[i] == ')':
            end += 1
            i += 1
    # end될 때 line 하나씩 추가해야 됨
    lines += end
    
    
    print(f'#{tc} {lines}')