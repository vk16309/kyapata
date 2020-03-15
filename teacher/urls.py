from django.urls import path,include
from . import views
urlpatterns = [
    path('personal/',views.personal,name='personal'),
    path('create/',views.create,name='create'),
    path('dashboard/<int:teacher_id>',views.dashboard, name='dashboard'),
    path('create_list/<int:create_id>',views.create_list, name='create_list'),
    path('payment/',views.payment,name='payment'),
    path('success/',views.success,name='success'),
    path('dashboardcheck/',views.check,name='check'),
    #path('<int:product_id>/upvote',views.upvote, name='upvote'),
    path('<int:teacher_id>/upvote',views.upvote, name='upvote'),
    path('<int:teacher_id>/edit',views.editform,name='editform')
]
