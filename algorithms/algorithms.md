# 알고리즘
## 정렬 알고리즘
**정렬**: 데이터를 특정한 기준에 따라 순서대로 나열하는 것

### 선택 정렬 알고리즘
> 처리되지 않은 데이터 중 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것을 반복

- 시간 복잡도는 O(N^2)

```
unordered_list = [5,2,6,1,7,3,0]

for i in range(len(unordered_list)):
    minimum = i
    for j in range(i+1, len(unordered_list)):
        if unordered_list[minimum] > unordered_list[j]:
            minimum = j
    unordered_list[i], unordered_list[minimum] = unordered_list[minimum], unordered_list[i]

```

### 삽입 정렬 알고리즘
> 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입

- 시간 복잡도 및 효율성이 선택 정렬 알고리즘보다 좋음
- 시간 복잡도는 O(N^2)에서 O(N) 사이이고 데이터의 정렬도에 따라 동작 속도가 더욱 빨라짐

```
unordered = [5,2,6,1,7,3,0]

for i in range(1, len(unordered)):
    for j in range(i, 0, -1):
        if unordered[j] < array[j-1]:
            unordered[j], unordered[j-1] = unordered[j-1], unordered[j]
        else:
            break

```

### 퀵 정렬 알고리즘
> 기준 데이터(Pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법

- 기준 데이터를 기본적으로 첫번째 값으로 정하고 왼쪽부터는 기준값보다 큰 데이터를, 오른쪽부터는 기준값보다 작은 데이터를 고른다. 그리고 그 두 데이터를 바꾼다.
- 작은 데이터와 큰 데이터가 엇갈릴 때는 작은 데이터와 기준값을 바꾼다. 그 후 기준값의 위치가 바뀌었을 때 오른쪽과 왼쪽의 배열에서 각각 다시 퀵 정렬을 수행한다.
- 시간 복잡도는 O(N^2)에서 O(NlogN) 사이이다.
- 퀵 정렬을 수행하는 함수를 def로 만들어서 적용


### 계수 정렬 알고리즘
> 데이터의 크기 범위가 제한됨. 크기가 정수 형태로 표현 가능할 때 사용

- 가장 작은 수부터 가장 큰 수가 담길 수 있는 리스트 생성
- 각각의 수가 몇 번 등장했는지 세면서 데이터와 동일한 값의 인덱스의 count 값을 하나씩 늘림
- 각각의 수가 몇 개 등장했는지 세는 리스트를 활용해 첫 번째 데이터부터 하나씩 count 값만큼 반복하여 출력
- 비효율성을 초래할 수 있기 때문에 동일한 값을 가지는 데이터가 여러 개 등장할 때 효과적으로 사용 가능

```
array = [5,2,6,1,7,3,0]

new = [0] * (max(array)+1)

for i in range(len(array)):
    new[array[i]] += 1

for i in range(len(new)):
    for j in range(new[i]):
        print(i, end=' ')

```