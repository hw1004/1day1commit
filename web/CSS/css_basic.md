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
|selector[attribute &#124;= "값"]|지정된 값 or 값- 으로 시작하는 요소 선택|p[lang&#124;="en"] {color:red} 이면 



