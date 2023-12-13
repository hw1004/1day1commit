# 공공데이터 API
> 제공하는 지자체, 정부마다 접근 url이 상이하다. 따라서, 요청 변수를 확인하고 사용해야 한다.

1. 변수명과 파라미터명을 매칭시켜서 파라미터 값을 설명한다.
```
QT = '1' # 약국 영업 요일 전달
QN = quote('삼성약국') # 검색하고자하는 약국의 이름(부분)
Q0 = quote('서울특별시') # 광역시도
Q1 = quote('강남구') # 시군구
ORD = 'NAME' # 정렬기준
numOfRows = '10' # 추출 data 수

paramset = '?servicekey='+servicekey + \
           '&QT='+QT + \
           '&QN='+QN + \
           '&Q0='+Q0 + \
           '&Q1='+Q1 + \
           '&ORD='+ORD + '&numOfRows='+numOfRows
paramset
```
- paramset는 사용할 파라미터 값들만 이용해서 구성할 수 있음

2. 접근 url에 파라미터 셋 결합시켜서 불러오기
```
url = (접근 url) + paramset

result = requests.get(url)
bs_obj = BeautifulSoup(result.content, 'html.parser')
```

3. bs_obj 확인 후 태그로 원하는 데이터 불러오기
```
bs_obj.findAll('item')[0].dutyname.text
# 'E-삼성약국'
```

4. 조건을 주어서 조건에 맞는 데이터를 불러올 수 있다.
- 특정 태그의 값이 2100 이상인 데이터들에 한해서만 데이터들을 불러올 수 있다.
- 불러온 데이터에 대해 이름, 주소, 전화번호 정보가 있다고 할 때, 3개의 정보의 데이터 개수가 동일해야 한다.
- 확인 후 데이터 프레임으로 생성한다.


## linux 환경에서 matplotlib 그래프 한글 설정
```
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

[f.fname for f in fm.fontManager.ttflist]

plt.rcParams["font.family"] = 'D2Coding'
plt.rcParams['font.size'] = 12.
```



