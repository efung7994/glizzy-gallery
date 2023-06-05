from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Glizzy

# Create your views here.
class Home(LoginView):
    template_name = 'home.html'

class GlizzyCreate(LoginRequiredMixin, CreateView):
  model= Glizzy
  fields = ['name','toppings','description','price']
  success_url = '/glizzys/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)
  

class GlizzyUpdate(LoginRequiredMixin, UpdateView):
  model = Glizzy
  fields = ['toppings', 'description', 'price']

class GlizzyDelete(LoginRequiredMixin, DeleteView):
  model = Glizzy
  success_url = '/glizzys/'

def about(request):
  return render(request, 'about.html')


@login_required
def glizzy_index(request):
  glizzys = Glizzy.objects.filter(user=request.user)
  return render(request, 'glizzys/index.html', { 'glizzys': glizzys })

@login_required
def glizzy_detail(request, glizzy_id):
  glizzy = Glizzy.objects.get(id=glizzy_id)
  return render(request, 'glizzys/detail.html', { 'glizzy': glizzy })


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('glizzy-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

