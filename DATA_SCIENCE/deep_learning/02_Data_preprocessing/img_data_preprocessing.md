# 이미지 데이터 전처리
> Tensorflow에 존재하는 MNIST 데이터 셋을 이용해서 이미지 데이터 전처리를 진행할 것이다.
> 흑백 손글씨 숫자 이미지(28x28 픽셀)을 0~9까지로 분류한 데이터 셋이다.


1. `from tensorflow.keras.datasets import mnist`: MNIST 데이터셋을 불러온다.
2. mnist 데이터셋은 6만개의 훈련 이미지와 만개의 테스트 이미지로 구성된다. 따라서 `(X_train, Y_train), (X_test, Y_test) = mnist.load_data()`를 사용해서 `X_train.shape[0]`을 구해보면 학습 데이터 6만개, X_test에 적용해보면 만개인 것을 확인할 수 있다.
3. `plt.imshow(X_train[0], cmap='gray_r')`로 이미지가 어떤 형태로 나오는지 확인해본다.
4. `X_train.shape(-1, 28*28)`: `(60000, 28, 28)`의 2차원 배열을 1차원 배열`(60000, 784)`로 변경한다.
   - `X_test.shape(-1, 28*28)`: 테스트 데이터도 차원 변경을 진행한다.
5. 이미지의 픽셀값은 0~255로 되어 있다. 서로 다른 피처의 크기를 통일해주기 위해 **정규화**를 수행해준다.
   - `X_train = X_train.astype('float32')/255`
   - 실수로 변환 후 255로 나누어주면 숫자들이 0에서 1 사이의 값으로 변경된다.
   - `X_test = X_test.astype('float32')/255`: 테스트 데이터도 정규화 시켜준다.
6. Y_train을 이용해 숫자가 실제로 어떤 값인지 알 수 있다. 실제로 어떤 값인지를 원-핫 인코딩을 이용해 바이너리화하여 알아보자.
   - `from tensorflow.keras.utils import to_categorical`
   - `Y_train = to_categorical(Y_train, 10)`: 0~9까지의 숫자 중 만약 숫자의 실제 값이 5라면 5를 제외한 나머지 부분은 0으로, 5만 1로 반환하는 리스트를 각 이미지에 대해 반환한다.
   - Y_test에 대해서도 똑같이 수행한다.