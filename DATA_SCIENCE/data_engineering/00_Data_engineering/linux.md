# 리눅스 관련 용어/개념 정리
|term|description|
|---|---|
|kernel|linux os의 주요 구성 요소이며 hardware와 process를 연결하는 핵심 인터페이스, 자원 관리(메모리, 디스크, 프로세서 등 관리)|
|shell|user와 kernel의 매개체 역할하는 프로그램 (user -> kernel 직접 명령 내릴 수 있게 하는 프로그램) - bash가 shell program의 예시|
|bashrc 파일|설정 파일로, 환경변수 설정의 역할을 한다.|
|root 계정|super user, 관리자 권한의 계정|
|일반 사용자 계정|root가 useradd로 생성한 모든 계정 (권한이 있는 파일, 디렉토리에 대해서만 읽고 쓸 수 있음)|

## 개념
1. user
|code|description|
|---|---|
|`useradd [사용자명]`|사용자 생성|
|`usermod [option] [사용자명]`|사용자 정보 수정|
|`userdel [option] [사용자명]`|사용자 삭제|

2. file
|code|description|
|---|---|
|`cp file1 file2`|file 복사|
|`mv file1 file2`|file 이동|
|`rm file1`|file 삭제|
|`mkdir dir1`|directory 생성|
|`cp -r dir1 dir2`|directory 복사|
|`mv dir1 dir2`|directory 이동|
|`rm -r dir1`|directory 삭제|

- 권한명
- r: read
- w: write
- x: execute

3. package
- APT(Advanced Packaging Tool): package installer

4. text
- `vi`: text editor
- `vim`: vi 기반 text editor
  - vim으로 text 파일 들어가서 esc - i로 입력모드로 전환하고 수정사항 변경 후 esc - :wq 하면 저장하고 종료

5. etc
|code|description|
|---|---|
|`ls`|목록 출력|
|`ls -l`|자세한 목록 정보까지 출력|
|`ls -a`|숨김파일 표시|
|`ls -lh`|파일크기를 단위로 표시|
|`cd`|home directory로 이동|
|`cd ~`|home directory로 이동|
|`cd [경로]`|해당 경로로 이동|
|`cd /`|최상위(root)로 이동|
|`cd ..`|상위 directory로 이동|
|`pwd`|현재 위치의 절대경로 확인|
|`cat 파일명`|파일 내용 확인|
