from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home-page'),
    path('login/',views.login_user,name='log-in-page'),
    path('register/',views.registration,name='sign-up-page'),
    path('delete-task/<str:todo_name>/',views.DeleteTask,name='delete'),
    path('update/<str:todo_name>/',views.Update,name='update'),
]
