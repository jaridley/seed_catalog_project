from django.urls import path
from seeds import views

urlpatterns = [
    path('', views.enter_seeds, name='enter_seeds'),
]