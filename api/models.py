from django.db import models




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
    descripcion_1 = models.CharField(max_length=100)
    descripcion_2 = models.CharField(max_length=100)




