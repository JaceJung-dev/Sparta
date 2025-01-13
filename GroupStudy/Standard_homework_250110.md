# 250110 배운 내용 정리

## accounts.models
```python
# django의 해당 프로젝트의 settings 모듈을 가져오기 위한 import
from django.conf import settings
# Custom User 모델을 만들기 위해 Django에서 기본적으로 제공하는 User 모델 불러오기
from django.contrib.auth.models import AbstractUser
# Django에서 모델을 정의하는데 쓰이는 모듈 import
from django.db import models

# Django Model에서 하나의 클래스는 하나의 데이터테이블 같은 개념이고, 클래스의 인스턴스는 해당 테이블의 하나의 행(row) 같은 개념.
# Django에서 제공하는 AbstractUser 모델을 상속받아서 Custom Model 클래스 생성
class User(AbstractUser):
    # 기존의 상속 받은 User모델에 bio라는 textfield를 추가함.
    bio = models.TextField()

# Profile이라는 사용자들의 프로필 모델을 생성
class Profile(models.Model):
    # user필드는 settings의 AUTH_USER_MODEL에 정의해둔 모델과 One-to-one relation으로 서로 참조. 
    # 이 때 settings.AUTH_USER_MODEL = "accounts.User" 로 위에서 새로 정의한 Custom User모델임.
    # on_delete=models.CASCADE : 참조하고 있는 부모모델(User)가 삭제되면 Profile도 삭제
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # address, zipcode  라는 Character field 정의, CharField는 max_length parameter도 지정해줘야함.
    address = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=6)
    
    # 생성자 매서드: Profile 클래스를 print하거나 admin페이지에셔 출력되는 문자열을 정의 
    def __str__(self):
        return self.address
```

## blog.models
```python
# Django에서 모델을 정의하는데 쓰이는 모듈 import
from django.db import models
# django의 해당 프로젝트의 settings 모듈을 가져오기 위한 import
from django.conf import settings

# Post model 생성 및 정의
class Post(models.Model):
    # author라는 field를 ForeignKey를 이용해서 정의. ForeignKey는 Many-to-One relation 관계를 정의할 때 사용
    # author필드는 settings의 AUTH_USER_MODEL에 정의해둔 모델과 관계를 맺고 있음.
    # 이 때 settings.AUTH_USER_MODEL = "accounts.User" 로 위에서 새로 정의한 Custom User모델이며 해당 모델이 부모모델.
    # on_delete=models.CASCADE : 참조하고 있는 부모모델(User)가 삭제되면 Profile도 삭제
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # message 라는 TextField 정의
    message = models.TextField()
    # created_at, updated_at 이라는 DateTimeField정의, auto_now_add는 생성될 때 현재 시간 저장, auto_now는 수정할 때 현재 시간 저장.
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Tag 도델과 Many-to-Many 관계를 형성하는 필드 정의
    # blank=True 태그를 작성하지 않아도 됨.
    tag_set = models.ManyToManyField('Tag', blank=True)


    # 생성자 매서드: Post 클래스를 print하거나 admin페이지에셔 출력되는 문자열을 정의 
    def __str__(self):
        return self.message


# Tag model 생성 및 정의
class Tag(models.Model):
    # name 이라는 CharField 정의
    name = models.CharField(max_length=44)

    # 생성자 매서드: Tag 클래스를 print하거나 admin페이지에셔 출력되는 문자열을 정의 
    def __str__(self):
        return self.name
```

## blog.urls
```python
# url패턴의 정의하고, view로 처리하기 위한 기능(함수) 불러오기
from django.urls import path
# blog app에 있는 views 모듈 불러오기
from blog import views

# route는 요청받은 url의 패턴으로 ''는 빈 문자열로 루트 url, view는 해당 url과 매핑 view 함수, name은 해당 url패턴의 이름.
# urlpatterns는 위의 주석내용을 바탕으로 URL과 view를 연결하는 리스트
urlpatterns = [
    # 루트 url과 post_list 연결
    path(route='', view=views.post_list, name='post_list'),
    # post_new/ url과 post_new 연결
    path(route='post_new/', view=views.post_new,),
]
```

