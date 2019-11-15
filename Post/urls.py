from django.urls import path

from Post import views

urlpatterns = [
    path('show/', views.PostListView.as_view(), name='post-list'),
    path('show/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('add/', views.PostCreateView.as_view(), name='post-create'),
]