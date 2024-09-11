from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from user import views
from user.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.registration, name="registration"),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html',authentication_form=LoginForm), name='login')
]
