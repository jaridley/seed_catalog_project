from django.urls import path
from seeds import views

urlpatterns = [
    path('', views.enter_seeds, name='enter_seeds'),
    path('list_seeds.html', views.list_seeds, name='list_seeds'),
    path('delete/<seed_id>', views.delete, name='delete')
]