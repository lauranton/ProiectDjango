from django.urls import path
from aplicatie3 import views
app_name = 'studenti'

urlpatterns = [
    path('', views.StudentiView.as_view(), name='lista_studenti'),
    path('adaugare/', views.CreateStudentiView.as_view(), name='adauga'),
    path('<int:pk>/update/', views.UpdateStudentiView.as_view(), name='update'),
    path('<int:pk>/stergere/', views.delete_student, name='sterge'),
    path('<int:pk>/activeaza/', views.activate_student, name='activeaza'),

]