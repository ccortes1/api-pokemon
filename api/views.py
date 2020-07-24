from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
#from django.views.decorators.csrf import csrf_exempt

from api.models import Pokemon2
from api.serializers import Pokemon2Serializer
#from rest_framework.parsers import JSONParser
from django.http import  Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
import django_filters.rest_framework 


class PokemonList(APIView):
    """
    list all pokemon
    """
    def get(self, request, format=None):
        pokemons = Pokemon2.objects.all()
        serializer = Pokemon2Serializer(pokemons, many=True)
        return Response(serializer.data)

class PokemonDetail(APIView):
    """
    detail a pokemon
    """
    def get_object(self, name_pokemon):
        try:
            return Pokemon2.objects.get(name_pokemon=name_pokemon)
        except Pokemon2.DoesNotExist:
            raise Http404

    def get(self, request, name_pokemon, format=None):
        pokemon = self.get_object(name_pokemon)
        serializer = Pokemon2Serializer(pokemon)
        return Response(serializer.data)

class PokemonStrong(generics.ListAPIView):
    queryset = Pokemon2.objects.all()
    serializer_class = Pokemon2Serializer
    
    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('fuerza_IV', None)
        print(value)
        return self.queryset.filter(fuerza_IV=value)


class PokemonAttack(generics.ListAPIView):
    queryset = Pokemon2.objects.all()
    serializer_class = Pokemon2Serializer
    
    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('attack', None)
        return self.queryset.filter(attack=value)


class PokemonDefense(generics.ListAPIView):
    queryset = Pokemon2.objects.all()
    serializer_class = Pokemon2Serializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('defense', None)
        print(value)
        return self.queryset.filter(defense=value)


class PokemonType(generics.ListAPIView):
    queryset = Pokemon2.objects.all()
    serializer_class = Pokemon2Serializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('type', None)
        print(value)
        return self.queryset.filter(type1=value)


class PokemonPredictLegendary(generics.ListAPIView):
    queryset = Pokemon2.objects.all()
    serializer_class = Pokemon2Serializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('predict_is_legendary', None)
        print(value)
        return self.queryset.filter(predict_is_legendary_2=value)



        
        

"""
def pokemon_list(request):
    
    pokemons = Pokemon2.objects.all()
    serializer = Pokemon2Serializer(pokemons, many=True)

    return JsonResponse(serializer.data, safe=False)

def pokemon_detail(request, name_pokemon):
    try:
        pokemon = Pokemon2.objects.get(name_pokemon=name_pokemon)
    except Pokemon.DoesNotExist:
        return HttpResponse(status=404)

    serializer = Pokemon2Serializer(pokemon)
    
    return JsonResponse(serializer.data)
"""



