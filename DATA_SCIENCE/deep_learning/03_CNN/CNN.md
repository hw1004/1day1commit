# 컨볼루션 신경망(CNN)

> 주로 시각적인 이미지를 분석하는 데 사용한다.
> 필터링 기법을 인공신경망에 적용하여 이미지를 효과적으로 처리할 수 있는 심층 신경망 기법으로 행렬로 표현된 필터의 각 요소가 데이터 처리에 적합하도록 자동으로 학습되는 과정을 통해 이미지를 분류하는 기법이다.
> - 동일 객체라도 전체적인 픽셀을 보았을 때 환경의 변화에 따라 변화가 큰 것들이 존재한다.
>   - 전체를 가지고는 같은 객체인지 판단하기 어렵지만 부분의 특징을 추출하고 결합하였을 때, 판단이 더 쉬워진다. (CNN의 장점)
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
>
> convolution > pooling > flatten 이후 fully connected 층에서 모두 연결되어 다층 퍼셉트론의 구조를 가진다. 최종적으로는 활성화 함수(softmax)를 이용하여 이미지가 분류된다.



- **합성곱 계층**(conv2D)은 이미지에 필터링 기법을 적용한다.
- **풀링 계층**(MaxPooling2D)은 이미지의 국소적인 부분들을 하나의 대표적인 스칼라 값으로 변환함으로써 이미지의 크기를 줄이는 등의 기능을 수행한다.


1. `from tensorflow.keras import layers`, `from tensorflow.keras import models`
2. `model = models.Sequential()`: 신경망 객체를 생성한다.
3. 합성곱층 생성
   - 합성곱 계층: `model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)))`
   - 풀링 계층:`model.add(layers.MaxPooling2D(2,2,))` 