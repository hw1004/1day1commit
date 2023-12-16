# selenium을 이용한 웹수집
> webdriver라는 API를 통해서 운영체제(os)에 설치된 웹 브라우저를 제어하는 함수를 포함한 패키지
>
> - **브라우저를 컨트롤하는 기능**이기 때문에 webdriver 프로그램을 사용한다.

## selenium 설치
```
!pip install selenium

# 패키지 임포트
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By # 셀레니움 4.0부터 포함된 함수(필수)
```

## 객체 생성
1. `service = Service()`: 서비스 객체 생성
2. `options = webdriver.ChromeOptions()`: 브라우저에 해당되는 옵션 객체 생성
3. `driver = webdriver.Chrome(service=service, options=options)`: 브라우저에 해당되는 driver 모듈 사용 (크롬브라우저를 핸들링할 수 있는 기능이 포함됨)

#### 함수화
```
def create_driver() :
    service=Service()
    options=webdriver.ChromeOptions()
    driver=webdriver.Chrome(service=service, options=options)
    return driver
```

## 페이지 접근 드라이버/브라우저 종료
- **페이지 접근**: `driver.get(url)`
- **화면 캡쳐**: `dirver.save_screenshot('shot.png')`
- **드라이버/브라우저 종료**: `driver.close()`
  

## html 소스 활용 bs4로 파싱
```
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# soup 객체를 이용해서 페이지 요소를 추출할 수 있음
soup.find(id='content')
```

## selenium 드라이버 함수 활용 파싱
**By**: 특정 속성값으로 태그를 찾을 때 사용
- (ex) `id_elem = driver.find_element(By.ID, 'root')`: ID 속성값이 root인 소스 반환 (모든 소스를 포함하는 태그이다.)
  - `By.ID`, `By.CSS_SELECTOR`, `By.NAME`, `By.XPATH` 등
- `id_elem.get_attribute('innerHTML')`: webelement 객체 내부의 html 소스코드를 추출한다.
- `id_elem.get_attribute('id')`: webelement 객체의 id를 반환한다.
