from django.urls import path
from aplicatie2 import views

app_name = 'profesori'

urlpatterns = [
    path('', views.ProfesoriView.as_view(), name='lista_profesori'),
    path('adaugare/', views.CreateProfesoriView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateProfesoriView.as_view(), name='update'),
    path('<int:pk>/stergere/', views.delete_profesor, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_profesor, name='activeaza'),
]
