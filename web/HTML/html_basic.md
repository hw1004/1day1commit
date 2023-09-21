# HTML
> HTML(Hyper Text Markup Langauge)는 웹페이지에 content를 부여하고 그 content를 어떻게 구조화할건지를 웹 브라우저에 지시한다.

## Basic HTML elements

|HTML element|설명|비고|
|---|---|---|
|`<!-- comments -->`|comments를 다는 역할을 한다. 코드가 아닌 comment로써 역할을 가지고 있다.||
|`<html>`|html 문서의 모든 content/구조 들이 포함된다.||
|`<head>`|html 문서의 metadata를 포함한다. (제목이나 stylesheet link 등)|`<html><head>Metadata</head></html>`|
|`<title>`|html 문서의 title 지정(웹 브라우저에서 열 때 탭의 제목으로 보여짐)|`<head>` 내에서만 포함될 수 있음|
|`<body>`|HTML 문서의 content를 대표한다.|
|`<h1>`|h1부터 h6까지 있고 제목을 지정할 때 사용된다.|`<h1 id="A1>`는 제목에 id를 지정해준다.|
|`<p>`|text block을 하나의 paragraph로 지정|`<p id="paragraph 1"`는 paragraph에 id를 지정해준다.|
|`<div>`|section을 나눈다.|`<div id="intro">`는 section명을 지어준다.|
|`<span>`|같은 paragraph 내에서 작은 content를 다른 개별적인 content로 구별/표기하는 것||
|`<em>`|글자 기울여서 강조|
|`<strong>`|글자 굵게 해서 강조|
|`<br>`|line break (paragraph 내에서 줄 바꾸기)|
|`<ul>`|unordered list||
|`<ol>`|ordered list||
|`<li>`|list의 각 요소들 작성할 때||
|`<img src="#" />`|이미지 주소 src, alt(alternative text)에 이미지의 의미 부여|`<img src="#" alt="설명" />`|
|`<video src="#" width="100" height="100" controls>`|video 주소 src|`<video src="#" width="100" height="100" controls> Video not supported </video>` 해당 비디오가 load 안되면 `Video not supported`를 내보인다.|
|`<a href="http://~">`|하이퍼링크 생성|`<a href="http:/~><img src="logo.jpg">Click this image</a>`와 같이 이미지를 클릭하면 해당 링크로 이동할 수 있게 설정할 수 있음/ `target="_blank"`를 추가하면 링크가 브라우제에서 새로운 탭에 열도록 설정할 수 있다.|
|`#`|하이퍼링크 `<a>`로 생성 시 같은 HTML 문서의 특정 paragraph나 부분으로 이동하게 설정하고 싶으면 `#`에 id를 붙여서 설정하면 된다.|`<a href="#id">`|
|`id`|고유하게 지정하는 것|문서전체에서 유일무의하게 지정해야 하기 때문에 중복 X|
|`class`|그룹으로 묶어서 지정할 때 쓰는 것|CSS 스타일 지정할 때 사용됨|

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
|`<table border="1">`|테이블 테두리 생성||
|`<td colspan="2">`|같은 row에 있는 2개의 data를 병합|`<td colspan="2">14</td>`에서는 14가 병합된 부분에 들어갈 값이다.|
|`<td rowspan="2">`|같은 column에 있는 2개의 row data 병합|병합 안된 부분은 순서에 따라 순차적으로 추가한다.|


