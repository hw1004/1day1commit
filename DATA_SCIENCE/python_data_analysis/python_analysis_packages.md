# 파이썬 데이터 분석 패키지

|package|description|
|---|---|
|Numpy|numerical python|
|Pandas|python data analysis|
|Matplotlib|data visualization|

## 파이썬 패키지 설치
```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```
- matplotlib의 기본 폰트에서 한글이 지원이 안 되기 때문에 폰트 변경 필요

```
# 한글 문제
# matplotlit의 기본 폰트에서 한글 지원되지 않기 때문에
# matplotlib의 폰트 변경 필요
import platform

from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':  # 맥OS 
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':  # 윈도우
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...  sorry~~~')
```

## data 불러오기 (csv, xls 파일)
- csv 파일 불러오기: `data = pd.read_csv('./data/서울특별시_일반음식점.csv', encoding='cp949', low_memory=False)`
- xls 파일 불러오기: `data = pd.read_excel('./data/01.population_in_Seoul.xls')`
- xls 파일에서 특정 열만 사용할 때: `data = pd.read_excel('./data/01.population_in_Seoul.xls', header=2, usecols = 'B, D, G, J, N')` => 첫번째 2행을 header로 처리하고 usecols에 있는 열만으로 테이블을 구성한다.


## data 조회/확인하기
### data
- 위에 데이터 확인하기 (기본값: 5개): `data.head(3)`
- 밑에 데이터 확인하기 (기본값: 5개): `data.tail(3)`
- 데이터 개요(일반정보(전체 행의 수) / Column, Non-Null Count, Datatype) 확인하기: `data.info()`

### column
- data가 들어있는 테이블의 column값들 확인하기: `data.columns`
- 특정 column의 모든 값들 확인하기: `data.<column명>`
- 특정 column의 모든 값들 array로 반환하기: `data.<column명>.values`
- 특정 column 값들의 종류 반환하기(중복을 제거한 column 값): `set(data.<column명>.values)`
- 특정 column의 값들 중 특정 단어를 가지고 있는 데이터 True로 반환(null값 제외): `data.<column명>.str.contains('특정 단어', na=False)`
- 특정 column의 값들 중 특정 단어들을 가지고 있는 데이터 True로 반환: `data.<column명>.isin([a, b])` (a 또는 b를 포함하는 데이터)

### slice, split
- `data.소재지전체주소.str.slice(start=11, stop=17)`: string 데이터들을 특정 인덱스 범위의 값만 slice해서 반환
- `data.소재지전체주소.str.split(' ').str[1]`: 뛰어쓰기를 기준으로 split해서 단어 리스트에서 필요한 인덱스를 규칙적으로 반환ㄴ

### 기타
- `data.rename(columns={원래값:바꾸려는 값}, inplace=True)`: column명을 바꿀 때 사용된다. `inplace=True`는 data가 바뀐 컬럼명으로 저장까지 되는 것이다.

## data 변형/삭제하기
- `data.<column명>.unique()`: 특정 column에 대해 column값들을 중복을 제외하고 반환한다.
- `data.<column명>.isnull()`: 값이 null이면 True를 반환하고 아니면 False를 반환한다.
- `data.sort_values(by=<column명>)`: 특정 column 값을 기준으로 data를 오름차순 정렬해준다. 내림차순의 경우 by 조건 옆에 `ascending=False`를 입력한다.
- `data = pd.merge(cctv_seoul, pop_seoul, on=None)`: `on`의 값을 기준으로 cctv_seoul과 pop_seoul의 데이터들을 합쳐준다. 교집합으로 inner join하는 방식이다.
- `del data[<column명>]`: 불필요한 column을 삭제해준다.
- `data.drop([0], inplace=True)`: pandas의 함수이며 0번째 행을 삭제해준다.
- `data.set_index('자치구별', inplace=True)`: 기본적으로 행 인덱스로 id값이 주어지는데, 이를 특정 컬럼(보통 첫번째 열)이 행 인덱스의 역할을 하게끔 설정하는 것이다.(시각화에 효율적)


## 정규식 패키지
`import re`
- `re.sub(정규식, 대체문자, 원문자).replace(' ','')`: replace와 같은 역할로 정규식의 예시는 r'[0-9]+'이고 정규식을 참조해 원문자에서 0-9까지의 숫자가 등장할 경우 대체문자로 변환하고 `.replace(' ', '')`는 빈칸을 제거해준 후 반환해준다.

## 상관관계
- **상관계수 분석**: 계수값이 절대값으로 0.3을 넘어가면 상관관계가 있다
  - 0.1 이하면 무시
  - 0.1 < 계수 <= 0.3이면 약한 상관관계
  - 값이 -면 음의 상관관계: 두 변수의 값 중 하나가 증가하면 나머지 변수의 값은 감소한다.
  - 값이 +면 양의 상관관계: 두 변수의 값 중 하나의 변수값 증가/감소하면 나머지 변수의 값도 증가/감소한다.

- `data.corr(data['소계'], data['고령자비율'])`: data 테이블의 컬럼들간의 상관계수를 계산하여 나타낸다.
- `data.corrcoef()`: 위의 코드가 모든 컬럼들간의 상관관계를 나타내준다면 이 코드로는 두개의 컬럼을 특정하여 그 두개의 컬럼의 상관계수를 반환할 수 있다.

## 시각화
### tree map 그래프를 활용한 시각화
```
!pip install --user squarify

import squarify
```
- `data.value_counts()`: 특정 column의 값들을 중복없이 나열했을 때 원본 데이터에 각 값들이 몇번씩 등장하는지 count한다.
- `squarify.plot(data, label=data.index)`: plot으로 나타나고자하는 data를 넣고 label은 tree map data의 면적에 해당되는 data index(예시: 연희동)를 각각의 면적에 표기하기 위함이다.
- `data.value_counts().values`: count한 개수들이 array로 출력됨
- `data.value_counts().index`: 특정 column의 값들(연희동, 옥천동...)이 array 형식으로 나타난다.

### barh 시각화
```
plt.figure(figsize=(10, 10))
data[['소계']].plot(kind='barh', grid=True)
# []를 두개 표시할 때는 주로 여러개의 비교값을 하나의 그래프에 나타낼 때!
```

- `data['소계'].sort_values().plot(kind='barh', grid=True)`: 소계가 많은 순으로 정렬해 줌

### 관계 표현 분산그래프 (약한 양의 상관관계)
```
plt.scatter(data.인구수, data.소계, s=50)  # s는 점의 크기
plt.xlabel('인구수')
plt.ylabel('구별 cctv 수')
plt.grid()
```

#### 산점도와 회귀선을 통해 분포를 보여주는 분산그래프

```
pip install seaborn
import seaborn as sns
```

- `sns.lmplot(x='인구수', y='소계', data=data_result)`: 회귀선이 포함된 분산그래프 반환