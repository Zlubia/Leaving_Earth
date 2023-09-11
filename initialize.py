# -*- coding: utf-8 -*-

"""
TABLE DES MATIERES
------------------

def ask_for_players()

def generate_missions()

def show_missions(missions, accomplished_missions)

def initialize_radiation()

def show_radiation_level(radiation_level)

def initialize_locations()


"""




from players import *
from location import *
from missions import *

import time
import random

def ask_for_players():
    """ask how many players and their name
    stock names in list 'players'
    """
    n='a'
    while not (type(n) == int and n>0):
    
        n = input("Welcome to Leaving Earth, how many players are you ? ")
        # atltough Leaving Earth is not playable with more than 5 playsers,
        # it is decided to not give this limitation in this game
        try:
            n = int(n)
        except:
            pass    
    
    players = []
    for i in range(n):
        name= input("Enter a player name: ")
        players.append(Player(name))  # create Player object
        
        if name == "Zluba" or name =="zluba":
            print("\nHello Zluba!")
            print("I can't wait to play with you !")
            print("You've the incredible combination of being the funniest and the best player I've played with.")
            print("Let's fly to some new heights !")
            
        elif name == "Goat" or name =="goat":
            print("\nHello Goat !")
            print("You're by far the best testing officer on deck. <3" )
            print("But if I may... I'd like to ask you something...")
            print("...")
            print("It hurts a little bit everytime I crash.. Please, try not to crash me too many times today.")
            print("\nI'll put a goat in orbit for you.")
            
            
        elif name == "Slougitan" or name == "Slougi" or name == "Tanguy":
            print("\nBonjour Sloughi.")
            print("Je suis très content de jouer avec toi encore.")
            print("Je suis désolé, mes français compétences sont mauvais. Mes créateurs n'ont pas appris le à moi encore.")
            print("I'll continue in english, good luck with your spaceflights !")
            
        else:
            print("\nHello", name)
            
            print("\nNice to meet you, I'm the Game.")
            print("Let's have some fun !")
            
    
    return players


