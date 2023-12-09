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
   - `bs_obj.find('div', {'class': 'reply'}).text`: class값이 reply인 div 태그 반환
   - `bs_obj.find('div', {'id': 'mainMenuBox})`: id가 mainMenuBox인 div 태그 반환 (아이디는 유일하기 때문에 `bs_obj.select('#mainMenuBox')`처럼 태그 명시하지 않아도 됨)
2. findAll(태그, [{속성명: 속성값}]): find_all과 같음
   - `bs_obj.find_all('li', {'class': 'reply'})`
3. 첫번째 태그를 기준으로 다음 태그 반환
   - `bs_obj.find('p').next_sibling`
4. 태그의 속성값 추출
   - `bs_obj.find('a')['href']`: a 태그의 href 속성값 추출
5. 특정 태그를 모두 찾아서 list로 반환
   - `bs_obj.select('a')`: a 태그 모두 찾아서 list로 반환

- css 선택자
  - 태그 선택자: 태그명
  - id 선택자: #id값 (ex. p #id)
  - class 선택자: .클래스 값 (ex. div .first)
  - 자식 선택자(`>`): 바로 아래 선택자 (ex. div .first > ul)
  - 자손 선택자(공백문자): 모든 아래 선택자 (ex. div .first ul)