
from django.urls import path

from aplicatie1 import views

app_name = 'cursuri'

urlpatterns = [
    path('', views.CursuriView.as_view(), name='lista_cursuri'),
    path('adaugare/', views.CreateCursuriView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateCursuriView.as_view(), name='update'),
    path('<int:pk>/stergere/', views.delete_curs, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_curs, name='activeaza'),

]