def generate_missions():
    
    missions = []
        
       #name, difficulty, reward, mission_type, goal
        
        #Difficulty can either be easy, medium or hard
        #Reward: amount of victory points awarded after the completion of the mission
        #Mission type: There are 5 types of missions: survey, sample return, probe, manned return, outpost
        #Goal : the location of the goal of the mission.
        #if it's a survey; the location to reveal
        #sample return; the location the sample is from
        #probe; the location the working probe or capsule needs to be
        #manned return; the location the man visited
        #outpost; the location where an astronaut needs to be at the start of the year
        
        
    #Easy Missions
    
    missions.append( Mission("Mars survey", "easy" , 5 , "survey" , "mars"))
    
    missions.append( Mission("Man in space", "easy" , 2 , "man return" , "suborbitalflight"))
    
    missions.append( Mission("Sounding rocket" , "easy" , 1 , "probe" , "suborbitalflight"))
    
    missions.append( Mission("Artificial satellite" , "easy" , 2 , "probe" , "earthorbit"))
    
    missions.append( Mission("Lunar survey" , "easy" , 4 , "survey" , "moon"))
    
    missions.append( Mission("Man in orbit" , "easy" , 4 , "man return", "earthorbit"))
    
    
    #Medium missions
    
    missions.append( Mission("Phobos sample return", "medium" , 12 , "sample return" , "phobos"))
    
    missions.append( Mission("Space station" , "medium" , 6 , "outpost" , "earthorbit"))
    
    missions.append( Mission("Mercury lander" , "medium" , 13 , "probe" , "mercury"))
    
    missions.append( Mission("Venus lander" , "medium" , 11 , "probe" , "venus"))
    
    missions.append( Mission("Mars lander" , "medium" , 7 , "probe", "mars"))
    
    missions.append( Mission("Mercury survey" , "medium" , 7 , "survey" , "mercury"))
    
    missions.append( Mission("Ceres lander" , "medium" , 8 , "probe" , "ceres"))
    
    missions.append( Mission("Man on the Moon" , "medium" , 12 , "man return" , "moon"))
    
    missions.append( Mission("Venus survey" , "medium" , 6 , "survey" , "venus"))
    
    missions.append( Mission("Lunar lander" , "medium" , 6 , "probe" , "moon"))
    
    missions.append( Mission("Lunar sample return" , "medium" , 10 , "sample return" , "moon"))
    
    
    #Hard missions
    
    missions.append( Mission("Mars sample return" , "hard" , 16 , "sample return" , "mars"))
    
    missions.append( Mission("Ceres sample return" , "hard" , 14 , "sample return" , "ceres"))
    
    missions.append( Mission("Mercury sample return" , "hard" , 19 , "sample return" , "mercury"))
    
    missions.append( Mission("Venus station" , "hard" , 27 , "outpost" , "venus"))
    
    missions.append( Mission("Man on Mars" , "hard" , 24 , "man return" , "mars"))
    
    missions.append( Mission("Lunar station" , "hard" , 15 , "outpost" , "moon"))
    
    missions.append( Mission("Mars station" , "hard" , 20 , "outpost" , "mars"))
    
    missions.append( Mission("Extraterrestrial life" , "hard" , 40 , "sample return" , "life"))
    
    missions.append( Mission("Man on Venus" , "hard" , 32 , "man return" , "venus"))
    
    missions.append( Mission("Venus sample return" , "hard" , 24 , "sample return" , "venus"))
    
    
    # make lists of easy, medium and hard missions
    
    easy_missions = [element for element in missions if element.difficulty == "easy"]
    
    medium_missions = [element for element in missions if element.difficulty == "medium"]
    
    hard_missions = [element for element in missions if element.difficulty == "hard"]
    
    
    # shuffle the lists of easy, medium and hard missions
    
    random.shuffle(easy_missions)
    random.shuffle(medium_missions)
    random.shuffle(hard_missions)
    
    boucle = True
    
    while boucle == True:
        #choose the challenge level:    
        print("\n Which challenge would you like to face for this game? \n 1: Easy \n 2: Normal \n 3: Hard \n 4: Very Hard \n 5: All missions active")
        i = input("enter your choice : ")
        
        #drawing the missions according to the chosen challenge level
        
        if i == '1': 
            # Easy challenge has been chosen : 5 easy missions will de drawn.
            boucle = False
            
            index = len(easy_missions) - 5
            #number of missions that will be removed from the easy_missions list.
            
            while index > 0:
            #remove the spare easy missions 
                del easy_missions[index + 4] # + 4 to remove the last items from the list
                index -= 1
            
            missions = easy_missions
            
            #Sort missions based on their rewards from lowest to highest values
            missions.sort(key = lambda x: x.reward)
            
            print("\nYou have chosen the easy challenge")
            print("Starting with small steps is always the wisest way \n")
            print("5 easy missions have been drawn : ")
            print("",missions[0].name, missions[1].name, missions[2].name ,missions[3].name ,missions[4].name , sep = "\n - ")
        
            
        elif i == '2':
            # Normal challenge has been chosen : 4 easy and 2 medium missions will be drawn
            boucle = False
            
            #list of easy missions
            
            index = len(easy_missions) - 4
            #number of missions that will be removed from the easy_missions list.
            
            while index > 0:
            #remove the spare easy missions 
                del easy_missions[index + 3] # + 3 to remove the last items from the list
                index -= 1
                
                
            #list of medium missions
            
            index = len(medium_missions) - 2
            #number of missions that will be removed from the medium_missions list.
            
            while index > 0:
            #remove the spare medium missions 
                del medium_missions[index + 1] # + 1 to remove the last items from the list
                index -= 1
            
            
            
            missions = easy_missions + medium_missions
            
            #Sort missions based on their rewards from lowest to highest values
            missions.sort(key = lambda x: x.reward)
            
            print("\nYou have chosen the normal challenge")
            print("Fly safe ! \n")
            print("4 easy and 2 medium missions have been drawn : ")
            print("", missions[0].name, missions[1].name, missions[2].name ,missions[3].name ,missions[4].name, missions[5].name , sep = "\n - ")
            
            
        elif i == '3':    
            # Hard challenge has been chosen : 3 easy, 3 medium and 2 hard missions will be drawn
            boucle = False
            
            #list of easy missions
            
            index = len(easy_missions) - 3
            #number of missions that will be removed from the easy_missions list.
            
            while index > 0:
            #remove the spare easy missions 
                del easy_missions[index + 2] # + 2 to remove the last items from the list
                index -= 1
            
            
            #list of medium missions
            
            index = len(medium_missions) - 3
            #number of missions that will be removed from the medium_missions list.
            
            while index > 0:
            #remove the spare medium missions 
                del medium_missions[index + 2] # + 2 to remove the last items from the list
                index -= 1
                
                
            #list of hard missions
            
            index = len(hard_missions) - 2
            #number of missions that will be removed from the medium_missions list.
            
            while index > 0:
            #remove the spare medium missions 
                del hard_missions[index + 1] # + 1 to remove the last items from the list
                index -= 1
            
            
            missions = easy_missions + medium_missions + hard_missions
            
            #Sort missions based on their rewards from lowest to highest values
            missions.sort(key = lambda x: x.reward)
            
            print("\nYou have chosen the hard challenge")
            print("A bold and big thinker !  \n")
            print("3 easy, 3 medium and 2 hard missions have been drawn : ")
            print("", missions[0].name, missions[1].name, missions[2].name ,missions[3].name ,missions[4].name, 
                  missions[5].name , missions[6].name , missions[7].name, sep = "\n - ")
            
            
        elif i == '4':    
            # Very Hard challenge has been chosen : 1 easy, 4 medium and 4 hard missions will be drawn
            boucle = False
            
            #list of easy missions
            
            index = len(easy_missions) - 1
            #number of missions that will be removed from the easy_missions list.
            
            while index > 0:
            #remove the spare easy missions 
                del easy_missions[index] # remove the last items from the list
                index -= 1
                
            
            
            #list of medium missions
            
            index = len(medium_missions) - 4
            #number of missions that will be removed from the medium_missions list.
            
            while index > 0:
            #remove the spare medium missions 
                del medium_missions[index + 3] # + 2 to remove the last items from the list
                index -= 1
                
                
            #list of hard missions
            
            index = len(hard_missions) - 4
            #number of missions that will be removed from the medium_missions list.
        
            
            while index > 0:
            #remove the spare medium missions 
                del hard_missions[index + 3] # + 1 to remove the last items from the list
                index -= 1
            
            
            missions = easy_missions + medium_missions + hard_missions
            
            #Sort missions based on their rewards from lowest to highest values
            missions.sort(key = lambda x: x.reward)
            
            print("\nYou have chosen the very hard challenge")
            print("You're crazy ! Is your name Elon?  \n")
            print("1 easy, 4 medium and 4 hard missions have been drawn : ")
            print("", missions[0].name, missions[1].name, missions[2].name ,missions[3].name ,missions[4].name, 
                  missions[5].name , missions[6].name , missions[7].name, missions[8].name, sep = "\n - ")
            
            
        elif i =='5':
            #All missions are available
            boucle = False
            
            missions = easy_missions + medium_missions + hard_missions
            
            #Sort missions based on their rewards from lowest to highest values
            missions.sort(key = lambda x: x.reward)
            
            print("\nYou have chosen to activate all the missions")
            print("You could not choose right? Good luck with finishing all missions before your time runs out..  \n")
            print("Beware this is not an official configuration. \n")
            print("6 easy, 11 medium and 10 hard missions have been drawn : ")
            print("", missions[0].name, missions[1].name, missions[2].name ,missions[3].name ,missions[4].name, 
                  missions[5].name , missions[6].name , missions[7].name, missions[8].name, missions[9].name,
                  missions[10].name, missions[11].name, missions[12].name, missions[13].name, missions[14].name,
                  missions[15].name, missions[16].name, missions[17].name, missions[18].name, missions[19].name,
                  missions[20].name, missions[21].name, missions[22].name, missions[23].name, missions[24].name,
                  missions[25].name, missions[26].name, sep = "\n - ")
            
        elif i =='6' or i =='0':
            #some fun
            print("Aha, I see..")
            print("You're the funny one, aren't you?")
            print("\nWell, as a funny game, I like funny people. I'll set up a funny game for you.")
            print("\n...\n")
            print("0 easy, 0 medium and 0 hard missions have been drawn.")
            boucle = False
            
                        
        
        else:
            
            print("\n Please read the instructions carefully and answer something plausible")
            
            # list of active missions, 2-uple : name, points
            # Coder le tirage au sort des missions en fonction du niveau de locationiculté
            # choisi
            # Pour le cas 5, mettre toutes les missions en jeu mais afficher un message
            # prévenant les joueurs que la partie ne peux pas être considérée comme
            # officielle
        
    # i = input("Press enter to start the game...")
        
    return missions

