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
3. api 호출
```
url = 'http://apis.data.go.kr/1352000/ODMS_COVID_04/callCovid04Api'
service_key = '공공데이터 웹사이트에서 제공하는 개인 서비스키'
file_dir = '/corona_data/patient/'

# 일자에 대한 해당 파라미터 생성
def create_param(std_day) : 
    return {'serviceKey' : service_key
            ,'pageNo' : 1
            ,'numOfRows' : '500'
            ,'apiType' : 'JSON'
            ,'std_day' : cal_std_day(std_day)}
```
4. api 호출해서 data를 추출하고 만들어둔 함수를 이용해서 hdfs에 저장한다. 저장에 문제가 있을 경우 log file에 저장하도록 설정한다.
```
for i in range(365,367) :
    params = create_param(i) # api 요청 파라미터 생성
    log_dict={
        "is_sucess":"Fail"
       ,"type":"corona_patient"
       ,"std_day":params['std_day']
       ,"params" :params
    }
    try:
        res = executeRestApi('get', url,{}, params) # 공공데이터 api에서 data 추출
        file_name='corona_patient_'+cal_std_day(i)+'.json' # 저장 파일명 생성
        client.write(file_dir+file_name,res,encoding='utf=8') # hdfs에 저장
    except Exception as e :
        log_dict['err_msg']= e.__str__() # Exception객체 내 에러메시지를 반환
        log_json = json.dumps(log_dict, ensure_ascill=False) # json형태로 기록
        co_logger.error(log_json) # 로그 파일에 기록
        
```

## 웹크롤링 hdfs 저장 예제
1. 만약 csv 파일에 loc, new, accumulate, rate 컬럼이 있으면 `cols = ['loc', 'new', 'accumulate', 'rate']`로 컬럼들을 명시해 주고, 각 행의 데이터를 추가하는 list 원소를 생성한다. (ex) tuple_t = []에 append로 한 행에 대한 정보를 넣고 for loop을 돌린다.
   - cols와 tuple_t에 대해 `for idx, tr, in enumerate(trs):`로 for loop을 돌리고 각 행마다 data = []에 {'컬럼명': 값} 형식으로 각 행들이 들어가게끔 `data.append(dict(zip(cols, tuple_t)))` 코드를 작성한다.
2. json에 포함시킬 meta data를 구성한다.
   - ```
        # json에 포함시킬 meta data 구성
        res = {
                'meta':{
                    'desc':'지역별 코로나 예방접종 인구 현황',
                    'cols':{
                        'loc':'지역'
                        ,'new':'신규접종'
                        ,'accumulate':'누적접종' 
                    ,'rate' : '접종률'
                        },
                    'stdDay':cal_std_day(1)
                },
                'data':data
        }
        res
     ```
3. 어제의 데이터를 json 파일로 저장한다.
   - ```
        file_dir='/corona_data/vaccine/'
        file_name='corona_vaccine_'+cal_std_day(1)+'.json'
        client.write(file_dir+file_name,json.dumps(res,ensure_ascii=False),encoding='utf=8')
     ```
    - `json.dumps()`: python 객체를 json 문자열로 변환하는 함수
    - `ensure_ascii=False`: True이면 ascii가 아닌 다른 문자들을 모두 이스케이프 문자로 표현한다. 따라서 이를 False를 설정하면 한글도 잘 출력되게 설정해줄 수 있다.
4. 저장한 데이터 파일 읽어오기
   - ```
        file_dir='/corona_data/vaccine/'
        file_name='corona_vaccine_'+cal_std_day(1)+'.json'
        vaccine=spark.read.json(file_dir+file_name)
        vaccine.show()
     ```