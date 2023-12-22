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