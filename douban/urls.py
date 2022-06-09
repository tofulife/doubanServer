from django.urls import path
from douban import views
from rest_framework import routers



# router = routers.DefaultRouter()
# router.register(r'book', views.bookView)

# 二级目录地址
urlpatterns =[
    path('booklist',views.bookView.show)
]