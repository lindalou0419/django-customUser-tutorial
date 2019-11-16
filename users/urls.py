from django.urls import path
from users import views

urlpatterns = [
  path('register/', views.SignUpView.as_view(), name='signup'),
]
