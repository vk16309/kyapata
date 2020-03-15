from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='homepage'),
    path('login.html',views.login,name=''),
    path('index.html',views.index,name=''),
    path('teacherlist.html',views.teacherlist,name=''),
    path('teacherinst',views.teacherinst,name=''),
    path('teacherdetail/<str:email>/',views.teacherdetail,name='teacherdetail'),
    path('upvote_teacher/<str:email>/',views.upvote_teacher,name='upvote_teacher'),
    path('dashboard',views.dashboard,name=""),
    path('finder', views.find, name='find'),
    path('support',views.support,name='support_form'),
    path('success/',views.success,name='success'),

]
