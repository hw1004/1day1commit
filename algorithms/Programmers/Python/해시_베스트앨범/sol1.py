# https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    
    answer = []
    # genres 재생횟수 많은 순
    genres_plays_asc = {}
    for i in range(len(genres)):
        if genres[i] in genres_plays_asc.keys():
            genres_plays_asc[genres[i]] += plays[i]
        else:
            genres_plays_asc[genres[i]] = plays[i]
    genres_plays_asc = sorted(genres_plays_asc.items(), key=lambda x: x[1], reverse = True)
    print(genres_plays_asc)
    # 장르 내에서 많이 재생된 노래 순
    for genre in genres_plays_asc:
        genre_plays = {}
        for i in range(len(genres)):
            if genres[i] == genre[0]:
                genre_plays.update({i:plays[i]})
        genre_plays = sorted(genre_plays.items(), key=lambda x: x[1], reverse=True)
        print(genre_plays)
        p = 0
        for k in range(len(genre_plays)): # 하나의 장르에 노래의 개수가 2보다 적을 수 있음
            p += 1
            if p <= 2:
                answer.append(genre_plays[k][0])

    return answer