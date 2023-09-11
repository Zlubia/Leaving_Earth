# -*- coding: utf-8 -*-


"""
TABLE DES MATIERES
------------------

def next_player(players, p)

def check_missions(locations, missions, players, p, accomplished_missions)
    
def begin_of_year(players, locations, missions, accomplished_missions)

def end_of_year_actions(players)

def obj(name)

def game_is_done()

def get_exploration_results(explo_type, radiation_level, locations, loc)

def ask_for_sharing_explo(explo_type)


"""




from numpy import argmin
from components import *

import math

def next_player(players, p):
    p = p+1
    if p == len(players): #♦If the last player has played, start at first player again.
        p = 0
    return p

def check_missions(locations, missions, players, p, accomplished_missions):
    
    sound_mission_accomplished = '277441__xtrgamr__tones-of-victory.wav'
    
    #fonction qui vérifie les missions ---- En construction
    
    list_size = len(missions)
    
    index = 0
    
    while index < list_size:

        #print(missions[index].name)        
        
        #1) Vérifier missions Survey        
        if missions[index].type == "survey":
            
            survey_goal = missions[index].goal
                
            if locations[survey_goal].explored == True:
                
                print("\nMission accomplished, you're the first agency to survey {0} !".format(survey_goal))
                
                #give the reward for the mission to the active player:
                players[p].points = players[p].points + missions[index].reward
                
                print("\n{0} you earn {1} points for this accomplishement.".format(players[p].name , missions[index].reward))
                
                print("\nWhich brings your total points to {0} !".format(players[p].points))
                
                #give all other players 10$
                if len(players) > 1:
                    print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                players[p].money = players[p].money - 10 #preventing active player to receive the extra funding.
                
                for player in players: #this gives every player +10 $
                    player.money = player.money + 10
                    print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                              
                #delete mission from the list (or better, move it to 'mission accomplished' list) 
                accomplished_missions.append(missions[index])
                del missions[index]
                #correction d'index et de list_size parce qu'un élément a été supprimé.
                index -= 1
                list_size -= 1
        

        #2) Vérifier missions Probe
        elif missions[index].type == "probe":
        
            probe_goal = missions[index].goal
            
            #Parcourir les spacecraft du joueurs:
            for spaceship in players[p].spacecraft:
                
                #si un spacecraft se trouve sur le lieu de l'objectif:
                # + cas particulier, si un spaceraft est passé par suborbital flight sans s'y arrêter
                if players[p].spacecraft[spaceship].location.name == probe_goal or (probe_goal == 'suborbitalflight' and players[p].spacecraft[spaceship].location.name == 'earthorbit'):
                    
                    #check si une capsule ou probe en état de marche est à bord du spacecraft:
                    for comp in players[p].spacecraft[spaceship].component:
                        if type(comp) in [Probe, Capsule] and comp.state == 1:
                            
                            print("\nMission accomplished, you're the first agency to bring a functional probe to {0} !".format(probe_goal))
                            
                            #give the reward for the mission to the active player:
                            players[p].points = players[p].points + missions[index].reward
                            
                            print("\n{0} you earn {1} points for this accomplishement.".format(players[p].name , missions[index].reward))
                            
                            print("\nWhich brings your total points to {0} !".format(players[p].points))
                            
                            #give all other players 10$
                            if len(players) > 1:
                                print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                            players[p].money = players[p].money - 10 #preventing active player to receive the extra funding.
                            
                            for player in players: #this gives every player +10 $
                                player.money = player.money + 10
                                print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                                          
                            #delete mission from the list (or better, move it to 'mission accomplished' list) 
                            accomplished_missions.append(missions[index])
                            del missions[index]
                            #correction d'index et de list_size parce qu'un élément a été supprimé.
                            index -= 1
                            list_size -= 1
    
    
    
        elif missions[index].type == "sample return":
            
            sample_goal = missions[index].goal
            
            #Parcourir les spacecraft du joueurs:
            for spaceship in players[p].spacecraft:
                
                #check s'il y en a un sur terre
                if players[p].spacecraft[spaceship].location.name == "earth":
                    
                    #parcourir les composants
                    for comp in players[p].spacecraft[spaceship].component:
                        
                        #s'il y a un sample parmis les composant vérifier s'il correspond à la mission.
                        if type(comp) == Sample and comp.location == sample_goal:
                            
                            print("\nMission accomplished, you're the first agency to bring a sample from {0} back on Earth !".format(sample_goal))
                
                            #give the reward for the mission to the active player:
                            players[p].points = players[p].points + missions[index].reward
                            
                            print("\n{0} you earn {1} points for this accomplishement.".format(players[p].name , missions[index].reward))
                            
                            print("\nWhich brings your total points to {0} !".format(players[p].points))
                            
                            #give all other players 10$
                            if len(players) > 1:
                                print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                            players[p].money = players[p].money - 10 #preventing active player to receive the extra funding.
                            
                            for player in players: #this gives every player +10 $
                                player.money = player.money + 10
                                print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                                          
                            #delete mission from the list (or better, move it to 'mission accomplished' list) 
                            accomplished_missions.append(missions[index])
                            del missions[index]
                            #correction d'index et de list_size parce qu'un élément a été supprimé.
                            index -= 1
                            list_size -= 1
                            
                        if type(comp) == Sample and sample_goal == 'life' and comp.life == True:
                            
                            print("\nMISSION EXTRATERESTRIAL LIFE ACCOMPLISHED !!!!, you're the first agency to bring a life sample, from {0} back on Earth !".format(comp.location))
                
                            #give the reward for the mission to the active player:
                            players[p].points = players[p].points + missions[index].reward
                            
                            print("\n{0} you earn {1} points for this accomplishement.".format(players[p].name , missions[index].reward))
                            
                            print("\nWhich brings your total points to {0} !".format(players[p].points))
                            
                            #give all other players 10$
                            if len(players) > 1:
                                print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                            players[p].money = players[p].money - 10 #preventing active player to receive the extra funding.
                            
                            for player in players: #this gives every player +10 $
                                player.money = player.money + 10
                                print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                                          
                            #delete mission from the list (or better, move it to 'mission accomplished' list) 
                            accomplished_missions.append(missions[index])
                            del missions[index]
                            #correction d'index et de list_size parce qu'un élément a été supprimé.
                            index -= 1
                            list_size -= 1
        
        

        elif missions[index].type == "man return":
            
            man_return_goal = missions[index].goal
            
            #Parcourir les spacecraft du joueurs:
            for spaceship in players[p].spacecraft:
                
                #check s'il y en a un sur terre
                if players[p].spacecraft[spaceship].location.name == "earth":
                    
                    #parcourir les composants
                    for comp in players[p].spacecraft[spaceship].component:
                        
                        
                        if type(comp) == Astronaut and (man_return_goal in comp.route or (man_return_goal == 'suborbitalflight' and 'earthorbit' in comp.route)):
                            # particular case of an astronaut going in space without make a stop in suborbitalflight
                            
                            print("\nMission accomplished, you're the first agency to bring an astronaut from {0} back on Earth !".format(man_return_goal))
                
                            #give the reward for the mission to the active player:
                            players[p].points = players[p].points + missions[index].reward
                            #playsound(sound_mission_accomplished)
                            
                            print("\n{0} you earn {1} points for this accomplishement.".format(players[p].name , missions[index].reward))
                            
                            print("\nWhich brings your total points to {0} !".format(players[p].points))
                            
                            #give all other players 10$
                            if len(players) > 1:
                                print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                            players[p].money = players[p].money - 10 #preventing active player to receive the extra funding.
                            
                            for player in players: #this gives every player +10 $
                                player.money = player.money + 10
                                print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                                          
                            #delete mission from the list (or better, move it to 'mission accomplished' list) 
                            accomplished_missions.append(missions[index])
                            del missions[index]
                            #correction d'index et de list_size parce qu'un élément a été supprimé.
                            index -= 1
                            list_size -= 1
                
            
        index += 1


    return players, missions, accomplished_missions
      
        
        
  

