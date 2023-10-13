# 표준 라이브러리

## 1. 내장 함수
> sum(), min(), max(), eval(), sorted() 와 같이 자주 쓰인 내장된 함수
> eval()함수는 수식이 있을 때 그 수식을 계산하여 반환해줌

## 2. itertools
> 반복되는 형태의 데이터 처리를 위한 라이브러리 (순열과 조합)

- 순열 => 순서를 고려함
  - `from itertools import permutations`
  - `list(permutations(['a', 'b', 'c'], 2))`
- 조합 => 순서를 고려하지 않음
  - `form itertools import combinations`
  - `list(combinations(['a', 'b', 'c'], 2))`
- 중복 순열
  - `form itertools import product`
  - `list(product(['a', 'b', 'c'], repeat=2))`
- 중복 조합
  - `form itertools import combinations_with_replacement`
  - `list(combinations_with_replacement(['a', 'b', 'c'], 2))`

## 3. heapq
> 힙 자료구조 제공 (우선순위 큐/최단거리)

## 4. bisect
> 이진 탐색

- 순차 탐색: 리스트의 데이터를 찾기 위해 앞에서부터 하나씩 데이터를 확인하는 방법
- 이진 탐색: 

## 5. collections
> 덱(deque), 카운터(counter) 자료구조 포함 (워드 클라우드 만들 때 유용!)

- 카운터(Counter): 등장 횟수 세기
  - `from collections import Counter`

## 6. math
> 수학적 기능 제공

- 최대공약수와 최소 공배수: `gcd()` 함수, `lcm`
