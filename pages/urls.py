from django.urls import path
from  pages import views

urlpatterns = [
  path('', views.root, name='index'),
  path('home/', views.HomePageView.as_view(), name='home'),
]
