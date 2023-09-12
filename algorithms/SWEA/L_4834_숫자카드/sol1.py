T = int(input())


for testcase in range(1, T+1):
    N = int(input())
    numbers = input()
    
    lists = []
    for num in numbers:
        lists.append(int(num))
    
    count_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            
    for i in lists:
        count_list[i] += 1
    
    i = len(count_list)-1
    while True:
        if count_list[i] == max(count_list):
            print(f'#{testcase} ' + str(i) + ' ' + str(count_list[i]))
            break
        else:
            i -= 1
        
        