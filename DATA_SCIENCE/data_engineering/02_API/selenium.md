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
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By # 셀레니움 4.0부터 포함된 함수(필수)
```

