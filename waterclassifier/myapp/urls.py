from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('login', views.login_page, name='login_page'),
    path('signup', views.signup_page, name='signup_page'),
    path('water', views.water_view, name='water_view'),
    
]