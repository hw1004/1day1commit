# 인공 신경망
## 퍼셉트론 (인공 뉴런)
> 인공 신경망의 구성 요소로 다수의 값을 입력받아 하나의 값으로 출력하는 알고리즘이다.
>![](https://otexts.com/fppkr/nnet2.png)
>
> - weight(w) : 가중치로 각각의 입력 신호에 부여되어 계산을 하고 신호의 총합이 임계값을 넘었을 때 1을 출력한다.

```
def XORGate(x1,x2) : 
    w1, w2, b = ?,?,?   
    
    y = x1 * w1 + x2 * w2 + b
    
    if y <= 0 :
        return 0
    elif y > 0 :
        return 1
    
print(XORGate(0,0))  # 0
print(XORGate(0,1))  # 1
print(XORGate(1,0))  # 1
print(XORGate(1,1))  # 0    

```

- 위와 같이 만족하는 w1과 w2 값을 찾지 못하겠을 때가 있는데, 이 때는 결과 본 후 여러 가중치를 학습하고 적절한 다른 퍼셉트론들을 합쳐서 생성한다.
- 이와 같이 선형적으로는 문제 해결을 할 수 없을 때 뉴런이 찾은 선형식을 그대로 다음 뉴런의 인풋으로 보내면 전달된 선형식이 무의미해질 수 있다.
- 따라서, **활성화함수를 써서 비선형으로 약간 비틀어야 한다.**
    - **MLP(Multilayer Perceptron)**: 여러 개의 뉴런으로 이루어진 신경망 구조
    - MLP의 각 뉴런들은 입력 값을 가중치로 조절하고 활성화 함수를 통과시킨다.
    - 
```
Input A -----\
              \
Input B ------- Hidden Layer -- Output Layer -- Output
              /
Input A' -----/
```
- 입력 뉴런층(Input): 입력 값을 받아들이는 뉴런층
- 은닉 뉴런층(Hidden layer): 뉴런들이 **비선형 활성화 함수**를 거쳐서 input 값들의 비선형 조합을 만들어낸다.
  - 활성화함수의 예시로는 sigmoid, relu 등이 있다.
- 출력 뉴런층(Output layer): 이전 층의 출력을 가중치로 가지며 선형 함수를 적용한다.

## 인공 신경망
> 선형회귀와 로지스틱회귀의 개념을 차출해서 생성한 개념이다.
> 대량의 가중치(W)와 b를 사용하기 때문에 과적합이 자주 발생한다.

### 딥러닝
> 기계가 병렬적 다층 구조를 통해 학습하도록 만든 기술이다.
> 여러 다층 구조를 통해 학습한 내용을 정해진 기준으로 판단하여 결과를 내놓게 함.

### tenserflow와 Keras

<신경망 예제>
1. `import tensorflow as tf`
2. `from tensorflow import keras`
3. `from keras.models import Sequential`: Sequential 모델은 하나의 파이썬 리스트로 단순이 층을 쌓을 수 있는 역할을 한다. 즉, 신경망프레임 모듈로 **층들을 담을 수 있는 그릇**과 같은 역할을 한다.
4. `from keras.layers import Dense`: Dense는 신경망을 정의하는 함수이다. 뉴런의 입력과 출력을 연결해주는 역할을 하는데 연결한 연결선은 **가중치**를 포함하고 있다. *가중치가 높을수록 입력값이 출력값에 미치는 영향이 커지고 낮을 수록 작아진다.*
5. AND 논리를 사용하는 데이터를 생성한다.
6. `and_model = Sequential()`: 신경망 프레임을 생성한다.
7. **`and_model.add(Dense(units=1, input_shape=(2,), activation='sigmoid'))`**: 신경망에 층을 추가한다.
   - `units`: 뉴런의 수
   - `input_shape`: 입력차원개수
   - `activation`: 출력을 위한 활성화 함수
     - `activation='sigmoid'`: 분류문제에서 값을 0~1로 변경시키는 역할을 한다.
8. `.summary()`: 신경망의 구조를 출력한다.
   - 파라미터(params): 모델에서 나오는 아웃풋 입력수 * 출력수 + 출력수
9. **`.compile()`**: 훈련 과정을 설정한다. 시용자 정의 손실이나 측정 지표를 전달하고 싶을 때 유용  
    - `loss`: 손실함수
      - 이진분류의 경우에는 `binary_crossentropy`를 사용한다.
      - `SparseCategoricalCrossentropy`는 다중분류일 때
      - ![](https://wikidocs.net/images/page/36033/%EC%86%90%EC%8B%A4%ED%95%A8%EC%88%98.PNG)
    - `optimizer`: 최적화 함수
      - SGD
      - RMSprop
      - Adam
      - Adagrad
    - `metrics`: 성능 평가 지표
10. **`.fit()`**: 훈련 루프 구현
    - `X`: inputs (훈련 데이터)
    - `y`: targets (훈련 타겟)
    - `epochs`: 훈련 루프를 반복할 횟수
    - `batch_size`: 가중치를 업데이트 할 때 사용할 훈련 샘플 개수
11. `.preict(X_test)`: 테스트 데이터를 이용해 예측을 진행한다.
12. `.evaluate(X_test, y_test)`: 평가를 진행하여 손실과 정확도를 확인한다.


<심층 신경망(다층 퍼셉트론) 예제>
![](https://heung-bae-lee.github.io/image/Deep_Neural_Network.png)
1. `.Sequential()`: 위와 동일하게 신경망 객체를 생성한다.
2. `model.add(Dense(1, input_shape=(2,), activation='sigmoid'))`: 뉴런의 개수를 1로 설정하고 입력은 2개를 받는다. 활성화함수는 시그모이드 함수를 사용한다.
3. `model.add(Dense(1, activation='sigmoid'))`: 두번째층은 첫번째 층의 아웃풋을 인풋으로 받기 때문에 input_shpae을 지정해주지 않아도 된다. 뉴런의 개수는 동일하게 1로 정한다.
4. 동일하게 compile 함수와 fit 함수를 적용한다.


### fit 함수로 신경망 모델 훈련하는 과정
1. 파라미터 초기화(가중치, 편향 초기화) 
   - 가중치 W와 편향 b 무작위로 초기화됨 (학습 과정의 시작점을 설정함)
2. 입력값 입력
   - 훈련데이터 모델에 입력. **Input layer**에 전달됨
3. 추론 
   - 입력 데이터를 모델을 통해 뉴런에 전파하고 예측값을 계산한다.
4. 오차 계산 
   - **예측값과 실제값의 오차** 계산 (**손실함수**를 통해 측정됨)
5. 오차 역전파 
   - 오차를 사용해서 모델 내의 **모든 가중치와 편향**에 대해 **미분**을 계산 (오차가 각 가중치와 편향에 어떻게 영향을 미치는지를 나타냄)
6. 가중치 갱신 
   - 미분 값(기울기)를 통해 경사 하강법과 같은 최적화 알고리즘을 사용해서 가중치와 편향을 갱신한다.
   - ![](https://miro.medium.com/v2/resize:fit:1400/0*riTo1mf-pYDDNX-x.png)
7. 반복 
   - 훈련데이터를 모두 사용할 때까지 2~6번 반복 (**에포크가 늘어날 수록 성능이 좋아짐**)
