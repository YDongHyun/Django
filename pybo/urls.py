from django.urls import path
from.import views

urlpatterns=[
    path('',views.index),
    path('<int:question_id>/',views.detail), #page ex) pybo/2 처럼 출력된다.
]