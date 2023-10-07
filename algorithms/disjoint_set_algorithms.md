# 서로소 집합 알고리즘
## 서로소 집합(disjoint sets)
- 공통 원소가 없는 두 집합
- **서로소 집합 자료구조**: Union Find 자료구조라고도 불리며 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
  - 합집합(Union), 찾기(Find) 연산 지원
  - **합집합**: 서로 연결된 a, b 노드의 루트 노드 A, B를 찾고 이를 부모 노드로 설정/ 여러번의 합집합 연산 끝날 때까지 반복
  - **찾기(Find) 함수를 최적화**하기 위해 *Path Compression*을 이용할 수 있음 => 찾기 함수 수행 후 해당 노드의 루트 노드가 바로 부모 노드가 됨
- 서로소 집합 자료구조에서는 **연결성**을 통해 집합의 형태를 확인할 수 있음

1. 처리할 연산들 확인 (ex) Union(1,4)
2. 부모 노드 초기화
3. 1, 4의 root node 찾기 (더 큰 root node가 더 작은 root node를 가리킴)
4. 따라서 1과 4의 root node는 1과 4로, 더 큰 root node의 값인 4의 root node가 1이 된다.
5. 연산들에 포함된 노드들의 부모 노드들을 지속적으로 찾는다.(루트 노드를 찾을 때까지 재귀 호출)

![서로소 집합 알고리즘](https://velog.velcdn.com/images/giraffelim/post/ac6af4b0-b8ad-45c1-b29d-d69165b03cf7/image.png)

<서로소 집합을 이용한 사이클 판별>
- 무방향 그래프에서 사이클 판별할 때 사용
1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드 확인
2. 루트 노드가 서로 다르면 합집합 연산 수행, 같으면 사이클이 발생했다고 할 수 있다. 이를 모든 간선에 대하여 반복

- 루트 노드가 서로 다를 때 합집합 수행
![1과 3의 루트 노드 다름](https://mblogthumb-phinf.pstatic.net/MjAyMjA4MDlfMjk5/MDAxNjYwMDQwNzY2MTY5.gtqMj9ytJBCvabIqOnKG-bjLUEirO3p3aH-6yunJ6zUg.WC0x98ZytImqmuA_R8Sja431dGZvbSlxuMcX5i8o_jgg.PNG.chanmuzi/image.png?type=w800)
![1과 3 합집합 수행](https://mblogthumb-phinf.pstatic.net/MjAyMjA4MDlfOTAg/MDAxNjYwMDQwNzg1MjM3.h0KvAcrCFSR9TNF6fBoQHbRp5keirl9PrK1Z8SU1Hhsg.ajlAjyx8cMID2IU0OOjmvdnP3JMUDo_SXdP9c7yMQKkg.PNG.chanmuzi/image.png?type=w800)

- 루트 노드가 서로 같을 때 사이클 발생 인지
![사이클 발생](https://mblogthumb-phinf.pstatic.net/MjAyMjA4MDlfMjI3/MDAxNjYwMDQwODE2NDUx.0z8DknjQq74G7fBqFJ1ZYw1auXXhL0n96fEihm3pyQ8g.iQcsDqaDZvyPKWa8UNgcAke-lwa7HHcykTYCtJSLWbwg.PNG.chanmuzi/image.png?type=w800)

