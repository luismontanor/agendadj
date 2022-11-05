#
from model_utils.models import TimeStampedModel
#
from django.db import models
#
from .managers import Reunionmanager

#
class Hobbie(TimeStampedModel):
    """Model definition for Hobbie."""

    hobbie = models.CharField('Pasatiempo', max_length=50)

    class Meta:
        """Meta definition for Hobbie."""

        verbose_name = 'Hobbie'
        verbose_name_plural = 'Hobbies'

    def __str__(self):
        """Unicode representation of Hobbie."""
        return self.hobbie


#
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """

    full_name = models.CharField(
        'Nombres',
        max_length=50,
    )
    job = models.CharField(
        'Trabajo',
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobbie = models.ManyToManyField(Hobbie)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return self.full_name


class Reunion(TimeStampedModel):
    """Model definition for Reunion."""

    persona = models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField('Asunto de reunión', max_length=100)


    objects = Reunionmanager()

    class Meta:
        """Meta definition for Reunion."""

        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'

    def __str__(self):
        """Unicode representation of Reunion."""
        return self.asunto
