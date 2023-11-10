# 자연어 처리 NLP(Natural Language Processing)
> 컴퓨터 알고리즘은 수치로 된 데이터만 이해하기 때문에 텍스트 자료를 딥러닝에 그대로 입력할 수 없다. 따라서 텍스트 전처리 과정이 필요하다.

## 피처 벡터화
> 텍스트 ==> 숫자형 값(벡터 값)
> 
> <피처 벡터화 방식>
> 1. **카운트 기반의 벡터화**
> 2. **TF-IDF(Term Frequency-Inverse Document Frequency) 기반의 벡터화**

### 1. 카운트 기반의 벡터화
> 단어 피처에 값을 부여할 때 **단어의 빈도 수** (Count)를 부여하는 것
>
> 카운트 값이 높을 수록 중요한 단어로 인식한다.

### 2. TF-IDF 기반의 벡터화
> 개별 문서에서 자주 나타나는 단어에 높은 가중치 
>
> **모든 문서에서 전반적으로 자주 나타나는 단어에 대해 패널티** (언어 특성상 범용적으로 자주 사용되는 경우일 수도 있기 때문)
>
> 문서마다 텍스트가 길고 문서의 개수가 많은 경우 TF-IDF 방식을 사용하는 것이 예측 성능을 향상시킬 수 있음

