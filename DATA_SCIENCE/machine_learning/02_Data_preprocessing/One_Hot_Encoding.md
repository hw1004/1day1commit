# 원-핫 인코딩(One-Hot Encoding)

> **원핫 인코딩**은 피처 값의 유형에 따라 새로운 피처를 추가해 고유 값에 해당하는 컬럼에만 1을 표시하고 나머지 컬럼에는 0을 표시하는 방식이다.

![원핫인코딩](https://miro.medium.com/v2/resize:fit:1200/0*PO_ENSfL80nPRqIg)

- Pandas에서 원-핫 인코딩을 쉽게 지원하는 API로는 **`get_dummies()`** 가 있다.
  - `pd.get_dummies(df)`
  - 원핫인코딩 수행 결과의 행렬을 반환함


1. `from sklearn.preprocessing import OneHotEncoding`
2. `import numpy as np`: 넘파이를 불러온다.
3. `items = np.array(items).reshape(-1,1)`: 2차원 ndarray 형태로 바꿔준다.
4. `oh_encoder = OneHotEncoder()`: 객체 인스턴스 생성
5. fit과 transform으로 원-핫 인코딩을 적용시킨다.
6. `print(oh_labels.toarray())`: 결과적으로 행렬 형태로 반환한다.