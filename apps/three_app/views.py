from django.shortcuts import render, HttpResponse, redirect
#1
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")
#2
def new(request):
    return HttpResponse("placeholder to later display a new form to create a new blog")
#3
def create(request):
    return redirect("/")
#4
def show(request,number):
    return HttpResponse(f"placeholder to display blog number : {number} ")
#4
def edit(request,number):
    return HttpResponse(f"placeholder to edit blog {number} ")
#5
def destroy(request,number):
    return redirect("/")





