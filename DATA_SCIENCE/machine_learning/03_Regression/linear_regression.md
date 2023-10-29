# 선형 회귀 (Linear Regression)
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


# 다항 회귀 (Polynomial Linear Regression Model)
> 다항회귀는 하나의 독립변수와 종속변수의 관계를 고차 다항식으로 표현하는 경우이다.
> 데이터의 분포가 곡선에 가까울 때 단순 선형 회귀보다 값을 더 잘 표현할 수 있음.

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
