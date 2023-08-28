!!!!!!!!!crud 가 가장 중요한 부분!!!!!!!!

# CRUD (create read update delete)

> '<>'는 변수를 의미하고 생성하고 싶은 이름을 넣음.

1. 프로젝트폴더 생성
2. 프로젝트 폴더로 이동/ vscode 실행
    -  `.gitignore`, `README.md` 생성
3. django 프로젝트 생성
    - `<pjt-name>` 공간은 변수를 의미합니다.
```bash
django-admin startproject <pjt-name> .
```

- . 잊지말기 잊으면 manage.py 가 폴더 안에 생겨버림


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
9. 앱 등록 => `settings.py`
```python
INSTALLED_APPS = [
    ...
    <app_name>,
]
```

10. `urls.py` => `views.py` => `templates/*.html` 순서로 코드 작성



- from posts import views 
- ulrpatterns = []에 path('index/', views.index) 추가
- views.py 에서 함수 생성
- html을 가져와야하는데 그려려면 render 을 해야햠 기본적으로 request 와 html 파일
- 앱 폴더에 templates 폴더 생성 후 그 안에 html 파일 생성하기



# Model

1. `model.py`
    - 모델의 이름은 기본적으로 단수 형태로 작성
    ```python
    from django.db import models
    # Creat your models here.
    class Post(models.Model): # models 모듈에서 Model 이라는 class를 상속ㅁ
    title = models.CharField(max_length=100)
    content = models.TextField()
    ```

2. 번역본 생성 (파이썬과 sql을 연결)
```bash
python manage.py makemigrations
```

3. DB에 반영
```bash
python manage.py migrate
```

4. SQL 스키마 확인
```bash
python manage.py sqlmigrate posts 0001
```

5. 생성한 모델 admin에 등록
```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

6. 관리자 계정 생성
```bash
python manage.py createsuperuser
```

## CRUD 로직 작성
### 1. Read

- 전체 게시물 출력
 ```python
 def index(request):
    posts = Post.objects.all()
    
    context = {
        'posts': posts,
    }
    return render(request, 'index.html', context)
```


- 하나의 게시물 출력 
```python
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }
    return render(request, 'detail.html', context )
    
```

### 2. Create
- 사용자에게 입력할 수 있는 폼을 제공
```python
def new(request):
    return render(request, 'new.html')
```

- 사용자가 입력한 데이터를 가지고 DB에 저장하는 로직

```python
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')

    post = Post()
    post.title = title # 변수 할당 
    post.conten = content
    post.save()

    return redirect(f'/posts/{post.id}')
```

### 3. Delete

```python
def delete(request, id):
    post = Post.objects.get(id=id)
    post.delete()

    return redirect('/index/')
```


### 4. Update
- 기존의 정보를 담은 form을 제공
```python
def edit(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post,
    }

    return render(request, 'edit.html', context)
```

- 사용자가 입력한 새로운 정보를 가져와서
- 기존정보에 덮어씌우기
```python
def update(request, id):
    # 방금 수정한 데이터
    title = request.GET.get('title')
    content = request.GET.get('content')

    # post = Post() => 새로운 게시물 만들때
    # 기존데이터
    post = Post.objects.get(id=id)
    post.title = title
    post.content = content
    post.save()

    return redirect(f'/posts/{post.id}/')
```
- 기존의 정보를 담은 form을 제공
- 사용자가 입력한 새로운 정보를 가져와서
- 기존정보에 덮어씌우기


- 오늘은 하나씩 배울 때 마다 commit 으로 업로드 해주고 복습할 때도 commit 목록을 보면서 어느 부분이 수정되어있는지 확인하며 부분으로 나눠서 학습 가능 
