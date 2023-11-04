# 인공신경망

## 로지스틱 회귀식
> 회귀 알고리즘으로 회귀계수를 구해서 각 결정값을 생성한다.
> y = w1*픽셀1 + w2*픽셀2 + ... + w784*픽셀784 + b
> ![](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSvVMed2Zj8JtdPBZQ8fcEcWH1DYfNygfJyUg&usqp=CAU)
> 이미지 분류 예제의 경우, 10개의 분류이기 때문에 10개의 방정식이 생성되고 각 방정식은 784개의 회귀계수를 가지게 된다.


## 인공 신경망
> **확률적 경사하강법(SGD)를 사용하는 로지스틱 회귀**와 같음
>![](https://velog.velcdn.com/images/kyungmin1029/post/954422d2-fb62-45ab-b6f2-e7ef49569bae/image.png)
> **뉴런**(유닛/노드): 출력층/ 결정값을 계산하는 단위
> ![](https://post-phinf.pstatic.net/MjAyMjA0MDdfMTc4/MDAxNjQ5Mjk0MzAwMDQy.SGhyuC6Lt1dlbPxh3lmLYzzFnWQ_UMdlw_Zwopw26nEg.WrEUAH0mNg2KvoCWlyCGUG-j8DkOMsEe9DpohdIRJR4g.JPEG/3.JPG?type=w800_q75)
> 인공 신경망은 입력층, 맨 마지막층인 출력층을 포함하며 그 외의 층은 모두 은닉층의 역할이다.


## 인공신경망으로 모델 만들기
> 교차검증 수행은 딥러닝에서 시간이 너무 오래 걸리기 때문에 사용하지 않음
> ![](https://blog.kakaocdn.net/dn/df6FPD/btq2hZzpLN5/VoeNXKFZuOirSNGY880AQk/img.png)
> 1. 인공신경망의 첫번째 층(입력층)을 생성한다.
> 2. 입력층은 임계값을 넘은 가중치들만 받아서 softmax 함수를 통해 각 아이템의 비율을 계산한다.


### 케라스 모델
- **Dense**
  - `dense = keras.layers.Dense(출력층 수, activation=활성화 함수, input_shape=입력크기)`
  - **softmax**: 다중분류
    - 모든 확률을 더하면 1이 되게 만든다.
  - **relu**: 시그모이드 함수의 대안
    - x가 0보다 작으면 모든 값을 0으로 처리 
    - 0보다 크기만 하면 여러 은닉층을 거치며 곱해지더라도 맨 처음 층까지 사라지지 않고 남아 있을 수 있다.
  - **sigmoid**: 이진분류
    - 보통 출력층에서만 사용한다.
- **Sequential**(밀집층 생성)
  - `model = Sequential(dense)`
- 위 코드로 신경망 모델이 생성됨




## (예제) MNIST 손글씨 분류
- MNIST 데이터는 훈련데이터와 테스트 데이터를 나눠서 반환함


1. `from tensorflow import keras`
2. `from keras.datasets import mnist`
3. `(train_input, train_target), (test_input, test_target) = (x_train, y_train), (x_test, y_test) = mnist.load_data()`: mnist 데이터를 훈련데이터와 테스트 데이터로 나눠서 반환한다.
4. 이미지를 확인한다.
   - ```
     fig, axs = plt.subplots(1, 10, figsize=(10,10))

     for i in range(10):
        axs[i].imshow(train_input[i], cmap='gray_r')
     ```
5. 각 이미지의 실제 숫자를 반환한다.
   - `print([y_train[i] for i in range(10))`
6. 타겟 데이터를 이용해서 0~9까지의 숫자가 카테고리별로 몇개씩 있는지 반환한다.
   - `print(np.unique(y_train, return_counts=True))`


## (예제) **로지스틱 회귀**로 손글씨 분류하기
### 확률적 경사하강법 모델에 로지스틱 회귀식을 학습하여 학습데이터의 정확도를 구한다.

1. 흑백 이미지이기 때문에 255로 나눠서 0~1 사이로 숫자의 범위를 줄인다.
   - `train_scaled = train_input / 255.0`
2. 2차원 행렬로 된 이미지를 1차원 벡터로 반환
   - `train_scaled = train_scaled.reshape(-1, 28*28)`
3. `from sklearn.model_selection import cross_validate`: 교차검증
4. `from sklearn.linear_model import SGDClassifier`
5. SGDClassifier 모델에서 **로지스틱손실**을 사용하여 학습한다.
   - 로지스틱 손실함수의 값을 최소화하기 위해 가중치를 조정하는 과정이다.
   - `sc = SGDClassifier(loss = 'log_loss', max_iter=5, random_state=42)`
6. 확률적 경사하강법을 사용한 모델을 적용하여 **학습데이터의 성능/정확도를 평가**한다.
   - 교차검증을 통해 과적합을 줄이고 성능을 평가한다.
   - `scores = cross_validate(sc, train_scaled, train_target, n_jobs=-1)`
   - `n_jobs`는 CPU 코어 수를 지정하는 것인데 -1로 지정하면 컴퓨터의 모든 코어를 사용한다는 뜻이다.
7. `test_score`에 해당하는 정확도의 평균을 구한다.
   - `np.mean(scores['test_score'])`


## (예제) 인공신경망으로 손글씨 아이템 분류하기
> 출력층은 10개의 뉴런이 있고 10개의 클래스에 대한 확률을 출려한다. 손글씨가 0~9 사이의 값들 중 하나일 확률들이다. 
> 
> **손실함수는 정답인 타겟의 예측 확률값만 받아 예측에 대한 손실값을 제외한 다른 타겟에 대한 손실값은 모두 제거**해야 한다.
>
> **`sparse_categorical_crossentropy`**: 다중분류일 때 사용하는 손실 함수
> **`binary_crossentropy`**: 이진분류일 때 사용하는 손실 함수

   
1. 케라스 모델을 구성한다.
   - `dense = keras.layers.Dense(10, activation='softmax', input_shape = (784,))`
   - `model = Sequential(dense)`
2. 다중분류이기 때문에 `sparse_categorical_crossentropy`를 사용한다.
   - 원-핫 인코딩 개념을 적용하여 손실값을 계산해준다.
   - `model.compile(loss = 'sparse_categorical_crossentropy', metrics = 'accuracy')`
   - `compile` 단계는 생성된 모델을 컴퓨터가 이해할 수 있도록 하는 단계
3. `model.fit(train_scaled, train_target, epochs=5)`
   - epochs는 반복훈련 횟수로, 반복할수록 손실값이 줄어들고 정확도가 상승하여 성능이 좋아진다.
4. 학습 데이터에 모델을 적용하여 손실값을 최소화하고 성능을 향상시킨 후 테스트 데이터로도 모델의 성능을 확인한다.
   - `x_test_scl = x_test / 255.0`
   - `x_test_scl = x_test_scl.reshape(-1, 28*28)`
   - 테스트 데이터에 대해 스케일링 적용 후 모델의 성능을 테스트 데이터로 검증한다.
   - `model.evaluate(x_test,scl, y_test)`