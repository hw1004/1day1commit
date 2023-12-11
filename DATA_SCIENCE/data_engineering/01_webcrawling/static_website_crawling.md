# 정적 쇼핑몰 크롤링
> 구성이 변화되지 않으면서 접속량이 일정 수준 이상인 사이트를 선정하여 정적 크롤링을 진행한다.

## 1. 특정 페이지 소스 추출하기
### 쇼핑몰 사이트 크롤링할 때 자주 발생하는 에러 해결하기
> **[SSL:CERTIFICATE_VERIFY_FAILED]** 에러 => ssl 패키지 활용해서 인증 전송하여 해결한다.

- `import ssl`
- `context = ssl._create_unverified_context()`: 인증에 대해 검사하지 않도록 하는 객체
- 따라서 이를 이용해 아래와 같이 특정 페이지 소스를 추출하면 된다.
```
import ssl
context = ssl._create_unverified_context()
url = ' http://jolse.com/category/toners-mists/1019/'
htmls = urlopen(url, context = context)
htmls = htmls.read()

# 파싱 객체 생성
bs_obj = BeautifulSoup(htmls, 'html.parser')
```


## 2. 크롤링할 데이터 결정 및 수집
1. 제품명, 가격, 세일가격 등 크롤링해 올 데이터를 결정한다.
2. 한 페이지에 있는 제품들을 반복문을 활용해서 모두 수집한다.
3. 수집한 데이터들 데이터프레임으로 변환

### 예제 코드 (함수로 구성)
- 전역으로 사용할 빈 df
```
## 전역으로 사용할 빈 df 생성
prd_dict = {'품목':[], 
            '가격':[],
            '세일가격':[]}
df_fin = pd.DataFrame(prd_dict)
df_fin
```

1. 서버에 요청 후 응답된 data를 파싱객체로 생성 후 반환하는 함수
```
def get_request_product(url) :
    # context 객체 생성
    context = ssl._create_unverified_context()
    # urlopen() 요청
    htmls = urlopen(url, context=context)
    html = htmls.read()
    # bs4 객체 bs_obj 생성
    bs_obj = BeautifulSoup(html, 'html.parser')
    return bs_obj
```

2. 페이지의 전체 제품 정보를 추출하는 함수 (get_request_product 함수도 사용하기 때문에 2번의 함수만 사용하면 됨)
```
def get_page_product(url) :
    global df_fin # 전역변수(함수 내외부에서 모두 사용 가능)
    bs_obj = get_request_product(url)
    # 특정 페이지의 전체제품정보 추출
    uls = bs_obj.find('ul',{'class':'prdList'})
    boxes = uls.findAll('div',{'class':'description'})
    # 1개의 제품 정보 추출
    for box in boxes :
        res = pd.DataFrame(get_product_info(box),index=range(1,2)) # 1개의 제품 정보에 대하여 df 생성
        df_fin = pd.concat([df_fin,res], axis=0, ignore_index=True)
```

3. 각 제품의 정보를 추출하는 함수
```
def get_product_info(box) :
    product=box.a.text.split(':')[1]
    ori_price=box.ul.select('li')[0].text.split(' ')[2]
    try : 
        sale_price=box.ul.select('li')[1].text.split(' ')[2]
    except : 
        sale_price=ori_price
    # 호출한 곳에서 반환 data 활용 df 생성
    return {'품목':product, '가격':ori_price, '세일가격':sale_price}
```
- 세일가가 없는(세일을 진행하지 않는) 제품이 있을 수도 있기 때문에 try, except를 사용하여 판별해준다.