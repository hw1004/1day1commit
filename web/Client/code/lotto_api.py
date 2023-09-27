import requests

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')

print(res.text)
type(res.text)   # str

type(res.json())   # dict
data = res.json()

numbers = [data[f'drwtNo{i}'] for i in range(1, 7)]

bonus_no = data["bnusNo"]

print(numbers, bonus_no)


# JSON => 개발자 쓰라고 제공 => Web API
# Application
# Programming
# Interface