def begin_of_year(players, locations, missions, accomplished_missions):
    """actions to take each year starting:
        - Funding
        - Check start of year missions
        - Turn in samples for money / research
        - Turn order
    """

    
    # 1) everybody's money is 25$
    
    for player in players:
    
        player.active = True  # switch all players to active for the new year
        player.money = 25
        
    
    # 2) Check Start of year missions:
    
        
    list_size = len(missions)
    
    index = 0
    
    while index < list_size:
        
        #Sort players based on their points, lowest values first.
        players.sort(key = lambda x: x.points)
        
        if missions[index].type == "outpost":
        
            for p in players:
        
                for spaceship in p.spacecraft:

                    if p.spacecraft[spaceship].location.name == missions[index].goal :
                        
                        for comp in p.spacecraft[spaceship].component:
                        
                            if type(comp) == Astronaut and comp.state == 1 :
                            
                                print("\nMission accomplished, you're the first agency to have a functionnal space station on {0} !".format(missions[index].goal))
                
                                #give the reward for the mission to the active player:
                                p.points = p.points + missions[index].reward
                                
                                print("\n{0} you earn {1} points for this accomplishement.".format(p.name , missions[index].reward))
                                
                                print("\nWhich brings your total points to {0} !".format(p.points))
                                
                                #give all other players 10$
                                if len(players) > 1:
                                    print("\nThe other players receive each 10$ extra funding from their governments to increase their efforts in the space race!")
                                p.money = p.money - 10 #preventing active player to receive the extra funding.
                                
                                for player in players: #this gives every player +10 $
                                    player.money = player.money + 10
                                    print ("\n{0} has now {1}$ in his bank account".format(player.name , player.money))
                                                              
                                #delete mission from the list (or better, move it to 'mission accomplished' list) 
                                accomplished_missions.append(missions[index])
                                del missions[index]
                                #correction d'index et de list_size parce qu'un élément a été supprimé.
                                index -= 1
                                list_size -= 1
                        
        index += 1                    
             
    # 4) Turn in samples on Earth for money / research
    
    #Pour chaque joueur:
    for p in players:
        
        #Chaque spaceship on Earth
        for spaceship in p.spacecraft:
            
            if p.spacecraft[spaceship].location.name == "earth": 
            
                #Chaque Sample à bord
                for comp in p.spacecraft[spaceship].component:
                    
                    if type(comp) == Sample:
                        
                        if comp.value > 0:
                            
                            print("\nYour spacecraft {0} has brought a sample from {1} back on Earth!".format(p.spacecraft[spaceship].name , comp.location))
                        
                            p.money == p.money + comp.value
                        
                            print("\nYou bring it in for {0} $, your funds are now at {1}.".format(comp.value , p.money) )
                            
                        elif comp.research == True:
                            
                            print("\nYour spacecraft {0} has brought a sample from {1} back on Earth!".format(p.spacecraft[spaceship].name , comp.location))
                            
                            print("\nThis sample yields you new scientific knowledge!")
                            boucle == True
                            
                            while boucle == True:
                                print("\nWhat do you want to do?")
                                print("1. You may gain a new advancement with no outcome cards on it.")
                                print("2. You may remove all outcome cards from any one of your existing advancements.")
                                
                                choice = int(input("Enter your choice:"))
                                
                                    
                                if choice == 1:
                                    
                                    adv = input("Which advancement would you like? :")
                                    
                                    if adv in p.advancements.keys():
                                        
                                        print("you have already bought this advancement")
                                    
                                    else:
                                        try:
                                            p.advancement[adv] = Advancement(adv)
                                            
                                            print("You have discovered {0} !".format(adv))
                                            boucle = False
                                                                                        
                                        except:
                                            print("This advancement has not been invented yet in this world!")
                                            
                                elif choice == 2:
                                    
                                    adv = input("From which advancement would you like to remove the outcomes? :" )
                                    
                                    if adv in p.advancements.keys():
                                        
                                        if len(p.advancements[adv].outcomes) == 0:
                                            
                                            print("There's already no outcomes anymore on this advancement. You can choose another one.")
                                            
                                        else:
                                            number_of_outcomes = len(p.advancements[adv].outcomes)
                                            
                                            p.advancements[adv].outcomes = []
                                            
                                            print("You have removed {0} outcomes from {1}.".format(number_of_outcomes, adv))
                                            boucle = False
                                        
                                    else:
                                        
                                        print("You don't posses this advancement.")
                                        
                                        
        

    # 5) turn order:
    players.sort(key = lambda x: x.points)
        
        
    return players, missions, accomplished_missions # p is the first player for next year

