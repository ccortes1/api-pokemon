from rest_framework import serializers
from api.models import Pokemon2

class Pokemon2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon2
        fields = [
            'id',
            'pokedex_number',
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
            'descripcion_1',
            'descripcion_2'

        ]




