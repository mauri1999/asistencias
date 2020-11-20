from django.urls import path
from .views import programa_lista, programa_detalle, programa_create, programa_edit,programa_delete, asignar_beneficio, buscar_beneficios, lista_beneficios


app_name = 'programa'
urlpatterns = [
    # programa views
    path('', programa_lista, name='programa_lista'),
    path('<int:pk>/', programa_detalle, name='programa_detalle'),
    path('create/', programa_create, name='programa_create'),
    path('edit/<int:pk>', programa_edit, name='programa_edit'),
    path('delete/', programa_delete, name='programa_delete'),
    path('asignarbeneficio/',asignar_beneficio, name='asignar_beneficio'),
    path('buscarbeneficios/<int:pk>',buscar_beneficios,name='buscar_beneficios'),
    path('listabeneficios/<int:pk>', lista_beneficios,name='lista_beneficios'),
]
