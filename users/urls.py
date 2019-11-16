from django.contrib.auth import views as auth_views
from django.urls import path
from users import views

urlpatterns = [
  path('register/', views.SignUpView.as_view(), name='signup'),
  path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, extra_context={'title': 'Login'}), name='login')
]
