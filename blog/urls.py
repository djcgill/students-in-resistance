from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('team/', views.TeamView.as_view(), name='team'),
    path('downloads/', views.DownloadsView.as_view(), name='downloads'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contributors/', views.ContribView.as_view(), name='contributors'),
    path('blog/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('blog/post/', views.post, name='post')
]
