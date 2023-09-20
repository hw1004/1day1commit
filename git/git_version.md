# Git
## Git 개념
> Git은 코드 관리 도구(Source Code Management Tool, SCM)로 command line에서 사용되는 프로그램이다. 버전 관리 도구(Version Control System)이기도 하여 버전을 통해 코드를 관리하는 도구이다. 또한, 분산된 형태로 버전을 통해 코드를 관리하는 도구로 분산형 버전 관리 도구(Distributed VCS)이기도 하다. Git의 저장소(프로젝트/코드)의 단위는 **폴더/디렉토리**이다. 

### Git의 목적
- version
- backup
- collaborate

## 버전 관리 Git CLI - Version Control
명령어를 이용해서 Git을 제어할 수 있다.

- Git이 익숙해지면 복잡한 gui 없이 Git을 다룰 수 있다.
- 처리할 일을 한번에 명령하여 한번에 처리할 수 있음
- GUI로 제어할 수 없는 서버 환경에서도 사용할 수 있는 유일한 방법

|Working Tree|Staging Area|Repository|
|---|---|---|
|파일 생성, 수정 단계로 수정된 내용 포함함(Version이 만들어지기 전)|파일 10개 중 2개를 Version으로 만들 때 staging area에 2개의 파일을 올림(Git에게 명령 시 2개만 Version화 됨)|version이 저장되어 있는 곳(저장소) - |
|`git add`이전|`git add`이후|commit 이후

`git status`를 입력했을 때 No commit Yet이라고 뜨면 아직 커밋된 것이 없어 Version이 존재하지 않는다는 의미이다.

### 여러개의 파일 Grouping
- 여러개의 파일을 하나의 버전으로 만들 수 있다. 수정된 이전 파일이든 새로 추가된 파일이든 `git add`를 수행하고 여러개의 파일 변경 내역을 한번에 commit할 수 있다.

- `git log --stat`: 한번의 version에 포함된 파일들의 이름과 추가된 줄 들의 개수를 출력한다.

### 추가
- `git add .`: 파일 하나하나 add 안해도 directory 내에 있는 모든 파일 add 가능
- `git commit -am`: add와 commit 동시에 (하지만 Untracked files에 대해서는 작동하지 않음)

### 버전 reset
- `git reset --hard`: git 버전의 변경사항 삭제 (git log에서 나오는 숫자에 해당하는 버전**으로** 리셋)
- collaboration에서 이미 공유된 버전은 리셋하면 안됨!!

### 버전 revert
- R3라는 버전으로 리셋되고 싶다면 `reset` 할 때는 R3로, `revert` 할 때는 그 이후의 버전인 R4로 지정해야 R4까지 revert(R3로 리셋된다).

## 기타
### 추가 Git 명령어
|명령어|설명|예시|
|---|---|---|
|nano|파일을 만들고 그 파일 안의 내용을 입력한다. 내용 입력 후 `ctrl + x`를 누르고 `Y`를 누르고 `Enter`를 누르면 저장됨|`nano hello.txt`|
|git diff|commit 사이에 다른점을 보요주는 명령어(Working Directory와 Staging Area 사이의 차이 확인)|add를 통해 staging area로 넘어가면 git diff 안나타남. 이전 add 이후에 아직 add하기 이전의 Working Directory에 있는 수정 내용이 git diff 값으로 나옴|
|git log -p|문제가 생겼을 때 어디 부분에서 오류가 생겼는지 알 수 있음||
|code .|git bash에서 현재 폴더를 vs code로 열 때||
|git restore|working directory에서의 change 취소|`git restore README.md`|
|git checkout|git log 조회했을 때 버전 별로 주어진 숫자(코드)가 있다. 그 숫자를 이용하여 checkout하면 과거의 변경사항이 삭제된다.|`git checkout 33664ba`, `git checkout master`|
|git remote|존재하는 원격저장소 확인|
|git remote remove|원격저장소 이름 제거 (기존에 연결된 원격 저장소 제거할 때)|`git remote remove origin`|

