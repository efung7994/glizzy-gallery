from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Glizzy

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

def glizzy_index(request):
  glizzys = Glizzy.objects.filter(user=request.user)
  return render(request, 'glizzys/index.html', { 'glizzys': glizzys })

def glizzy_detail(request, glizzy_id):
  glizzy = Glizzy.objects.get(id=glizzy_id)
  return render(request, 'glizzys/detail.html', { 'glizzy': glizzy })