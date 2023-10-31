# 선형 회귀 모델의 학습/예측/평가
## 1. 모델 학습
### 단일 모델의 RMSE 값 반환
```
def get_rmse(model):
    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)  # 예측값과 실제값의 오차
    rmse = np.sqrt(mse)
    return rmse
```
```
# 여러 모델의 RMSE 값 반환
def get_rmses(models) :
    rmses = [] # 반환 된 각 모델의 rmse값 저장
    for model in models:
        rmse = get_rmse(model)
        rmses.append(rmse)
    return rmses
```

### 데이터의 타깃과 피처 분할 및 훈련/테스트 데이터 임의 지정
```
# 데이터 분할(타겟과 피처)
X_features = df.drop('SalePrice', axis=1, inplace=False)
y_target = df['SalePrice']

# 훈련/테스트 데이터 임의 지정
X_train, X_test, y_train, y_test = train_test_split(X_features, y_target, test_size=0.2, random_state=156)
```

## 2. 모델 예측
### 회귀 예측
- 일반 선형 회귀: `lr_reg = LinearRegression()`
  - `lr_reg.fit(X_train, y_train)`
- 릿지 회귀: `ridge_reg = Ridge()`
  - `ridge_reg.fit(X_train, y_train)`
- 라쏘 회귀: `lasso_reg = Lasso()`
  - `lasso_reg.fit(X_train, y_train)`
- 학습된 모델 전달 `models = [lr_reg, ridge_reg, lasso_reg]`
- rmse값을 반환한다. `get_rmses(models)`
  - rmse값이 작을수록 성능이 좋은 회귀이다.


### 회귀 계수의 시각화
> 피처(컬럼)별 회귀 계수를 시각화한다.
> 회귀계수의 최대값 10개 피처, 최솟값 10개 피처를 시각화하자.

1. 상위 10개, 하위 10개를 반환하는 함수 만들기

```
def get_top_bottom_coef(model):
    coef = pd.Series(model.coef_, index=X_features.columns)

    coef_high = coef.sort_values(ascending=False).head(10)
    coef_low = coef.sort_values(ascending=False).tail(10)

    return coef_high, coef_low
```

2. 모델별(선형회귀, 릿지, 랏쏘) 회귀계수를 상위 10개, 하위 10개를 추출하여 시각화한다.

```
def visualize_coefficient(models):
    fig, axs = plt.subplots(figsize=(24,10), nrows=1, ncols=3)
    fig.tight_layout()  # 위에 세팅된 레이아웃을 자동 적용한다.

    for i, model in enumerate(models):
        coef_high, coef_low = get_top_bottom_coef(model)
        coefs = pd.concat([coef_high, coef_low])

        axs[i].set_title(model.__class__.__name__, size=25)

        # 그래프의 tick 설정 눈금의 크기, 눈금의 방향 등을 설정할 수 있다.
        axs[i].tick_params(axis="y", direction="in", pad=-120)

        for label in (axs[i].get_xticklabels() + axs[i].get_yticklabels()):
            label.set_fontsize(22)
        sns.barplot(x=coef_concat.values, y=coef_concat.index, ax=axs[i])

visualize_coefficient(models)

```

### 교차검증으로 평가 한번 더
> `cross_val_score(model, 학습데이터, 타겟데이터, scoring=평가지표, cv=폴드수)`

