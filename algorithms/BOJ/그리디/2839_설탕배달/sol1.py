# https://www.acmicpc.net/problem/2839
# 25분 걸림

# 3kg 봉지와 5kg 봉지
# 최대한 적은 봉지
# ex. 18kg -> 5 kg 3개, 3 kg 1개
# N kg을 배달하여야 할 때 5kg 봉지를 우선적으로 선택하고
# 5kg 봉지를 뺀 남은 kg 수가 3의 배수일 때까지 5kg 봉지를 선택하고
# 남은 kg 수를 3kg으로 채운다.
N = int(input())
remain = N
counts = 0

remain -= (N // 5)*5
counts += (N // 5)

if remain % 3 != 0:
    while remain <= N:
        remain += 5
        if remain > N:  # 정확히 N kg 만들어질 수 없을 때
            counts = -1
            break
        counts -= 1  # 5를 더해보기 떄문에 counts 하나 감소
        if remain % 3 == 0:  # 5를 더했을 떄 3으로 나누어 떨어지면
            counts += (remain // 3)  # 그만큼의 3kg 봉지를 들기
            break
    
else:
    counts += (remain // 3)
print(counts)