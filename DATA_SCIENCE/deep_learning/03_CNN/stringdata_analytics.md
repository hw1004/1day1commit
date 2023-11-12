# 문자열 데이터 수치화
## 데이터 전처리
1. 정규화로 한국어만 남기기
   - `import re`: 정규식 함수
   - `re.sub('[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]','',정규화할 문장)`: 한글과 공백제외 모두 제거한다.
2. 형태소 분석기로 어간 추출
   - `from konlpy.tag import Okt`
   - `okt = Okt()`
   - `okt.morphs(형태소 단어 단우이로 나눌 문장, stem = True)`
     - 텍스트를 형태소 단위로 나눈다.
     - `stem`: 각 단어에서 어간 추출 (기본값 False)
   - 비고
   - `okt.nouns()`: 텍스트에서 명사만 추출
   - `okt.phrases()`: 텍스트에서 어절을 뽑아냄
3. 불용어 제거
   - `stop_words = [불용어 (은,는,이,가 등)을 나열한다.]`: 제거할 불용어 나열
   - `s_lis = [token for token in 문장 if not token in stop_words]`: 불용어가 아닌 토큰들을 s_lis에 포함하여 리스트 생성
   - 불용어 제거한 토큰을  word index로 변환: `tokenizer.fit_on_texts(s_lis)`
     - `tokenizer.texts_to_sequences(s_lis)`
     - `word_vocab = tokenizer.word_index`
     - 위의 과정을 함수로 만들어서 train data와 test 데이터에 적용
4. 문장 인덱스 벡터로 전환
   - 학습데이터 리뷰들로 단어 사전을 생성해서 **문자 데이터를 인덱스로 바꾸어 준다.**
   - `tokenizer.fit_on_texts(clean_train_review)`
   - `tokenizer.texts_to_sequences(clean_train_review)`: 테스트 데이터도 숫자 seq로 변환
   - **단어사전 생성**: `word_vocab = tokenizer.word_index`
5. 패딩 처리
   - `pad_sequences(학습데이터 seq로 바꾼 결과, maxlen=8, padding='post)`: 패딩 진행 (평가데이터로도 패딩을 진행한다.)
   - **학습 데이터 라벨 벡터화**: `train_labels = np.array(train_data['label'])`: 평가 데이터 라벨 벡터화도 진행한다.
6. 전처리가 완료된 데이터를 넘파이 파일로 저장한다.
   - ```
     DATA_PATH = '.npy 파일 저장 경로'
     TRAIN_INPUT_DATA = 'train_input.npy'
     TRAIN_LABEL_DATA = 'train_label.npy'
     TEST_INPUT_DATA = 'test_input.npy'
     TEST_LABEL_DATA = 'test_label.npy'
     DATA_CONFIGS = 'data_configs.json'
     # json 파일은 word_vocab 단어 사전 저장하는 파일명이다.
     ```
   - **전처리된 학습데이터 넘파이로 저장**
   - `np.save(open(DATA_PATH + TRAIN_INPUT_DATA, 'wb'), train_inputs)`
   - `np.save(open(DATA_PATH+TRAIN_LABEL_DATA,'wb'),train_labels)`
   - **전처리된 테스트데이터 넘파이로 저장**
   - `np.save(open(DATA_PATH + TEST_INPUT_DATA, 'wb'), test_inputs)`
   - `np.save(open(DATA_PATH+TEST_LABEL_DATA,'wb'),test_labels)`
   - **데이터 사전 json으로 저장**
   - `json.dump(data_configs, open(DATA_PATH + DATA_CONFIGS, 'w'), ensure_ascii=False)`
7. 저장된 넘파이 파일 불러오기
   - `train_input = np.load(open(DATA_PATH + INPUT_TRAIN_DATA, 'rb'))`
   - `train_label = np.load(DATA_PATH + LABEL_TRAIN_DATA, 'rb')`
   - `vocabulary = json.load(open(DATA_PATH + DATA_CONFIGS, 'r'))`


## CNN 모델 생성
- `from tensorflow.keras.models import Sequential`
- `from tensorflow.keras.layers import Dense, Flatten, Embedding`

```
model = Sequential()
# 128 크기의 벡터 생성
model.add(Embedding(vocab_size, 128))
# 1차원의 sequential 데이터에 cnn 적용 Conv1D 사용
model.add(tf.keras.layers.Conv1D(100, 5, activation='relu'))
# 100(5) - Dropout 0.5 - 250 - 1
model.add(tf.keras.layers.GlobalMaxPooling1D())
model.add(tf.keras.layers.Dropout(rate=0.5))
model.add(tf.keras.layers.Dense(250, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))  # 긍부정 이진 분류
```

- `from tensorflow.keras.models import save_model`
- model fit하고 save 하기

- **모델 평가하기**: `model.evaluate(test_input, test_label_data[:10000])`
- **예측하기**: 모델 불러오고 (`tf.keras.model.load_model(경로)`) 예측 확률이 0.5 이상일 시 긍정리뷰 `float(model.predict(pad_new)) * 100`, 다른 경우 부정리뷰로 예측 `(1 - float(model.predict(pad_new))) * 100`