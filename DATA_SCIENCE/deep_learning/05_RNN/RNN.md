# 순환신경망 (RNN)
> keras의 신경망 알고리즘으로 순차 데이터나 시계열 데이터를 이용하는 인공 신경망 유형
>
> ![](https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2017/10/06/intro-gluon-1.gif)
>
> 순차적 데이터를 hidden layer에 한번에 한 단계씩 전달함. hidden layer은 단기 기억 구성 요소의 미래 예측을 위해서 이전 입력값을 기억하고 사용할 수 있다. 


## 모델 생성
```
from tensorflow import keras

model = keras.Sequential()
model.add(keras.layers.SimpleRNN(8, input_shape=(100, 500)))  # 하나의 샘플이 100개의 숫자로 되어 있고, 각각의 숫자가 500개의 features로 되어 있다.
model.add(keras.layers.Dense(1, activation='sigmoid'))
```
> 출력크기는 8, 500차원의 입력층*뉴런 8 + 은닉층 크기(8*8) + 절편 8

1. 모델 생성
2. 패딩된 seq 데이터를 원핫인코딩 변환
   - `train_oh = keras.utils.to_categorical(train_seq)`
   - `val_oh = keras.utils.to_categorical(val_seq)`
3. compile, fit으로 모델 훈련하기

## 임베딩 사용한 순환 신경망 모델
> 유사성이 높은 단어들은 비슷한 수치의 단어로 생성 (에포크 한번 반복될 때마다 유사성 반영하도록 모델 구성)

```
model2 = keras.Sequential()
model2.add(keras.layers.Embedding(500, 16, input_length=100))
# 500개의 단어 하나당 16개의 값을 가지는 벡터로 만들게 됨
model2.add(keras.layers.SimpleRNN(8))
model2.add(keras.layers.Dense(1, activation='sigmoid'))

```