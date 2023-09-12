T = int(input())

for testcase in range(1, T+1):
    point = input()
    N = int((point.split())[0])
    M = int((point.split())[1])

    lists = input().split()

    sort_list = []
    for i in lists:
        sort_list.append(int(i))
    
    max_sum = -100000000000000000000000000
    min_sum = 100000000000000000000000000
    
    for k in range(0, N-M+1):
        default = 0
        for j in range(0, M):
            default += sort_list[k+j]
        if max_sum < default:
            max_sum = default
        if min_sum > default:
            min_sum = default
                

    print(f'#{testcase} ' + str(max_sum - min_sum))


    
    