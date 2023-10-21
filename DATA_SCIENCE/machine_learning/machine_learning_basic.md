# 머신러닝 개요
> Machine Learning(기계학습)이란 컴퓨터 프로그램이 **데이터와 처리 경험**을 이용한 학습을 통해 정보 처리 능력을 향상시키는 것에 대한 연구 분야이다.
> *(ex)자율 주행 자동차, 필기체 문자 인식*
> 사례: 이미지 분류, 텍스트 분류(자연어 처리), 텍스트 요약, 자연어 이해, 예측, 음성 인식, 이상치 탐지, 군집 작업, 데이터 시각화, 추천 시스템, 강화 학습 등

## 머신러닝의 주요 알고리즘
1. **확률적 모델링**
   - 초창기 머신러닝의 형태
   - 통계학 이론을 데이터 분석에 응용
   - 로지스틱 회귀
2. **신경망**
   - 1세대: Perceptron
   - 2세대: Multilayer Perceptron, Back Propagation
   - 3세대: Boltzmann Machine, ReLU, Dropout, Local Minima 
3. **커널(Kernel)**
   - 분류 알고리즘
   - 컴퓨터 운영체제의 핵심이 되는 컴퓨터 프로그램
   - 서포트 벡터 머신
4. **결정 트리**
   - 랜덤 포레스트
   - 그래디언트 부스팅

## 머신러닝의 종류
|machine learning method|description|algorithms|
|---|---|---|
|Supervised Learning|Task Driven(Regression/Classification) - (ex)scatter plot|KNN, Linear regression, Logistic Regression, Support Vector Machine, Decision Tree, Random Forest, Neural Network|
|Unsupervised Learning|Data Driven(Clustering/decrease dimension) - (ex)cluster graph|Clustering, 시각화와 차원축소, 이상치 탐지, 연관 규칙(Association rule)|
|Reinforcement Learning|Algorithm learns from mistakes|
|데이터 비교|새로운 샘플과 훈련 샘플들의 비교|
|모델 기반|방정식이나 특정 모델을 가지고 비교|

## Machine Learning Workflow!!
1. collect data
2. Prepare data (데이터 전처리)
3. Split data
4. Train a model
5. Test and validate a model
6. Deploy a model
7. Iterate

## 머신러닝에서 사용되는 주요 패키지
|package|description|
|---|---|
|Scikit-Learn|machine learning|
|Numpy|array, linear algebra, statistics package|
|SciPy|array, linear algebra, statistics package|
|Pandas|python data analysis(데이터 핸들링)|
|Matplotlib|Visualization|
|Seaborn|Visualization|
|Tensorflow|Deep learning|
|Keras|Deep learning|

## 머신러닝, 딥러닝, 인공지능
|term|description|
|---|---|
|Deep Learning|머신러닝의 하위 집합, 신경망을 기반으로 특정 작업을 기계 스스로 학습하는 기법|
|Machine Learning|인공지능의 하위 집합이며 딥러닝을 포함, 기계가 *경험*을 바탕으로 스스로 개선해 가는 기법|
|Artificial Intelligence|머신러닝 포함, 컴퓨터가 인간의 지능을 흉내 낼 수 있게 하는 모든 기술|

## 머신러닝의 장점
- 많은 수동 조정과 규칙이 필요한 문제에 대해 머신러닝 모델이 코드를 간단하게 만듦
- 전통적인 방식으로 해결할 수 없는 복잡한 문제에 대해 해결 방법을 제시할 수 있음
- 머신러닝 시스템은 유동적으로 새로운 데이터에 적응할 수 있다.

