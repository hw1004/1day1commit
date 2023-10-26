# 생선 분류 문제
두 종류의 생선에 대해서 각 생선이 가지고 있는 특징을 **feature**이라고 한고 이를 변수로 사용한다.

<변수의 종류>
- **독립변수**: 종속변수의 원인들임
- **종속변수**: 예측해야 하는 대상

## K-최근접 이웃 알고리즘
> K-Nearest Neighbor (K-최근접 이웃 알고리즘)은 test data K개와과 train data들의 y값을 비교하는 알고리즘이다. 

- 분류: k개 최근접 이웃들의 class들 중 다수결 결과로 class 예측
- 회귀: k개 최근접 이웃들이 가지고 있는 값의 평균을 결과값으로 예측

![k-최근접 이웃 알고리즘](https://t1.daumcdn.net/cfile/tistory/9978A4425DB04A2B18)

- 모수 방식: 정규분포와 이항분포 등 알려진 확률분포를 기반으로 모수를 추정한다.
- 비모수 방식: 알려진 확률분포 기반이 아닌 다른 방식으로 모수를 추정한다.


## Scikit-learn package
> 파이썬 머신 러닝 패키지 중 가장 많이 알려진 패키지로 머신러닝 알고리즘 사용법을 배우게 됨
> 학습 데이터를 모두 저장하고 있다가 새로운 데이터가 들어오면 새로운 데이터로부터 직선 거리에 어떤 데이터가 있는지 확인만 하면 된다.
> 하지만 데이터를 보관하기 위해서는 아주 많은 메모리가 필요하고 새로운 데이터와 기존 학습 데이터 사이의 거리 계산에 많은 시간이 소요된다.

- 다양한 분류, 회귀, 서포트 벡터 머신, 랜덤 포레스트, 그라디언트 부스팅, k-평균, DBSCAN 등 클러스터링 알고리즘을 라이브러리로 가지고 있음
- Numpy와 Scipy와 함께 운용되도록 설계되었음
- 사이킷런 모델 알고리즘은 **2차원 데이터**를 요구한다. 따라서 데이터는 2차원 리스트 형태로 준비해야 한다.


- `!pip install scikit-learn`: 사이킷런 패키지 install
- `from sklearn.neighbors import KNeighborsClassifier`: 사이킷런의 K-최근접이웃 클래스 import
- **`kn = KNeighborsClassifier()`**: k-최근점이웃 클래스의 객체를 생성하며 kn을 통해 모든 속성과 메서드를 이용할 수 있다.
  - `kn49 = KNeighborsClassifier(n_neighbors=49)`: 몇개의 가까운 데이터를 참고하는지의 기준을 정하기 위해 `n_neighbors`를 사용한다.
  - **하이퍼 파라미터**: `n_neighbors`처럼 모델링을 하는 사람이 설정할 수 있도록 하는 파라미터
- **`kn.fit(fish_data, fish_target)`**: 데이터와 정답 데이터를 kn class에 저장
- **`kn.score(fish_data, fish_target)`**: 정답 데이터가 원본 데이터와 비교했을 때 얼마나 정확한지 정확도를 알려는 모델 평가이다.
  - **정확도**: 정확히 맞힌 개수 / 전체 데이터 수
- **`kn.predict([[30, 600], [50, 550]])`**: 데이터가 빙어인지 도미인지 예측하는 함수로 2차원의 새로운 데이터를 받아 이전에 생성한 모델을 바탕으로 새로운 데이터를 예측한다.
- `kn._fit_X`: 학습에 사용한 test data를 모델에 가지고 있음
- `kn._y`: 학습에 사용한 결정값인 target data를 모델에 가지고 있음

### 위의 방식은 정답을 알려주고 시행하는 것과 같다.
- `zip(fish_length, fish_weight)`: 여러개의 순회 가능한 객체를 인자로 받고 튜플 형태로 차례로 접근할 수 있는 반복자 반환
- 올바른 훈련데이터와 테스트데이터 구성하기
  - `input_arr = np.array(fish_data)`: numpy를 np로 import하고 데이터를 넣으면 배열 형태로 데이터가 만들어진다.
  - `input_arr.shape`: 데이터의 수와 몇차원인지 튜플 형태로 출력한다.
  - `np.random.seed(42)`: seed를 42로 고정하여 한 번 출력한 random 값을 고정한다.
  - `index = np.arrage(49)`: 0부터 48까지의 일련되 수를 index로 지정한다.
  - `np.random.shuffle(index)`: index에 있는 섞는다. (순서를 뒤죽박죽 섞는다.)


## 데이터 전처리
![column_stack, concatenate](https://blog.kakaocdn.net/dn/Kv3wG/btqHjprfZmj/AovG4uJwyTKWPUJkOkIGK1/img.png)
- `np.column_stack((fish_length, fish_weight))`: 두 리스트를 column방향으로 합친다. 2차원 배열로 나타난다.
- `np.concatenate((np.ones(35), np.zeros(14)))`: 35개의 1과 14개의 0이 있는 target 데이터를 생성할 때 사용. row 방향으로 두 리스트를 하나의 배열로 합친다.
- `from sklearn.model_selection import train_test_split`: 사이킷런으로 훈련 데이터와 테스트 데이터 나눌 때 사용
- **`pd.Series()`**: 값과 함께 우리가 원하는 index를 입력할 수 있다.
- `.value_counts()`: 열에 있는 모든 값의 개수를 반환한다.
- `train_test_split()의 stratify 변수`: stratify 값으로는 target 값을 지정해준다. stratify 값을 적용하면 target의 class 비율을 유지한 채로 데이터 셋을 split 하게 된다.
- 찾고자 하는 데이터와 이웃하는 데이터들 찾기!
  - `dist, idx = kn.kneighbors([[25, 150]], n_neighbors=5)`: 기본적으로 `n_neighbors=5`가 default이고 이는 이웃들의 출력 개수가 5개임을 뜻한다. kneighbors를 통해 [25, 150]과 이웃하는 데이터들 5개과 값의 거리 dist와 인덱스 idx를 구할 수 있다.
  - 최근접 알고리즘은 **거리**를 기반으로 가까운 이웃을 결정한다.
- plot에서 축의 범위를 맞춰서 기준 맞추기
  - `plt.xlim((0, 1000))`, `plt.ylim((0, 1000))`
- 열과 행의 값을 기준값으로 결정할 때 `axis`변수를 사용하는데 0은 각 열의 모든 행이고 1은 각 행의 모든 열이다.
- `np.mean()`:평균 구하기 
- `np.std()`: 표준편차 구하기
- `(train_input - mean)/std`: 평균을 0, 분산을 1로 맞추려고 할 때 train_scaled의 값, 스케일된 학습데이터와 일반 테스트 데이터를 비교하면 크기가 다르다.
  - 위에 식으로 스케일링된 학습데이터와 테스트데이터를 학습을 실행한다. `.fit`와 `.score`, 그리고 `.predict`를 이용한다.
  - **스케일링된 데이터가 학습 및 평가에 훨씬 정확함!!**


