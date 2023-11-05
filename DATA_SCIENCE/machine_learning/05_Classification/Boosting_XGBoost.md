# XGBoost (eXtra Gradient Boost)
> 여러개의 학습기를 순차적으로 학습하면서 잘못 예측된 데이터에 **가중치를 부여**해 오류를 개선해 나가며서 학습하는 방식이다. **경사하강법**을 사용한다.
> ![](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/xgboost/img-3.png)
> 트리 기반의 앙상블 학습에서 가장 각광받고 있는 알고리즘 중 하나이다.

## 예제
1. 데이터 프레임을 형성하고 데이터 프레임의 맨마지막 열에 target column을 추가한다.
2. 학습 데이터와 테스트 데이터를 분리한다.
3. `from xgboost import XGBClassifier`
4. `xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_dept = 3)`: 모델 객체 인스턴스 생성
5. 학습 데이터/검증 데이터/테스트 데이터로 분할
   - `X_train, X_val, y_train, y_val=train_test_split(X_train, y_train, test_size=0.1, random_state=156 )`
6. 검증 데이터를 리스트에 튜플 형식으로 넣는다.
   - `evals = [(X_val, y_val)]`
7. `xgb_wrapper.fit(X_train, y_train, eval_set=evals, eval_metric='logloss', early_stopping_rounds = 100,  verbose=True)`
   - `eval_set`: 검증 데이터 세트
   - `eval_metric`: 검증함수(손실함수)
   - `early_stopping_rounds`: 조기종료 (손실이 증가하면 조기 종료문으로 설정되어 있는 수치만큼 돌려보고 그래도 손실이 감소하지 않으면 종료한다.)
   - `verbose`: 각 반복별 손실결과 출력 여부
8. `pred = xgb_wrapper.predict(X_test)`: 테스트 데이터로 예측 진행
9. `pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1]`: 예측 확률
10. 성능 평가 지표를 다 반환하는 함수를 만들어 예측 성능 평가를 수행한다.
    - `get_clf_eval(y_test, pred, pred_proba)`
    - 오차 행렬, 정확도, 정밀도, 재현율, f1 score 반환

