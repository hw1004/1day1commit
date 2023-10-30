# 선형 회귀
1. 선형회귀
   1. 선형회귀
   2. 다항회귀
   3. 다중회귀
2. 규제
   1. 릿지회귀
   2. 라쏘회귀

## 선형 회귀 (Linear Regression)
> 대표적인 회귀 알고리즘으로 **특성이 하나일 때 직선을 학습하는 알고리즘**이다. 특성을 잘 나타내는 직선을 찾아야 한다.
> 회귀알고리즘은 특성을 잘 나타내는 직선을 자동으로 찾아내는 알고리즘이다.

- **변수**: 변하는 수
- **상수**: 변하지 않는 수
- **계수**: 변수 앞에 붙어있는 상수인 인수


![선형 회귀](https://upload.wikimedia.org/wikipedia/commons/b/be/Normdist_regression.png)

1. `from sklearn.linear_model import LinearRegression`으로 선형회귀 모듈을 불러온다.
2. 선형회귀 객체 인스턴스 생성: `lr = LinearRegression`
3. 미리 훈련 데이터와 테스트 데이터를 랜덤 지정했다고 가정하고 훈련 데이터에 선형회귀 모듈을 학습시킨다.: `lr.fit(train_input, train_target)`
4. 선형회귀 모듈을 학습시키면 데이터를 나타내는 적절한 직선을 알아낼 수 있는데, 이 때 계수(기울기)와 절편을 알아낼 수 있다.: `print(lr.coef_, lr.intercept_)`
5. 훈련 세트의 산점도를 그린다.: `plt.scatter(train_input, train_target)`
6. 생성된 직선을 그린다.: `plt.plot([a, b], [a*lr.coef_ + lr.intercept_, b*lr.coef_ + lr.intercept])`
7. `lr.preict([[예측하고자하는 값의 x값]])`: 예측하고자하는 값의 좌표를 나타낸다.
8. 예측한 값을 표시한다.: `plt.scatter(x값, y값, marker='^')`
9. 훈련세트와 테스트세트의 score를 확인한다.: `lr.score(train_input, train_target)`


## 다항 회귀 (Polynomial Linear Regression Model)
> 다항회귀는 하나의 독립변수와 종속변수의 관계를 고차 다항식으로 표현하는 경우이다.
> 데이터의 분포가 곡선에 가까울 때 단순 선형 회귀보다 값을 더 잘 표현할 수 있음.
> 다만, 과적합(훈련세트에 과대적합)이 되기 쉽기 때문에 차수를 어떻게 정하느냐가 관건이다.

> 다항 회귀로 차수를 늘릴수록 훈련데이터에 대해 성능이 높아진다. **특히, 샘플갯수보다 특성의 개수가 더 많으면** 훈련세트에 대해서는 완벽한 훈련을 하게되지만, 테스트 세트에 대해서는 성능이 매우 안좋아진다. 차수를 높일 때, 이러한 것을 방지하기 위해 **규제**를 가한다.

![다항회귀](https://t1.daumcdn.net/brunch/service/user/1bVd/image/9JP7muUQVHjb_1WiU2NkwbGNFT4.png)


1. `from sklearn.linear_model import LinearRegression`으로 선형회귀 모듈을 불러온다.
2. 선형회귀 객체 인스턴스 생성: `lr = LinearRegression`
3. 훈련세트와 테스트세트의 2차항을 데이터에 추가한다. `train_poly = np.column_stack((train_input**2, train_input))` : a*x**2 + b*x + c 형태이기 때문에 x제곱과 x의 값이 둘 다 필요하다.
4. 2차항을 추가한 훈련 데이터에 선형회귀 모듈을 학습시킨다.: `lr.fit(train_poly, train_target)`
5. 새로운 데이터를 예측할 때 2차항도 포함한다.: `lr.predict([[50**2, 50]])`
6. 선형회귀 모듈을 학습시키면 데이터를 나타내는 적절한 곡선을 알아낼 수 있는데, 이 때 두개의 계수(기울기)와 절편을 알아낼 수 있다.: `print(lr.coef_, lr.intercept_)` : 이때, 계수인 coefficient의 값이 2개가 출력된다.
7. 훈련 세트의 산점도를 그린다.: `plt.scatter(train_input, train_target)`
8. 곡선은 짧은 직선들을 이어 그린 것이기 때문에 범위에 대한 정수 배열을 생성한다. `point = np.arange(15, 49)`
9. 생성된 곡선을 그린다.: `plt.plot(point, 1.01*point**2-21.6*point+116.05)`: 각각의 계수와 상수는 lr.coef_, lr.intercept_를 통해 얻은 값이다.
10. `lr.preict([[예측하고자하는 값의 x값]])`: 예측하고자하는 값의 좌표를 나타낸다.
11. 예측한 값을 표시한다.: `plt.scatter([x값], [y값], marker='^')`
12. 훈련세트와 테스트세트의 score를 확인한다.: `lr.score(train_poly, train_target)`


- **사이킷런은 다항회귀를 위한 클래스를 명시적으로 제공하지 않는다. 다항회귀는 선형회귀이기 때문에 PolynomialFeatures 클래스를 통해서 독립변수를 다항식변수로 변환한다.**

1. `from sklearn.preprocessing import PolynomialFeatures`을 통해 클래스를 불러온다.
2. 독립변수를 2차원 array 형식으로 변환한다. `X = np.array([x1, x2])`
3. poly 객체 인스턴스 생성 `poly = PolynomialFeatures(degree=2)`: 차수를 2로 지정
4. poly를 훈련시키고 2차 다항값으로 변환한다. `poly.fit(X)`, `poly_ftr = poly.transform(X)`
5. poly_ftr을 확인해보면 x1과 x2에 대해 변환된 2차 다항식의 계수인 `[[1,(X1), (X1)**2], [1, (X2), (X2)**2]]`을 출력한다.
6. `poly.get_feature_names_out`를 실행하면 결과값에 대해 ndarray 형태로 출력한다.




## 다중 회귀 (Multie Linear Regression)
> 다중회귀는 여러개의 특성을 사용한 선형 회귀이다. 독립변수와 종속변수의 관계가 일차방정식으로 표현된 회귀이며 직선으로 표현한다. 선형회귀는 평면을 학습하는 반면 특성이 두개이면 타겟값과 함께 **3차원** 공간을 형성한다. `y = ax1 + bx2 + c` 형태로 나타난다.

> 특성이 늘어나면 선형회귀의 능력이 매우 강해진다.

![다중회귀](https://user-images.githubusercontent.com/17154958/72317675-5af68880-36dd-11ea-94d2-9174fdfc70bd.png)

1. 여러 특성을 가지는 DataFrame을 2차원 배열 형태로 변환한다.: `df.to_numpy()`
2. 타겟데이터의 데이터 배열을 생성한다. `weight = np.array([~])`
3. 학습데이터와  테스트데이터를 임의로 나누어 정한다. `train_input, test_input, train_target, test_target = train_test_split(full, weight, random_state=42)`
4. 선형회귀 모듈을 불러온다. : `from sklearn.linear_model import LinearRegression`
5. 선형회귀 객체 인스턴스를 생성한다. : `lr = LinearRegression()`
6. 선형회귀 모듈을 학습데이터에 학습시킨다. `lr.fit(train_input, train_target)`
7. 학습시킨 학습데이터의 score를 구하고 똑같이 테스트데이터의 score을 구해서 비교한다. `lr.score(train_input, train_target)`
   - 고차항보다는 점수가 낮게 나오지만 특성이 하나일 때보다는 성능이 좋아졌다.
8. 계수와 절편을 확인한다. `lr.coef_, lr.intercept_`


# 규제
> 다항회귀에서 차수를 너무 많이 올려서 테스트 데이터에 대한 성능이 쓰레기가 된 경우처럼 **머신러닝 모델이 훈련세트에 대해 너무 과도하게 학습하지 못하도록 훼방하는 것**을 **규제**라고 한다.
>
> 즉, 모델이 너무 과대적합되지 않게끔 하는 방법이다.
>
> 새로운 데이터가 들어왔을 때, 규제를 가해주면 **예측의 오차**가 적은 예측을 할 수 있다.

아래의 그림에서 두번째 회귀식이 가장 이상적이다. Overfitted된 식에 대해 규제를 통해 두번째처럼 그려질 수 있다.
![최적의 회귀식](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F7vchA%2FbtqDjeASZK5%2F7V4fGRlesJtu67v2mTgIOK%2Fimg.png)

- **규제의 첫번째 단계는 표준 정규화를 진행하는 것이다.**
  - `from sklearn.preprocessing import StandardScaler`
  - `ss = StandardScaler()`
  - fit과 transform을 사용해 데이터에 표준 정규화 모듈을 학습시키고 적용한다.


- **릿지와 라쏘**는 선형회귀 모델에 규제를 적용한 알고리즘이다.
  - **릿지**: (계수)**2을 기준으로 규제 적용
    - 계수의 크기를 줄여주지만 0으로 만들지는 않는다.
  - **라쏘**: |계수|를 기준으로 규제 적용
    - 계수를 아예 0으로 만들 수도 있다.


## 릿지 회귀 (Ridge Regression)
> 계수의 제곱을 기준으로 규제를 적용하는 회귀이다.

> 릿지 회귀의 주요 파라미터는 **alpha**이다. 규제 계수이며, alpha값을 감소시키면 RSS(W)최소화에 근접하고, alpha값을 증가시키면 회귀계수(W)가 감소한다. 따라서 적절한 alpha값 조정을 통해 가장 최적의 alpha값을 구한다.

1. `from sklearn.linear_model import Ridge`
2. `ridge=Ridge()`: 객체 인스턴스 생성
3. `ridge.fit(train_scaled, train_target)`을 통해 릿지 회귀 학습시킴
4. `ridge.score(test_scaled, test_target)`

- RMSE(평균 제곱근 오차)는 예측값과 실제값의 차이이다. 따라서, 데이터들의평균 **RMSE**가 작을수록 예측성능이 좋다.
  - 릿지 회귀의 alpha값을 여러개 적용해보며 최소 RMSE를 가지는 최적의 alpha값을 탐색한다.

```
alphas = [0.001, 0.01, 0.1, 1, 10, 100]
train_score = []
test_score = []

for alpha in alphas:
    ridge = Ridge(alpha = alpha)
    ridge.fit(train_scaled, train_target)
    train_score.append(ridge.score(train_scaled, train_target))
    test_score.append(ridge.score(test_scaled, test_target))

# 특정 alpha값을 가질 때의 학습데이터의 예측 성능과 테스트데이터의 예측 성능을 계산하여 최적의 alpha값을 찾아낸다.

ridge = Ridge(alpha=0.1)
ridge.fit(train_scaled, train_target)
# 최적의 alpha 값으로 다시 릿지회귀를 학습시킨 후 ridge.score()를 통해 성능을 확인한다.
    
```


## 라쏘 회귀 (Lasso Regression)
> 계수의 절댓값을 기준으로 규제를 적용하는 회귀이다.

> 랏쏘 회귀 또한 alpha를 주요 파라미터로 가지고 있다.

1. `from sklearn.linear_model import Lasso`
2. `lasso=Lasso()`: 객체 인스턴스 생성
3. `lasso.fit(train_scaled, train_target)`을 통해 릿지 회귀 학습시킴
4. `lasso.score(test_scaled, test_target)`

  - 라쏘 회귀의 alpha값을 여러개 적용해보며 최소 RMSE를 가지는 최적의 alpha값을 탐색한다.

```
alphas = [0.001, 0.01, 0.1, 1, 10, 100]
train_score = []
test_score = []

for alpha in alphas:
    lasso = Lasso(alpha = alpha, max_iter=100000)
    lasso.fit(train_scaled, train_target)
    train_score.append(lasso.score(train_scaled, train_target))
    test_score.append(lasso.score(test_scaled, test_target))

# 특정 alpha값을 가질 때의 학습데이터의 예측 성능과 테스트데이터의 예측 성능을 계산하여 최적의 alpha값을 찾아낸다.

lasso = Lasso(alpha=10)
lasso.fit(train_scaled, train_target)
# 최적의 alpha 값으로 다시 라쏘회귀를 학습시킨 후 lasso.score()를 통해 성능을 확인한다.
    
```

- **`max_iter`**을 늘리는 것은 과소적합을 줄이기 위해 최적의 계수(alpha값)을 줄이면서 증가시켜야 하는 계산의 반복횟수이다.
  - 라쏘 모델은 반복적인 계산을 수행하기 때문이다.


### 릿지와 라쏘
- 릿지회귀는 특성의 중요도가 전체적으로 비슷하면 사용한다.
- 라쏘회귀는 회귀 계수를 0으로 만들 수도 있기 때문에 **모델에 유용한 특성들을 골라내는 용도**로 사용된다.