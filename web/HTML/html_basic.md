# HTML
> HTML(Hyper Text Markup Langauge)는 웹페이지에 content를 부여하고 그 content를 어떻게 구조화할건지를 웹 브라우저에 지시한다.

## Attribute
요소의 성질, 특징
![attribute](https://poiemaweb.com/img/html-attribute.png)

## Basic HTML elements

|HTML element|설명|비고|
|---|---|---|
|`<!-- comments -->`|comments를 다는 역할을 한다. 코드가 아닌 comment로써 역할을 가지고 있다.||
|`<html>`|html 문서의 모든 content/구조 들이 포함된다.||
|`<head>`|html 문서의 metadata를 포함한다. (title, style, script, stylesheet link 등)|`<html><head>Metadata</head></html>`|
|`<title>`|html 문서의 title 지정(웹 브라우저에서 열 때 탭의 제목으로 보여짐)|`<head>` 내에서만 포함될 수 있음|
|`<body>`|HTML 문서의 content를 대표한다.|
|`<h1>`|h1부터 h6까지 있고 제목을 지정할 때 사용된다.|`<h1 id="A1>`는 제목에 id를 지정해준다.|
|`<p>`|text block을 하나의 paragraph로 지정|`<p id="paragraph 1"`는 paragraph에 id를 지정해준다.|
|`<div>`|section을 나눈다.|`<div id="intro">`는 section명을 지어준다.|
|`<span>`|같은 paragraph 내에서 작은 content를 다른 개별적인 content로 구별/표기하는 것||
|`<em>`|글자 기울여서 강조|
|`<strong>`|글자 굵게 해서 강조|
|`<br>`|line break (paragraph 내에서 줄 바꾸기)|종료 태그 없음|
|`<hr>`|horizontal line 추가|
|`q`|인용부호(quotation mark)|인용할 부분을 `""`으로 감싼다.|
|`blockquote`|긴 인용문 들여쓰기|
|`<ul>`|unordered list||
|`<ol>`|ordered list||
|`<li>`|list의 각 요소들 작성할 때||
|`pre`|preformatted(형식화된) text 지정|특정 content는 html 문서에서 작성된 그대로 브라우저에 표시됨|
|`<img src="#" />`|이미지 주소 src, alt(alternative text)에 이미지 파일이 없을 경우 표시되는 문장 삽입, width와 height로 이미지 크기 지정|`<img src="#" alt="설명" width="100" height="100">`|
|`<video src="#" width="100" height="100" controls>`|video 주소 src|`<video src="#" width="100" height="100" controls> Video not supported </video>` 해당 비디오가 load 안되면 `Video not supported`를 내보인다.|
|`id`|고유하게 지정하는 것|문서전체에서 유일무의하게 지정해야 하기 때문에 중복 X|
|`class`|그룹으로 묶어서 지정할 때 쓰는 것|CSS 스타일 지정할 때 사용됨|
|`lang`|요소의 언어를 지정함. 검색엔진 크롤링 시 언어를 인식할 수 있게 함|예시: 크롬의 자동번역 interface/ `<html lang="ko-KR>`|
|`style`|요소에 인라인 스타일 지정|
|`script`|client-side scripts(ex javascript)를 정의할 때 사용|`<script src="main.js>`를 사용하면 외부 Js 파일 로드 가능|
|`meta`|메타데이터(구조화된 데이터) 정의에 사용됨|`<meta name="keywords" content="HTML, CSS, XML, XHTML, JavaScript>`|

## Link
|tag|설명|비고|
|---|---|---|
|`<a href="http://~">`|하이퍼링크 생성|`<a href="http:/~><img src="logo.jpg">Click this image</a>`와 같이 이미지를 클릭하면 해당 링크로 이동할 수 있게 설정할 수 있음|
|`_blank`|`target="_blank"`를 추가하면 링크가 브라우제에서 새로운 탭에 열도록 설정할 수 있다.|
|`rel="noopener noreferrer"|`"_blank"`를 사용하면 보안 취약점(Tabnabbing 피싱 공격)이 있기 때문에 대비하기 위한 관계 정의|
|`_self`|`target="_self"`을 설정하면 연결문서를 현재 브라우저에서 열 수 있다.|기본값이다.|
|`#`|하이퍼링크 `<a>`로 생성 시 같은 HTML 문서의 특정 paragraph나 부분으로 이동하게 설정하고 싶으면 `#`에 id를 붙여서 설정하면 된다.|`<a href="#id">`|
|`link`|외부 리소스와의 연계 정보 정의(HTML과 외부 CSS 파일 연계할 때 사용됨)|`<link rel="stylesheet" href="./style.css">`/`rel`은 relationship을 뜻하며 현재 문서와 연결한 파일의 관계를 설명함|
|`./`|현재 작업 중인 파일에 위치한 파일(directory)|
|`../`|현재 작업 중인 파일(directory)의 부모 directory|
|fragment identifier|페이지 내부 이동 방법|제목을 `<h1 id="top">`로 id 지정을 해놓았다고 가정하면 `<a href="#top">`을 통해 제목으로 이동 가능하다|

## form tag
> form tag는 사용자가 입력한 데이터 수집을 위해 사용된다.

```
<!DOCTYPE html>
<html>
  <body>
    <form action="http://jsonplaceholder.typicode.com/users" method="get">
      ID: <input type="text" name="id" value="1"><br>
      username: <input type="text" name="username" value="Bret"><br>
      <input type="submit" value="Submit">
    </form>
  </body>
</html>
```
|attributes|설명|비고|
|---|---|---|
|action|입력한 데이터가 전송될 url을 지정한다.|
|method|입력 데이터의 전달 방식을 지정한다.|`method="get"`으로 지정 시 url에 입력한 데이터를 쿼리스트링으로 보내는 방식임/ `method="post"` 으로 지정 시 request body에 담아 보내는 방식임|

### input
```
<input type="button" value="Click me" onclick="alter('Hello World!')">
# Click me를 누르면 'Hello world' 창의 위에 뜬다.
```
|input type attribute value|설명|
|---|---|
|button|버튼 생성|
|checkbox|체크 박스|
|color|컬러 선택할 수 있음|
|date|년, 월, 일|
|datetime|년, 월, 일, 시, 분, 초|
|datetime-local|지역 년, 월, 일, 시, 분, 초|
|email|이메일 입력 form(submit 시 자동 검증)|
|file|파일 선택|
|hidden|감추어진 입력 form 생성|
|image|submit button을 이미지로|
|month|월 선택|
|number|숫자 입력|
|password|비밀번호 입력|
|radio|보기 중 선택하는 button|
|range|범위 선택|
|reset|초기화 button|
|search|검색어 입력|
|submit|제출 button|
|tel|전화번호 입력|
|text|텍스트 입력|
|time|시간 선택|
|url|url 입력|
|week|주 선택|

#### textarea
> 여러 줄의 글자를 입력할 때 크기가 큰 text창을 만든다.

`<textarea name="message" rows="10" cols="30">` : row와 column에 들어갈 글자 수를 지정

#### button
> `<input type=button>`은 빈 tag이지만 `<button>` tag는 요소에 텍스트나 이미지 같은 콘텐츠를 사용할 수 있다.


### select
1. 보기 선택 form을 직접 클릭해서 확인/선택
   
|tag|설명|비고|
|---|---|---|
|`select`|보기 선택 form 생성|
|`option`|각각의 보기 생성|`<option value="a">` value는 보기의 내용|
|`selected`|기본 선택되어 있는 값|
|`disabled`|선택하지 못하게 설정|

2. 보기의 개수만큼 보기 선택 form이 열어져 있음

`<select name="2" size="4" multiple>` : 보기가 4개이기 때문에 보기 4개가 한번에 보여질만큼의 보기 선택 form이며 `multiple`을 통해 두 개 이상의 보기를 선택할 수 있게 지정한다.
- `multiple`은 불리언 값이며 기본값은 true이다.

3. 보기 선택 form을 직접 클릭해서 확인/선택하는데 보기의 내용을 두 집합으로 나눠야 할 때

`optgroup label="Cake"` : 특정 보기들을 Cake이라는 그룹으로 묶는다. 특정 보기들의 위에는 Cake이라는 설명이 들어간다.  

### fieldset
> 여러 input form을 하나의 집합으로 묶기 위해 사용

`<fieldset>`으로 묶고 `<legend>`를 통해 집합명을 표시하고 `Username <input type="text" name="username"`과 같이 집합에 들어갈 input form들을 지정한다.


## Text-formatting
- tag 또는 다른 tag 내의 style 요소를 통해 text-formatting 가능

|tag|설명|비고|
|---|---|---|
|`<b>`|bold체 지정(강조)|non-semantic|
|`<i>`|italic체 지정(강조)|non-semantic|
|`<strong>`|bold체 지정(웹표준에 바람직)|semantic|
|`<em>`|italic체 지정|semantic|
|`<del>`|가로줄을 표시하여 삭제 표시|
|`<ins>`|밑줄을 칠 inserted(added) text 지정|
|`<small>`|text 내의 특정 부분을 작은 text로 지정|
|`<mark>`|text 내의 특정 부분을 highlight한다.|
|`<sub>`|아래에 쓰인 text 지정|
|`<sup>`|위에 쓰인 text 지정|


## HTML Table
|HTML element|설명|비고|
|---|---|---|
|`<table>`|`<body>` 내에 table 생성할 때|
|`<thead>`|`<table>`내에서 head에 해당하는 `<tr>`들을 담는다.|`<table><thead><tr><td>`|
|`<tbody>`|`<table>`내에서 head와 root를 제외한 body에 해당하는 `<tr>`들을 담는다.|`<table><tbody><tr><td>`|
|`<troot>`|`<table>`내에서 마지막 root에 해당하는 `<tr>`들을 담는다.|`<table><troot><tr><td>`|
|`<tr>`|row|
|`<td>`|`<tr>`안에 사용되어 각 row에 해당하는 columns(data)|`<tr><td>14</td><td>20</td></tr>`|
|`<th>`|heading 부분 지정|`<th scope="col">Col1</th>` col이나 row를 통해 heading을 지정하려는 row/column을 지정|
|`<table border="1">`|테이블 테두리 생성|테두리 두께 지정|
|`<td colspan="2">`|같은 row에 있는 2개의 data를 병합|`<td colspan="2">14</td>`에서는 14가 병합된 부분에 들어갈 값이다.|
|`<td rowspan="2">`|같은 column에 있는 2개의 row data 병합|병합 안된 부분은 순서에 따라 순차적으로 추가한다.|

## Structure
`header, nav, aside, section, article, footer`을 통해 웹페이지 레이아웃을 나눈다.

![structure](https://poiemaweb.com/img/building-structure.png)

## Semantic Web
- **웹사이트**는 **검색엔진**에의 노출이 매우 중요하다.
- SEO(Search Engine Optimization): 검색엔진이 본인의 웹사이트를 검색하기 알맞은 최적의 구조
- **크롤링**: 검색엔진이 Robot을 통해 전세계의 웹사이트 정보 수집하는 행위
- **인덱싱**: User가 검색할 만한 키워드를 미리 예상해서 검색 키워드에 대응하는 **인덱스**를 만드는 행위(행위 주체: **인덱서**)
### Semantic element
> 검색 엔진이 HTML 코드만으로 의미를 인지해야 하는데, 이때 해석하는 것이 **시맨틱 요소**(Sementic elemet)이다.

```
# 의미론적으로 아무 의미 X
<font size="6"><b>Hello</b></font>
# header 중 가장 상위 레벨이라는 의미
<h1>Hello</h1>
```
요소의 의미가 명확히 드러나는 것의 중요성
- 코드의 가독성 상승
- 유지보수 쉬워짐

#### `meta` Tag 활용
|meta tag|설명|
|---|---|
|`<meta name="keywords" content="HTML, CSS">`|SEO를 위해 keywords 정의|
|`<meta name="description" content="Search Engine Optimization">`|웹페이지의 설명 정의|
|`<meta name="author" content="John Doe">`|웹페이지 저자|
|`<meta http-equiv="refresh" content="10">`|웹페이지를 10초마다 refresh한다.|


#### 시맨틱 태그(Semantic Tag)
> 브라우저, 검색 엔진, 개발자 모두에게 *콘텐츠의 의미*를 명확히 설명하는 역할

![시맨틱 태그](https://poiemaweb.com/img/building-structure.png)

|semantic tag|설명|
|---|---|
|`nav`|네비게이션 의미, `<ul>`, `<li>`태그와 메뉴를 만들 때 사용하는 것이 일반적|
|`aside`|본문 내용과 분리되는 내용을 사이드에 위치하는 공간에 배치할 때 사용|
|`header`|도입부 또는 nav 링크의 집합이 들어감|
|`section`|article을 포함하는 공간|
|`article`|본문의 주내용이 들어가는 공간|
|`footer`|저자 정보, 저작권 정보, 연락처, 연관 페이지 등 가장 아래에 올 내용들을 포함|



#### 시맨틱 웹(Semantic Web)
> 수많은 웹페이지들에 **Metadata**(데이터에 관한 표준화되고 구조화된 데이터)를 부여하여 웹페이지를 단순한 데이터의 집합이 아닌 **의미와 관련성**을 가지는 데이터베이스로 구축하는 웹 개념

|non-semantic 요소|semantic 요소|
|---|---|
|content에 대한 설명 X|content에 대한 설명 명확|
|div, span|form, table, img|

