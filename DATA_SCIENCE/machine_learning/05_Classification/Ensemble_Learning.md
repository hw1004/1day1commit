# 앙상블 학습
> 여러 개의 분류기를 사용해서 예측 결합함으로써 보다 정확한 최종 예측을 도출하는 기법이다.
> 단일 분류기 보다 신뢰성이 높은 예측값을 얻을 수 있다.

## 앙상블 알고리즘

- **랜덤포레스트** (배깅)
- **그레디언트 부스팅** (부스팅)
- **XGBoost** (부스팅)
- **LightGBM** (부스팅)
- **Stacking**

## 앙상블 학습 결과 결합 방법
![](https://blog.kakaocdn.net/dn/QB2vt/btrFNGAxuWZ/DMkTGRlTgzw2sJI5PAHP4k/img.png)
1. 보팅(Voting)
   - 여러 분류기가 투표를 통해 최종 예측 결과를 결정하는 방식이다.
   - 모든 분류기가 동일한 데이터 전체를 학습한다.
   1. **하드 보팅**: 예측한 결과값들 중에서 다수의 분류기가 결정한 예측값을 최종 보팅 결과값으로 선정하는 방식이다.
   2. **소프트 보팅**: 분류기들의 레이블 값 결정 확률을 평균내어 확률이 가장 높은 레이블 값을 최종 보팅 결과값으로 선정한다.
   ![](https://velog.velcdn.com/images/gangjoo/post/951b55aa-ae86-4f8e-a95e-2d7a334ff55c/image.png)
2. 배깅(Bagging)
   - 여러 분류기가 투표를 통해 최종 예측 결과를 결정하는 방식인 점은 보팅과 유사하다.
   - 하지만 각각의 분류기가 학습하는 데이터는 **샘플링**을 서로 다르게 하여 학습을 수행하므로 다르다.
     - 샘플링 방식은 *부트 스트래핑 분할 방식*을 사용하여 교차 검증을 제외하는 것에 한하여 각 샘플링된 데이터 내에서는 중복 데이터를 포함한다.
   - 예시로는 *랜덤 포레스트* 알고리즘이 있다.
   - ![](https://velog.velcdn.com/images/gangjoo/post/f80a7b15-6f39-492e-947a-16ce991469b5/image.png)
3. 부스팅(Boosting)
   - 여러개의 분류기가 **순차적으로** 학습된다.
   - 학습한 후 다음 분류기에는 가중치를 부여하며 샘플을 전달하고 그 다음 분류기는 가중치를 포함한 학습과 예측을 진행한다.
   - 예시로는 *Gradient Boost, XGBoost, LighGBM*이 있다.




## 보팅(Voting) 방식의 앙상블 예제
1. `from sklearn.ensemble import VotingClassifier`
2. `cancer = load_breast_cancer()`: 불러온 데이터셋의 객체 생성
3. 데이터프레임 생성: `data_df = pd.DataFrame(cancer.data, columns = cancer.feature_names)`
   - `cancer.target`은 악성 여부를 나타낸다.
4. `lr_clf = LogisticRegression(solver='liblinear')`: 랏쏘, 릿지 규제를 모두 지원하는 하이퍼파라미터를 사용하여 로지스틱 회귀 객체 생성
5. `knn_clf = KNeighborsClassifier(n_neighborss=8)`: k 최근접 이웃 객체를 생성한다.
6. **VotingClassifier의 소프트 보딩 기반의 앙상블 모델로 객체를 생성한다.**
   - `vo_clf = VotingClassifier(estimators=[('LR', lr_clf), ('KNN', knn_clf)], voting = 'soft')`
   - `estimators`: 리스트 값으로 보팅에 사용될 분류 객체들을 튜플 형식으로 입력 받는다.
   - `voting`: 보팅 방식
7. 학습 데이터와 테스트 데이터를 분리한다.
8. `vo_clf.fit(X_tain, y_train)`: 보팅 모델을 학습한다.
9. `pred = vo_clf.predict(X_test)`: 테스트 데이터 예측
10. `accuracy_score(y_test, pred)`: 실제값과 예측값을 비교해 Voting 분류기의 정확도를 계산한다.


## 배깅(Bagging) 방식의 앙상블 예제
1. `from sklearn.ensemble import RandomForestClassifier`
2. `rf_clf = RandomForestClassifier(random_state=0, n_estimators=150)`: 랜덤 포레스트 객체 생성
   - `n_estimators`: 결정 트리의 개수 (개수를 증가시킨다고 무조건적으로 성능이 향상되는 것은 아니다.)
3. `rf_clf.fit(X_train, y_train)`: 학습시킨다.
4. `pred = rf_clf.predict(X_test)`: 테스트 데이터 예측
5. `accuracy_score(y_test, pred)`: 실제값과 예측값을 비교해 랜덤 포레스트의 정확도를 계산한다.


## 개별 feature들의 중요도 시각화
```
ftr_import = rf_clf.feature_importances_
# 시리즈 형태로 변환하면 value_count나 sort_values 사용 가능
pd.Series(ftr_import)
top_20 = pd.Series(ftr_import, index=X_train.columns).sort_values(ascending=False)[:20]

plt.figure(figsize=(8,6))
plt.title('Feature Importance Top 20')
sns.barplot(x=top_20, y=top_20.index, palette='Set3')
plt.show()
```