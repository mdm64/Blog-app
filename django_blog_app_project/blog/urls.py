from django.urls import path
from . import views
from .views import (
    PostListView, 
    PostDetailView,
    PostCreatelView,
    PostUpdateView,
    PostDeleteView

)

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('detail/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreatelView.as_view(), name='create'),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    # path('create/', views.create, name='create'),
    path('about/', views.about, name='blog-about'),
    path('myposts/', views.myposts, name='myposts'),
    path('userpost/<str:username>', views.userpost, name='userpost'),
]