# XGBoost
> 기존의 경사하강법(gradient boosting) 알고리즘 보완한 알고리즘 (오버피팅, 속도 보완)
> 앙상블 부스팅의 특징인 가중치 부여를 경사하강법으로 하지만 더 빠르고 **early stopping**과 같은 규제가 포함되어 오버피팅을 방지할 수 있다.
![](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/xgboost/img-3.png)


1. 경사하강법 사용하여 학습률을 조금씩 키워나가며 적당한 값을 찾는다.
2. **과대적합에 들어갔는지**: 최소점을 지나가버렸다던가 지역 최소점에 빠져 나오지 못하면 손실값 커진 상태로 반복하게 됨
3. XGBoost로 과대적합 방지

## XGBoost 예제
1. 사이킷런 Wrapper XGBoost 적용
2. 0 또는 1로 구분되는 target 추가된 데이터 프레임 생성
3. 학습 데이터/테스트 데이터 분리
4. `from xgboost import XGBClassifier`
5. 데이터는 train/val/test로 분할을 한다.
   - 한 번의 학습 진행 후 손실계산을 한다.
   - 충분한 양의 데이터 필요
6. `xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_dept=3)`: 모델 객체 인스턴스 생성
   - **learning_rate**: 학습률
   - **n_estimators**: 반복 횟수
7. `xgb_wrapper.fit(X_train, y_train, eval_set=[(X_val, y_val)], eval_metric="logloss", verbose=True)`
   - **XGBoost 학습 파라미터**
   - **eval_set**: 검증데이터 세트
   - **eval_metric**: 검증함수(손실함수, 비용함수)
   - **verbose**: 각 반복별 손실결과 출력여부
   - **early_stopping_rounds**: 손실값이 증가하면 조기종료할지 말지 (설정값만큼 더 돌려보고 손실값 감소하지 않으면 종료)
8. 설정된 반복 횟수에 대하여 모든 반복이 진행되면 반복에 대한 손실함수 결과를 본다. (손실값이 감소하다가 다시 증가하면 과적합)
9. early_stopping_rounds 설정
   - `xgb_wrapper.fit(X_train, y_train, eval_set=evals, eval_metric="logloss", early_stopping_rounds=100, verbose=True)`
   - 데이터 양이 xgboost에 진행하기에 너무 적을 경우 조기종료가 효과 없다.
10. 예측 성능 평가
    - 실제 값과 예측 값 비교하여 성능 평가 진행 (정확도, 정밀도, 재현율, F1 score 등)