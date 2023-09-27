my = [1, 2, 3, 4, 5, 6]

real = [1, 2, 3, 4, 5, 6]
bonus = 7

# 1등 my와 real이 6개 같음
# 2등 my와 real이 5개 같음 + my 나머지 하나가 bonus
# 3등 my와 real이 5개 같음
# 4등 my와 real이 4개 같음
# 5등 3개 같음

same_count = 0
for num in my:
    if num in real:
        same_count += 1
        
if same_count == 6:
    print(1)
elif same_count == 5 and bonus in my:
    print(2)
elif same_count == 5 and bonus not in my:
    print(3)
elif same_count == 4:
    print(4)
elif same_count == 3:
    print(5)