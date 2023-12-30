from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    template = loader.get_template('users.html')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return HttpResponse(template.render({'form': form}, request))

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            p_form.save()
            u_form.save()
            
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
# Create your views here.

# # walkthrough:
# when we submitted the form as post request
# then create a new form which has the date same as post data
# check if form is valid, django check everything required to form to be valid, like if username already exist or not or pswd matching or not
# if its not valid it will return the original empty form or shows error messages
# if it's valid save the form and redirect the page to home page

