# 이상치 탐색 및 제거
> **이상치 데이터**
> - 데이터의 특성의 분포를 볼 때 주로 나타나는 값의 분포가 아닌 너무 크거나 너무 작은 값인 경우 이상치로 판단함
> - 사분위수로 이상치를 주로 판단하지만 도메인적인 판단도 가미됨
> - 왜도 전처리 필요함

> **IQR Rules(사분위수)**
> - 데이터 집단을 크기 순으로 나열했을 때 4개의 구간으로 나뉘고 구간의 경계점을 1, 2, 3사분위수라고 명칭함
> - **IQR**: 3사분위수 - 1사분위수
> - **이상치(Outlier)**: 아래와 같이 분포에서 벗어난 데이터

![사분위수](https://thebook.io/img/080217/216.jpg)


- IQR rule 계산하는 함수 만들어서 이상치 판단

```
def IQR_rule(val_list):
    Q1 = np.quantile(val_list, 0.25)
    Q3 = np.quantile(val_list, 0.75)
    IQR = Q3 - Q1

    not_outlier = (Q3 + 1.5 * IQR > val_list) & (Q1 - 1.5 * IQR < val_list)
    return not_outlier

# 학습데이터에 함수 적용
conditions = Train_X.apply(IQR_rule)

# 이상치가 없는 레코드를 판별
no_out_row = conditions.sum(axis=1) == (len(Train_X.columns))
# True면은 이상치가 없는 레코드, False면 이상치가 있는 레코드
```

## DBSCAN 활용 이상치 판단 방법
- 밀도 기반 군집화 수행
- 군집에 속하지 않는 값은 이상치라고 간주

> **DBSCAN(Density-based Spatial clustering of applications with noise)** 는 점이 세밀하게 몰려 있어서 밀도가 높은 부분을 클러스터링 하는 방식이다. (어느 점을 기준으로 반경 x내에 점이 n개 이상 있으면 하나의 군집으로 인식하는 방식이다.)


1. `from sklearn.cluster import DBSCAN`
2. 학습데이터와 평가 데이터 임의로 분리 (`tran_test_split` 함수 사용)
3. plot에 나타나는 모든 점들끼리의 거리를 구해서 **거리행렬** 생성 (`distance.cdist(Train_X, Train_X)`)
4. 거리행렬을 연속적인 array로 반환한다. (`np.ravel(거리행렬)`)
5. 거리행렬을 연속적인 array로 변환한 것(DM_t)으로 **boxplot** 그리기 (`plt.boxplot(DM_t)`)
6. 1사분위, 2사분위, 3사분위수를 구하기 (`np.quantile(DM, 0.25)` => 1사분위수)
7. **특정 컬럼에 대한 이상치 판단이 아니라 전체 레코드의 특성상 어느 군집에도 포함되지 않으면 이상치로 판단한다.**
   - `cluster_model = DBSCAN(eps=0.63, min_samples=4).fit(Train_X)`
     - DBSCAN의 주요 파라미터
       - **eps**: 이웃이라고 판단하는 반경의 원의 반지름
       - **min_samples**: eps 내에 들어와야 하는 최소 샘플 수
       - **metric**: 사용하는 거리 척도
   - `sum(cluster_model.labels == -1)`: cluster_model.labels가 -1이면 군집 반경에 포함되지 않는 이상치로 판단한다. 이를 sum함수를 통해 이상치로 판단하는 값의 개수를 출력한다.
