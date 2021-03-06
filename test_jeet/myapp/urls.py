from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('registration/', views.UserRegistration.as_view(), name='registration'),
]