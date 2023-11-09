# 컨볼루션 신경망(CNN)

> 주로 시각적인 이미지를 분석하는 데 사용한다.
> 필터링 기법을 인공신경망에 적용하여 이미지를 효과적으로 처리할 수 있는 심층 신경망 기법으로 행렬로 표현된 필터의 각 요소가 데이터 처리에 적합하도록 자동으로 학습되는 과정을 통해 이미지를 분류하는 기법이다.
> - 동일 객체라도 전체적인 픽셀을 보았을 때 환경의 변화에 따라 변화가 큰 것들이 존재한다.
>   - 전체를 가지고는 같은 객체인지 판단하기 어렵지만 부분의 특징을 추출하고 결합하였을 때, 판단이 더 쉬워진다. (CNN의 장점)
>
> 1. **특징 추출**: Convolution Layer + Pooling Layer를 반복
> 2. **분류기**: Dense layer + Dropout Layer(과적합 방지) + Dense Layer
>
> ![](https://velog.velcdn.com/images%2Fdltjrdud37%2Fpost%2Fc6c85370-639c-4261-8cef-f418226d66f5%2Fcnn_banner.png)
>
> **합성곱**
> - **필터(커널)** 을 통해 이미지 전체를 훑고 특징을 추출함
> - **필터와 그 필터가 비추는 이미지 부분의 내적값**
> ![](https://velog.velcdn.com/images%2Fdltjrdud37%2Fpost%2F0f6daba1-639d-4e66-897f-6ec5172c6aa1%2FScreen%20Shot%202021-01-27%20at%203.58.06%20PM.png)
>
> **Stride**
> - 필터가 입력 데이터(이미지)를 훑을 때 얼마만큼의 픽셀만큼 움직이는지를 지정
>
> **padding**
> - stride가 크면 출력데이터는 더 작아진다.
> - 이를 방지하기 위해서 입력 이미지에 의미없는 값을 더하는데, 이를 통해 크기가 줄어들어 발생하는 손실을 개선할 수 있다.
> - 의미없는 값을 더하는 행위를 **padding**이라고 한다.
>
> **Pooling**
> - 합성곱 연산을 한 결과인 출력데이터를 입력으로 받는다.
> - 출력데이터의 **크기를 줄이거나 특정 부분을 강조하기 위한 샘플링 과정**이다.
> - **Max Pooling**: 최댓값을 취해 추출
> ![](https://velog.velcdn.com/images%2Fdltjrdud37%2Fpost%2F48a47c04-e3b8-42ea-98b4-8cbba26e8f51%2FScreen%20Shot%202021-01-27%20at%203.23.21%20PM.png)
>
> **CNN 모델은 convolution(특징 추출)과 pooling(샘플링)의 반복이다.**
>
> **Flatten**
> - convolution, pooling층의 결과인 **feature map**을 1차원 벡터로 펴는 것을 말함
> - 컨볼루션 층과 맥스 풀링층을 지나 다시 **Dense()함수를 이용해 만들었던 기본층에 연결**할 때
>
>**Drop out**
> - 은닉층에 배치된 노드(뉴런) 중 일부를 임의로 꺼주는 것
> ![](https://thebook.io/img/080324/235.jpg)
> - 랜덤하게 노드를 끄기 때문에 학습 데이터에 지나치게 치우쳐서 학습되는 과적합 방지 가능
> 
>![](https://thebook.io/img/080324/236.jpg)
>
>
> convolution > pooling > flatten 이후 fully connected 층에서 모두 연결되어 다층 퍼셉트론의 구조를 가진다. 최종적으로는 활성화 함수(softmax)를 이용하여 이미지가 분류된다.



- **합성곱 계층**(conv2D)은 이미지에 필터링 기법을 적용한다.
- **풀링 계층**(MaxPooling2D)은 이미지의 국소적인 부분들을 하나의 대표적인 스칼라 값으로 변환함으로써 이미지의 크기를 줄이는 등의 기능을 수행한다.

## Convolution, MaxPooling 모델
1. `from tensorflow.keras import layers`, `from tensorflow.keras import models`
2. `model = models.Sequential()`: 신경망 객체를 생성한다.
3. 합성곱층 생성
   - 합성곱 계층: `model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))`
   - 풀링 계층:`model.add(layers.MaxPooling2D(2,2,))` 

## 이미지
1. `import cv2`
2. 이미지 파일을 Color로 읽어온다.
   - `img_color = cv2.imread(경로, cv2.IMREAD_COLOR)`
3. 컬러 이미지를 채널멸로 분리한다.
   - `b, g, r = cv2.split(img_color)`
4. 각 채널의 이미지에서 merge 함수를 사용해 채널의 이미지를 합칠 수 있다. 하나의 채널 이외의 빈 이미지를 사용하면 그 채널만 강조된 이미지를 볼 수 있다.
   - `zeros = np.zeros((img_color.shape[0], img_color.shape[1]), dtype=uint8)`
   - `b = cv2.merge([b, zeros, zeros])`: b 색만 강조된 이미지 반환

## MNIST 이미지 인식에 컨볼루션 신경망 적용
1. 이미지 데이터 로드 및 전처리 진행
   - `from tensorflow.keras.datasets import mnist`
   - `from tensorflow.keras.utils import to_categorical`
   - `(X_train, Y_train), (X_test, Y_test) = mnist.load_data()`
2. 정규화
   - `X_train = X_train.reshape(X_train.shape[0], 28, 28, 1).astype('float32') / 255`
   - test 데이터도 동일하게 정규화를 진행한다.
3. 원-핫 인코딩
   - `Y_train = to_categorical(Y_train, 10)`
   - `Y_test = to_categorical(Y_test, 10)`
4. **컨볼루션 신경망 모델 설정**
   - `from tensorflow.keras.models import Sequential`
   - `from tensorflow.keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D,AveragePooling2D`
   - 모델 생성
   - `model = models.Sequential()`
   - 컨볼루션층 생성: `model.add(layers.conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)))`
   - 풀링층 생성: `model.add(layers.MaxPooling2D((2,2,)))`
   - 컨볼루션층, 풀링층 반복
   - dropout 생성: `model.add(Dropout(0.25))`: 0.25%만큼의 노드를 dropout한다.
   - flatten층 생성: `model.add(Flatten())`
   - Dense()층과 연결: `model.add(Dense(128, activation='relu'))`
   - Dropout(과적합 방지): `model.add(Dropout(0.5))`
   - Dense()층으로 마무리: `model.add(Dense(10, activation='softmax))`
5. 모델 컴파일
   - `model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')`
6. 생성한 모델을 저장한다.
   - `from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping`
   - `import os`
   - 모델 디렉토리를 생성한다.: `MODEL_DIR = '경로'`
     - 경로 존재 여부에 따른 조건 부여: `if not os.path.exists(MODEL_DIR): os.mkdir(MODEL_DIR)`
   - 모델 안에 파일로 저장한다.: `modelpath="./model/{epoch:02d}-{val_loss:.4f}.hdf5"`
   - `checkpointer = ModelCheckpoint(filepath = modelpath, monitor='val_loss', verbose=1, save_best_only=True)`
     - **특정 에포크에서 모델의 가중치를 저장할 수 있음**
     - `filepath`: 모델을 저장할 경로
     - `monitor`: 모델을 저장할 때 기준이 되는 값 (val_loss: 검증 셋의 손실이 가장 작을 때 저장, loss: 학습 셋의 손실이 가장 작을 때 모델 저장)
     - `save_best_only`: True인 경우, monitor 되고 있는 값을 기준으로 가장 좋은 값으로 모델 저장, False인 경우, 매 에폭마다 모델이 filepath{epoch}로 저장됨
7. 모델 최적화 단계에서 학습 자동 중단을 설정한다. (**Early Stopping**)
   - `early_stopping_clbk = EarlyStopping(monitor='val_loss', patience=10)`
     - **손실이 더 이상 개선되지 않을 때 학습을 중지**
     - `patience`: 개선이 안된다고 바로 종료하지 않고 개선을 위해 몇번의 에포크를 기다릴지 설정
8. 모델 실행/학습
   - `history = model.fit(X_train, Y_train, validation_data=(X_test, Y_test), epochs=30, batch_size=200, callbacks=[early_stopping_clbk, checkpointer])`
     - `batch_size`: 전체 학습 데이터 셋을 여러 작은 그룹으로 나누었을 때 batch size는 하나의 소그룹에 속하는 데이터 수를 말한다.
     - `callbacks`: 모델 학습 중에 추가적인 동작을 수행하도록 지정한다. (ModelCheckpoint, EarlyStopping 등이 있음)
9. 모델 평가 (테스트 정확도를 출력한다.)
    - `model.evaluate(X_test, Y_test)[1]`: accuracy를 반환한다.
    - 테스트 셋의 오차: `history.history['val_loss']`
    - 학습셋의 오차:`history.history['loss']`
10. 테스트 셋의 오차와 학습셋의 오차가 에포크가 진행되면서 어떻게 변화하는지 그래프로 나타낸다.
