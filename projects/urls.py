from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('projects/', views.Projects.as_view(), name='projects'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
