from rest_framework import serializers
from api.models import Pokemon, TypePokemon

class Pokemon2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name_pokemon',
            'experience_growt',
            'attack',
            'defense',
            'sp_attack',
            'sp_defense',
            'speed',
            'hp',
            'abilities',
            'generation',
            'is_legendary',
            'predict_is_legendary_2',
            #'fuerza',
            'fuerza_IV',
            'type1',
            'type2',
        ]

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name_pokemon',
            'experience_growt',
            'attack',
            'defense',
            'sp_attack',
            'sp_defense',
            'speed',
            'hp',
            'abilities',
            'generation',
            'is_legendary',
            'predict_is_legendary_2',
            #'fuerza',
            'fuerza_IV',
            'type1',
            'type2',
            ]

class TypePokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypePokemon
        fields = ['name_type']



