# 모델 성능 평가 (Evaluation Metric)
## 평가지표
### 분류모델평가지표
1. 정확도 (Accuracy)
2. 오차행렬 (Confusion Matrix)
3. 정밀도 (Precision)
4. 재현율 (Recall)
5. F1 score
6. ROC AUC

### 회귀모델평가지표
1. MSE(Mean Square Error)
2. RMSE(Root Mean Square Error)
3. MAE(Mean Absolute Error)
4. MAPE(Mean Absolute Percentage Error)

### 분류 유형
1. 이진 분류
   - 결정 클래스 값 종류의 유형에 따라 긍정/부정과 같은 2개의 결과값만을 가지는 분류
2. 멀티 분류
   - 여러 개의 결정 클래스 값을 가지는 분류

## 분류 모델의 성능 평가 지표
![](https://blog.kakaocdn.net/dn/rNVIW/btrCXy6nquO/82Xjh99BdfgtdonEbpK14k/img.png)
1. 정확도
   - 실제 데이터와 예측 데이터의 유사성을 판단하는 지표 (직관적임)
   - **(예측 결과가 동일한 데이터 건수)/(전체 예측 데이터 건수)**
   - 정확도만으로 성능을 판단하기에는 무리가 있음 (특히 이진분류 문제)
     - 데이터가 균일하지 않은 경우 아무것도 하지 않아도 높은 수치가 나타날 수 있다.
     - 불균형한 데이터 세트에서는 정확도보다 **정밀도와 재현율**이 더 선호되는 평가 지표이다.
   - `from sklearn.metrics import accuracy_score`: 사이킷런의 정확도 계산 모듈을 불러온다.
   - 전처리와 예측 모델 학습 과정을 진행한다.
   - `accuracy_score(y_test, df.predict(X_test))`
2. 오차행렬
   ![](https://velog.velcdn.com/images%2Fsset2323%2Fpost%2F2fb704cf-8556-40fc-87a2-75b8feb32986%2Fimage.png)
   - 이진 분류의 예측 오류가 얼마인지와 더불어 어떠한 유형의 예측 오류가 발생하고 있는지를 나타내는 지표
   - `from sklearn.metrics import confusion_matrix`: 사이킷런의 오차행렬 API이다.
   - `confusion_matrix(y_test, df.predict(X_test))`: 2차원 배열 형태로 [[TN, FP], [FN, TP]] 나타낸다.
     - 이 배열에서의 4가지 값을 통해 정확도, 정밀도, 재현율의 값을 계산할 수 있다.
3. 정밀도
   - 정밀도는 예측을 Positive(1)로 한 대상 중에 실제값도 Positive(1)인 데이터의 비율이다.
     - Positive(1/양성) 예측 성능을 더 정밀하게 측정하기 위함이다.
     - 스팸메일의 분류의 경우, 정밀도가 더 중요한 지표임
   - `from sklearn.metrics import precision_score`: 정밀도 모듈 불러오기
   - `precision_score(y_test, df.predict(X_test))`
4. 재현율
   - 재현율은 실제의 값이 Positive(1/양성)인 대상 중에 예측값도 Positive(1)인 데이터의 비율이다.
     - 실제로 Positive(1/양성)인 데이터를 음성으로 잘못 판단하면 업무상 큰 영향을 미치는 경우에 중요한 지표로 사용된다.
     - 암 판단 모델이나 보험 사기 적발 모델의 경우 재현율이 더 중요한 지표가 된다.
   - `from sklearn.metrics import recall_score`: 재현율 모듈 불러오기
   - `recall_score(y_test, df.predict(X_test))`
   ![](https://mblogthumb-phinf.pstatic.net/MjAxOTA2MTZfMTI3/MDAxNTYwNjY5NjY3NzQz.6SDbhq3dnUttIl4-oOWcBhWxmQZh87TdNHc9WiV34_8g.Y_zj_PaqjcV974THDhL01AJO4XIm7YQawCberizuphsg.PNG.duqrlwjddns1/image.png?type=w800)
5. **정밀도와 재현율 트레이드 오프**
   - 업무에 따라 정밀도와 재현율의 중요도가 다른데, 정밀도 또는 재현율이 특별히 강조되어야 할 경우, *분류의 결정 임계값(Threshole)*를 조정해서 정밀도나 재현율의 수치를 높일 수 있다.
     - 분류의 결정 임계값을 낮출수록 True의 값이 많아진다.
   - 이 때, 하나를 강제로 높이면 다른 하나의 수치가 떨어지는 것을 트레이드 오프라고 한다.
   - `from sklearn.preprocessing import Binarizer`: 분류 결정 임계값을 조정하여 정밀도와 재현율의 트레이드 오프를 진행한다.
   - ```
     X = [[ 0.5, -1, 2],
          [2, 0, 0],
          [0, 1.1, 1.2]]

      bina = Binarizer(threshole=0.4).fit(X)

      bina.transform(x)
      # 0.5를 임계값으로 설정하여 0.4 이하이면 0, 초과면 1을 반환한다.
      # 0.5일 때보다 더 많은 1을 반환한다.

     ```
   - 트레이드 오프를 진행하며 임계값을 적용해 보기 위해 여러 임계값을 리스트 객체로 저장하여 각 임계값일 때 평가를 수행한다.
   - 정확오, 정밀도, 재현율을 모두 반환하는 함수를 이용해 정밀도와 재현율을 비교해보고 균형을 맞추어 임계값을 설정한다.
   - 임계값에 따른 정밀도, 재현율, 임계값을 한번에 추출하기 위한 방법
     - `from sklearn.metrics import precision_recall_curve`
     - `precision_recall_curve(y_test, df.predict_proba(X_test)[:, 1])`: 레이블 값이 1일 때 예측 확률 추출
   - **임계값이 낮아지면 재현율이 높아지고 정밀도의 값이 낮아짐**
6. F1 score
   ![](https://assets-global.website-files.com/5d7b77b063a9066d83e1209c/639c3d2a22f93657640ef19f_f1-score-eqn.webp)
   - 정밀도와 재현율의 조화평균
   - F1 score이 높을수록 정밀도와 재현율의 균형이 잘 맞다.
   - `from sklearn.metrics import f1_score`
   - `f1 = f1_score(y_test, df.preidct(X_test))`
   - f1 score도 정밀도와 재현율과 같이 임계값에 따라 변화하는 지표;