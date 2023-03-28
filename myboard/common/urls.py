from django.urls import path
from django.contrib.auth import views as auth_view

# 현재 폴더에서 views.py를 가지고 오는데 그 이름이 common_view
from . import views as common_view

urlpatterns = [
    path('', common_view.index),
    path('login/', auth_view.LoginView.as_view(template_name = 'common/login.html')),
    path('logout/', auth_view.LogoutView.as_view()),
    path('signup/', common_view.signup),
    # 회원가입
    # 회원수정
    path('update/', common_view.update),
    # 회원삭제
    path('delete/', common_view.delete)
]