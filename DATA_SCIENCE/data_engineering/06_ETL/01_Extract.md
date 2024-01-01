# Extract
> **DataWarehouse**에서 **DataLake**의 필요 data를 이동하여 저장하는 단계
>
> api 수집 및 웹 페이지 크롤링 등으로 얻은 데이터의 형식을 변환하거나 유지하여 hdfs에 저장한다.
>
> **HDFS (Hadoop Distributed File System)**은 하둡의 저장소이며 여러 머신에 대용량 파일들을 분산처리 저장을 한다. 여러 서버에 분산 저장을 하기 때문에 다른 서버에서 복구할 수 있어 데이터 안정성을 얻는다.

```
from hdfs import InsecureClient # hadoop 서버와 연결하는 client 객체 모듈(hdfs 접근)
import requests # web 사용
import json
import datetime as dt
```

1. `client = InsecureClient('http://localhost:9870', user='root')`: hdfs client 연결객체 생성
2. hdfs에서 client 객체를 사용해서 file 읽어오기
   - `with client.read('/rdd/score.txt) as reader: score = reader.read()`: byte 코드로 읽어오기 때문에 decoding이 필요하다.
   - `score_data = bytes.decode(score)`: decoding 진행
3. hdfs에 쓰기
   - 로컬 데이터 파일을 열고 hdfs client를 통해서 쓰기 모듈 사용 등록 후 로컬 파일의 내용을 한줄씩 읽어서 hdfs에 쓴다.
   - ```
     with open('./data/corona_data/sido_area.csv',encoding='CP949') as reader, client.write('/corona_data/sido_area_tmp.csv') as writer:
        for line in reader :
            writer.write(line.encode('CP949'))
     ```
4. hdfs에 수정하기
   - hdfs.client.write(파일명, '수정내용', append=True)를 이용해서 수정내용 update
   - `client.write('/rdd/score.txt','최연성 장고 100'.encode('UTF-8'),append=True)`
   - 위의 읽어오기를 사용해서 읽어보면 수정내용이 업데이트 된 것을 볼 수 있다.
5. hdfs 권한 수정
   - `client.set_permission('/corona_data/loc', '777')`
6. hdfs 삭제
   - `client.delete('/corona_data/loc/sido_area.xlsx)`

## 공공데이터 API 수집 후 hdfs 저장 예제
1. REST_API로 일간 코로나 발생 데이터(전국)를 호출해서 hdfs에 저장한다.
```
def executeRestApi(method, url, headers, params):  
    
    # raise Exception('응답코드 : 500')  # 예외 테스트
    # err_num = 10/0 # 예외 테스트
    if method == "get":
        res = requests.get(url, params=params, headers=headers)
    else:
        res = requests.post(url, data=params, headers=headers)

    if res == None or res.status_code != 200:
        raise Exception('응답코드 : ' + str(res.status_code))
       
    return res.text


```
2. 어느 기준일자부터 현재까지의 데이터를 끌어올지 정하기 위해서 기준일자를 구하는 함수를 생성한다.(5일 전이면 5일 전 데이터부터 현재 데이터)
```
# 현재 날짜로부터 befor_day 만큼 이전의 날짜를 생성해주는 함수
def cal_std_day(befor_day):   
    x = dt.datetime.now() - dt.timedelta(befor_day)
    year = x.year
    month = x.month if x.month >= 10 else '0'+ str(x.month)
    day = x.day if x.day >= 10 else '0'+ str(x.day)  
    return str(year)+ '-' +str(month)+ '-' +str(day)
```
