# 신경망을 위한 데이터 표현
## 텐서 (tensor)
- 다차원 넘파이 배열
- 머신러닝의 기본적인 구성 요소
- 숫자 데이터를 위한 컨테이너
- 임의의 차원(축) 개수를 가지는 행렬의 일반화된 모습
- `s=np.array(12)`로 scalar을 지정하고 `s.ndim`을 수행하면 **축의 개수**인 0을 반환한다.


1. 축의 개수: `.ndim`
2. 크기(shape): 0, (5,), (3,5), (3,5,5)처럼 텐서의 크기를 알 수 있다.: `.shape`
3. 데이터 타입: float32, uint8, float64 등이 될 수 있으며 numpy 배열은 가변 길이의 문자열은 지워하지 않는다.


![](https://blog.kakaocdn.net/dn/qS1NF/btqubStze09/5sbnC8DVd3aQsUULgjv6Kk/img.png)

|type|rank|example|description|
|---|---|---|---|
|scalar|0|[1]|하나의 숫자 / float32, float64 타입의 숫자|
|vector|1|[1,1]|숫자의 배열|
|matrix|2|[[1,1], [1,1]]|행(첫번째 축)과 열(두번째 축)|
|3-tensor|3|[[[1,1], [1,1]], [[1,1], [1,1]], [[1,1], [1,1]]]| 행렬들을 하나의 새로운 배열로 합침|
|n-tensor|n|위처럼 차원을 확장시킴|

