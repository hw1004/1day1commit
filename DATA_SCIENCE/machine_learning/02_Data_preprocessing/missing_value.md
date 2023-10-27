# 결측치
## 결측치 확인 및 제거
> - 결측치
>   - Nan: 값이 있어야 하는데 없는 결측 => **대체, 추정, 예측**으로 처리
>   - None: 값이 없는게 값인 결측(ex 직업-백수) => **새로운 값으로 정의**하여 처리
> - **결측 레코드**: 결측치를 포함하는 레코드
> - **결측치 비율**: 결측 레코드 수 / 전체 레코드 수

#### 결측치 처리방법
- 결측치 개수 확인 방법
  - `df.isnull().sum(axis=0)`: 각 컬럼의 결측치 개수를 반환한다.
  - `df.isnull().sum(axis=1)`: 각 레코드(행)의 결측치 개수를 반환한다.
- 결측치 비율 확인 방법
  - `df.isnull().sum(axis=0) / len(df)`: 컬럼별 결측치 비율을 반환한다. **모든 컬럼에 결측이 하나라도 발생하면(결측치가 없는 컬럼이 없다면) 열을 삭제할 수 없다.**

1. **행단위 결측 삭제**: 결측 삭제 이후에 들어오는 **새로운 데이터는 결측을 포함하면 안된다.** 또한 결측이 없는 레코드가 충분히 있어야 한다.
   1. `df.dropna(inplace=True)`: dataframe에서 결측값을 가지는 레코드(행)들을 삭제한다.
   2. `(df.isnull().sum(axis=1) > 0).sum()`: 결측값 삭제 후 df에 결측값이 남아 있는지 확인한다.
2. **열단위 결측 삭제**: 어느 특정 변수(컬럼)에만 결측이 많이 포함되어 있을 때 사용한다. 
   1. `df.replace('?', np.nan).isnull().sum() / len(df)`: NaN이 제공받은 데이터에서는 '?'로 표시될 때, 문자열인 '?'를 결측값인 NaN으로 변경한다. 그리고 결측치 비율을 확인한다.
   2. 컬럼 중에 결측치가 아예 없는 컬럼들이 있고 하나의 컬럼에 결측이 많이 포함되어 있는 경우 열을 제거한다.!
   3. `df.dropna(axis=1)` 또는 `df.drop('삭제하고자하는 컬럼', axis=1, inplace=True)`를 통해 결측치가 많이 있는 열을 삭제한다.
   4. `df.replace('?', np.nan).isnull().sum()/len(df)`로 열 삭제가 잘 되었는지 확인한다.


## 대표값을 활용한 결측치 대체
> 결측치를 처리하는 것의 대표적인 방법
> 특정 컬럼에 결측이 쏠린 경우 또는 v1+v2=1과 같은 명확한 상관성이 있는 경우에는 대표값을 활용하여 결측치를 대체하는 것은 부적절하다.

#### sklearn을 이용한 전처리 모델
- 평가 데이터는 전처리 모델을 학습하는데 사용하지 않음
- 모든 전처리는 학습 데이터에 준한다.
- 따라서 반드시 학습/평가 데이터론 분리하고 전처리를 진행해야 한다.

