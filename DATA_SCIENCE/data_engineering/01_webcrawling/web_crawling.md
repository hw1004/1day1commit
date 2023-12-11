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

- 원하는 내용 추출하기 (웹에서 F12 또는 검사 통해서 소스코드 확인)
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

## 자동화 봇으로 보고 연결 끊는 경우 해결방법
- 통신 규칙상 웹으로의 요청은 브라우저를 통해서 연결하는 것이 약속임
- 소스 코드로 요청하면 서버측에서는 공격으로 인지 할 수 있고 그렇게 되면 해당 서버는 연결을 끊는다.
- **서버에 요청할 때 header를 추가해서 봇이 아님을 증명**
  - header에 브라우저의 종류 추가해서 요청 (User-Agent)
  - 현재 사용중인 브라우저의 정보를 얻어와서 header에 추가
  - 크롬 개발자 도구(F12) > Network > All > 맨 위 > User-Agent

```
headers = {'User-Agent': 
           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
res = requests.get(url, headers=headers)
```

## 3. 추출한 데이터 Dataframe으로 합치기
1. 빈 데이터프레임 생성 후 데이터를 행으로 추가하기
```
# 빈 df 생성
nate_menu = pd.DataFrame({'메뉴':[], '링크':[]})

```
2. 각각의 행을 데이터프레임으로 생성 후 concat으로 결합
```
index = 0
for li in menu_li :
    menu_text = li.text
    menu_link = li.a['href']
    if menu_link == '' or menu_link == 'javascript:;' or menu_text in nate_menu['메뉴'].values :
        continue # 아래 코드 실행하지 않음
    temp = pd.DataFrame({'메뉴':menu_text,'링크':menu_link},index=[index])
    nate_menu = pd.concat([nate_menu, temp])
    index = index +1
```

