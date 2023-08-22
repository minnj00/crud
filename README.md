!!!!!!!!!crud 가 가장 중요한 부분!!!!!!!!

# CRUD (create read update delete)

1. 프로젝트폴더 생성
2. 프로젝트 폴더로 이동/ vscode 실행
    2.1 `.gitignore`, `README.md` 생성
3. django 프로젝트 생성
```bash
django-admin startproject <pjt-name> .
```
4. 가상환경 설정 (venv 폴더 생성됨, django 가 전역에 있지만 이 프로젝트는 가상환경에서 실행하기 위해 django 를 가상환경에도 결국 설치해서 실행)
```bash
python -m venv venv
```
5. 가상환경 활성화
```bash
source venv/bin/activate
```
- 확인법: 터미널 오른쪽에 base(전역) 말고 이 폴더 이름에 파이썬이 띄어져 있음

6. 가상환경에 django 설치
```bash
pip install django
```