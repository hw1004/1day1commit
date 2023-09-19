# Github에 파일/폴더 업로드 하기

## 1. vscode, github 연동
vscode 소스 제어에서 commit할 변경사항 체크 후 ver1 commit 실행

## 2. git
```
# 파일 준비
git init

git add .
# 특정 파일만 원하면 git add github.md

git commit -m "first commit"
```
```
# 업로드하기
git remote add origin https://github.com/hw1004/1day1commit.git

git push -u origin main

# branch 이름 바꾸고 싶으면
git branch -m main master
```