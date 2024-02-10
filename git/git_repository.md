# 깃허브 파일 업로드, 프로젝트 올리는 방법
```
# vs code에서 파일 열어서 저장소 생성
git init
git remote add origin [github repository 주소]
git branch -m master main # branch main으로 변경

# 로컬에 없는 README.md 파일이 있기 때문에 pull 진행
git pull [branch name]
git add .
git commit -m "commit message"
git push origin main
```

## 깃허브 저장소 관련 명령어
```
# 원격 저장소 이름, 주소 확인
git remote -v
# 원격 저장소 삭제
git remote rm origin
# branch 확인
git branch
```