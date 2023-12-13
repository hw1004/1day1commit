# 네이버 OPEN API
> https://developers.naver.com/main/

- 로그인이 필요한 오픈 API: 네이버 아이디로 로그인 인증을 해서 접근 토큰을 획득해야 하는 기능을 사용할 때
- 로그인이 필요하지 않은 오픈 API: HTTP 헤더에 개발자 등록 id/key값 전송하면 인증됨 (검색, 공유, 지도 등)

## 검색 open API 예제
1. 개발자 등록해서 id/key값 가지고오기
2. `urllib.parse.quote()`: 글자를 URL 인코딩 해줌
   - `keyword = urllib.parse.quote('강남역')`: 강남역을 %EA%B0%95%EB%82%A8%EC%97%AD로 URL 인코딩 해줌
3. url json 형식으로 반환
4. 헤더 설정: 인증 정보 가이드 문서에서 확인하고 사용
   - `headers = {"X-Naver-Client-Id" : client_id, "X-Naver-Client-Secret" : client_secret}`
5. 요청하고 응답한 후에 json으로 요청했기 때문에 json 객체를 반환한다.
   - `result = requests.get(url=url, headers=headers)`
   - `json_obj = result.json()`
6. json 객체 확인 후 속성값들을 불러올 수 있음
   - `json_obj['items'][0].keys()`: 검색해 온 값들의 종류를 반환받을 수 있음 (title, link, description 등)

### 검색 결과의 수를 제한하고 싶을 때
> json 형식으로 url 받아올 때 display 설정
>
> 결과 요청 item 수는 100개가 최대이고, 100개 이후 데이터를 출력하려면 start 파라미터를 조정해서 그 이 후의 100개를 또 출력할 수 있다.
>
> 파라미터(display, start) 생성 할 때 공백이 있으면 안됨, 파라미터간의 구분은 &로 함

```
def create_url(b_url, keyword, display=10, start=1) :
    base_url = b_url #'https://openapi.naver.com/v1/search/blog.json'
    param = '?query=' + keyword + '&display=' + display + '&start=' + start 
    url = base_url + param
    return url

url = create_url(url, keyword, str(100), str(1))
```

## 네이버 API 이미지 검색
- 검색해서 이미지 저장
- `urllib.request.urlretrieve`
```
def down_image(url, t_name) : 
    down_path = './crawl_data/image/'+t_name
    try : 
        urllib.request.urlretrieve(url,down_path)
    except :
        return '이미지없음'
    return down_path
```

