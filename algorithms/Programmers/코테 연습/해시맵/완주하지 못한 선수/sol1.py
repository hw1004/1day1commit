# https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    # dictionary를 만들어서 participant의 이름별 사람 수를 센다.
    # dictionary에서 completion에 있는 사람들을 하나씩 빼고
    # value가 0이 아닌 사람을 return한다.
    participate = {}
    for person in participant:
        if person in participate:
            participate[person] += 1
        else:
            participate[person] = 1
    
    for complete in completion:
        if participate[complete] == 0:
            continue
        else:
            participate[complete] -= 1
    
    for name, counts in participate.items():
        if counts != 0:
            return name