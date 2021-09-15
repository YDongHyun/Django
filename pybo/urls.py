from django.urls import path
from.import views

app_name='pybo' #앱 이름 설정

urlpatterns=[
    path('',views.index,name="index" ),#http://localhost:8000/pybo/ URL은 index, http://localhost:8000/pybo/2와 같은 URL에는 detail 이라는 이름을 부여했다.
    path('<int:question_id>/',views.detail,name='detail'), #page ex) pybo/2 처럼 출력된다. detail 추가
]