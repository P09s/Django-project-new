from django.contrib import admin
from django.urls import path
from blogapp import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
       path('admin/', admin.site.urls),
       path('login/', blog_views.custom_login_view, name='login'),
       path('dashboard/', blog_views.dashboard, name='dashboard'),
       # Add other URL patterns as needed
   ]
