from django.shortcuts import render, redirect
from .forms import UserRagistrationForm

def registration(request):
    if request.method == 'POST':
        form = UserRagistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserRagistrationForm()
    
    return render(request, "registration.html", {'form' : form})
