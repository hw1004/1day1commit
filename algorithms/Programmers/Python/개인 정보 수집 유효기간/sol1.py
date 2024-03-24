def solution(today, terms, privacies):
    from datetime import datetime
    from datetime import timedelta
    # 모든 달은 28일까지 있다.
    # A 6달
    # B 12달
    # C 3달
    
    # terms
    answer = []
    for term in terms:
        answer.append(term.split())
        
    # privacies
    privacy = []
    for i in privacies:
        privacy.append([datetime.strptime(i.split[0],'%Y-%m-%d'),i.split[1]])
    
    # privacy의 각 원소를 for loop으로 돌면서 유효마감일을 수집한다.
    due = []
    for i in pravacy:
        for t in answer:
            if i[1] == t[0]:
                due.append(i[0] + timedelta(months=6))

        
    return due