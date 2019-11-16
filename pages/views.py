from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

def root(request):
  return redirect('login')


@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
  template_name = 'index.html'
  # title = "Welcome"

  def get_context_data(self, *args, **kwargs):
    context = super(HomePageView, self).get_context_data(*args, **kwargs)
    context['title'] = 'Welcome'
    return context