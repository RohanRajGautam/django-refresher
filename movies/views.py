from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie

def movies(req):
  data = Movie.objects.all()
  return render(req, 'movies/movies.html', {'movies': data})

def home(req):
  return HttpResponse('homepage')

def detail(req, id):
  data = Movie.objects.get(pk=id)
  return render(req, 'movies/detail.html', {'movie': data})

def add(req):
  title = req.POST.get('title')
  year = req.POST.get('year')

  if title and year:
    movie = Movie(title=title, year=year)
    movie.save()
    return HttpResponseRedirect('/movies')

  return render(req, 'movies/add.html')

def delete(req, id):
  data = Movie.objects.get(pk=id)
  data.delete()
  
  return HttpResponseRedirect('/movies')
