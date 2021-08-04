from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse

# Create your views here.
def root(request):
    return redirect("/blogs")

def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request, blog_id):
    return HttpResponse(f"placeholder para mostrar el blog numero: {blog_id}")

def edit(request, blog_id):
    return HttpResponse(f"placeholder para editar el blog {blog_id}")

def destroy(request, blog_id):
    return redirect("/blogs")

def json(request):
    return JsonResponse({
        "title": "Titulo",
        "Name": "Nombre"
        })