1. app `review`
2. url 분리 (`review/`)
3. 패턴 `''` => 함수명 `index`
4. `h1` 포함하는 `index.html` render


1. 새로운 프로젝트 practice 
2. app util 
3. url list 
   1. /util/ => index 함수 
      1. 메인 페이지
      2. h1 으로 구성
   2. /util/clock/ => time 함수
      1. 날짜 요일 시간을 보여줌
4. `base.html` 활용
5. `nav`로 url 이동 가능하게 만듬

# 실습
## utils app에서 진행
1. `util/lotto_in/` => view function `lotto_in`
   1. 사용자가 번호 6개를 입력할 수 있는 input 제공(`lotto_in.html`)
2. `util/lotto_out/` => view function `lotto_out`
   1. 사용자 번호 6개
   2. 실제 당첨번호와 보너스 번호 (`requests`)
   3. 등수 보여주기 (`lotto_out.html`)