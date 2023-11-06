# 심층 신경망
> 층이 여러개 존재하는 신경망이다.
> 입력층과 출력층 사이에 밀집층을 추가한다.
> - **은닉층**: 입력층과 출력층 사이의 모든 층
>   - 은닉층에도 활성화 함수(선형방정식의 계산식에 적용하는 함수)가 들어가 있다.
>   - 출력층의 뉴런 수보다 은닉층의 뉴런 수를 많이 설정하는 것이 성능에 좋음


```
model = Sequential()

dense1 = keras.layers.Dense(100, activation='sigmoid', input_shape=(784,))  # 은닉층
dense2 = keras.layers.Dense(10, activation='softmax') 
```
- 784개의 input를 100개의 분류에 할당한다.
- 이후 출력값을 다음 층의 입력값으로 받고 10개의 분류에 할당한다.
  - 이 때, 입력값은 이전 층의 출력값을 입력값으로 받으므로 `input_shape` 설정을 생략해도 된다.

- **여러개의 층을 추가하려면 리스트로 만들어서 전달해야 한다.(층력층을 맨 마지막)**
  - `model = keras.Sequential([dense1, dense2])`
  - 층을 다른 방법으로도 추가할 수 있다.
  - ```
    model = keras.Sequential([
    keras.layers.Dense(100, activation='sigmoid', input_shape=(784,)), # 은닉층
    keras.layers.Dense(10, activation='softmax', name='output')], name='손글씨분류')
    # model의 이름을 설정할 수도 있다.
    ```

## 렐루 활성화 함수
> 입력이 양수일 경우 활성화 함수가 없는 것처럼 그냥 통과시키고 음수일 경우 0으로 만든다.
> 이미지 처리에 좋은 성능을 낸다.

## flatten 층
> `.reshape(-1, 28*28)`처럼 1차원으로 변경하도록 층을 하나 제공하는데, 그것이 flatten 층임.
>
> `keras.layers.Flatten(input_shape(28, 28))`으로 이미지를 2차원에서 1차원으로 처리한다.
>
> flatten층을 추가했기 때문에 1차원으로 재배치를 진행하지 않는다.

## 옵티마이저
> 하이퍼파라미터 배치나 조정을 가장 적절하게 바꿔주는 역할을 한다. 손실함수가 최저 손실값을 찾아가도록 하는 것이 **최적화 함수**이다.
>
> **SGD, Adam을 많이 사용한다.**
> - `model.compile(optimizer='sgd',loss='sparse_categorical_crossentropy', metrics='accuracy')`
> - optimizers 객체를 이용할 수도 있다.
>   - `sgd = keras.optimizers.SGD()`
>   - `sgd = keras.optimizers.SGD(learning_rate=0.1, momentum=0.9, nesterov=True)`
>     - `learning_rate`: 학습룰
>     - `momentum`: 접선의 기울기에 한 시점 전의 접선의 기울기값을 일정한 비율만큼 반영해 관성같은 역할을 한다. (적절한 방향으로 진행하게 하고 곡점을 줄여줌)
>     - `nesterov`: 규제

> 옵티마이저 함수는 **SGD, Adam**를 많이 사용한다.
> `model.compile(optimizer='adam',loss='sparse_categorical_crossentropy', metrics='accuracy')`


