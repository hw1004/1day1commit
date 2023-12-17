# 동적 로그인 진행
> input box가 있는 페이지에서 driver을 이용해서 값을 전달한다.
>
> seleniumm 객체는 파싱, 명령전달, 스크립트 진행 모두 가능하다.

1. driver 생성: `driver = create_driver()`
   - ```
        def create_driver() :
        service=Service()
        options=webdriver.ChromeOptions()
        driver=webdriver.Chrome(service=service, options=options)
        return driver
     ```
2. login 페이지 url 전달: `driver.get(url)`
3. input box 요소 찾기: `id_elem = driver.find_elemnet(By.ID, 'id')`
   - 또는 xpath를 이용해서 찾을 수 있다.: `driver.find_element(By.XPATH, xpath값)`
4. 기존 input box에 입력되어 있던 값 지우기: `id_elem.clear()`
5. 아이디/패스워드 값 보내기: `id_elem.send_keys('값')`
6. 로그인 클릭 버튼의 xpath 찾기: `login = driver.find_element(By.XPATH, xpath값)`
7. 로그인 버튼 클릭하기(아이디/패스워드 값들 보내고 로그인 버튼 실행): `login.click()`

## input 태그에 값 설정하는 javascript 코드 생성
1. 현재 페이지 문서를 document라고 할 때
   - `id_script = "document.getElementsByName('id')[0].value='"+id_input+"'"`
   - `pw_script = "document.getElementsByName('pw')[0].value='"+pw_input+"'"`
2. 자바스크립 코드를 통해서 값을 전달한다.
   - `driver.execute_script(id_script)`
   - `driver.execute_script(pw_Script)`
3. login 버튼 클릭: `login.click()`
4. 로그인된 상태에서 메일 페이지에 접근하여 서버에게 페이지 재요청한다. 드라이버에서 구동되고 있는 브라우저의 세션값이 같이 서버에게 전달되기 때문에 로그인이 유지된다.: `driver.get(네이버 메일 url)`