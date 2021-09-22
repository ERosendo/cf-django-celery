from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('create-user/', views.create_user),
]