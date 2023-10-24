# 데이터 전처리

## python packages
1. `from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"`: jupyter notebook에서 마지막 값만 출력하지 않고 출력값이 있는 모든 값을 출력한다.


## 데이터 병합
- `pd.merge(df1, df2, left_on=[], right_on=[])`: 두 데이터 파일을 병합한다. `left_on`에는 df1에서 병합할 columns들의 list를, `right_on`에는 df2에서 병합할 columns의 list를 적는다. 아파트와 건물명은 다른 명칭이지만 컬럼이 가지는 데이터는 나타내는 바가 같다. 따라서 아파트를 left_on, 건물명을 right_on에 배치한다.
- `df.set_index(['아파트'], inplace=True)`: 아파트 컬럼을 테이블의 index로 설정한다. `inplace=True`는 변경내용을 적용하여 저장하는 것이다.

#### 하버사인 패키지
- `!pip install haversine`으로 설치
- `from haversine import haversine`으로 하버 사인 설치
> 평면이 아니라 곡선으로 거리가 생성되므로(지구의 특성) 피타고라스 정리는 사용할 수 없기 때문에 곡선의 거리를 구하는 공식인 하버 사인 공식을 사용한다.

- `from scipy.spatial.distance import cdist`는 두개의 행렬을 바탕으로 거리 행렬을 반환하는 함수를 불러온다.
- `cdist(df1, df2, metric=haversine)`: 거리 측정 기준으로 haversine을 사용해서 df1과 df2 사이의 곡선 거리를 구하고자 함


- `pd.Dataframe(dist_mat, columns=df3.index, index=df.index)`: dataframe 생성을 하는 것(이 때, columns와 index로 행과 열의 index를 지정해줄 수 있다.)
- `loc[]`: 특정 인덱스를 가지는 행을 반환
- `iloc[:10,;]`: iloc[행, 열]로 처음부터 10개의 행과 그 행 들의 전체 열을 반환하는 것
- `np.array()`: list를 가지고 배열을 생성하는 것이다.
- `.reshape(-1, 3)`: 배열(np.array(list))이 [1, 2, 3, 4, 5, 6] 이런식이라면 행은 열에 맞추고(-1) 열은 3개로 반환하라는 것이다. 즉, [1, 2, 3, 4, 5, 6]을 열 3개로 반환하면 [1, 2], [3, 4], [5, 6]이 된다.
- `.argsort(axis=0)`: array를 정렬하는 함수이다. axis=0이면 행이기 때문에 같은 열에 위치한 행들의 크기를 비교하여 인덱스를 매긴다. axis=1이면 열이기 때문에 같은 행에 위치한 열들의 크기를 비교하여 인덱스를 메긴다.
  - 아파트와 가까운 지하철역의 순서를 알아야 할 때 아파트가 행의 index, 지하철역이 열의 index라고 하면 .argsort(axis=1)을 이용해서 각 아파트에서 가까운 지하철역 순위를 알 수 있다.


## **데이터 요약이 포함되는** 데이터 병합
> 중복 레코드(중복 되는 ID와 같은 것들)을 포함하는 데이터를 요약한 후 병합
> 예를 들어 고객 데이터와 고객 구매 데이터가 있을 때 고객 ID가 중복되고, 고객 구매 데이터에도 유일한 고객 ID를 가진 고객이 여러개의 주문을 생성할 수 도 있다.

|python|usage|description|
|---|---|---|
|`df.groupby()`|데이터 요약|특정 column에 대해서 같은 값을 가진 것들끼리 group한다. 주로 `count()`를 같이 사용하여 `df.groupby('고객ID')['구매금액'].count()`와 같이 고객ID별로 group하여 고객별로 구매 횟수를 count한다.|
|`.rename()`|값들이 포함된 column의 index명을 재지정한다.|
|`right_index=True`|병합 기준 지정|데이터를 병합할 때 `merge()`함수에서 right_index=True 조건이 들어가면 해당 객체 인덱스가 병합 기준이 된다.|
