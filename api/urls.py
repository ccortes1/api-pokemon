from django.urls import path, re_path
from api import views

urlpatterns = [
    path('pokemon/', views.PokemonList.as_view()),
    path('pokemon/<name_pokemon>', views.PokemonDetail.as_view()),
    #path('pokemon/strong/<int:fuerza_IV>', views.PokemonStrong.as_view()),
    re_path(r'^pokemon/strong/$', views.PokemonStrong.as_view()),
    re_path(r'^pokemon/attack/$', views.PokemonAttack.as_view()),
    #path('pokemon/defense/<int:defense>', views.PokemonDefense.as_view()),
    re_path(r'^pokemon/defense/$', views.PokemonDefense.as_view()),
    re_path(r'^pokemon/type/$', views.PokemonType.as_view()),
    re_path(r'^pokemon/predict/$', views.PokemonPredictLegendary.as_view()),
    re_path(r'^pokemon/legendary/$', views.PokemonLegendary.as_view()),
]


