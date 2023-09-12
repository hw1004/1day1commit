T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    positive_num = input().split()
    
    int_list = []
    for num in positive_num:
        int_list.append(int(num))
        
    sort_list = sorted(int_list)
    
    print(f'#{test_case} ' + str(sort_list[-1] - sort_list[0]))