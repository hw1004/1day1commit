# DataFrame
## DataFrame 생성
> `SparkSession.createDataFrame(data, schema=None, samplingRatio=None, verifySchema=True)`

## Row 객체로 DF 생성
```
!pip install pandas

import pandas as pd
from datetime import date, datetime
from pyspark.sql import *

df = spark.createDataFrame([
    Row(name='김철수',age=15,birth=date(2022,7,22)),
    Row(name='이제동',age=20,birth=date(2021,7,22)),
    Row(name='김명운',age=25,birth=date(1998,7,22))
])

df.show()
```
<schema 생성>
- `df.printSchema()`: 데이터 프레임의 스키마 구조 확인
```
# 스키마를 명시해서 데이터프레임을 생성할 수 있다.
df2 = spark.createDataFrame([
    Row(name='김철수',age=15,birth=date(2022,7,22)),
    Row(name='이제동',age=20,birth=date(2021,7,22)),
    Row(name='김명운',age=25,birth=date(1998,7,22))
], schema = 'name string, age int, birth date')

df2.show()
```

<StructType 객체로 Schema 지정>
```
from pyspark.sql.types import *

data = [
    ('김철수', 15, date(2022,7,22)),
    ('이제동', 20, date(2021,7,22)),
    ('김명운', 25, date(2020,7,22))
]

schema = StructType([
    StructField('name',StringType(),False),
    StructField('age',IntegerType(),False),    
    StructField('birth',DateType(),False)    
])

df3 = spark.createDataFrame(data=data, schema=schema)
```

## 중첩 스키마 적용
- 컬럼의 데이터가 단일 데이터가 아니라 iter 데이터일 때 해당 컬럼의 스키마를 컬럼 원소값 각각에 대해 생성할 수 있다.
- 예를 들면 전화번호 010-1234-5678에서 -를 기준으로 3개의 원소에 대해 각각 스키마를 생성한다.

```
data = [
    ('김철수', 15, date(2022,7,22), ('010','1111','2222')),
    ('이제동', 20, date(2021,7,22), ('010','2222','3333')),
    ('김명운', 25, date(2020,7,22), ('010','4444','5555'))
]

schema = StructType([
    StructField('name',StringType(),False,{'desc':'이름'}),
    StructField('age',IntegerType(),False,{'desc':'나이'}),    
    StructField('birth',DateType(),False,{'desc' :'생일'}),
    StructField('phone', StructType([
        StructField('phone1',StringType(),True),
        StructField('phone2',StringType(),True),
        StructField('phone3',StringType(),True)]),False,{'desc':'전화번호'}) # 중첩스키마
])

df4 = spark.createDataFrame(data=data, schema=schema)
```