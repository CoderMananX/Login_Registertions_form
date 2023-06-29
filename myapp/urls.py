from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name="home"),
    path('login',views.login,name="login"),
    path('',views.register,name="register"),
    path('logout',views.logout,name="logout"),
    path('data',views.data,name="data"),
    path('data',views.data,name="data"),
    path('/delete_data/<int:name>', views.delete_data, name="delete_data")
]