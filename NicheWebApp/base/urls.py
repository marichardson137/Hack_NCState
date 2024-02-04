from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('create/', views.createPage, name="create"),
    path('saves/', views.savesPage, name="saves"),
    path('profile/', views.profilePage, name="profile"),
    path('', views.home, name="home"),
]
