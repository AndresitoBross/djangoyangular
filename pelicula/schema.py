import graphene
from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from pelicula.models import Pelicula

class PeliculaNode(DjangoObjectType):
    class Meta:
        model = Pelicula
        filter_fields = {'nombre':['exact', 'icontains', 'istartswith'], 
        'descripcion':['exact', 'icontains', 'istartswith'],
        'categoria':['exact', 'icontains', 'istartswith'],
        'genero':['exact', 'icontains', 'istartswith'],
        'fecha':['exact', 'icontains', 'istartswith'],}
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    pelicula = relay.Node.Field(PeliculaNode)
    all_pelicula = DjangoFilterConnectionField(PeliculaNode)

