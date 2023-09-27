import requests
from bs4 import BeautifulSoup

# 요청(HTTP Request Method(Verb)) - return 있음
# 1. GET : 95%
# 2. POST : 4%

# 브라우저에게 get 요청 보낸다고 말하기(Enter을 치는 행위)
response = requests.get('http://finance.naver.com/sise')
# HTML 문서 파싱 완료 결과
soup = BeautifulSoup(response.text, 'html.parser')
kospi_tag = soup.select_one('#KOSPI_now')
kosdaq_tag = soup.select_one('#KOSDAQ_now')
a_tag = soup.select_one('#popularItemList')

print(a_tag.text)