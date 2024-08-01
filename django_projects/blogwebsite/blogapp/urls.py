from django.urls import path
from .views import custom_login_view, dashboard_view

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
