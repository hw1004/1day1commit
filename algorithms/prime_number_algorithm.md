# 소수 판별 알고리즘(Prime Number Algorithm)

- 소수: 1보다 큰 자연수 중 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수

```
def prime_number(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
```
- 위의 알고리즘은 2부터 n-1까지 판별해야하기 때문에 시간 복잡도가 O(X)이다.


## 약수의 성질
- 모든 약수는 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룬다.
- 자연수의 모든 약수를 찾을 때 가운데 약수까지만 확인하여도 된다.

<약수의 성질을 이용해서 개선된 알고리즘>
```
import math

def advanced_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
```

- 2부터 n의 제곱근까지의 모든 자연수에 대해 연산을 수행하기 때문에 시간 복잡도는 O(N^(1/2))이기 때문에 시간 복잡도가 줄어든다.


## 다수의 소수 판별
- 특정한 수의 범위 내에 존재하는 모든 소수를 찾아야 할 때!

### 에라토스테네스의 체 알고리즘
1. 2 ~ n까지의 모든 자연수 나열
2. 남은 수 중 아직 처리하지 않은 가장 작은 수 i(소수) 2부터 시작되게 된다!
3. 남은 수 중 i의 배수 모두 제거
4. 2, 3번 반복

```
import math

def range_prime_number(n):
    array = [True] * n
    for i in range(2, int(math.sqrt(n)+1)):
        if array[i] == True:
            for j in range(i+1, n):
                if j % i == 0:
                    array[j] = False
    for i in range(2, n+1):
        if array[i]:
            print(i)

```

 - 선형 시간에 가까울 정도로 빠름. 시간 복잡도 O(NloglogN)
 - 하지만 범위 내 모든 자연수의 소수 여부를 저장해야 하기 때문에 메모리가 많이 필요함.

