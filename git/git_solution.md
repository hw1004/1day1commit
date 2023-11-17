# 깃 오류 해결
## 1. error: src refspec main does not match any
error: failed to push some refs to 'https://github.com/hw1004/Machine-Learning-Semi-project.git'

- 레포 생성 후 첫 commit 할 때 원격 저장소에 로컬 파일에 없는 파일/커밋이 있으면 오류가 생김 (initial commit)
- `git push origin main` 실행하면 생기는 오류
- `git pull --rebase origin main` 진행하고 `git log`로 원격 저장소의 커밋 기록이 있나 확인
- 다시 push 진행하면 해결 