# 합성곱 신경망 - 다중분류

![](https://i0.wp.com/healthyinsight.co.kr/wp-content/uploads/2023/07/head-optimized.png?resize=836.25%2C214&ssl=1)
## 이미지에서 특징 감지
|import|description|
|---|---|
|`import urllib.request`|url을 가져오기 위한 파이썬 모듈|
|`import zipfile`|압축 파일 쓰기, 읽기, 해제하기|
|`from tensorflow.keras.preprocessing.image import ImageDataGenereator`|원본 이미지의 수평/수직 반전, 회전, crop, RGB 채널 순서 변경, 색조 변경 등의 **증강 기법**을 대신해줌|
|`from tensorflow.keras.optimizer import RMSprop`|optimizer로 합 대신 지수의 평균값을 활용한다.|

## `image_dataset_from_directory`
> 디스크에서 이미지 데이터를 로드하여 Tensroflow 데이터셋을 만드는 데에 사용된다.
```
tf.keras.utils.image_dataset_from_directory(
    directory,
    labels='inferred',   # 레이블이 디렉토리 구조에서 생성됨
    label_mode = 'int',  # 인코딩 설명
    class_names=None  # labels가 `inferred`인 경우에만 유효
    color_mode = 'rgb',
    batch_size = 32,
    image_size = (256, 256),
    shuffle = True,
    seed = None,
    validation_split=None,
    subset=None,
    interpolation = 'bilinear',  # 문자열, 이미지 크기를 조정할 때 사용되는 보간 방법 (bilinear, nearest, area 등)
    follow_links = False,  # 심볼릭 링크가 가리키는 하위 디렉토리 방문할지 여부
    crop_to_aspect_ratio = False, # 이미지를 지정된 가로 대 세로 비율로 자르는 데 사용 (True일 시 비율이 유지된다.)
    **kwargs
)
```

## 다중 분류
1. `import wget`: 웹에서 파일을 다운로드하는 목적으로 사용되는 도구
2. `wget.download(경로)`
3. 데이터 압축을 푼다.
   - `import zipfile`
   - `zip_ref = zipfile.ZipFile(zip파일 경로, 'r')`: 'r'은 read를 나타내어 zip 내의 파일을 읽어오는 모드이다. w는 쓰기 모드, a는 추가 모드이다.
   - `zip_ref.extractall('./')`: zip 파일 내의 모든 파일을 지정된 디렉토리로 압축 풀기하는 과정이다.
   - `zip_ref.close()`: zip 파일을 명시적으로 닫는다.
   - 학습 데이터와 검증 데이터에 대해 모두 데이터 압축 해제를 진행한다.
4. **학습 데이터** 전처리 및 데이터 증강을 위한 객체 (학습/평가 데이터) 각각 생성
   - `Training_DIR = 경로`
   - ```
     training_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        shear_range=0.5,
        zoom_range=[0.8,2.0],
        horizontal_flip =True,
        vertical_flip=True,
        fill_mode='nearest'
     )
     ```
5. **검증 데이터** 준비 및 전처리
   - 3번의 zip 파일 압축 해제를 검증 데이터에도 적용하여 준비한다.
   - 폴더 내의 이미지 파일을 폴더로 split해주는 패키지 install: `!pip install split-folders[full]`
6. train/val/test 비율을 적용하여 나눈다.
   - `import splitfolders`
   - `splitfolders.ratio(원본 디렉토리의 경로, output=분할된 데이터를 저장할 대상 디렉토리 경로, seed=1336, ratio=(0.8, 0.2))`
     - `ratio`: 학습 데이터 80%와 검증 데이터 20%로 분할하겠다는 뜻
7. 검증 데이터와 테스트 데이터 지정
   - 위에서 분할된 데이터를 저장할 대상 디렉토리 경로에 대해 train, val에 대하여
   - `VALIDATION_DIR = "./rps-test-val/train"`
   - `TEST_DIR = "./rps-test-val/val"` 를 지정한다.

## 이미지 전처리
1. 검증, 테스트 데이터는 증강을 사용하지 않고 학습 데이터만 증강을 사용한다.
   - `val_datagen = ImageDataGenerator(rescale = 1./255)`: 검증 데이터는 증강 사용 안한다.
2. train_datagen generator로 train,val,test 이미지 증식
   ```
   train_generator = training_datagen.flow_from_directory(
    TRAINING_DIR,
    target_size=(300,300),
    class_mode='categorical'
    )   # 학습 데이터만 데이터 증강해도 무방하다.

   validation_generator = val_datagen.flow_from_directory(
    VALIDATION_DIR,
    target_size=(300,300),
    class_mode='categorical'    
   )

   test_generator = val_datagen.flow_from_directory(
    TEST_DIR,
    target_size=(300,300),
    class_mode='categorical'    
   )
   ```

## 모델 생성, 학습 및 적용 (Checkpoint, EarlyStopping)
1. 모델 생성
```
model_b = tf.keras.models.Sequential([
    # 입력 크기는 원하는 이미지(150x150, 3채널)와 맞아야 합니다.
    # 첫 번째 합성곱 층
    tf.keras.layers.Conv2D(16, (3,3), activation='relu', 
                           input_shape=(300,300, 3)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # 두 번째 합성곱 층
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # 세 번째 합성곱 층
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # 네 번째 합성곱 층
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    # 밀집 층에 전달하가 위해 펼칩니다.
    tf.keras.layers.Flatten(),
    # 512개 뉴런을 가진 은닉층
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
    # 출력층(다중분류이므로 softmax)
])
```

2. 모델 compile, fit
   - `model_b.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics = 'accuracy')`
   - `model_b.fit(train_generator, epochs=15, validation_data=validation_generator)`

3. 테스트 데이터 검증결과 확인
   - 테스트 데이터 검증: `model_b.evaluate(test_generator)`
4. 학습 데이터와 테스트 데이터가 차이가 있다. 따라서 더 학습해야 한다.
5. 조기종료 및 chk point 코드
   - `ck_cb = tf.keras.callbacks.ModelCheckpoint('rps-best-model.h5')`: 학습 중에 모델 성능이 향상되거나 특정 지점에서 모델을 저장한다. 지정된 경로에 저장한다.
   - `early_cb = tf.keras.callbacks.EarlyStopping(patience=2, restore_best_weights=True)`
6. 조기 종료와 체크 포인트를 적용하여 모델을 다시 학습한다.
   - `history = model_b.fit(train_generator, epochs=25, validation_data = validation_generator, callbacks = [ck_cb, early_cb])`


# 이미지에 대한 예측 확인
- `sample_images = ['./image/rsp_image_{}.jpg'.format(i) for i in range(1, 4)]`
```
rsp_name = ['보', '바위', '가위']

for image in sample_images:
    # 이미지 출력
    plt.imshow(mpimg.imread(image))
    plt.show()
    
    # 이미지 불러오기
    img = tf.keras.utils.load_img(image, target_size=(300,300))
    x = tf.keras.utils.img_to_array(img)  # 이미지를 numpy 배열로 변환
    x = np.expand_dims(x, axis=0)  # 배열의 차원을 확장한다. (axis는 새로 추가될 차원의 위치이다.)
    
    classes = model_b.predict(x) # 보, 바위, 가위의 각 확률값이 나옴
    print(classes)
    idx = np.argmax(classes[0]) # 보, 바위, 가위 중 가장 확률값이 높은 것의 인덱스 반환
    
    print(image + "는 {}입니다.".format(rsp_name[idx]))
```

## 드롭아웃 규제
> 신경망 모델의 과적합을 줄이는 데 사용된다. 학습 중 무작위로 일부 뉴런을 비활성화하여 과적합을 감소시킬 수 있다.

- 모델을 생성할 때 `tf.keras.layers.Dropout(0.5)`로 드롭아웃 층을 추가한다.
- 드롭아웃층을 추가한 모델을 생성 후 똑같이 compile을 진행한다.
- checkpoint와 early_stopping 객체도 생성한다.
- fit함수를 이용해 checkpoint, early_Stopping을 적용하여 드롭아웃 층이 추가된 모델을 적용한다.
- 드롭아웃 규제를 한다고 하여 무조건 적으로 성능이 좋아지지 않는다.

![](https://velog.velcdn.com/images%2Fjoo4438%2Fpost%2F90e2d4a0-c31b-4be6-b59d-5a63d9d81bc0%2Fimage.png)

## 모델 재구성 (패딩/노드 수 감소)
- 모델 생성 시 **Conv2D**, 컨볼루션 층의 파라미터에 `padding='same'`을 적용한다.
- **패딩**은 입력 이미지 주변에 가상의 픽셀을 추가하여 출력 크기를 입력과 동일하게 유지한다.

![](https://wikidocs.net/images/page/64066/conv10.png)


## Conclusion
- 합성곱층과 풀링층으로 구성된 모델, 드롭아웃층이 추가된 모델, 패딩이 추가된 모델 등 **여러 경우로 구성해서 모델링을 진행한 후** 가장 성능이 좋은 테스트 결과의 모델을 사용한다.