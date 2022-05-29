from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User created successfully!")
            return redirect('home_page')
    else:
        form = RegisterForm()
        return render(request, "profiles/register.html", {"form": form})