1. **모든 특징(인스턴스)의 타입이 같은 경우**
   1. 학습데이터와 평가데이터를 분리한다. 학습데이터는 Train_X, 평가데이터는 Train_y이다.
    ```
    X = df.drop('Output', axis = 1)
    y = df['Output']

    Train_X, Test_X, Train_y, Test_y = train_test_split(X, y, random_state=4)   
    ```
    2. 결측치를 확인한다.
        - `Train_X.isnull().sum()`: 학습데이터의 컬럼별 결측치 개수를 확인한다.
    3. 새로 들어올 데이터에도 결측이 있을 수도 있다고 가정, 결측이 있는 열은 중요한 열이라고 가정하자.
    4. 결측치를 대표값으로 대체
        - 독립변수들간의 관계성이 적어야 함
        - **독립변수들간의 상관계수**를 구하고 **변수의 상관계수의 평균**을 활용하여 관계성 추정 (수치형 변수에)
        1. **평균 상관계수**: `Train_X.corr().sum()/len(Train_X.columns)`: **상관계수는 -1과 1 사이이고 절대값이 1에 가까울 수록 상관성이 높다.**
        2. **SimpleImputer**: 결측이 있는 변수의 대표값으로 결측을 대체하는 인스턴스이다.
            1.  `si = SimpleImputer(strategy='mean')`: 평균으로 결측값을 대체하는 객체변수(객체인스턴스 생성)
            2.  `si.fit(Train_X)`: 학습 데이터로 대표값 계산
            3.  `si.transform(Train_X)`: 학습데이터에 대체값으로 대체(변환)한다.
            4.  `Train_X = pd.DataFrame(si.transform(Train_X), columns=Train_X.columns)`: 대체한 값으로 학습 데이터 df를 대체한다.
            5.  `Test_X = pd.DataFrame(si.transform(Test_X), columns=Test_X.columns)`: 평가데이터는 학습데이터로 생성한 대표값으로 변환만 진행한다.
    5. 예측
        - 새로운 데이터를 이용해서 예측을 할 때 결측이 있을 수 있기 때문에 si 변수는 instace 그대로 저장해두고 **dump()**함수를 사용해야 한다.

2. **다른 타입의 특징이 있는 경우**
   1. 학습데이터와 평가데이터를 분리한다. 학습데이터는 Train_X, 평가데이터는 Train_y이다.
    ```
    X = df.drop('Chd', axis = 1)
    y = df['Chd']

    Train_X, Test_X, Train_y, Test_y = train_test_split(X, y, random_state=4)   
    ```
    2. 결측치를 확인한다.
        - `Train_X.isnull().sum()`: 학습데이터의 컬럼별 결측치 개수를 확인한다.
    3. 평균상관계수를 확인한다. **주어진 데이터는 범주형 데이터가 있다고 가정하지만 정수형이므로 포함해서 확인한다.**
        - `Train_X.corr().sum()/len(Train_X.columns)`
    4. 학습데이터와 평가데이터 분류
        ```
        # 학습 데이터
        Train_X_cate = Train_X[['Famhist']]
        Train_X_cont = Train_X.drop('Famhist', axis=1)

        # 평가데이터
        Test_X_cate = Test_X[['Famhist']]
        Test_X_cont = Test_X.drop('Famhist', axis=1)
        ``` 
    5. 대표값으로 결측치 대체
        - 다른 타입의 특징이 있는 상태이다. Famhist라는 특징만 범주형 변수이고 다른 특징들은 연속형 변수를 가진다고 가정하자.
        - **범주형 변수**는 최빈값으로 대체
          - `si_mode = SimpleImputer(strategy='most_frequent')`
        - **연속형 변수**는 평균값으로 대체
          - `si_mean = SimpleImputer(strategy='mean')`
        - `si_mode.fit(Train_X_cate)`로 최빈값 대표값은 Famhist에 적용해준다.
        - `si_mean.fit(Train_X_cont)`로 평균은 그 외의 특징들에 적용해준다.
        - `si_mode.transform(Train_X_cate)`: Famhist 열에 최빈값 대표값으로 변환되어 적용된다.
    6. 데이터 결합
       1. ```
           Train_X_cate = pd.DataFrame(si_mode.transform(Train_X_cate),
                            columns=Train_X_cate.columns)

            Train_X_cont = pd.DataFrame(si_mean.transform(Train_X_cont),
                            columns=Train_X_cont.columns)

            Test_X_cate = pd.DataFrame(si_mode.transform(Test_X_cate),
                            columns=Test_X_cate.columns)

            Test_X_cont = pd.DataFrame(si_mean.transform(Test_X_cont),
                            columns=Test_X_cont.columns)
          ```
          최빈값으로 대체되는 열과 평균으로 대체되는 열을 각각 적용해주어 DataFrame을 다시 만들어준다.

        2. 데이터 결합
            - `pdf.concat([Train_X_cate, Train_X_cont], axis=1)`: Famhist 열과 다른 열들의 데이터를 다시 결합해준다. Test 데이터에 대해서도 동일하게 수행한다.


