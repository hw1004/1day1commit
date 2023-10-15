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
- 이진 탐색: **정렬되어 있는 리스트**에서 탐색 범위를 *절반씩* 좁혀가며 데이터를 탐색하는 방법
  - O(logN)의 시간 복잡도를 보장함
  - `bisect_left(a, x)`: 배열 a에 x를 삽입할 가장 왼쪽 인덱스 반환
  - `bisect_right(a, x)`: 배열 a에 x를 삽입할 가장 오른쪽 인덱스 반환
  - ex: a = [1, 2, 4, 4, 8]이고 x = 4 일 때 left 실행 시 인덱스 2에 4가 삽입되고 right 실행 시 인덱스 4에 4가 삽입됨
- **일반적인 선형 탐색(Linear Search)로는 시간 초과 판정을 받을 수 있기 때문에 정렬되어 있는 데이터에 한해서는 이진 탐색을 수행하면 시간 복잡도가 감소한다.**

- 이진탐색 library를 이용하여 데이터 개수 구하기
```
from bisect import bisect_left, bisect_right

def count(a, left, right):
  left_index = bisect_left(a, left)
  right_index = bisect_right(a, right)
  return right_index - left_index

print(count(a, 1, 3))
```
- **파라메트릭 서치**: 최적화 문제를 결정 문제(예, 아니오)로 바꾸어 해결하는 기법

## 5. collections
> 덱(deque), 카운터(counter) 자료구조 포함 (워드 클라우드 만들 때 유용!)

- 카운터(Counter): 등장 횟수 세기
  - `from collections import Counter`

## 6. math
> 수학적 기능 제공

- 최대공약수와 최소 공배수: `gcd()` 함수, `lcm`
