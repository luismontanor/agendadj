#
from dataclasses import fields
from rest_framework import serializers, pagination
#
from .models import Hobbie, Person, Reunion


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')


# Construccion de un serializer sin necesidad de estar conectado a un modelo en especifico
class PersonaSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    # Le ponemo default = False para que no sea obligatorio
    # ya que el campo no se encuentra especificado enb el modelo
    is_active = serializers.BooleanField(required=False)


#
class PersonaSerializer2(serializers.ModelSerializer):

    is_active = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')


#
class ReunionSerializers(serializers.ModelSerializer):

    persona = PersonSerializers()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )


class HobbieSerielizers(serializers.ModelSerializer):

    class Meta:
        model = Hobbie
        fields = ('__all__')


class PersonSerializers3(serializers.ModelSerializer):

    # De esta manera se hace para un serializador en una relacion de muchos a mmuchos
    hobbie = HobbieSerielizers(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbie',
        )


#
class ReunionSerializers2(serializers.ModelSerializer):

    # De esta forma indicamos un nuevo campo con el valor que devuelve un metodo
    fecha_hora = serializers.SerializerMethodField()

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
            # Aunque no pertenezca al modelo es necesario agregar el serializador(SerializerMethodField) al conjunto de atributos
            'fecha_hora',
        )

    # De esta forma definimos una funcion para operar dos campos dentro de un serializer
    # El atributo obj hace referencia a la instancia la cual se esta iterando dentro del conjunto de valores
    def get_fecha_hora(self, obj):
        return str(obj.fecha) + ' - ' + str(obj.hora)


# De la siguiente manera se hace para heredar un link de referencia a otro
# modelo en las relaciones en vez de mandar toda la informacion serializada
class ReunionSerializersLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Reunion
        fields = (
            'id',
            'fecha',
            'hora',
            'asunto',
            'persona',
        )
        # Para referenciar el link hacia los datos del modelo relacionado lo hacemos de la siguiente manera
        extra_kwargs = {
            'persona': {
                'view_name'     :'persona_app:persona_detail',
                'lookup_field'  :'pk'
            }
        }


# De esta maneria se hace un serializador con paginacion
class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100


# Construccion de un serializer sin necesidad de estar conectado a un modelo en especifico
class CountReunionserializer(serializers.Serializer):

    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()