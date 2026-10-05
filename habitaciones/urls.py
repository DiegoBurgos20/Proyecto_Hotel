from django.urls import path

from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("habitaciones/", views.lista_habitaciones, name="lista_habitaciones"),
    path("habitaciones/crear/", views.crear_habitacion, name="crear_habitacion"),
    path(
        "habitaciones/editar/<int:pk>/",
        views.editar_habitacion,
        name="editar_habitacion",
    ),
    path(
        "habitaciones/eliminar/<int:pk>/",
        views.eliminar_habitacion,
        name="eliminar_habitacion",
    ),
]
