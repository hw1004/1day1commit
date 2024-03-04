# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# start 포인트를 리스트에 넣어놓고 대응되는 end 포인트에 따라 pop을 진행한다.
# 선행되는 start가 없는데 end 포인트가 등장하면 False를 리턴
# for loop을 다 돌리고 나서 남은 원소가 start에 남아 있더라도 False를 리턴
# 효율성 검사 통과함

def solution(s):
    # "("에 대응되는 ")"가 있어야 함
    # list에 "("가 등장할 때 추가하고 만약 ")"가 나왔는데 리스트가 비어 있다면 false를 반환
    start = []
    for i in s:
        if i == "(":
            start.append("(")
        else:
            if len(start) == 0:
                return False
            else:
                start.pop()  # start가 비어있지 않는데 ")"를 마주쳤으면 pop해서 지워준다.
    # start의 원소가 남아 있지 않으면 True, 매칭이 안되어서 남아있으면 False
    if len(start) == 0:
        return True
    else:
        return False