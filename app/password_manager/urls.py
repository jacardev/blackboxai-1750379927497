from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add/', views.add_record_view, name='add_record'),
    path('edit/<int:record_id>/', views.edit_record_view, name='edit_record'),
    path('delete/<int:record_id>/', views.delete_record_view, name='delete_record'),
]
