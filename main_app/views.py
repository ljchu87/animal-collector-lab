from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Animals, Toy
from .forms import FeedingForm

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def animals_index(request):
  animals = Animals.objects.filter(user=request.user)
  return render(request, 'animals/index.html', { 'animals': animals })

@login_required
def animals_detail(request, animal_id):
  animal = Animals.objects.get(id=animal_id)
  toys_animal_doesnt_have = Toy.objects.exclude(id__in = animal.toys.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form': feeding_form, 'toys': toys_animal_doesnt_have })

@login_required
def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals_detail', animal_id=animal_id)

@login_required
def assoc_toy(request, animal_id, toy_id):
  Animals.objects.get(id=animal_id).toys.add(toy_id)
  return redirect('animals_detail', animal_id=animal_id)

class AnimalCreate(LoginRequiredMixin, CreateView):
  model = Animals
  fields = ['name', 'breed', 'description', 'age']
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class AnimalUpdate(LoginRequiredMixin, UpdateView):
  model = Animals
  fields = ['breed', 'description', 'age']
  

class AnimalDelete(LoginRequiredMixin, DeleteView):
  model = Animals
  success_url = '/animals/'

class ToyCreate(LoginRequiredMixin, CreateView):
  model = Toy
  fields = '__all__'

class ToyList(LoginRequiredMixin, ListView):
  model = Toy

class ToyDetail(LoginRequiredMixin, DetailView):
  model = Toy

class ToyUpdate(LoginRequiredMixin, UpdateView):
  model = Toy
  fields = ['name', 'color']

class ToyDelete(LoginRequiredMixin, DeleteView):
  model = Toy
  success_url = '/toys/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('animals_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
