from django.db import models

"""from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])"""


class Pokemon2(models.Model):
    #id_pokemon
    pokedex_number = models.IntegerField()
    name_pokemon = models.CharField(max_length=100)
    experience_growt = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    abilities = models.CharField(max_length=100)
    generation = models.IntegerField()
    is_legendary = models.IntegerField()
    predict_is_legendary_2 = models.IntegerField()
    fuerza = models.IntegerField()
    fuerza_IV = models.IntegerField()
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)


class Pokemon(models.Model):
    #id_pokemon
    name_pokemon = models.CharField(max_length=100)
    experience_growt = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    hp = models.IntegerField()
    abilities = models.CharField(max_length=100)
    generation = models.IntegerField()
    is_legendary = models.IntegerField()
    predict_is_legendary_2 = models.IntegerField()
    fuerza = models.IntegerField()
    fuerza_IV = models.IntegerField()
    type1 = models.ForeignKey('TypePokemon', on_delete=models.CASCADE, related_name = 'type1')
    type2 = models.ForeignKey('TypePokemon', on_delete=models.CASCADE, related_name = 'type2')




class TypePokemon(models.Model):
    name_type = models.CharField(max_length=100)
    name_type_2 = models.ManyToManyField('self', symmetrical=False, through='Pokemon', through_fields=('type1','type2'))

