from django.shortcuts import render, redirect
from .forms import UserDetailsForm
from .models import UserDetails


def register_user(request):
    if request.method == "POST":
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request,"user_details.html",{"user": user})
    else:
        form = UserDetailsForm()
    return render(request,"register.html",{"form":form})

