from django.contrib import admin
from django.urls import path, include
from chat_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('chat_bot/', views.chat, name='chat'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path("ask_question/", views.ask_question, name="ask_question"),
]
