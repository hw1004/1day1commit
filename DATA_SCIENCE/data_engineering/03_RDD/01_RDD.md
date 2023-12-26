# RDD
> [spark RDD](https://github.com/hw1004/TIL/blob/main/DATA_SCIENCE/data_engineering/00_Data_engineering/hadoop.md) 관련 내용 정리

1. 파이썬 객체 리스트를 spark rdd 객체로 변환한다.
   - parallelize 함수내 data 전달은 집합형으로 전달되어야 한다.
   - `foods = sc.parallelize(list)`
   - `foods = sc.parallelize(list, 1)`: 파티션 수를 한개로 명시
2. 파티셔닝 수 반환
   - `foods.getNumPartitions()`
3. rdd 객체를 출력이 가능한 형태로 변환 후 반환
   - `foods.collect()`

## Map_Reduce
> - Map: data의 각 원소를 key-value 형식으로 구성한다.
> - Reduce: key를 기준으로 value 처리

1. 1차원 구조의 data를 key value RDD로 생성하는 함수를 생성한다.
```
def single2key(rdd):
   foods_tmp = rdd
   return (foods_tmp, 1)
```
2. Map 처리: foods의 원소 각각에 single2key 함수를 호출한다.
   - `key_rdd = foods.map(single2key)`
   - key_rdd는 map 객체이다.
   - key만 추출: `key_rdd.keys().collect()`
   - value만 추출: `key_rdd.values().collect()`
   - key 기준 정렬: `key_rdd.sortByKey().collect()`
   - key가 같은 원소들끼리 그룹 형성: `key_rdd.groupByKey().collect()`
   - value의 형태 변환: `key_rdd.groupByKey().mapValues(list).collect()`: 그룹 형성되어 있는 key들에 대해 각각의 values를 list 형태로 반환
   - 동일한 원소들끼리 개수 세서 반환: `foods.countByValue()`
3. Reduce 처리: key-value rdd를 사용해서 그룹핑을 진행한다
   - key를 기준으로 동일한 키의 value를 더하는 작업을 진행한다.
   - `count = key_rdd.reduceByKey(lambda a, b = a+b)`
4. key-value map 객체에 대해 values를 조정/추가
   - `mapValues(연산함수)`
   - `count_mapvalues = count.mapValues(lambda x : (x, 1))` : 지연 연산 
   - 원래 ('짜장면', 4) 형식의 map 객체를 ('짜장면', (4, 1)) 형식으로 바꾼다.
5. 연산함수 연산 진행: `count_mapvalues.collect()`


## RDD 기본 함수
|function|description|ex|
|---|---|---|
|`take(하위집합의 수)`|RDD 데이터의 일부를 확인하는데 사용되고 하위집합의 수만큼의 데이터만 불러온다.|`foods.take(3)`|
|`first()`|데이터의 첫번째 하위 집합을 반환한다.|`foods.first()`|
|`counts()`|rdd 객체의 하위집합 수를 반환한다.|`foods.count()`|
|`distinct()`|중복을 제외한 원소를 생성한다.|`foods.distinct().collect()`|
|`foreach(연산함수)`|RDD의 각 요소에 연산함수를 적용하는 연산함수이다.|`def f_tmp(x) : print(x)`라는 함수가 있을 때 rdd 객체인 foods에 대해 `foods.foreach(f_tmp)`를 통해 foods의 각 원소에 f_tmp 함수를 적용할 수 있다.|
|`foreachPartition`|RDD 파티션에 기능을 적용한다. 파티션별로 일부 작업을 수행할 때 사용한다.|`def f1(iterator): for x in iterator: print(x)`라는 함수가 있을 때 rdd 객체인 foods에 대해 `foods.foreachPartition(f1)`을 통해 파티션별로 f1 함수를 수행할 수 있다.|
|`map()`|iterable한 data structure의 모든 요소 각각에 함수를 적용시킨다. (key-value 생성할 때 주로 사용한다.)|`sc.parallelize([1, 2, 3]).map(lambda x: x+2).collect()`|
|`flatMap()`|iterable한 객체의 각 요소를 한 단계 더 작은 단위로 쪼갠다. map 기능에 flat 기능이 포함된다.|`flatmapMovies = movieRDD.flatMap(lambda x: x.split(" "))`: split() 적용해서 2차원 구조로 완성된 결과에 flat 적용해서 1차원으로 변환한다.|
|`filter(조건함수)`|조건함수에 만족하는 데이터만 추출한다.|`flatmapMovies.filter(lambda x: x != "매트릭스")`|
|`intersection()`|교집합|`num1.intersection(num2)`|
|`union()`|합집합(중복 포함)|`num1.union(num2)`|
|`subtract()`|차집합|`num1.subtract(num2)`: num1에서 num2의 원소 빼기|
|`groupBy([함수])`|요소들을 동일한 key값으로 분류하는 함수|`foods.groupBy(lambda x: x[0])`: 각 요소의 첫글자가 같은 요소들끼리 그룹 생성|

