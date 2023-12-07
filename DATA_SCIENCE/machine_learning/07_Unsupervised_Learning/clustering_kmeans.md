# 비지도 학습
> **비지도 학습**: 결과값 없이 입력값만 주고 학습을 시켜 유사성 파악하게 하는 방식
>
> 1. 비지도 변환: 데이터를 새롭게 표현해서 더 쉽게 해석할 수 있도록 함 (ex. 차원축소 - 피처가 많은 데이터를 특성의 수를 줄이면서 꼭 필요한 특징을 포함한 데이터로 표현하는 방법)
> 
> 2. 군집: 데이터를 비슷한 것끼리 그룹화 (ex. k-means, DBSCAN)


## 군집화
- 데이터 포인트들을 별개의 군집으로 그룹화 하는 것
- 유사성 높은 데이터들을 같은 그룹으로 분류

### 군집화 알고리즘
1. K-Means: centroid를 선택해서 centroid에 가장 가까운 포인트들 선택
   - `KMeans(n_clusters=3, init='k-means++', max_iter=300, random_state=0)`: n_clusters로 centroid 개수 설정, init으로 초기 centroid 좌표 설정
   - 결과값 없이도 특징들을 고려해서 n_clusters만큼 데이터를 군집화시킴
2. Mean Shift
3. Gaussian Mixture Model
4. DBSCAN