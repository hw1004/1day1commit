## 입력과 출력
`print('a', 'b', 'c')`: 공백 하나로 이어서 출력 (a b c)

`print('a', 'b', 'c', sep = " and ")`: sep로 지정된 문자열로 이어서 출력 (a and b and c)

`print("James is my friend.\nHe is Korean.")`: 출력하고자 하는 문자열 내에 "\n"이 포함되어 있으면 그 뒷 문장을 한 줄 내려서 출력

`print("Welcome to ", end = "")`: 줄바꿈 없이 출력됨


### 형식 지정 출력
`print("%type %type" % (data1, data2))`: %type에서 type은 문자열일 때 s, 정수이면 d or i, 실수이면 f or F으로 표기한다. %type에 문자열 뒤로 오는 data들을 순서대로 type에 맞게 대입한다. 
```
name = '혜원'
print('%s은 저입니다.' % name)   # 혜원은 저입니다.
```
`print("Animal: {1}, {2}, {0}".format(animal0, animal1, animal2))`: index 순서대로 출력되어 index 1, 2, 0에 해당하는 animal1, animal2, animal 0 순서대로 출력 # Animal: animal1, animal2, animal0 이 출력된다.

`print("Animal: {}, {}, {}".format(animal0, animal1, animal2))`: 순서 상관없이 순차적으로 출력하고 싶으면 {} 안에 아무것도 넣지 않아도 된다. # Animal: animal0, animal1, animal2 가 출력된다.

##### 숫자 출력 형식 지정
`print("{0:.2f}, {0:.5f}".format(a))`: 숫자 형식 a에서 2번째 자리수까지, 5번째 자리수까지 반올림해서 출력 # a = 0.123456789이면 0.12, 0.12346이 출력됨

### 파일 읽고 쓰기
`f = open('file_name', 'mode')`: file_name을 가진 파일을 속성 mode를 설정하여 연다.
- mode

|mode|의미|
|---|---|
|r|읽기 모드(기본 설정값)|
|w|쓰기 모드(같은 이름의 파일이 있으면 기존 내용 모두 삭제됨)|
|x|쓰기 모드(같은 이름의 파일이 있으면 오류)|
|a|추가 모드(같은 이름의 파일이 없을 때 w와 같은 역할)|
|b|바이너리 파일 모드|
|t|텍스트 파일 모드(기본 설정값)|

- 파일 쓰기(mode w로 지정)

`f.write(str)`: 문자열 형태로 문자열 작성 가능(str 안에 쓰고자 하는 문자열 삽입)

`f.close()`: 파일 닫기

- 파일 읽기(mode r로 지정)

`data = f.read()`: 파일 내에 있는 내용들을 변수 data에 저장 (f.close()한 후에 print(data)로 읽기 가능)

**`readline()`**: 파일에서 내용을 한줄씩 읽는 방법

**`readlines()`**: 파일에서 내용 한줄을 리스트의 한 요소로 넣어서 모든 내용에 적용한 후 하나의 리스트 반환


