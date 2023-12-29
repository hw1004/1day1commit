# text data RDD 활용 word counting
1. hdfs에서 텍스트 파일 읽어오기
   - `sc.textFile('/rdd/shakespeare.txt')`
2. 읽어온 rdd 원소의 글자수가 0인 것은 제외한다.
   - `sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).collect()`
3. "영문자, 숫자 그리고 밑줄문자 이외의 문자가 1번이상 나오면" => 정규식 기호로 만든다.
   - `\W+`
4. 정규식 기호를 기준으로 rdd 원소인 문자열을 split
   - list로 되면서 rdd가 2차원으로 변환되기 때문에 1차원으로 유지시켜야 한다.
   - `sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).flatMap(lambda x : re.split('\W+', x)).collect()`
5. 1차원 rdd에서 한글자도 없는 단어가 생성
   - `sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).flatMap(lambda x : re.split('\W+', x)).filter(lambda x : len(x) > 0).collect()`
6. 각 단어를 key-value pair rdd로 변환한다. (tuple)
   - `sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).flatMap(lambda x : re.split('\W+', x)).filter(lambda x : len(x) > 0).map(lambda x : (x.lower(), 1)).collect()`
7. key를 기준으로 key가 같은 rdd들의 value를 모두 더한다. (동일단어 수 세기)
   - `sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).flatMap(lambda x : re.split('\W+', x)).filter(lambda x : len(x) > 0).map(lambda x : (x.lower(), 1)).reduceByKey(lambda x, y : x+y).collect()`
8. value를 기준으로 내림차순 정렬한다. (최종 코드)
   - `wordcount = sc.textFile('/rdd/shakespeare.txt').filter(lambda x : len(x) > 0).flatMap(lambda x : re.split('\W+', x)).filter(lambda x : len(x) > 0).map(lambda x : (x.lower(), 1)).reduceByKey(lambda x, y : x+y).sortBy(lambda x: x[1], ascending=False)`
9. 텍스트 파일로 저장한다.
    - `wordcount.saveAsTextFile(경로)`

## Wordcloud
```
!pip install wordcloud

from wordcloud import WordCloud

# 워드클라우드 설정
word_c = WordCloud(width=800, height=400, background_color='white', max_font_size=100, max_words=100)

# 워드클라우드에 data는 dictionary로 전달한다.
# data 빈도를 기준으로 워드클라우드 생성
# 위에서 만든 wordcount list를 이용해서 워드클라우드 생성
cloud = word_c.generate_from_frequencies(dict(wordcount.collect()))

# 사진파일 저장
cloud.to_file('test.jpg')
```

## 텍스트에서 명사만 카운팅하는 방법 (nltk)
```
! pip install nltk

import nltk
from nltk.tokenize import word_tokenize

# nltk 문법 다운로드
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# 글자수가 0인 것 제외
sonnets = sc.textFile('/rdd/shakespeare.txt')\
            .filter(lambda x: len(x) > 0)\
            .collect()

# 공백을 기준으로 단어를 분할한다.
token = map(lambda t: word_tokenize(t), sonnets)

# 품사 분류 함수를 사용해서 각 단어의 품사를 분류한다.
# NN으로 분류되는 단어는 명사
# 단어와 단어의 품사를 pair로 생성
tagged = list(map(lambda t : ntlk.pos_tag(t), token))

# 2차원으로 되어 있기 때문에 1차원으로 변형하고
# 단어의 품사가 NN(명사)인 것만 추출한다.
# pair로 품사 표시되어 있던 것을 품사 제외한 단어만 추출한다. (품사가 명사인 단어들이 출력되게 됨)
sc.parallelize(tagged)\
    .flatMap(lambda e: e)\
    .filter(lambda e: e[1] == 'NN')\
    .map(lambda x: x[0]).collect()

# 위의 명사인 단어들만 추출된 list를 key-value pair로 만들고
# key가 같은 요소들끼리 count한 후 sort 진행
wordcount_2 = sc.parallelize(tagged)\
    .flatMap(lambda e: e)\
    .filter(lambda e: e[1] == 'NN')\
    .map(lambda x: x[0])\
    .map(lambda x: (x.lower(), 1))\
    .reduceByKey(lambda a, b : a + b).\
    .sortBy(lambda x: x[1], ascending=False)

# 텍스트 파일로 저장
wordcount_2.saveAsTextFile('/rdd/wordcnt_nn')
```



