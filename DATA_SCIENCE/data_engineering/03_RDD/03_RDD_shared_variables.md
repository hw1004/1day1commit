# 공유 변수 (shared variable)
## Broadcast Variables
> 각 노드에 공유되는 읽기 전용 변수

- spark session을 이용해서 broadcast variables 생성
  - `code_desc = {"DE":"Data Engineer", "DS":"Data Science", "WD":"Web Developer"}`
  - `broadcast_S = spark_session.sparkContext.broadcast(code_desc)`: code_desc는 읽기전용 공유변수로 이후에 수정이나 삭제를 진행하면 **broadcast 객체변수에는 적용이 되지만 sc에는 생성시점의 data가 유지 된다.**