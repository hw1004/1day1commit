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
  - 동적으로 브라우저 핸들링 할 때 약간의 지연이 있을 수 있으므로 기다린다. : `driver.implicitly_wait(2)`
- 브라우저 크기 max로 설정: `driver.maximize_window()`
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

## 다른 페이지/검색 버튼 클릭
- `driver.find_element(By.CSS_SELECTOR, sel).click()`
1. 다른 페이지 (ex. 네이버 페이지에서 쇼핑 클릭) 클릭: 클릭을 통해서 쇼핑 페이지로 들어가면 브라우저 탭(윈도우)이 하나 더 열려서 driver가 핸들링 할 수 있는 창이 2개가 됨
   - `print(driver.window_handles)`: 현재 드라이버의 활성창 확인
   - `driver.switch_to.window(driver.window_handles[1])`: driver의 활성창을 두번째 탭인 쇼핑 페이지 탭으로 변경
   - `driver.close()`: driver 닫을 때 두개의 탭이 열려 있으므로 close 두번 진행해야 한다.
2. 검색 버튼 클릭: 검색창에 검색할 내용 값 전송 후 클릭
   - `search.send_keys('아이폰 13')`
   - `from selenium.webdriver.common.keys import Keys`
   - `search.send_keys(Keys.ENTER)`: click과 같은 효과

## 페이지의 스크롤 동작
1. 탭에서 스크롤의 현재 위치를 저장한다.
   - `before_h = driver.execute_script('return window.scrollY')`: javascript 코드로 동작
2. 무한 스크롤을 진행한다.
   - ```
      while True : 
          # 창의 가장 아래로 스크롤 내림, 스크롤이 창 바닦에 닿으면 새로운 창이 확장됨
          driver.find_element(By.CSS_SELECTOR,"body").send_keys(Keys.END)
          # 스크롤 사이 페이지 로딩시간 대기
          time.sleep(1)
          # 스크롤 후 높이
          after_h = driver.execute_script('return window.scrollY')
          print(after_h)
          if after_h==before_h:
              break
          before_h = after_h
     ```
3. 필요한 정보 추출