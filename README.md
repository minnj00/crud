!!!!!!!!!crud 가 가장 중요한 부분!!!!!!!!

# CRUD (create read update delete)

> '<>'는 변수 

1. 프로젝트폴더 생성
2. 프로젝트 폴더로 이동/ vscode 실행
    -  `.gitignore`, `README.md` 생성
3. django 프로젝트 생성
    - `<pjt-name>` 공간은 변수를 의미합니다.
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
7. 서버 실행 확인
```bash
python manage.py runserver
```
실행했을 때 rocket 이 뜨면 good!

8. 앱 생성(큰 기능이 있을 때마다 앱을 생성할 것)
```bash
django-admin startapp <app-name>
```

setting.py에 앱 등록
그 다음 첫 시작은 항상 urls 

from posts import views 
ulrpatterns = []에 path('index/', views.index) 추가

views.py 에서 함수 생성

posts



- 오늘은 하나씩 배울 때 마다 commit 으로 업로드 해주고 복습할 때도 commit 목록을 보면서 어느 부분이 수정되어있는지 확인하며 부분으로 나눠서 학습 가능 