def show_missions(missions, accomplished_missions):
    # function to make player able to check current missions.
    # I suggest to use it at the end of initialize_missions() and on player demand
    
    print("\nlist of active missions and points \n")
    
    index = len(missions) -1

    while index >= 0:
        print(missions[index].name , " - " , missions[index].reward)
        index -= 1
    
    print("\n \nlist of accomplished missions and points\n")
    
    index = len(accomplished_missions) -1

    while index >= 0:
        print(accomplished_missions[index].name , " - " , accomplished_missions[index].reward)
        index -= 1

#def start_of_the_game(missions):
#    print("Initialization of solar system...")
#    solar_system = Univers()
#    time.sleep(2)
#    print("Each player receives 25 M$ to start")
#    time.sleep(2)
#    print("Some missions are available for your research program \n")
#    for elem in missions:
#        print("Mission: {0} for {1} points".format(elem[0], elem[1]))
#    time.sleep(2)
#    print("\n"); print("Be smart, be excellent, be spatial")
#    print("#######################################")
#    time.sleep(2)
    
#def initialize_objects():
#    """Create 1 of each buyable object"""
#    juno = Rocket("juno", 1, 1, 4)
#    atlas = Rocket("atlas", 5, 4, 27)
#    soyuz = Rocket("soyuz", 8, 9, 80)
#    saturn = Rocket("saturn", 15, 20, 200)
    
