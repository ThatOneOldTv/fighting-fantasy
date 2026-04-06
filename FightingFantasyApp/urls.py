from django.urls import path

from FightingFantasyApp.views import home, play

urlpatterns = [
    path("", home.main_menu, name="home"),
    path("new_adventure/", home.new_adventure, name="new_adventure"),
    path("get_adventures/", home.get_adventures, name="get_adventures")
]