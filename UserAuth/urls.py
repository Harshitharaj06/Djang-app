
from django.urls import path
from . import views
#from django.contrib.auth import login
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView,LogoutView
#from django.views.generic.base import TemplateView



urlpatterns = [
   path('', views.index, name='index'),
   path('UPLOAD/',views.upload, name = 'upload'),
   path('register/',views.register,name='register'),
   path('success/',views.success,name='success'),
   path('login/',LoginView.as_view(),name='login'),
   path('logout/',LogoutView.as_view(next_page='upload'),name='logout'),
   # path('login/', auth_views.LoginView, { 'template_name': "registration/login.html"}, name='login'),
   # path('logout', auth_views.LogoutView, { 'template_name': "registration/logout.html"}, name='logout'),
   #path('accounts/login/', auth_views.LoginView, { 'template_name': "registration/login.html"}, name='login'),
]
