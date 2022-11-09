from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animals
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def animals_index(request):
  animals = Animals.objects.all()
  return render(request, 'animals/index.html', { 'animals': animals })

def animals_detail(request, animal_id):
  animal = Animals.objects.get(id=animal_id)
  feeding_form = FeedingForm()
  return render(request, 'animals/detail.html', { 'animal': animal, 'feeding_form': feeding_form })

def add_feeding(request, animal_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.animal_id = animal_id
    new_feeding.save()
  return redirect('animals_detail', animal_id=animal_id)

class AnimalCreate(CreateView):
  model = Animals
  fields = '__all__'
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animals
  fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animals
  success_url = '/animals/'