## 텍스트 전처리 작업
![](https://blog.kakaocdn.net/dn/wdpqf/btq2tlCJO3r/rzzOOkjk4of1S4FhFR9XJ1/img.png)
1. 정규화: 표현 방법이 다른 단어들을 통합시켜서 같은 단어로 만든다.
   1. 정제(Cleaning): 노이즈 데이터 제거
      - 정규 표현식: 특정 규칙이 있는 텍스트 데이터를 빠르게 제거한다.
   2. 어간 추출, 표제어 추출: 하나의 단어로 일반화시켜서 문서 내의 단어 수를 줄이는 작업
   3. 불용어 제거: 문장에서 자주 등장하지만 실제 의미 분석에 거의 기여하는 바가 없는 단어 제거
2. 토큰화: 토큰이라 불리는 단위로 나누는 작업
3. 정수 인코딩: 각 단어를 고유한 정수에 맵핑한다.(index 부여)
4. 패딩: 여러 문장의 길이를 임의로 동일하게 맞춰준다. 하나의 행렬로 보아 처리
5. 원-핫 인코딩: 문자를 숫자로 변환한다.

### 텍스트 토큰화
> **Tokenization**: 입력된 텍스트를 잘게 나누는 과정이다.
>
> **Token**: 작게 나누어진 하나의 단위 (단어, 문장, 형태소 등)
>
> ![](https://fineproxy.org/wp-content/uploads/2023/05/Tokenization-in-natural-language-processing-1.jpeg)

1. 토큰화 시작
   - `import tensorflow.keras.preprocessing.text import Tokenizer`
   - `tk = Tokenizer(num_words=100)`
     - num_words는 단어의 개수를 제한 (num_words - 1)개의 단어만 토큰화 진행
     - **전부 소문자로 변환되며 ?는 제거되어 하나의 단어로 일반화시킨다.**
   - `tk.fit_on_texts(sentences)`: 문자 데이터를 입력받아서 리스트의 형태로 변환한다.
   - `tk.word_index`: 단어와 숫자의 키-값 쌍의 딕셔너리를 반환한다. {'today':1}
   - `tk.index_word`: 단어와 숫자의 인덱스 값-키 쌍의 딕셔너리를 반환한다. {1:'today'}
   - **단어 빈도수 확인**: `tk.word_counts`
   - **시퀀스형태로 변환**: `tk.texts_to_sequences(sentences)`
     - 부여된 숫자(word_index)로 문장을 변환한다. 예를 들어, [[4,2,1,3]]은 지정된 인덱스 값의 단어들로 문장이 구성되어 있음을 뜻한다.
     - ![](https://codetorial.net/tensorflow/_images/natural_language_processing_in_tensorflow_02.png)
   - **단순 텍스트를 분리한다.**
     - `from tensorflow.keras.preprocessing.text import text_to_word_sequence`
     - `test_to_word_sequence(text)`: 단어들로 구성된 문장을 단어 토큰별로 구분하여 list를 반환한다.
2. 단어의 빈도수 확인
   - 단어의 빈도수 확인은 `tk.word_counts`를 통해 확인한다.
   - 토큰의 구분에 사용된 문장의 수: `tk.document_count`
   - 하나의 토큰이 몇 개의 문장에 포함되는지 **소속된 문장의 수**를 구하기 위해서는 `tk.word_docs`
3. 단어의 원-핫 인코딩
   - 벡터 공간을 0으로 채우고 index에 해당하는 값만 1로 변경한다.
   - `from tensorflow.keras.utils import to_categorical`
   - `word_size = len(token.word_index) + 1`: 인덱스가 0을 제외한 1부터 진행되기 때문에 1을 더한다.
   - `to_categorical(token.texts_to_sequences([text]), num_classes = word_size)`: 인덱스가 있는 부분이 1로 채워지는 행렬이 만들어진다.

## 원-핫 인코딩의 대안
> 원-핫 인코딩은 벡터의 길이가 너무 길어진다는 단점이 있다.

1. 말뭉치(Corpus): 언어의 표본을 추출한 집합
2. 밀집 표현: 사용자가 설정한 값으로 모든 단어의 벡터 표현의 차원을 맞춤 (0,1만 가진 값이 아닌 실수값을 가짐)
   - 벡터의 차원이 조밀해짐
   - ![](https://heung-bae-lee.github.io/image/Dense_representation.png)
3. **단어 임베딩** (word embedding): 단어의 의미를 고려하고 밀집 벡터의 형태로 표현한다. 의미가 비슷한 단어는 비슷한 방향에 위치한다.
   - 각 단어를 임의 숫자로 부여하고 학습을 통해 유사도를 계산한다. (문장과 단어와의 관계 파악을 통한 유사도 계산)
   - ![](https://www.goldenplanet.co.kr/data/data/2021/12/2021-12-23_14-21-28-33530-1640236888.png)
4. 패딩: 문장의 길이를 나타내는 배열의 크기를 동일하게 맞추는 작업 (빈 부분은 0으로 채움)

### 패딩
![](https://thebook.io/img/080328/239.jpg)
- `from tensorflow.keras.preprocessing.sequence import pad_sequences`
- 문장들을 시퀀스 형태로 출력한다.: `result = token.texts_to_sequences(sentences)`
- `pad_sequences(result)`: 기본 설정은 앞에 0을 추가해서 배열의 길이를 맞추는 것이다.
  - `maxlen`: 맞출 길이를 지정한다.
  - `padding='pre'/'post'`: pre는 앞 부분을 0으로 채움, post는 뒷 부분을 0으로 채움.


### 단어 임베딩
1. 문서 분류나 감성 예측과 같은 문제와 함께 단어 임베딩 학습
2. 사전 훈련된 단어 임베딩

- `from tensorflow.keras.layers import Dense, Flatten, Embedding`
- 문장들 시퀀스화 => 패딩
- `model = Sequential()`
- Embedding층 추가: `model.add(Embedding(len(word_index)+1, 총 단어의 개수, input_length=4))`
- 순환 신경망 추가: `model.add(keras.layers.SimpleRNN(64, input_shape=(4,1)))`
- `model.add(Flatten())`
- `model.add(Dense(1, activation='sigmoid'))`
- `model.compile('rmsprop', 'mse')`
- `model.predict(패딩한 배열 데이터)`
  - 차원이 늘어난 결과가 나온다. (3,4) => (3,4,8)
  - 단어 4개로 패딩한 문장 3개에 대해 문장 3개에 들어가는 unique한 단어들은 총 8개이다.
  - 이 때, 한개의 단어가 정수 1로 인코딩 되었다면 **임베딩층을 통해서 8개의 밀집 데이터로 재 인코딩 되었다.**
- 모델 학습: `model.fit(패딩된 결과, 결과 리스트, epochs=20)`
- 모델 평가: `model.evaluate(패딩된 결과, 결과 리스트)[1]`
- 예측: `model.predict([[0,6,7,8]])` # 확률 0.5 이상이면 1로 분류