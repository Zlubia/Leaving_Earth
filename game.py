# -*- coding: utf-8 -*-


# from playsound import playsound
from PIL import Image
import re # to use regular expression (re.match(expression, string))

from components import *
#from players import *
from spacecraft import *
from initialize import *
#from game_functions import*
#from location import*
#from advancements import*

#Initialize the game: missions, locations, radiation level
locations = initialize_locations()
radiation_level = initialize_radiation()
missions = generate_missions()

#create an empty list, will be used to remember which mission has been accomplished during the game.
accomplished_missions = []

DEVELOPER_MODE = False
if DEVELOPER_MODE:
    chance = True
    players = []
    players.append(Player("Vlad"))
    players.append(Player("Pif"))
    for p in players:
        p.money = 300
    Vlad = players[0]
    Vlad.points= 35
    Vlad.spacecraft["hermes"] = Spacecraft("hermes", locations["earthorbit"])
    Vlad.spacecraft["artemis"] = Spacecraft("artemis", locations["earthorbit"])
    Vlad.spacecraft["moony"] = Spacecraft("moony", locations["lunarorbit"])
    Vlad.spacecraft["moony2"] = Spacecraft("moony2", locations["lunarorbit"])
    Moony = Vlad.spacecraft["moony"]
    Moony2 = Vlad.spacecraft["moony2"]
    Moony.component = [obj("probe"), obj("atlas"), obj("pilot")]
    Moony2.component = [obj("probe")]
    Vlad.component.append(obj("juno"))
    Hermes = Vlad.spacecraft["hermes"]
    Artemis =  Vlad.spacecraft["artemis"]
    Hermes.component = [  obj("juno"), obj("juno"), obj("juno"), obj("atlas"), obj("atlas"), obj("saturn"), obj("saturn"), obj("saturn"), obj("apollo"), obj("ionthruster"), obj("ionthruster"), obj("ionthruster"),obj("pilot"), obj("mech"), obj("supply")]
    Artemis.component = [obj("juno"), obj("probe"),  obj("apollo"), obj("pilot")]
    Hermes.mass = 75
    Artemis.mass = 1+20+4+4+4+4
    Moony.mass = 5
    Vlad.advancements["juno"] = Advancement("juno", chance)
    Vlad.advancements["ionthruster"] = Advancement("ionthruster", chance)
    Vlad.advancements["atlas"] = Advancement("atlas", chance)
    Vlad.advancements["saturn"] = Advancement("saturn", chance)
    Vlad.advancements["surveying"] = Advancement("surveying", chance)
    Vlad.advancements["landing"] = Advancement("landing", chance)
    Vlad.advancements["rendezvous"] = Advancement("rendezvous", chance)
    Vlad.advancements["reentry"] = Advancement("reentry", chance)
    Vlad.advancements["lifesupport"] = Advancement("lifesupport", chance)
    
    Pif = players[1]
    Pif.points = 0
else:
    players = ask_for_players()

game_finished = False

year = 1956 # starting year  , could be changed for outer planets
end_of_game = 1976 # could be changed for outer planet


end_of_year = False

img = Image.open('actions_list.jpg')
img.show()

# game is starting here
while (not game_finished and year <= end_of_game): # while game is not finish, loop this
    #new year
    print("\n ================================ \n we are in {0} \n ================================".format(year)) 

    p = 0 # used to track active player       

    while (not end_of_year): # loop this until every player has finished the year
        
        if players[p].active == True:           # check that player has not finished its turn
            choice = players[p].actions_list()  # ask choice
            p, locations, end_of_year = players[p].actions(choice, p, locations, players, end_of_year, missions, radiation_level, accomplished_missions, show_missions)  # actions, regarding the choice
                #return p to know who's active player after each action
                #return location because some location could be affected by actions
        else: 
            p = next_player(players, p)
                        
        
    # end of year
    players = end_of_year_actions(players) # actions taken at end of year, choose of first player
    year +=1 # year is incremented
    end_of_year = False
    players, missions, accomplished_missions = begin_of_year(players, locations, missions, accomplished_missions) # actions affecting players at begin of year

game_is_done()
