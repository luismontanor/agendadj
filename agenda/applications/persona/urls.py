from django.contrib import admin
from django.urls import path, re_path, include

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersona.as_view(),
        name='Personas'
    ),
    path(
        'api/persona/lista/',
        views.PersonListApiView.as_view(),
    ),
    path(
        'lista/',
        views.PersonListView.as_view(),
        name='lista'
    ),
    path(
        'api/persona/search/<kword>/',
        views.PersonListView.as_view(),
    ),
    path(
        'api/persona/create/',
        views.PersonaCreateApiView.as_view(),
    ),
    path(
        'api/persona/detail/<pk>/',
        views.PersonDetailApiView.as_view(),
        name='persona_detail'
    ),
    path(
        'api/persona/delete/<pk>/',
        views.PersonDeleteApiView.as_view(),
    ),
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateApiView.as_view(),
    ),
    path(
        'api/persona/modify/<pk>/',
        views.PersonRetrieveUpdateApiView.as_view(),
    ),
    #
    path(
        'api/persona/',
        views.PersonApiLista.as_view(),
    ),
    path(
        'api/persona2/',
        views.PersonApiLista2.as_view(),
    ),
    path(
        'api/persona3/',
        views.PersonApiLista3.as_view(),
    ),
    path(
        'api/reuniones/',
        views.ReunionApiLista.as_view(),
    ),
    path(
        'api/reuniones-link/',
        views.ReunionApiListaLink.as_view(),
    ),
    path(
        'api/personas/paginacion/',
        views.PersonPaginationListApiView.as_view(),
    ),
    path(
        'api/reunion/by-jobs/',
        views.ReunionByJobs.as_view(),
    ),
]