def end_of_year_actions(players):
    """actions taken at end of year:
        1) Repair / heal components on Earth -- check
        2) Incapacitated astronauts not on Earth die -- check
        3) Each agency draws an outcome from Life Support for each capsule they have off Earth. 
           If the result is a failure (or ther do not have Life Support), all astronauts aboard the capsule die. 
           If the spacecraft has multiple capsules, astronauts may survive in capsules that succesfully provided 
           life support limited by number of seats.
        4) Astronauts off Earth consume supplies: One supply is enough for up to 5 astronauts. 
           Any astronaut who is not fed dies.
        5) Move calendar marker to the next year. If it is past 1976, the game ends.  (this is done in the main game file) 
        6) Remove one time token from each craft with any on it.
        7) Destroy empty spacecraft *not in the rules."""
    
    for player in players:
        to_destroy = [] #will be filled with empty spacecrafts to destroy, for the player
        
        # 1) Repair components on Earth in the stock of the player
        for comp in player.component:
            if comp.state == 0:
                print("{0} from {1}'s stock is repaired".format(comp.name, player))
                comp.state = 1
                
        #Parcours spacecrafts.        
        for key in player.spacecraft:
            
                       
            # if spacecraft on earth, repair components
            if player.spacecraft[key].location.name == "earth":
                for comp in player.spacecraft[key].component:
                    if comp.state == 0:
                        print("{0} from {1} is repaired".format(comp.name, key))
                        comp.state = 1
            
            # if spacecraft is not on earth        
            elif player.spacecraft[key].location.name != "earth":
                
                for comp in player.spacecraft[key].component:
                    
                    # 2) Incapacitated astronauts not on Earth die
                    if type(comp) == Astronaut and comp.state == 0:
                        
                        print("Incapacitated astronaut {0} from spacecraft {1} dies from his wounds".format(comp.name, player.spacecraft[key].name))
                    
                
                for comp in player.spacecraft[key].component:
                    
                    # 3) Draw a life support outcome for every capsule.    
                    if type(comp) == Capsule:
                        
                        print("\n{0}, you have a {1} capsule on board of {2}, checking capsule's life support.".format(player.name, comp.name, player.spacecraft[key].name))
                        print("...")
                        
                        #Check if player has the life support tech.
                        if "lifesupport" in player.advancements.keys():
                            
                            mech = False
                            
                            #Check if there's a mechanic on board that can help reduce the severity of the outcomes
                            for astro in player.spacecraft[key].component:
                                
                                if type(astro) == Astronaut:
                                    
                                    if astro.name == "mech" and astro.state == 1:
                            
                                        mech = True

                            #draw outcome
                            outcome_result = player.draw_outcome("lifesupport", mech)
                            
                        #if the player doesn't have the life support, it is an automatic failure
                        else:
                            outcome_result = "major failure"
                            print("\nYour astronauts can not survive on long duration flights whithout life support.")
                            print("This is a sad day for space exploration.")
                            
                        
                        #Result of the outcome:
                        if outcome_result == "minor failure" or outcome_result == "major failure":
                            
                            print("\nLife support in {0} failed.".format(comp.name))
                            
                            available_seats = player.spacecraft[key].availableSeats() - comp.capacity
                            
                            killed_astronauts = 0 - available_seats
                            
                            #Kill astronauts            
                            if available_seats < 0:
                                
                                player = player.spacecraft[key].killAstronauts_bis(player, killed_astronauts)   
                        
                        elif outcome_result == "succes":
                            
                            print("\Life support in {0} is working as planned.".format(comp.name))
                        
                #4) Astronauts of earth consume supplies                     
                astronauts_on_board = len(player.spacecraft[key].astronautsOnBoard())
                
                #calculs de nombre de supplies nécéssaires et du nombre de supplies à bord.
                supplies_consumed = math.ceil(astronauts_on_board / 5)
                
                supplies_on_board = player.spacecraft[key].suppliesOnBoard()
                
                #s'il y a des astronautes à bord.
                if astronauts_on_board > 0:
                
                    #s'il y a assez de supplies à board
                    if supplies_consumed <= supplies_on_board:
                        
                        print("\n{2}, Your astronauts on board of {1} consume {0} supplies.".format(supplies_consumed, player.spacecraft[key].name, player.name))
                        
                        #delete supplies consumed
                        while supplies_consumed > 0 :
                            
                            for supply in player.spacecraft[key].component:
                                
                                if type(supply) == Supply:
                                
                                    del supply
                            
                            supplies_consumed =- 1 
                            
                    #s'il n'y a pas assez de supplies à bord        
                    elif supplies_consumed > supplies_on_board:
                        
                        print("\nYou do not have enough supplies onboard of {0} to sustain all your astronauts. \nThis is a sad day for space exploration.".format(player.spacecraft[key].name))
                        
                        #utilisation de tout les supplies à bord
                        for supply in player.spacecraft[key].component:
                                
                                if type(supply) == Supply:
                                
                                    del supply
                    
                        #calcul du nombre d'astronauts qui vont mourir par manque de supplies.
                        supplied_astronauts = astronauts_on_board - (supplies_on_board * 5)
                        
                        hungry_astronauts = math.floor (supplied_astronauts / 5) + (supplied_astronauts % 5)
                        
                        
                        #kill hungry_astronauts
                        
                        player = player.spacecraft[key].killAstronauts_bis(player, hungry_astronauts)
                       
          
                                    
                                    
            
            # 6) Remove timetokens            
            if player.spacecraft[key].ttoken > 0:
                player.spacecraft[key].ttoken -= 1            
            
            #7) delete empty spacecraft with mass of 0
            if len(player.spacecraft[key].component) == 0: #check if empty
                assert player.spacecraft[key].mass == 0 # if this condition is not ok, there is an error
                   
                print("{0}, as your spacecraft {1} is empty, it is removed from the game".format(player.name, player.spacecraft[key].name))
                to_destroy.append(key)
                    
        for elem in to_destroy:        # need to be outside of the existing spacecraft loop to not change size of dictionnary during it is read             
            player.DestroySpacecraft(elem)

            
        
        
    return players
        
