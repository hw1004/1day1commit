num = int(input())

scores = input().split()

int_scores = []
for score in scores:
    int_scores.append(int(score))

M = max(int_scores)

total = 0
for score in int_scores:
    total += int(score) / int(M) * 100
    

    
print(total / num)

