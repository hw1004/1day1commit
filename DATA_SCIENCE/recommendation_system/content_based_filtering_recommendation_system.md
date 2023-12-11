# 컨텐츠 기반 필터링 추천 시스템
> 사용자가 특정한 아이템을 매우 선호할 때, 그 아이템과 비슷한 컨텐츠를 가진 다른 아이템을 추천하는 방식
>
> (ex. 특정 영화에 높은 평점을 주었을 때, 그 영화의 장르, 출연 배우, 감독, 영화 키워드 등이 유사한 다른 영화 추천)

## 컨텐츠 기반 필터링 구현 프로세스
1. 영화별 컨텐츠(장르)에 대한 여러 텍스트 정보들을 피처 벡터화
   1. 카운트 기반의 벡터화
        - 단어의 빈도 수
        - 카운트 값이 높을수록 중요 단어로 인식
        - `from sklearn.feature_extraction.text import CountVectorizer`: 단어 카운트
          - `min_df`: 정한 퍼센트 이하로 나오는 단어 제거
          - `max_df`: 정한 퍼센트 이상 나오는 단어 제거
          - `ngram_range=(1, 2)` 파라미터: 한개의 단어와 두개의 단어를 합쳐서도 만들라는 뜻
   2. TF-IDF(Term Frequency-Inverse Document Frequency) 기반의 벡터화
        - 개별 문서에서 자주 나타나는 단어에 높은 가중치
        - 모든 문서에서 전반적으로 자주 나타나는 단어에는 패널티 줌
        - 문서마다 텍스트가 길고 문서의 개수가 많은 경우, TF-IDF 기반이 더 선호되며 카운트 기반의 벡터화를 보완해준다.
2. **코사인 유사도**로 컨텐츠별 유사도 계산
   ![](https://mblogthumb-phinf.pstatic.net/MjAyMDExMjJfNCAg/MDAxNjA2MDMxNjEzNDM4.22sWFjl5her1D_YNTWJgpi75LVe4TusTnGlAQnG27Lkg.m8hcgkUMZai9xX9cJymHvXXkMTkpJwX0YNUEYXLoldsg.PNG.dmtgjh/image.png?type=w800)
   - 벡터와 벡터 간의 코사인 각도를 이용해서 유사도 산정
   - 방향이 완전 동일: 1 (1에 가까울수록 유사도 높음)
   - 벡터 사이의 각 90도: 0 (상관관계 없음)
   - 벡터 사이의 각 180도: -1 (완전 반대)
   - `from sklearn.metrics.pairwise import cosine_similarity`
   - `cosine_similarity(df.values)`: df.values의 요소들 간의 유사도 반환
3. 컨텐츠 별로 **가중 평점** 계산
   - Weighted Rating: (v/(v+m)) * R + (m/(v+m)) * C
     - v: 개별 영화에 평점을 투표한 횟수
     - m: 평점을 부여하기 위한 최소 투표 횟수
     - R: 개별 영화에 대한 평균 평점
     - C: 전체 영화에 대한 평균 평점
4. 유사도가 높은 컨텐츠 중 평점이 좋은 컨텐츠 순으로 추천

