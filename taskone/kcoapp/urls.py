from django.urls import path
from . import views
from.views import user_register, login_view, custom_logout_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/', user_register, name= 'kcoapp-register'),
    path('Login/', login_view, name= 'Login'),
    #path('course/', auth_views.course.as_view(template_name='course.html'), name= 'course'),
    path('Login/', auth_views.LoginView.as_view(template_name='kcoapp/Login.html'), name= 'Login'),
    path('portal/', views.portal_view, name='portal'),
    path('logout/', custom_logout_view, name='logout')
]

