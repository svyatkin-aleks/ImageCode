from django.urls import path
from .views import *


app_name = "main"

urlpatterns = [
    path('image/create', ImgCodeCreateView.as_view()),
    path('image/list', ImgList.as_view())
]