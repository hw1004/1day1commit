# 로지스틱 회귀 (Logistic Regreesion)
> 선형 회귀 방식을 분류에 적용한 알고리즘이다. 
> 선형 함수가 아닌 시그모이드 함수의 최적선을 찾고 그 반환 값을 확률로 간주하여 확률에 따라 분류를 결정한다.
![](https://velog.velcdn.com/images%2Fmetterian%2Fpost%2Fee23f919-20f3-4acd-8110-b39a99df6096%2Fimage-20210413212222497.png)
> 로지스틱 회귀는 똑같이 선형회귀식을 학습한다. (z = ax1 + bx2 + cx3 + cx4 + e)
> z가 아주 큰 음수일 때는 0, 아주 큰 양수일 때는 1이 된다. 따라서 0과 1 사이이고, 이에 따라 분류가 된다.
> 
> `phi = 1/(1+np.exp(-z))`일 때, 특정 범위 내에서 연속적으로 나타내는 값들의 배열인 z에 대하여 `plt.plot(z, phi)`는 시그모이드 그래프를 나타낸다.
> z의 범위가 커질수록  시그모이드 함수가 0,1에 완전 수렴한다.


## 이진 분류
> 0, 1, 2의 총 3개의 품종 중에 0과 1만 추출하자. 0, 1은 True, 2는 False로 적용하여 0과 1의 품종만 남긴다. 이 때, 로지스틱 회귀를 사용하여 샘플이 0일 확률과 1일 확률을 판별하자.

1. `from sklearn.linear_model import LogisticRegression`
2. `lr_cfg = LogisticRegression`: 로지스틱 회귀 객체 생성
3. 0과 1만 있는 이진분류 데이터에 대해 로지스틱 회귀를 학습시킨다.
4. `predict`를 이용하여 샘플에 대한 예측을 실행한다.
5. `predict_proba`를 이용하여 샘플에 대해 0일 확률과 1일 확률을 2차원 배열 형태로 반환한다. (**분류에 대한 확률**)
6. `lr_cfg.coef_, lr_cfg.intercept_`: 회귀계수는 피처들(품종을 결정하는데 쓰이는 변수/컬럼들)의 개수만큼 나오고, 절편은 1개가 나온다.
7. `desc = lr_cfg.decision_function(X_train_two)`: 위의 회귀계수와 절편으로 만들어지는 선형회귀식으로 나오는 z값을 반환한다.
8. 시그모이드 함수에 z값을 적용하면 `expit(desc)`, 샘플들에 대해 1일 확률을 반환한다. 이진분류이기 때문에 0일 확률은 1에서 1일 확률을 빼면 된다.


## 다중 분류
> 다중분류의 `LogisticRegression(C=20, max_iter=1000)`에서 C는 로지스틱 규제 파라미터로 값이 작아질수록 규제가 강해진다. max_iter은 반복횟수이다. **회귀 알고리즘은 반복 알고리즘을 사용하여 잔차가 적은 회귀식을 찾아낸다.**

1. `from sklearn.linear_model import LogisticRegression`
2. `lr_cfg = LogisticRegression`: 로지스틱 회귀 객체 생성
3. 0, 1, 2 품종이 포함된 데이터에 대해 로지스틱 회귀를 학습시킨다.
4. `predict`를 이용하여 샘플에 대한 예측을 실행한다.
5. `predict_proba`를 이용하여 샘플에 대해 0일 확률과 1일 확률, 2일 확률을 2차원 배열 형태로 반환한다. (**분류에 대한 확률**)
6. `lr_cfg.coef_, lr_cfg.intercept_`: 회귀계수는 피처들(품종을 결정하는데 쓰이는 변수/컬럼들)의 개수만큼 나오고, 절편은 1개가 나온다.
7. `desc = lr_cfg.decision_function(X_train_two)`: 위의 회귀계수와 절편으로 만들어지는 선형회귀식으로 나오는 z값을 반환한다.
8. **다중 분류는 시그모이드 함수가 아닌 softmax를 사용한다.** softmax(desc, axis=1)을 수행하면 z값을 0이나 1로 변환하여 0, 1, 2일 확률들을 반환한다.
   - 품종 a, b, c에 대한 샘플의 z값들에 대하여 `np.exp(a,b,c 중 하나의 z값) / sum(np.exp(a), np.exp(b), np.exp(c))`을 세개의 품종에 대해 모두 구한다. 이것을 쉽게 구해주는 함수가 softmax 함수이다.
   - 이 세개의 품종에 대한 z값을 이용해 구한 확률들을 모두 합하면 1이 된다.