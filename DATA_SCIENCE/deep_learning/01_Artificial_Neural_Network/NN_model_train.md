# 신경망 모델 훈련
> **인공 신경망 모델이 최적화 하는 대상은 정확도가 아닌 *손실함수*이다.**

## 손실 곡선
- **사이킷런 알고리즘**: 모델의 구조가 어느 정도 고정되어 있음
- **케라스 알고리즘**: 모델의 구조를 직접 만드는 느낌이 강함

- **History 클래스 객체**: 훈련과정에서 계산한 지표(손실도, 정확도) 값이 저장되어 있다.
  - 이 값을 사용해 손실곡선 그래프를 그릴 수 있다.
  - `history.history.index()`: 'loss', 'accuracy', 'val_loss', 'val_accuracy'와 같이 지표가 반환됨


1. `import pickle`: 모델에서 가중치만 저장하려고 할 때 사용한다.
2. `(train_input, train_target), (test_input, test_target) = mnist.load_data()`: 학습데이터와 테스트 데이터를 mnist data set에서 불러온다.
3. 학습 데이터 정규화 시키기
   - `train_scaled = train_input / 255.0`
4. 정규화한 학습데이터를 학습데이터와 검증데이터로 나눈다.
   - `train_scaled, val_scaled, train_target, val_target = train_test_split(train_scaled, train_target, test_size = 0.2, random_state=42)`
5. 모델을 구성하는 함수를 생성할 것이다. **(sequential, dense 과정 다 들어간 함수)**
   - ```
     # m_layer을 전달 안하면 없는 것으로 함

     def model_create(m_layer=None):
        model = keras.Sequential()
        model.add(keras.layers.Flatten(input_shape=(28,28)))
        model.add(keras.layers.Dense(100, activation='relu'))
        model.add(keras.layers.Dense(10, activation='softmax'))
        # 다중 분류이기 때문에 활성화함수는 softmax 사용
        return model
     ```
     - `model = model_create()`
6. 모델 compile
   - `model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy')`
7. 정규화된 학습데이터에 모델을 학습시켜 history 변수에 저장한다.
   - `history = model.fit(train_scaled, train_target, epochs=5, verbose=0)`
     - `epochs`: 모델 학습 반복 횟수 **(epoch를 늘릴수록 손실은 감소하고 정확도는 증가하지만 과적합의 가능성을 고려해야 함)**
     - `verbose`: verbose가 0이면 훈련과정 출력 안함
8. epoch를 20으로 늘려 그래프를 그려본다.
   - ```
     plt.plot(history.history['loss'])
     plt.plot(history.history['accuracy'])
     plt.xlabel('epoch')
     plt.ylabel('loss')
     plt.savefig('loss2', dpi=300)
     plt.show()
     ```
   - epoch가 늘어날수록 손실이 감소하고 정확도가 증가하여 성능이 좋아진다.
   - 하지만 반복학습이기 때문에 과대/과소 적합의 가능성이 있다.
9. 과적합 가능성을 파악하기 위해 **훈련 세트뿐만 아니라 검증세트에 대한 점수**도 필요하다.
    - history에 검증데이터를 추가하여 같이 학습시킨다.
    - `history = model.fit(train_scaled, train_target, epochs=20, verbose=1, validation_data=(val_scaled, val_target))`
10. 검증데이터의 학습도 진행 후 **학습데이터의 손실값과 검증데이터의 손실값**을 그래프로 나타낸다.
    - **훈련손실값**은 계속 감소하다가 0으로 수렴한다.
    - **검증손실값**은 감소하다가 감소정도가 줄어든다.
11. optimizer을 adam으로 변경 후 확인한다.
    - `model = model_create()`
    - `model.compile(loss='sparse_categorical_crossentropy', metrics='accuracy', optimizer='adam')`
    - `history = model.fit(train_scaled, train_target, epochs=20, verbose=1, validation_data=(val_scaled, val_target))`


## 과적합 감소를 위한 드롭아웃
> 훈련 과정에서 층에 있는 일부 뉴런을 랜덤하게 끔(출력을 0으로 만듬)
> 특정 뉴런에 과대하게 의존하는 것을 줄일 수 있으므로 모든 입력에 주의를 기울이게 됨

- 은닉층 뒤에 드롭아웃 층 추가
   - `model = model_create(keras.layers.Dropout(0.3))`: 100개를 전달받지만 30%는 0으로 출력된다.
- 결과적으로 과적합이 줄었다.

## 모델 저장과 복원
- **`save_weights()`**: 훈련된 모델의 파라미터 저장
  - `model.save_weights('model-weight.h5')`
- **`save()`**: 훈련된 모델의 구조와 파라미터 저장
  - `model.savee('model-whole.h5')`

1. 새로운 모델을 만들고 기존에 훈련시켜 놓은 모델에서 **저장한 파라미터**를 로드시켜 새 모델에 적용한다.
   - `model = model_create(keras.layers.Dropout(0.3))`
   - `model.load_weights('./model-weight.h5')`
2. 저장된 모델을 읽어와서 모델을 이용한 평가 **(모델의 구조와 가중치가 저장된 파일 읽어오기)**
   - `model = keras.models.load_model('./model-whole.h5')`
 - 위의 두 모델은 같은 모델의 파라미터를 사용하고 있기 때문에 정확도의 결과도 동일하고 같은 모델이다.


## 콜백
> 훈련 과정 중에 다른 프로그램을 호출하는 개념이다.

1. 모델을 생성하고 compile 한다.
2. 체크포인트(콜백함수)를 생성한다.
   - `cb = keras.callbacks.ModelCheckpoint('best-model.h5')`
3. 콜백을 적용하여 모델 학습을 진행한다.
   - `model.fit(train_scaled, train_target, epochs=20, verbose=1, validataion_data=(val_scaled, val_target), callbacks=[cb])`

### early stopping callback
> 조기종료 콜백

1. 모델을 생성하고 compile 한다.
2. 체크포인트(콜백함수)를 생성한다.
3. 조기종료 객체를 생성한다.
   - `early_cb = keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)`
     - `patience`: n번 연속 검증 점수가 향상되지 않으면 훈련 중지
     - `restore_best_weights`: True로 지정하면 가장 낮은 검증 손실을 낸 모델 파라미터로 되돌린다.
4. 콜백을 적용하여 모델 학습을 진행한다.
   - `callbacks=[cb, early_cb]`를 fit함수에 적용
5. 언제 종료되었는지를 저장한 속성을 확인한다.
   - `early_cb.stopped_epoch`
