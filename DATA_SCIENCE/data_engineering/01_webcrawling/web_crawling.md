# 웹 데이터 수집(크롤링)
> 1. urllib 패키지: url을 넘겨주면 데이터를 텍스트 형태로 반환
>   - urlopen(), read()
> 
> 2. BeautifulSoup 패키지: find()/findAll()

## 1. urllib 패키지를 사용해서 소스 추출
```
from urllib.request import urlopen

url = "http://www.nate.com"
html = urlopen(url)

html.read()
```
## 2. 문서에서 원하는 내용 추출(Parsing)
- BeautifulSoup library 사용
```
import bs4

# 소스코드와 파서기가 있고 bs4 모듈을 사용할 수 있는 객체 생성
bs_obj = bs4.BeautifulSoup(html, 'html.parser')

# html 소스코드를 가독성 좋게 표현
print(bs_obj.prettify())
```

- 원하는 내용 추출하기
1. find(태그, [{속성명: 속성값}])
2. findAll(태그, [{속성명: 속성값}]): find_all과 같