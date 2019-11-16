from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.views.generic.base import ContextMixin

from .forms import CustomUserCreationForm

class SignUpView(CreateView):
  form_class = CustomUserCreationForm
  success_url = reverse_lazy('login')
  template_name = 'signup.html'
  title = 'Create an Account'

  def get_context_data(self, *args, **kwargs):
    context = super(SignUpView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Create an Account'
    return context