# RDD
> [spark RDD](https://github.com/hw1004/TIL/blob/main/DATA_SCIENCE/data_engineering/00_Data_engineering/hadoop.md) 관련 내용 정리

1. 파이썬 객체 리스트를 spark rdd 객체로 변환한다.
   - `foods = sc.parallelize(list)`
   - `foods = sc.parallelize(list, 1)`: 파티션 수를 한개로 명시
2. 파티셔닝 수 반환
   - `foods.getNumPartitions()`
3. rdd 객체를 출력이 가능한 형태로 변환 후 반환
   - `foods.collect()`

## Map_Reduce
