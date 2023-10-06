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

# 실습 2
1. Project `PRACTICE`
2. APP `crud`를 만들고 진행
3. model `Student` 클래스 생성
   1. `name` => CharField(100)
   2. `age` => IntegerField
   3. `major` => CharField(10)
   4. `description` => TextField
4. 데이터 베이스 반영(migrate)
5. URL 패턴 세팅
   1. `school/new/` => `new` => `new.html` (학생 정보 입력 화면)
   2. `school/create/` => `create` => 실제 학생 저장 => detail로 redirect
   3. `school/` => `index` => `index.html` (전체 학생 조회)
   4. `school/1/` => `detail` => `detail.html` (단일 학생 조회)
   5. `school/1/edit/` => `edit` => `edit.html` (학생 수정 입력 화면)
   6. `school/1/update/` => `update` => 학생 정보 수정 저장 => detail redirect
   7. `school/1/delete/` => `delete` => 학생 삭제 => index redirect
6. HTML은 `base.html`을 만들고 확장해서 사용
   1. nav바 간단하게 만들기