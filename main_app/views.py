from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Animals

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
  return render(request, 'animals/detail.html', { 'animal': animal })

class AnimalCreate(CreateView):
  model = Animals
  fields = '__all__'
  success_url = '/animals/'

class AnimalUpdate(UpdateView):
  model = Animals
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['breed', 'description', 'age']

class AnimalDelete(DeleteView):
  model = Animals
  success_url = '/animals/'