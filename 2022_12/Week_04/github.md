# guthub

- push 로컬 저장소의 버전을 원격저장소로 보냄

## 초기 원격저장소 설정하는 법
- $ git remote(원격저장소) add(추가) origin(origin으로) https://github.com/IM-jihye/TIL.git(user name)/TIL(저장소 이름).git

- 로컬 저장소 버전 -> 원격 저장소로 push 
    - $ git push<원격저장소이름><브랜치이름>
- 로컬 저장소 버전 -> 원격 저장소로 pull
    - $ git pull <원격저장소이름><브린치이름>
##

- Clone : 원격저장소 복제
- Pull : 원격저장소 커밋 가져오기

##

- 로컬에서 새로운 프로젝트 시작 : git init
- 원격에 있는 프로젝트 시작 : git Clone
- 프로젝트 개발 중 다른사람 커밋 받아오기 : git pull
- 내가 한 로컬 프로젝트 개발 공유 : git push

## <명령어 정리>

- git clone <url> 원격저장소 복제
- git remote -v  원격저장소 정보 확인
- git remote add <원격저장소><url>
- git remote rm <원격저장소>
- git push <원격저장소><브랜치>
- git pull <원격저장소><브랜치>