#def choice_is_valid():
#    """ check is player input is ok"""
#    return True #for now, all choices are valid
    

def obj(name):
    """function use to return an object from his name as a string"""
    if name   == "juno": return Rocket("juno", 1, 1, 4)
    elif name == "atlas": return Rocket("atlas", 5, 4, 27)
    elif name == "soyuz": return Rocket("soyuz", 8, 9, 80)
    elif name == "saturn": return Rocket("saturn", 15, 20, 200)
    elif name == "ionthruster": return Thruster()
    elif name == "probe": return Probe()
    elif name == "eagle": return Capsule("eagle", 4, 1, 2, False, ["landing"])
    elif name == "apollo": return Capsule("apollo", 4, 3, 3, True, ["reentry"])
    elif name == "vostok": return Capsule("vostok", 2, 2, 1, True, ["reentry"])
    elif name == "aldrin": return Capsule("aldrin", 4, 3, 8, False, ["lifesupport"])
    elif name == "pilot": return Astronaut("pilot" , "pilot") 
    elif name == "mech": return Astronaut("mech", "repair") 
    elif name == "doctor": return Astronaut("doctor", "heal")
    elif name == "supply": return Supply()
    
    
    
    else:
        raise NameError("Invalid name")
    
def game_is_done():
    """Occur when a player won or at the end of last year"""
    
    print("\nThe game has ended.")
    ending = False
    
    while ending == False:
        answer = input("Did you enjoy it? (y/n):")
        
        if answer == 'y':
            print("Awesome ! \nI enjoyed playing with you too ! \nLet's play again as soon as possible !")
            ending = True
        elif answer == 'n':
            print("Is this true? \nI cannot believe you, I'm a great game ! \n Maybe you should give it another try?")
            ending = True
        else:
            print("I'm sorry, I only understand 2 letters: y and n")


def get_exploration_results(explo_type, radiation_level, locations, loc):
    print("Be ready to see the {0} results, be careful to not be spied by other players".format(explo_type))
    pause=input("Press any key to see the result")
                        
    if loc == "solarradiation" :                            
        show_radiation_level(radiation_level)
                            
    else: 
        print(locations[loc].exploration)
                                
    return locations[loc].exploration
                        
def ask_for_sharing_explo(explo_type):
                        
    if explo_type == 'exploration':
        print("Be careful, if you don't share the information, your spacecraft will be automatically destroyed")
    
    answer = '-'
    while answer not in ['y', 'n', 'yes', 'no']:
        answer = input("Are you sharing this information with other players? (y/n): ")
                                                   
    if answer in ["y", "yes"]:                           
        print("\nYou tell others players the results of your {0}.".format(explo_type))                            
                            
    elif answer in ["n", "no"]:
        print("\nYou keep the information secret.")
                            
    return answer