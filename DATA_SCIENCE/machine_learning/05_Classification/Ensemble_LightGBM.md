# LightGBM
> XGBoost의 학습시간 문제를 보완하기 위한 모델
> 작은 데이터 세트에서는 과적합 발생하기 쉬움
> ![](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcK7V4G%2FbtqFjEE1RDM%2FnCUgDyrYVhZI2FfoYna30K%2Fimg.png)


## LightGBM 예제
1. `from lightgbm import LGBMClassifier`
2. 데이터 생성 및 분할
3. test 데이터를 이용해서 손실값을 계산한다. (검증)
4. `lgbm_w = LGBMClassifier(n_estimators=400)`: xgboost와 동일하게 설정
5. `lgbm_w.fit(X_train, y_train, eval_metric='logloss', eval_set=[(X_test, y_test)], verbose=True)`: 반복해서 손실값 구하기
6. 예측 성능 평가 진행
   - `lgbm_w.predict(X_test)`
   - 정확도, 정밀도, 재현율, F1 score 등으로 예측 성능 평가 진행
7. 조기 종료 조건
   - `lgbm_w.fit(X_train, y_train, eval_metric='logloss', eval_set=evals, early_stopping_rounds=100, verbose=True)`


- **LightGBM의 성능은 부스팅 계열에서 가장 성능이 좋다고 알려져 있음**
- 양이 적은 데이터에 대해서는 과적합이 발생하기 때문에 사용하면 안됨
- 하이퍼 파라미터 튜닝은 트리 알고리즘과 유사