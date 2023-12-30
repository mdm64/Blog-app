from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Post, NewPost
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView

)
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # creates a fn. which allow only to update the form of users post


# @login_required
# def home(request):
#     members = NewPost.objects.all()
#     context = {
#         'members': members
#     }
#     template = loader.get_template('home.html')
#     return HttpResponse(template.render(context, request))

class PostListView(ListView):
    model = NewPost
    template_name = 'home.html'
    context_object_name = 'members'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = NewPost
    template_name = 'detail.html'

# from django import forms
# class CreateForm(forms.ModelForm):
#     class Meta:
#         model = NewPost
#         fields = ['title', 'content']

# def create(request):
#     if request.method == 'POST':
#         # a = NewPost.objects.filter(author = request.user.username)
#         form = CreateForm(request.POST)

#         if form.is_valid():
#             a = form.save(commit=False)
#             a.author = request.user
#             a.save()
#             return redirect('blog-home')
#     else:
#         form = CreateForm()
    
#     context = {
#         'form': form
#     }

#     return render(request, 'create.html', context)
# above code can be written in class form like below
class PostCreatelView(LoginRequiredMixin, CreateView):
    model = NewPost
    fields = ['title', 'content']
    template_name = 'create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user # to tell that only user can create the post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk}) # this is to redirect on the post you  just created

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = NewPost
    fields = ['title', 'content']
    template_name = 'update.html'

    def form_valid(self, form):
        form.instance.author = self.request.user # to tell that only user can create the post
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk}) # this is to redirect on the post you  just created

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = NewPost
    template_name = 'delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request, 'about.html')

@login_required
def myposts(request):
    members = NewPost.objects.all()
    context = {
        'members': members
    }
    # template = loader.get_template('myposts.html')
    return render(request, 'myposts.html', context)

def userpost(request, username):
    members = NewPost.objects.filter(author__username = username) # use __username otherwise it'll consider it as pk
    context = {
        'members': members
    }
    # template = loader.get_template('myposts.html')
    return render(request, 'userpost.html', context)
# Create your views here.
