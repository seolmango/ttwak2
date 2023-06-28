from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'ttwakuser'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='ttwakuser/login.html'))
]