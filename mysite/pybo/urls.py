from django.urls import path
from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # 웹페이지 주소의 'pybo/' 까지는 config/urls.py의 URL을 맵핑하고, '2/' 는 pybo/urls.py의 URL 맵핑한다.
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]
