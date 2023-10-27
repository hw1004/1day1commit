# 범주형 데이터
## 변수 크기 조정
### 피처 스케일링과 정규화
> **피처 스케일링**: 서로 다른 변수의 값 범위를 일정한 범위 수준으로 맞추는 작업
>- Z-scaling: 표준화 작업
>   - 평균이 0, 분산이 1인 정규분포로 변환
>   - `sklearn.preprocessing.StandardScaler` 모듈을 사용한다.
>   - 사전에 **반드시** 표준화 작업을 진행해야 함
> - Min-Max scaling: 0~1 사이의 값으로 변환하는 작업
>   - 최소값 0, 최댓값 1
>   - `sklearn.preprocessing.MinMaxScalar` 모듈을 사용한다.

### **Z-scaling (StandardScaler)**
- (Xi - (X 컬럼의 평균))/(X의 표준편차)

1. `from sklearn.preprocessing import StandardScaler`
2. `scaler = StandardScaler()` 객체 인스턴스 생성하기
3. `scaler.fit(iris_df)`: sepal length, sepal width, petal length, petal width를 컬럼으로 가진 iris_df의 각 컬럼의 평균과 표준편차를 계산하여 위의 통계량을 구한다. (인스턴스 값 - 평균)/표준편차
4. `scaler.transform(iris_df)`: z-scaling 데이터프레임에 적용하기
5. 정규화된 값을 데이터프레임으로 나타내 준다. : `pd.DataFrame(data=scaler.transform(iris_df), columns=iris.feature_names)`
6. 변환 후에 특성의 평균값을 `.mean()`함수로 구해서 변환 이전의 특성의 평균값과 비교해 보면 0에 가깝게 됨을 볼 수 있고 표준편차는 1에 가깝게 된 것을 볼 수 있다.


### **MinMaxScaler**
- 데이터의 분포가 정규분포와 너무 관련이 없을 때 MinMaxScaler을 사용한다.
- 도메인적으로 해당 컬럼(특성)의 최솟값과 최댓값이 변경되지 않는다는 것이 신뢰되면 사용한다.

1. `from sklearn.preprocessing import MinMaxScaler`
2. `m_scaler = MinMaxScaler()`: 객체 인스턴스 생성
3. `m_scaler.fit(iris_df)`로 최소/최댓값 통계량을 설정해주고 `m_sclaer.transform(iris_df)`로 적용해준다.
4. `.max()`, `.min()` 함수를 적용하여 특성들의 최대최소 값을 구한다.
5. (xi - min(X))/(max(X) - min(X))를 사용하여 0~1 사이의 값으로 데이터들을 변환해준다.


## 변수 치우침 제거
- 모델링에 가장 적합한 확률분포는 **정규분포**이다.
- 수집된 data들은 특정방향으로 치우쳐져 있는데 한쪽으로 치우친 변수에 대해서는 꼬리부분이 이상치처럼 작용할 수 있으므로 치우침을 제거해야 한다.
- **왜도**는 분포의 비대칭도를 나타낸다.
  - |왜도| >= 1.5 이면 데이터 분포가 치우쳤다고 판단한다.

![왜도](https://www.oppadu.com/wp-content/uploads/2021/02/%EC%97%91%EC%85%80-skew-%ED%95%A8%EC%88%98-%EC%99%9C%EB%8F%84-%EC%84%A4%EB%AA%85-768x315.png)

1. `df.skew()`를 통해 데이터의 왜도를 확인할 수 있다. (절대값이 1.5 이상이면 해당 컬럼의 데이터들이 비대칭이라고 판단)
2. matplotlib의 `hist()`를 통해 왜도(skewness) 확인
3. 왜도를 기준으로 치우친 변수 제거한 컬럼들의 집합: `df.columns[df.skew().abs() <= 1.5]`
4. 왜도를 기준으로 치우친 변수들의 집합: `df.columns[df.skew().abs() > 1.5]`
    - 왜도를 기준으로 치우친 변수들에 대해 log 변환
    - `np.log2(df[왜도 1.5보다 큰 컬럼]).hist()`
    - log 변환한 값으로 기존의 값 대체
    - `df[왜도 1.5보다 큰 컬럼들의 집합] = np.log2(df[왜도 1.5보다 큰 컬럼들의 집합])`
5. log 변환 후 컬럼들의 왜도를 확인해보면 왜도 절대값이 1.5를 초과하는 컬럼이 없어짐
    - 다만, 모든 데이터가 log 변환 후 왜도값이 1.5 이하로 떨어지는 것은 아니다.
    - 치우침을 제거했다고 하더라도 성능이 절대적으로 좋아지는 것은 아니다.