# CSS
> CSS(Cascading Style Sheets)는 HTML이나 XML과 같은 구조화 된 문서를 화면에 어떻게 렌더링할 것인지 브라우저에게 설명하기 위한 언어

## CSS 형식
![selector](https://poiemaweb.com/img/css-syntax.png)

- 셀렉터(무엇을)
- 선언블록(어떻게 할 것인지)
  - property(속성)
  - value(속성값)

## HTML과 CSS 연동

|번호|코드|설명|예시|
|---|---|---|---|
|1|`<link rel="" href="">`|HTML에서 외부 CSS파일 로드할 때|`<link rel="stylesheet" href="./style.css">`|
|2|`<style>`|HTML 파일 내부에 CSS 포함할 때 `<head>` 안에 CSS 포함시킴|`<style> h1 {color: red;}`|
|3|`<h1 style="color: red">`|Inline style| 이는 디자인 통일성이 없고 우선순위가 가장 세기 때문에 보통 사용하지 않고 Link style을 많이 사용한다.|

## Selector(셀렉터)
|selector|설명|예시|
|---|---|---|
|`*`|HTML 문서 내의 모든 요소|`* {color: red; }`|
|Tag|지정된 태그|`p {color: red; }`, `h1 {color: pink}`|
|`#ID`|지정된 id 어트리뷰트 값(중복 될 수 없는 유일한 값)|`#p1 {color:red;}`|
|`.class`|지정된 class 어트리뷰트 값|`.container {color:red;}`|
|`selector[Attribute]`|지정된 어트리뷰트를 갖는 모든 요소 선택|`a[href] { color:red; }`이면 `<a href="#">` 형식의 모든 요소 선택|
|`selector[attribute="값"]`| 지정된 어트리뮤트를 가지며 추가적으로 지정된 값을 가지는 모든 요소 선택|`a[target="_blank"]`이면 `<a href="#" target="_blank">` 형식의 모든 요소 선택|
|`selector[attribute ~= "값"]`|지정된 어트리뷰트의 값이 지정된 값을 단어로 포함하는 요소 선택|`h1[title="first"]`이면 `<h1 title="heading first">`와 같이 first를 포함하는 요소들을 선택 단, -first와 같이 공백으로 분리되지 않은 요소는 안됨|
|selector[attribute &#124;= "값"]|지정된 값 or 값- 으로 시작하는 요소 선택|p[lang&#124;="en"] {color:red} 이면 p의 요소 중에 lang 어트리뷰트의 값이 "en"과 일치하거나 "en-"로 시작하는 요소|
|`a[href^="http://"]`|"http://"로 시작하는 요소를 선택한다.|
|`a[href$=".html"]`|".html"로 끝나는 요소를 선택한다.|
|`div[class*="test"]`|class 어트리뷰트 값에 "test"를 포함하는 div 요소 선택|

> **자손 요소**: 자신의 1 level 하위에 속하는 요소
> **후손 요소**: 자신보다 n level 하위에 속하는 요소'
> **형제 요소**: 동위 관계에서 뒤에 위치하는 요소
> `div > p { color: red; }`: div의 **자손요소** 중 p 요소에 대해 style 적용
> `div p { color: red; }`: div의 **후손요소** 중 p 요소에 대해 style 적용
> `p + ul { color: red; }`: p요소의 형제 요소 중 p 요소 바로 뒤의 ul 요소 선택
> `p ~ ul { color: red; }`: p요소의 형제 요소 중 p 요소 뒤에 위치하는 ul 요소 모두 선택


> **가상 클래스 셀렉터**: 요소의 특정 상태에 따라 스타일 정의
> `a:hover { background-color: red; }`: hover 상태일 때(커서를 위에 올려놓을 때)
> `input:focus { background-color: yellow; }`: focus 상태일 때(입력창을 클릭했을 때)
> `a:link { color: orange; }`: a 요소가 방문하지 않은 링크일 때
> `a:visited { color: green; }`: a 요소가 방문한 링크일 때
> `a:active { color: blue; }`: a 요소가 클릭된 상태일 때




