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
|class|지정된 class 어트리뷰트 값|


