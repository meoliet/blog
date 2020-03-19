from django.urls import path
from . import views

urlpatterns = [
    # post_list라는 뷰가 루트 url에 할당됨
    # 장고 url 확인자는 전체 url 경로에서 접두어에 포함되는 도메인이름
    # (http://127.0.0.1:8000/)을 무시하고 받아들임
    # 이 패턴은 누군가가 웹사이트에 http://127.0.0.1:8000/ 로 들어왔을 때
    # views.post_list를 보여주라고 말해줌#
    path('', views.post_list, name='post_list')
]