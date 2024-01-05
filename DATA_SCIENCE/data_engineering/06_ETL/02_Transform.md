# Transform

> HDFS에 저장한 데이터를 LOAD 해서 다른 의미의 가공 데이터 처리하는 프로그램
>
> 프로그램 내 처리하는 코드를 Data Warehosue 또는 Data Mart에 저장할 때 사용한다.

1. Data Warehouse에 있는 data를 사용하기 위해서 hdfs 클라이언트 객체를 생성한다.
   - `client = InsecureClient('http://localhost:9870', user='root')`
   - aws : `user='labxx'`
2. 기준일 생성 함수
   - ```
        # 기준일 생성 함수
        def cal_std_day(before_day) :
            x = dt.datetime.now()-dt.timedelta(before_day)
            year = x.year
            month = x.month if x.month >=10 else '0'+str(x.month)
            day = x.day if x.day >= 10 else '0'+str(x.day)
            return str(year)+'-'+str(month)+'-'+str(day)
     ```

3.  data transform에 필요한 data들을 불러온다.
   - `area = spark.read.csv('/corona_data/loc/sido_area.csv', encoding='CP949', header=True)`
   - `popu = spark.read.csv('/corona_data/loc/sido_population.csv',encoding='CP949',header=True)`
4. 위의 데이터로 단위면적당 인구수 data를 생성한다.
   - area data와 popu data join: `area_pop = area.join(popu, on='loc')`
   - loc 컬럼과 새로 popu_density 컬럼을 만들어서 transformed df를 생성한다.: `area_pop = area_pop.select(area_pop.loc, ceil(area_pop.total/area_pop.area)).alias('popu_density'))`: loc와 popu_density 컬럼으로 이루어진 df가 됨


## 컬럼 중 dict 요소들로 이루어진 list 안의 데이터 끌어오는 방법
- `tmp_fin = tmp.select('items').first()`: items 컬럼 데이터가 list 한 개이므로 first() 함수로 리스트 내의 데이터들을 가져온다.
- `spark.createDataFrame(tmp_fin['items'])`: 위에서 가져온 json 파일의 - 각 행의 정보들을 이용해서 df를 생성한다.
- `co_rate.toPandas()`: spark df를 pd df로 변환한다.


### 데이터를 결함해서 중요피처만 추출한 것은 Data Warehouse의 db에 저장하고 데이터를 결합해서 값의 transform을 진행한 것은 Data Mart의 db에 저장한다.
![](https://panoply.io/uploads/versions/diagram16-1---x----750-371x---.jpg)

