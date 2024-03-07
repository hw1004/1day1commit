## DATE_FORMAT
> 날짜 형식 설정
```
SELECT DATE_FORMAT(COLUMN_A, "%Y-%m-%d") AS COLUMN_A;
SELECT * FROM TABLE WHERE MONTH(COLUMN)="2"
SELECT * FROM TABLE WHERE DAYOFMONTH(COLUMN)="2"
```
## ORDER BY
> 정렬 기준 여러개 일 때
> 먼저 온 컬럼을 기준으로 정렬한 후 먼저 온 컬럼이 같은 값에 한하여 다음 컬럼으로 정렬

```
ORDER BY column1 DESC, column2 DESC
# column1으로 내림차순 정렬 후 column1이 같은 값에 한해 column2로 내림차순 정렬
```

## CASE WEHN
> 만약 컬럼이 00이면 이렇게하고, ELSE이면 이렇게한다. END로 마무리
```
SELECT CASE WHEN TLNO IS NULL THEN 'NONE' ELSE TLNO END
```