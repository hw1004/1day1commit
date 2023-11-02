# 교차 검증
## 검증 세트
> 모델의 과적합 여부를 파악하기 위한 데이터 세트이다.
> 훈련 데이터에서 검증 세트를 분리해서 사용한다.

## 교차 검증 방법
> 1. K 폴드 교차 검증
> - K개의 데이터 폴드를 생성해서 각 폴드에 학습, 검증 평가를 반복적으로 수행한다.
> 2. Stratified K 교차 검증
> - 불균형한 분포도를 가진 데이터에 사용하며 process는 K 폴드 교차 검증과 유사하다. 
>   - 대출 사기의 경우 사기인 경우가 매우 적게 나타나는데 사기인 경우가 학습/테스트 데이터 중 하나에 몰려져 있으면 안된다. 이 때, 미리 원본 데이터 레이블의 분포를 파악한 후에 이 분포와 동일하게 학습/검증 데이터 세트를 분배한다.
> - 분류에서는 대게 Stratified K 교차 검증을 사용한다.

![](https://imghub.insilicogen.com/media/photos/cv.png)

### 1. K 폴드 검증 방법
1. `from sklearn.model_selection import KFold`
2. `features = df.data`, `label = df.target`을 이용해서 features와 label 값을 구한다.
3. `train_test_split`으로 훈련데이터와 테스트 데이터를 구한다.
4. `kfold = KFold(n_splits = 5)`: 5폴드의 객체 생성
5. `for s in kfold.split(y_train): print(s)`: for문을 사용해서 폴드별로 학습용, 검증용 데이터 세트의 행 인덱스를 확인한다. 폴드별로 생성된 학습용 인덱스와 검증용 인덱스가 존재한다.
6. `dt_clf = DecisionTreeClassifier(random_State=156)`: 의사결정트리를 이용해서 교차검증을 진행한다.
7. 폴드별 학습용/검증용 인덱스를 이용해서 학습 데이터를 의사결정트리를 이용해 학습하고 검증용 데이터(테스트 데이터)를 예측한다.
8. `accuracy_score(y_val_tmp, pred)`를 이용해서 교차 검증의 정확도를 측정한다.
9. 폴드별로 7,8 번을 반복하여 교차 검증의 정확도를 측정하여 리스트로 기록하고, 전체 평균 검증 정확도를 구한다.


### 2. Stratified K 폴드 교차 검증
1. 3개의 품종의 종류를 label feature로 가지고 있는 df에 대하여 `df['label'].value_counts()`를 통해 원본 데이터의 레이브르 분포를 확인한다.
2. `s_kfold = StratifiedKFold(n_splits=3)`: 3개의 폴드를 가진 객체 생성
3. `for train_index, test_index in s_kfold.split(df, df['label'])`: KFold가 아닌 Stratified K 교차 검증 실행하면 학습 레이블과 검증 레이블 데이터 값의 분포도가 거의 동일하게 나타나는 것을 볼 수 있다.
4. `dt_clf = DecisionTreeClassifier(random_State=156)`: 의사결정트리를 이용해서 교차검증을 진행한다.
5. 폴드별 학습용/검증용 인덱스를 이용해서 학습 데이터를 의사결정트리를 이용해 학습하고 검증용 데이터(테스트 데이터)를 예측한다.
6. `accuracy_score(y_val_tmp, pred)`를 이용해서 교차 검증의 정확도를 측정한다.
9. 폴드별로 7,8 번을 반복하여 교차 검증의 정확도를 측정하여 리스트로 기록하고, 전체 평균 검증 정확도를 구한다.

- Stratified K 폴드의 경우 원본 데이터의 레이블 분포도 특성을 반영한 학습 및 검증 데이터 세트를 만들 수 있으므로 **왜곡된 레이블 데이터 세트**에서의 교차 검증은 반드시 Stratified 폴드를 이용하여 교차 검증을 해야 한다.
- 회귀는 레이블이 아닌 연속적인 값이기 때문에 Stratified K 폴드가 지원되지 않는다.


### 교차 검증을 더 간편하게 할 수 있는 사이킷런 API
1. `cross_val_score(estimator = dt_cfg, X = features, y = labels, scoring = 'accuracy', cv = 5)`
   - estimator: 분류/회귀 객체
   - X: 피처 데이터 세트
   - y: 라벨 데이터 세트
   - scoring: 예측 성능 평가 지표
   - cv: n_splits인 교차 검증 폴드 수
   - 함수에서 `scores`를 사용하면 교차 검증별 정확도를 array로 반환한다.
2. `cross_validate()`
   - n_splits: 교차 검증 폴드 수
   - shuffle: True or False 데이터를 섞을지 말지
   - 정확도 뿐만 아니라 여러개의 평가 지표를 반환하고 수행 시간도 반환한다.


## GridSearchCV 클래스
> 분류나 회귀에 사용되는 하이퍼 파라미터(사용자 지정)를 순차적으로 입력하면서 최적의 파라미터를 편리하게 도출할 수 있는 방법
> ![](https://miro.medium.com/v2/resize:fit:1154/1*a4ENJEahtQsSKS3pWoaKLg.png)

1. `params{'하이퍼파라미터명':[튜닝할 수치들]}` 예를 들면 `'max_depth':[1, 2, 3]'`으로 하이퍼파라미터를 설정한다.
2. `dtree = DecisionTreeClassifier(random_State=42)`: 의사결정트리 객체를 생성한다.
3. `grid_dtree = GridSearchCV(dtree, param_grid=params, cv=3, refit=True, return_train_score=True)`
   - `param_grid`: key(파라미터명)와 리스트 값(파라미터 값)을 가지는 딕셔너리
   - `scoring`: 예측 성능 평가 지표
   - `cv`: 교차 검증 폴드 개수
   - `refit`: 최적의 하이퍼 파라미터 찾은 뒤 입력된 객체를 해당 하이퍼 파라미터로 재학습할건지 여부 (True 디폴트)
