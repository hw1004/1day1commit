# .gitignore
> .gitignore 파일은 프로젝트 레포지토리에서 원하지 않는 파일들을 제외하는 파일이다.
> - git이 관리할 때 아예 무시할 파일들
> - 캐시파일, 중요한 파일을 무시해야 함


1. .git 파일이 있는 최상위 루트 디렉토리로 이동
2. gitignore.io 사이트에서 사용하는 운영체제, IDE, 언어, 로그파일들을 작성해서 생성
3. 결과물을 .gitignore 파일 생성해서 복붙한다.


## 프로젝트 진행 중 .gitignore 파일 추가
```
git rm -r --cached .
git add .
git commit -m "commit message"
git push origin main
```