## blog.views
```python
# html템플릿으로 출력하기 위한 render와 url로 리다이렉트 하기 위한 기능(함수) 불러오기
from django.shortcuts import render, redirect
# blog app의 forms 모듈에 있는 PostForm 불러오기
from blog.forms import PostForm
# blog app의 models 모듈에 있는 Post 불러오기
from blog.models import Post

'''
1. view : urls 있는 주소에 매핑 확인 후 요청 처리 로직 
2. 데이터 처리: 데이터베이스 핸들링(읽고, 쓰고, 수정, 삭제 등등등)
3. 응답 반환(랜더링) 템플릿
'''

# url과 연결한 post_list view함수 정의
def post_list(request):
    # Post model에 있는 데이터 가져오기
    posts = Post.objects.all()
    # url의 요청을 받아 blog/post_list.html 템플릿에 posts 데이터를 전달해서 랜더링 후 반환
    return render(request=request, template_name='blog/post_list.html', context={'posts': posts})

# url과 연결한 post_new view함수 정의
def post_new(request):
    '''
    POST: 사용자가 데이터를 던질 때
    GET: 사용자가 페이지를 열었을 때(데이터 안 던질 때)
    '''
    # 요청 매서드가 POST인지 확인
    if request.method == 'POST':
        # 제출한 데이터로 채운 Postform 객체 생성
        form = PostForm(request.POST)
        # 폼 데이터가 조건에 맞는 유효한 데이터인지 확인
        if form.is_valid():
            # post객체를 데이터베이스 반영 및 저장하지 않고 메모리에만 저장 (commit=False)
            post = form.save(commit=False)
            # request.user == 로그인한 사용자 id
            # post의 author를 요청한 유저로 설정
            post.author = request.user
            # post객체를 데이터베이스에 반영 및 저장
            post.save()
            # post_list url로 리다이렉트
            return redirect('post_list')
    # 요청 매서드가 POST가 아닌 경우 (e.g. "GET")
    else:
        # 빈 Postform 객체 생성
        form = PostForm()
    # blog/post_new.html 템플릿에 form 데이터를 전달해서 랜더링 후 반환
    return render(request=request, template_name='blog/post_new.html', context={'form': form})
```

## blog.forms
```python
# django의 form관련 기능을 위한 모듈 불러오기
from django import form
# blog app의 models 모듈에 있는 Post 불러오기
from blog.models import Post

'''
Forms
1. HTML 폼을 자동 생성
2. 사용자가 입력한 데이터를 검증 -> 데이터베이스 상호 작용(반영, 저장, 쓰고, 수정하거나 등등)
'''

# ModelForm을 상속받아 PostFrom 정의
class PostForm(forms.ModelForm):
    # 해당 폼의 메타 데이터를 정의하는 내부의 클래스
    class Meta:
        # 기준이 되는 모델을 Post로 정의
        model = Post
        # 사용할 필드 설정
        fields = ['message', 'tag_set']
```

## blog/post_list.html
```html
<!-- h1 태그: 제목정도..? -->
<h1>i hate u</h1>
<!-- view에서 전달한 posts의 데이터 리스트를 순회하며 post.message 출력 -->
<ui>
    {% for post in posts %}
        {{ post.message }}
    {% endfor %}
</ui>
```

## blog/post_new.html
```html
<!-- h1 태그: 제목정도..? -->
<h1>post_new</h1>
<!-- POST method로 데이터를 제출, action이 없어서 현재 페이지의 url로 제출 -->
<form method="post">
    <!-- POST같이 데이터를 던질 떄, CSRF라는 보안 토큰이 필요하기 때문에 추가 -->
    {% csrf_token %}
    <!-- view에서 전달 받은 form데이터를 <p> 태그로 출력 -->
    {{ form.as_p }}
    <!-- 폼 제출 버튼 -->
    <button type="submit">Submit</button>
</form>
```