## 시계열 결측치 대체
- 시계열 변수인 경우 결측이 바로 이전 값 혹은 이후 값과 유사할 가능성이 높기 때문에 근처값으로 대체한다.
- `df.fillna(value, method)`: value는 결측치를 대체할 값, method는 결측치를 대체할 방법
  - method 중 `ffill`은 결측치 이전의 *유효한* 값 중 가장 가까운 값으로 채우는 것이고 `bfill`은 결측치 이후의 유효한 값 중 가장 가까운 값으로 채우는 것이다.
- **시간 순서대로** 나타나는 시계열 데이터이기 때문에 train_test_split으로 임의 분할한 경우에는 적용할 수 없다.
- 이전의 결측치 대체와 다르게 시계열 결측치는 *유일하게* 분할 이전에 결측치 대체가 가능하다.
- `df.fillna(method='ffill').fillna(method='bfill')`: 결측 데이터 전후의 데이터를 모두 살핀다.


## 결측치 예측 모델 활용
> 결측이 발생하지 않은 컬럼을 바탕으로 결측치를 예측하는 모델
> - 결측이 소수의 컬럼에만 쏠려있으면 안됨
> - 특징 간에 관계가 존재해야 됨

- `sklearn.impute.KNNImputer` 결측 예측 모델: 결측이 아닌 값만 사용해서 이웃을 구하고 이웃값들의 대표값으로 결측을 대체한다.

```
# v1의 결측치(c,d) - v2로 이웃을 결정
plt.grid()
plt.scatter([3,3,3,3,3], df_temp['v2'])
for i in range(0, 5):
    plt.annotate(df_temp.index[i], (3,df_temp['v2'][i]))
```
- 위에 `annotate`는 pyplot에서 주석을 달기 위함인데 각 점에 df_temp.index[i] 값을 주석으로 달아주고 (3,df_temp['v2'][i])는 좌표를 뜯한다. 따라서 x좌표가 다 3이고 y좌표가 v2값들이면, v1의 결측치(c,d)를 v2의 이웃들로 대체할 수 있다. (*반대로 v2의 결측값도 v1의 이웃으로 대체한다.*)

#### KNNImputer
- `ki = KNNImputer(n_neighbors=5, weights='distance')`: 객체 인스턴스 설정(n_neighbor는 이웃의 범위 수이다.)
- `ki.fit(Train_X)`를 통해 이웃을 결정한다.
- `pd.DataFrame(ki.transform(Train_X), columns=Train_X.columns)`: 가까운 이웃 값을 이용해서 결측치를 변환해준다.

## 범주형 변수 처리
> 범주형 데이터는 종류를 표시하는 데이터로 카테고리형 데이터라고도 불린다.

<범주형 변수 변환 방법>
- 인코딩과 디코딩
  - **인코딩** : 사람이 인지할 수 있는 문자를 규칙에 따라 컴퓨터가 이해하는 언어로 바꾸는 것
  - **디코딩** : 인코딩 된 데이터를 다시 원본 데이터로 디코딩한다.

