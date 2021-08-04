"""primer_proyecto_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.root, name='index'),
    path("blogs", views.index, name="blogs"),
    path("blogs/new", views.new, name="new"),
    path("blogs/create", views.create, name="create"),
    path("blogs/<int:blog_id>", views.show, name="show"),
    path("blogs/<int:blog_id>/edit", views.edit, name="edit"),
    path("blogs/<int:blog_id>/delete", views.destroy, name="delete"),
    path("blogs/json", views.json, name="json"),

]
