from django.shortcuts import render

from django.views.generic import ListView, TemplateView
#
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)
#
from .models import Person, Reunion
#
from .serializers import (
    PersonSerializers,
    PersonaSerializer,
    PersonaSerializer2,
    ReunionSerializers,
    PersonSerializers3,
    ReunionSerializersLink,
    PersonPagination,
    CountReunionserializer
)


class ListaPersona(ListView):
    model = Person
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()


# Construccion de una api para listar personas
class PersonListApiView(ListAPIView):

    # En toda construccion de una api es importante un serializador
    # Esto indica el foprmato en el que se va a serializar nuestra api ejemplo(json)
    serializer_class = PersonSerializers

    # Necesitamos un get.queryset para generar una lista
    def get_queryset(self):
        return Person.objects.all()


class PersonListView(TemplateView):
    template_name = "persona/lista.html"


#
class PersonSearchApiView(ListAPIView):

    # En toda construccion de una api es importante un serializador
    # Esto indica el foprmato en el que se va a serializar nuestra api ejemplo(json)
    serializer_class = PersonSerializers

    # Necesitamos un get.queryset para generar una lista
    def get_queryset(self):
        # Filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )


class PersonaCreateApiView(CreateAPIView):

    # El CreateApiView necesita de un serializer
    serializer_class = PersonSerializers


class PersonDetailApiView(RetrieveAPIView):

    # El RetrieveAPIView necesita de un serializer
    serializer_class = PersonSerializers

    # El RetrieveAPIView necesita especificar el parametro queryset
    # Al igual que todas las vistas de djangop rest framework que necesiten de un modelo
    queryset = Person.objects.all()


class PersonDeleteApiView(DestroyAPIView):

    # El RetrieveAPIView necesita de un serializer
    serializer_class = PersonSerializers

    # El RetrieveAPIView necesita especificar el parametro queryset
    # Al igual que todas las vistas de djangop rest framework que necesiten de un modelo
    queryset = Person.objects.all()


class PersonUpdateApiView(UpdateAPIView):

    # El RetrieveAPIView necesita de un serializer
    serializer_class = PersonSerializers

    # El RetrieveAPIView necesita especificar el parametro queryset
    # Al igual que todas las vistas de djangop rest framework que necesiten de un modelo
    queryset = Person.objects.all()


class PersonRetrieveUpdateApiView(RetrieveUpdateAPIView):

    # El RetrieveAPIView necesita de un serializer
    serializer_class = PersonSerializers

    # El RetrieveAPIView necesita especificar el parametro queryset
    # Al igual que todas las vistas de djangop rest framework que necesiten de un modelo
    queryset = Person.objects.all()


class PersonApiLista(ListAPIView):

    """Vista para interactuar con un serializer construido sin
    la necesidad de estar conectado a un modelo en especifico"""

    serializer_class = PersonaSerializer

    # Sobreescribimos la funcion get_queryset
    def get_queryset(self):
        return Person.objects.all()


class PersonApiLista2(ListAPIView):

    """Vista para interactuar con un serializer construido sin
    la necesidad de estar conectado a un modelo en especifico"""

    serializer_class = PersonaSerializer2

    # Sobreescribimos la funcion get_queryset
    def get_queryset(self):
        return Person.objects.all()


class ReunionApiLista(ListAPIView):

    serializer_class = ReunionSerializers

    # Sobreescribimos la funcion get_queryset
    def get_queryset(self):
        return Reunion.objects.all()


class PersonApiLista3(ListAPIView):

    serializer_class = PersonSerializers3

    # Sobreescribimos la funcion get_queryset
    def get_queryset(self):
        return Person.objects.all()


class ReunionApiListaLink(ListAPIView):

    serializer_class = ReunionSerializersLink

    # Sobreescribimos la funcion get_queryset
    def get_queryset(self):
        return Reunion.objects.all()


# Construccion de una api para listar personas con paginacion
class PersonPaginationListApiView(ListAPIView):

    # En toda construccion de una api es importante un serializador
    # Esto indica el foprmato en el que se va a serializar nuestra api ejemplo(json)
    serializer_class = PersonSerializers

    pagination_class = PersonPagination

    # Necesitamos un get.queryset para generar una lista
    def get_queryset(self):
        return Person.objects.all()


# Vista para el serializer de un manager
class ReunionByJobs(ListAPIView):

    serializer_class = CountReunionserializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reuniones_job()