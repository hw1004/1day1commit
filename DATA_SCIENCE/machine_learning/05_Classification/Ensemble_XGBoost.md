# XGBoost
> 기존의 경사하강법(gradient boosting) 알고리즘 보완한 알고리즘 (오버피팅, 속도 보완)
> 앙상블 부스팅의 특징인 가중치 부여를 경사하강법으로 하지만 더 빠르고 **early stopping**과 같은 규제가 포함되어 오버피팅을 방지할 수 있다.
![](https://www.nvidia.com/content/dam/en-zz/Solutions/glossary/data-science/xgboost/img-3.png)


1. 경사하강법 사용하여 학습률을 조금씩 키워나가며 적당한 값을 찾는다.
2. **과대적합에 들어갔는지**: 최소점을 지나가버렸다던가 지역 최소점에 빠져 나오지 못하면 손실값 커진 상태로 반복하게 됨
3. XGBoost로 과대적합 방지

## XGBoost 예제
1. 사이킷런 Wrapper XGBoost 적용
2. 