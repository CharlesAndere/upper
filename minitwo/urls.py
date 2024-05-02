from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='myhome'),
    path('dashboard/', views.dashboard, name='mydashboard'),
    path('loggingin', views.loggingin, name='mylogin'),
    path('edituser/<id>', views.edituser, name='myedituser'),
    path('deleteuser/<id>', views.deleteuser, name='mydeleteuser'),
    path('updateuser/<id>', views.updateuser, name='')
]