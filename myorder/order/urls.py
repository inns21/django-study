from django.urls import path

from .import views

urlpatterns = [
    path('',views.index),
    # 주문접수
    path('add_order/', views.add_order),
    # 주문 확인
    path('order_list/', views.order_list),
    # 주문 수정
    path('<int:id>/update/', views.update),
    # 주문 삭제
    path('<int:id>/delete/', views.delete),
    # 주문 검색
    path('order_list/search/', views.search),
    # 주문 상세 내역서
    path('<int:id>/', views.show),
]