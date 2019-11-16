from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
  template_name = 'index.html'


def root(request):
  return redirect('login')
