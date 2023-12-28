# RDD Transformation, Action
> Transformation: 데이터를 가공하기 위한 논리적 실행계획 - action 함수가 적용될 때까지 지연연산을 진행한다.
>
> Action: transformation 연산을 통해 생성한 실행계획을 최적화하여 연산을 수행함

## Transformation 메서드
1. filter(): 조건에 맞는 데이터만 추출
   - `score_rdd.filter(lambda e : '스파크' in e)`
   - **셔플**: 모든 키에 대한 모든 값을 찾기 위해 모든 파티션을 탐색하고 해당 값들을 하나의 파티션으로 옮겨온는 과정
   - filter를 이용하면 각 파티션에 있는 하나의 튜플에 대해 조건을 탐색하면 되기 때문에 셔플이 발생하지 않는다.
2. map(): 전달 함수의 연산을 rdd 객체의 각 요소별로 적용한 결과를 합해서 rdd 객체로 반환
   - `rdd2.map(lambda e : e*2)`
3. flatMap(): 각각의 요소에 함수를 적용하고 평면화 시켜준다.
   - `score_rdd.flatMap(lambda e : e + '점')`
4. distinct(): 중복을 제거하고 유일 원소로 구성된 rdd 객체로 반환
   - `dist_rdd.distinct()`
5. zip(): 두개의 집합 객체를 전달받아서 인덱스가 동일한 원소들끼리 튜플로 묶어서 반환
   - 두개의 리스트를 rdd 객체 foods, category로 생성했을 때
   - `category.zip(foods)`를 진행하면 반환되는 튜플의 0번 index key가 category, 1번 index value가 foods로 반환됨
6. join(): 두개의 rdd 객체의 key를 기준으로 key값이 같은 요소들끼리 결합
   - `students.join(sub_avg)`
7. reduceByKey(): key값을 기준으로 동일 키 요소들끼리 그룹화하여 value값들을 연산
   - `tmp.reduceByKey(lambda a, b : a + ',' + b)`
8. mapValues(): key-value 쌍에서 value값만 전달하여 map 연산 진행
   - `tmp.mapValues(lambda e : e.split(', '))`: e는 key-value쌍에서 value
9.  flatMapValues()
10. sortBy(): rdd 객체 중에 pair-rdd일 경우에 정렬 기준을 정해야 한다.
    - key 기준 오름차순: `res.sortBy(lambda e : e[0])`
    - value 기준 오름찻순: `res.sortBy(lambda e : e[1])`
    - key 기준 내림찻순: `res.sortBy(lambda e : e[0], ascending=False)`
    - value 기준 내림차순: `res.sortBy(lambda e : e[1], ascending=False)`
11. groupByKey


## Action Method
1. collect(): rdd 안의 모든 데이터를 파이썬 리스트로 반환한다. 따라서 rdd 객체를 collect하면 리스트 형태로 반환된다.
2. take(): 인자로 받은 수량만큼 데이터를 리스트로 반환한다.
3. takeOrdered(): rdd 객체를 정렬한 후에 인자로 받은 수량만큼 데이터를 리스트로 반환한다.
4. top(): rdd 객체를 *내림차순* 정렬한 후에 인자로 받은 수량만큼 데이터를 리스트로 반환한다.
5. coutByValue(): rdd 객체에서 같은 요소들이 몇 개있는지 count해서 반환한다.
   - `sc.parallelize(['a', 'a', 'b', 'b', 'b', 'c', 'c', 'd']).countByValue()`
   - 결과값: defaultdict(int, {'a': 2, 'b': 3, 'c': 2, 'd': 1})
6. foreach(): rdd의 모든 요소에 특정한 함수를 적용하는 메서드
   - `def f(x): print(x)`
   - `nums.foreach(f)`
7. reduce(): 각 요소에 대해 주어진 함수를 실행하고 하나의 결과를 반환한다.
8. saveAsTextFile(): rdd를 텍스트 파일로 저장
   - 파티셔닝 되어 하둡에 디렉토리로 저장된다. (디렉터리 내부에서 rdd 객체 구성할 때 사용했던 파티션 모두 저장됨)
9.  fold(): reduce와 비슷한데 기본값이 있다.
    - `rdd = sc.parallelize([5,4,3,2],4)`
    - `fold_rdd_b = rdd.fold(3,lambda x,y : x+y)`
    - 여기서, 기본값 3을 더한 8, 7, 6, 5에 대해 함수 연산을 적용한고, 이 때 기본값 3까지 더해주기 때문에 8 + 7 + 6 + 5 + 3이 된다.
10. max()
11. min()
12. mean()
13. variance()
14. stdev()
15. stats()