def initialize_radiation():
    
    radiation_level = random.choice([0,1,2])
    
    return radiation_level


def show_radiation_level(radiation_level):

    print("The Solar Radiation level is: {0}".format(radiation_level))
    
    
def initialize_locations():
    
    locations = {} # locations have to put in a dictionnary to make easier the return with only 1 variable
    # name
    #Encoder maneuvres sous forme de dictionnaire de listes [difficulté, time tokens, "hasards: no hasard, solar radiation, reentry, landing, optionnal landing"]
    #list of locations that we can survey from this location.
    #auto maneuver - par défaut = "no auto maneuver"
    #no effect, spacecraft destroyed, minerals, supplies, sickness, radiation, life, alien origin , astronaut incapacitated - par défaut = ["no effect"]
    #boolean, True if the location is explorable
    #boolean, True if the location has already been explored
    
    locations["earth"] = Location("earth", 
                     {"suborbitalflight":[3 , 0] , 
                      "earthorbit" : [8 , 0] })
    
    locations["suborbitalflight"] = Location("suborbitalflight", 
                                 {"earthorbit" : [5 , 0] , 
                                  "earth" : [0 , 0 , "optionnal landing"]}, 
                                  [] ,
                                 "earth", 
                                 random.choice(["no effect" , "no effect" , "roll 1 : astronaut incapacitated" , "roll 1-3 : astronaut incapacitated" ]),
                                 True)
    
    locations["earthorbit"] = Location("earthorbit", 
                           {"earth" : [0 , 0 , "reentry" , "optionnal landing" ], 
                            "marsorbit" : [5 , 3 , "solar radiation"], 
                            "marsflyby" : [3 , 3 , "solar radiation"],
                            "innerplanetstransfer" : [ 3 , 1 ],
                            "outerplanetstransfer" : [6 , 1 , "solar radiation"],
                            "lunarorbit" : [3 , 0 ],
                            "lunarflyby" : [1 , 0]},
                            ["solarradiation"])
    
    locations["lunarflyby"] = Location("lunarflyby",
                           {"earthorbit" : [1 , 0],
                            "lunarorbit" : [2 , 0],
                            "moon" : [4 , 0 , "landing"]},
                            ["moon" , "solar radiation"],
                            "lost")
    
    locations["lunarorbit"] = Location("lunarorbit",
                           {"earthorbit" : [3 , 0],
                            "moon" : [2, 0 , "landing"]},
                            ["moon"])
    
    locations["moon"] = Location("moon",
                    {"lunarorbit" : [2, 0]},
                    [],
                    "no auto maneuver",
                    random.choice(["no effect", {"minerals" : 25}, "life" , "spacecraft destroyed"]),
                    True)
    
    locations["marsflyby"] = Location("marsflyby",
                          {"marsorbit" : [3 , 0],
                           "mars" : [3 , 0 , "reentry", "landing"]},
                           ["mars"],
                           "lost")
    
    locations["marsorbit"] = Location("marsorbit",
                          {"mars" : [0 , 0 , "reentry", "landing"],
                           "phobos" : [1 , 0 , "landing"],
                           "outerplanetstransfer" : [5 , 1 , "solar radiation"],
                           "innerplanetstransfer" : [4 , 2 , "solar radiation"],
                           "earthorbit" : [5 , 3 , "solar radiation"]},
                           ["phobos" , "mars" , "solarradiation"])
    
    locations["mars"] = Location("mars",
                    {"marsorbit" : [3 , 0 ]},
                    [],
                    "no auto maneuver",
                    random.choice(["no effect", {"minerals" : 50} , ("life", "supplies")]),
                    True)
    
    locations["phobos"] = Location("phobos",
                                   {"marsorbit" : [ 1 , 0 ]},
                                   [],
                                   "no auto maneuver",
                                   random.choice(["no effect" , "no effect" , "alien origin"]),
                                   True)
    
    locations["innerplanetstransfer"] = Location("innerplanetstransfer",
                                      {"earthorbit" : [3 , 1],
                                      "marsorbit" : [4 , 2 , "solar radiation"],
                                      "ceres" : [5 , 1 , "solar radiation" , "landing"],
                                      "venusorbit" : [3 , 1 , "solar radiation"],
                                      "venusflyby" : [2 , 1 , "solar radiation"],
                                      "mercuryflyby" : [5 , 1 , "solar radiation"]},
                                       ["ceres","solarradiation"]
                                       , "lost")
    
    locations["venusflyby"] = Location("venusflyby",
                                        {"venusorbit" : [1 , 0],
                                         "venus" : [1 , 0 , "reentry" , "optionnal landing"]},
                                         ["venus"],
                                         "lost")
    
    locations["venusorbit"] = Location("venus_orbit",
                                        {"innerplanets_transfer" : [ 3 , 1 , "solar radiation"],
                                         "outerplanets_transfer" : [ 9 , 1 , "solar radiation"],
                                         "venus" : [ 0 , 0 , "reentry" , "optionnal landing"]},
                                         ["venus" , "solarradiation"])
    
    locations["venus"] = Location("venus",
                                  {"venusorbit" : [ 6 , 0 ]},
                                  [],
                                  "no auto maneuver",
                                  random.choice(["spacecraft destroyed" , "spacecraft destroyed" , "supplies" , ("life" , "supplies")]),
                                  True)
    
    locations["mercuryflyby"] = Location("mercuryflyby",
                                          {"mercuryorbit" : [ 2 , 0 ],
                                           "mercury" : [ 4 , 0 , "landing" ]},
                                           ["mercury"],
                                           "lost")
    
    locations["mercuryorbit"] = Location("mercuryorbit",
                                          {"innerplanetstransfer" : [ 7 , 1 , "solar radiation"],
                                           "mercury" : [ 2 , 0 , "landing"]},
                                           ["mercury" , "solar radiation"])
    
    locations["mercury"] = Location("mercury",
                                     {"mercuryorbit" : [ 2 , 0]},
                                     [],
                                     "no auto maneuver",
                                     random.choice(["no effect", {"minerals" : 50}]),
                                     True)
    
    locations["ceres"] = Location("ceres",
                                   {"outerplanetstransfer" : [ 3 , 1 , "solar radiation"],
                                    "innerplanetstransfer" : [ 5 , 2 , "solar radiation"]},
                                    ["solarradiation"],
                                    "no auto maneuver",
                                    random.choice(["no effect" , "supplies" , {"minerals" : 50} ]),
                                    True)
    
    locations["solarradiation"] = Location("solarradiation", {})
    
    
    return locations

    