1. **더미화**
   1. 레이블 인코딩
      - 해당 범주별로 가중치를 다르게 주려고 사용함
      - `from sklearn.preprocessing import LabelEncoder`
      1.  객체 인스턴스 `encoder = LabelEncoder` 생성
      2.  `encoder.fit(items)`, `encoder.transform(items)` 적용하여 **a~z, 가~하 순으로 items list를 정렬하고 앞에서부터 labele을 생성**한다.
      3.  `encoder.classes_`: 인코딩된 문자열 값 목록을 저장한다.
      4.  `encoder.inverse_transform([0, 1, 2])`: 인코딩된 데이터를 디코딩하는 것으로 index 0, 1, 2에 해당하는 문자열을 반환한다.
   2. 원핫인코딩(OneHotEncoder)
      1. 레이블 인코딩에서 `encoder.transform(items)` 값을 `labels=encoder.transform(items)`로 정의하고 `labels.reshape(-1,1)`을 사용하여 2차원 데이터를 생성한다.
      2. **원핫 인코딩: `from sklearn.preprocessing import OneHotEncoder`**을 적용한다.
      3. 객체 인스턴스 `one_encoder = OneHotEncoder()` 생성
      4. `one_encoder.fit(labels)`, `one_labels = one_encoder.transform(labels)` 적용하여 더미컬럼 생성 (더미컬럼 one_labels는 출력했을 때 나오는 셀을 제외한 셀들을 0으로 반환한다.)
      5. `print(one_labels.toarray())`: 전체 셀을 2차원 배열로 반환한다.
      6. ### Pandas의 df.get_dummies() method
        - 원핫 인코딩을 수행하고 라벨인코딩 없이 바로 변환한다.
        1. `df = pd.DataFrame({'items':items})`
        2. `pd.get_dummies(df)`를 통해 items의 값(열)들과 labels(행)으로 더미테이블을 생성한다.
            - columns에 대해서 0 또는 1을 개별적으로 할당한다.
2. **연속형 변수로 치환**
   - 더미화의 차원 문제가 발생할 때 사용
   - 각 범주형 변수들의 레벨에 따른 종속형변수의 빈도값을 기준으로 변환한다.
  
   ```
   X = df.drop('Class', axis=1)
   y = df['Class']
   # Class 특징은 'negative'와 'positive'의 두 문자 라벨값을 가지고 있다.

    # 따라서 문자 라벨값을 숫자로 변환해준다.
   Train_y.replace({"negative":-1, "positive":+1}, inplace=True)
    Test_y.replace({"negative":-1, "positive":+1}, inplace=True)
   ```
   1. 위와 같이 문자 라벨값을 숫자로 변환해준다.
   2. 목적변수로 진행해야 하기 때문에 학습데이터와 목적변수를 다시 결합한다.
        - `train_df = pd.cocat([Train_X, Train_y], axis=1)`
   3. 결합한 테이블에 각 컬럼들의 값들의 종류별 개수를 반환한다. 예를 들어 Buying이라는 컬럼에 med, high, low라는 값이 반복되면, 각각의 값이 몇번 등장하는지 센다.
        - `for idx in train_df.columns:
    print(train_df[idx].value_counts())`
    4. 위의 값들을 가지는 컬럼을 **범주형 변수**라고 하는데, 각 범주의 빈도가 차이가 많이 나지 않으며 범주에 대응하는 목적변수 값의 평균을 이용해서 범주형 변수를 대체한다.
        - 즉, 예를 들면 med,high,low는 범주들이고 이 값들을 가지는 Buying column이 범주형 변수이다.
        - 이 때, 목적변수는 Class라는 column이다. Class column은 1또는 -1로 나타나고 있다.
        - Buying column에 med 범주가 167개 있고, med를 가지는 행의 Class 값들을 봤더니 -1값이 162, 1이 5개씩 있다면 Buying column의 'med'를 Class 값들의 평균인 -0.9491197...로 대체하여 연속형 변수로 대체하는 것이다.
        - `train_df.groupby('Buying')['Class'].mean().to_dict()`를 `tmp_dict`로 정의하자. 이는 med, low, high 범주를 이용한 위와 같은 Class 값 평균을 dictionary 형태로 나타난다.
        - `train_df[['Buying']].replace(tmp_dict)`로 범주형 데이터들을 연속형 변수로 변환한다.