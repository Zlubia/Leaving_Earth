# -*- coding: utf-8 -*-


"""
TABLE DES MATIERES
------------------

class Player:
    
    def __init__(self, name)
    
    def actions_list(self)
    
    def draw_outcome(self, adv_name, astronaut = False)
    
    def remove_outcome(self, adv_name, result, price)
    
    def DestroySpacecraft(self, craft)
    
    def actions(self, choice, p, locations, players, end_of_year, missions, radiation_level, accomplished_missions, show_missions)
    
    def ACTION_research(self, adv, choice)
    
    def ACTION_buy(self, comp_list)
    
    def ACTION_spacecraft(self, name, locations)
    
    def ACTION_assemble(self, name, comp_list)
    
    def ACTION_disassemble(self, name)
    
    def ACTION_move(self, craft, destination, locations, radiation_level, players, p, missions, accomplished_missions):
    
    def ACTION_rendezvous(self, spacecraft1, spacecraft2, players, p, locations)
    
    def ACTION_survey(self, loc, craft, locations, players, p, missions, accomplished_missions, radiation_level)
    
    def ACTION_collect(self, loc, locations)

"""



from components import *
from advancements import *
from game_functions import *
from spacecraft import *
from location import *
from initialize import *
import time

import random
import math

class Player:
    """contains everything about a player:
    - name
    - money
    - spacecrafts informations
    - advancements information
    - points
    """
    def __init__(self, name):         # class constructor
       self.name = name
       self.money = 25
       self.advancements = {}
       self.spacecraft = {}
       self.component =[]
       self.points = 0
       self.active = True
    
    def actions_list(self):
        """Look for all actions possible for the current player
        and ask what he wants"""
        
        print("\n##############################")
        print("{0}, what do you want to do ?". format(self.name))
        # normal actions
        actions_list = ["R, #advancement: Research for an advancement (10$)", \
                        "B, #component: Buy a component", \
                        "CS, #name: Create a spacecraft on earth", \
                        "AS, #spacecraft, #component1, #component2, ... : Assemble a component on a spacecraft", \
                        "DS, #spacecraft: Disassemble a spacecraft",\
                        "M, #spacecraft, #location: Maneuvering a spacecraft to a location", \
                        "RV, #spacecraft_A, #spacecraft_B:Organize a rendez vous between Spacecraft A and Spacecraft B", \
                        "S, #location, #spacecraft: Survey a location, with a spacecraft", \
                        "C, #location : Collect a sample in a location", \
                        "NN: Nothing now, go to next player", \
                        "NY: Nothing else this year", \
                        "status: Check my status", \
                        "missions: display active missions", \
                        "save: save game"]
        
        
        i = 0
#        for elem in actions_list:
#            print(elem)
        choice = input("Enter your choice: ")
        choice = choice.lower() # set every character in lower case
        choice = choice.replace(" ", "") # remove spaces
        #choice = choice.replace("_", "") # remove "_"
        choice = choice.split(",") # separate 
        return choice  # choice is a list. first elem is the action, others are optional parameters       
 
          
    def draw_outcome(self, adv_name, astronaut = False):
        """ Check if there are still outcomes on the card.
        If yes draw one and ask to remove it"""
        if len(self.advancements[adv_name].outcomes) == 0:
            result = "success"
        else:
            result = random.choice(self.advancements[adv_name].outcomes)
            print("Technology {0} is not safe yet, an outcome is drawn...".format(adv_name))
            time.sleep(1)
            print("....a..")
            time.sleep(2)
            
            if astronaut == True:
                
                if result == "minor failure":
                    
                    #proposer de remove le minor failure?
                    print(result, "... luckily you had an astronaut on board that could prevent the failure. \nIt is considered a succes! ")
                    price = 5
                    self.remove_outcome(adv_name, result, price)
                    
                    result = "success"
                    
                    
                elif result == "major failure":
                    
                    #proposer de remove le major failure
                    print(result, "... luckily you had an astronaut on board that could reduce the failure's intensity. \nIt is considered a minor failure! ")
                    price = 5
                    self.remove_outcome(adv_name, result, price)
                    
                    result = "minor failure"
                    
                else:
                    #proposer de remove le succes.
                    print("..success ! Congratulations")
                    price = 10
                    if len(self.advancements[adv_name].outcomes) == 1:
                        self.advancements[adv_name].outcomes.remove(result)
                        print("the last outcome is a success, so it is automatically removed")
                    else:
                        self.remove_outcome(adv_name, result, price)
                    
            else:
                if result == "success":
                    print("..success ! Congratulations")
                    price = 10
                    if len(self.advancements[adv_name].outcomes) == 1:
                        self.advancements[adv_name].outcomes.remove(result)
                        print("the last outcome is a success, so it is automatically removed")
                    else:
                        self.remove_outcome(adv_name, result, price)
                                         
                if not result == "success":
                    print(result, " :-( .. sooo baad ")
                    price = 5
                    self.remove_outcome(adv_name, result, price)
            
        return result
    
    def remove_outcome(self, adv_name, result, price):
        answer = input("Would you like to pay {0}$ to fix this technology ? : (y/n)".format(price))
        if answer == 'y':
            if self.money < price :
                print("You don't have enough money to remove the outcome")
            else:    
                print("Ok, that will not happen anymore, that costed you {0}$".format(price))
                self.money -= price
                self.advancements[adv_name].outcomes.remove(result)
                
                
        elif answer == 'n': 
            print("ok, maybe next time")
        else:
            print("what you've just entered is not allowed, please be careful next time")
            self.remove_outcome(adv_name, result, price)
    
    
    def DestroySpacecraft(self, craft):
        """ Delete the spacecraft from the player's list. Give 2 negative point per died Astronaut"""
        dead = 0
        for comp in self.spacecraft[craft].component:
            if type(comp) == Astronaut:
                dead += 1
        points_lost = dead*2
        if dead > 0:
            print("Because of the accident, {0} astronauts died. You lose {1} points.".format(dead, points_lost))
        self.points -= points_lost
        del self.spacecraft[craft]
    
    
    def actions(self, choice, p, locations, players, end_of_year, missions, radiation_level, accomplished_missions, show_missions):
        """ ACTION TAKEN BY CURRENT PLAYER """
        
        #Ceci sert à vérifier si l'input 1 et l'input 2 sont corrects.
        try:
            choice[1]
            choice_1 = True
        except:
            choice_1 = False
            
        try:
            choice[2]
            choice_2 = True
        except:
            choice_2 = False
            
        
        if choice[0]=='r' and choice_1 == True:                      # ACTION RESEARCH
            self.ACTION_research(choice[1], choice)     # choice[1] = advancement name
            
        elif choice[0]=='b' and choice_1 == True:                    # ACTION BUY
            self.ACTION_buy(choice[1:])         # choice[1:] = component list
                
        elif choice[0]=='cs' and choice_1 == True:                   # ACTION CREATE SPACECRAFT
            self.ACTION_spacecraft(choice[1], locations)   
                                                # choice[1] = spacecraft name
            
        elif choice[0]=='as' and choice_1 == True and choice_2 == True:                   # ACTION ASSEMBLE A SPACECRAFT
            self.ACTION_assemble(choice[1], choice[2:])    
                                                # choice[1] = spacecraft name 
                                                # choice[2:] = list of comp
                                                
        elif choice[0]=='ds' and choice_1 == True:                   # ACTION DISASSEMBLE A SPACECRAFT
            self.ACTION_disassemble(choice[1])  # choice[1] = spacecraft name
        
        elif choice[0]=='m' and choice_1 == True and choice_2 == True:                    # ACTION MOVE  
            self.ACTION_move(choice[1], choice[2], locations, radiation_level, players, p, missions, accomplished_missions)
                                                # choice[1] = spacecraft name
                                                # choice[2] : destination
        
        elif choice[0]=='rv' and choice_1 == True and choice_2 == True:                   # ACTION RENDEZ VOUS
            self.ACTION_rendezvous(choice[1], choice[2], players, p, locations)
                                                # choice[1] = spacecraft1
                                                # choice[2] = spacecraft2
        
        elif choice[0]=='s' and choice_1 == True and choice_2 == True:                    # ACTION SURVEY
            self.ACTION_survey(choice[1], choice[2], locations, players, p, missions, accomplished_missions, radiation_level)
                                                # choice[1] = location to survey
                                                # choice[2] = spacecraft name
                                                
        elif choice[0]=='c' and choice_1 == True:                    # ACTION COLLECT A SAMPLE
            self.ACTION_collect(choice[1], locations)      # choice[1] = location


            
        elif choice[0]=='nn':                   # NEXT PLAYER
            p = next_player(players, p)
            print("See you next turn")                
                
            
        elif choice[0]=='ny':                   # DONE FOR THIS YEAR
            players[p].active = False
            print("Enjoy your holidays and see you next year!")
            if (all(elem.active == False for elem in players)):
                end_of_year = True
            else:
                p = next_player(players, p)
                
        # Show player status
        elif choice[0]=='status':
            print("Player : {0}, {1}$, {2} points".format(self.name, self.money, self.points))
            print("Advancements developed:")
            for a in self.advancements.keys():
                print(a, "(", len(self.advancements[a].outcomes), "outcomes)")
            print("Components in stock:")
            for a in self.component:
                if a.state == 0: condition = ", damaged"
                else: condition = " "
                print(a.name, condition)
            print("has {0} spacecrafts:".format(len(self.spacecraft)))
            for s in self.spacecraft.values():
                
                if s.ttoken > 0:
                    print("{0}, on {1} with {2} time tokens, with a mass of {3} and on board:".format(s.name, s.location.name,s.ttoken, s.mass))
                
                else:
                    print("{0}, on {1}, with a mass of {2} and on board:".format(s.name, s.location.name, s.mass))
                
                if len(s.component) >0: 
                    for c in s.component:
                        try:
                            if c.state == 0: condition = ", damaged"
                            else: condition = " "
                        except AttributeError:
                            condition = " "
                            
                        print("a {0}".format(c.name), condition)

                    
        # Show missions
        elif choice[0] == "missions":           
            show_missions(missions, accomplished_missions)
            
        # save game
        elif choice[0] == "save":
            print("Good luck with that, this part has not been coded yet. Haha!")
        
        elif choice[0] == "stop":
            raise ValueError("WHAT THE FUCK ARE YOU DOING !! YOU CRASHED MY GAME !!!")
            
        elif choice[0] == "interstellar":
            print("Interstellar travel is not possible in this version of the game.")
            print("But I strongly suggest you to watch the movie of the same name !")
            
        elif choice[0] == "hello":
            print("Hello {0},".format(self.name))
            
            i = input("Nice to meet you, are you enjoying the game? : " )
            
            if i == "y" or i == "yes":
                print("Awesome ! I think we will get along !")
                print("\nFly safe !")
                
            elif i =="n" or i == "no":
                print("Oh come on ! I'm sure this can't be true ! I'm a great game ! ")
                
            else:
                print("Let me think about it...")
        
        else: print ("please do not write something silly, (no actions selected)")
        
        return p, locations, end_of_year

    def ACTION_research(self, adv, choice):
        """Research for an advancement. 
        Check money and pay 10M$
        Set outcomes"""
        
        if adv in self.advancements.keys():
            print("you have already bought this advancement")
                    
        elif self.money < 10:   # all researches are for 10$
            print("You don't have enough money")
                                                        
        else:
            if len(choice) == 3:
                if choice[2] == 'chance':
                    chance = True
            else: 
                chance = False
                
            try:
                self.advancements[adv] = Advancement(adv, chance) # create obj and add it to player adv dict
                self.money -= 10  # 10$ is spent for the research
                print("You spent 10$ to start research : {0} \n you have now {1}$".format(adv, self.money))
                nb_adv = len(self.advancements[adv].outcomes)
                if nb_adv == 1: print("1 outcome have been randomly set on your card")
                else: print("{0} outcomes have been randomly set on your card".format(nb_adv))
                
            except (KeyError, NameError):
                print("This advancement has not been invented yet in this world!")
                    
    def ACTION_buy(self, comp_list):
        """Pay the cost, add component in stock"""
        for comp_str in comp_list:
            try:
                comp = obj(comp_str)            # to convert in an object
                if self.money < comp.cost:
                    print("{0}: You don't have enough money".format(comp_str))
                    
                elif not all(req in self.advancements.keys() for req in comp.requirements):
                    print("{0}: you first need to research the required advancements".format(comp_str))
    
                else:                        
                    self.component.append(comp)
                    self.money = self.money - comp.cost
                    print("you have bought a {0} for {1}$, you have {2}$ left".format(comp.name, comp.cost, self.money))
            except:
                print("Are you mad ? {0} object cannot be bought".format(comp_str))
        
    def ACTION_spacecraft(self, name, locations):
        """ Create an empty Spacecraft for the player"""
        
        try:
            self.spacecraft[name]
            already_exists = True
            
        except:
            already_exists = False
            
        if already_exists == False:
            
            if name == "endurance":
                
                print("Great name ! I'd suggest you to hire Joseph Cooper as the pilot of this ship. ;)")
                self.spacecraft[name] = Spacecraft(name, locations["earth"])
            
            elif name == "juno" or name == "atlas" or name == "soyuz" or name == "saturn" or name == "probe" or name == "ionthruster" or name == "eagle" or name == "vostok" or name == "apollo" or name == "aldrin" or name == "pilot" or name == "mech" or name == "doctor" or name == "supply":
                
                print("Don't give your spacecraft the same name as a component, it would confuse me.")
            
            elif name == "voyager" or name == "voyager1":
                
                print("The Voyager 1 probe is the most distant from Earth of all known man-made objects.")
                print("May it inspire your {0} spacecraft".format(name))
                self.spacecraft[name] = Spacecraft(name, locations["earth"])
            
            else:
                self.spacecraft[name] = Spacecraft(name, locations["earth"])
                print("What an amazing spacecraft ! {0} is ready for a great space travel".format(name))
        
        elif already_exists == True:
            print("You already have a spacecraft named {0}, it is currently situated on {1}.".format(self.spacecraft[name].name, self.spacecraft[name].location.name))
            
    def ACTION_assemble(self, name, comp_list):
        """ Move components from player stock to spacecraft on earth. 
        Adapt mass"""
                                                
        #assembled = False
        # check if spacecraft exists and is on earth:
        try: # if spacecraft does not exist --> go to except
            if not(self.spacecraft[name].location.name == "earth"):
                print("{0} is not on earth".format(name))
                
            else:                    
                for comp_to_add in comp_list:
                    if len(self.component) == 0:
                        print("You don't have any component in your stock")
                    else:
                        for comp_in_stock in self.component:
                            assembled = False
                            if (comp_to_add == comp_in_stock.name): # and comp_in_stock.location):
                                # there is a comp_in_stock (on earth) matching comp_to_add 
                                if type(comp_in_stock) == Astronaut and self.spacecraft[name].availableSeats()<=0 :
                                    print("There is no seats available for an astronaut in this spacecraft")
                                    assembled = True # not assembled but action is done
                                else:
                                    self.spacecraft[name].addComponent(comp_in_stock, self)
                                    self.spacecraft[name].arrangeComponents()
                                    assembled = True
                            if assembled == True:
                                break
                        if assembled == False:
                            print("not available in your stock")
        except KeyError:
            print("You don't have such a spacecraft: {0}".format(name))
            
    
    def ACTION_disassemble(self, name):
        """ Disassemble a spacecraft on heart. 
        Delete the spacecraft"""
        
        try: # if spacecraft does not exist --> go to except
            if not(self.spacecraft[name].location.name == "earth"):
                print("{0} is not on earth".format(name))
            else:
                for elem in self.spacecraft[name].component:
                    self.component.append(elem) # component of spacecraft is put back player stock 
                print("{0} is dissasembled, components are available in your stock".format(self.spacecraft[name].name))
                del self.spacecraft[name] # spacecraft is deleted
        except KeyError:
            print("You don't have such a spacecraft: {0}".format(name))

    
    def ACTION_move(self, craft, destination, locations, radiation_level, players, p, missions, accomplished_missions):
                                       
        # 1) check if destination and spacecraft exists with no time token
        if not craft in self.spacecraft:
            print("You don't have such a spacecraft: {0}".format(craft))
        elif self.spacecraft[craft].ttoken > 0:
            print("This spacecraft is currently traveling to {0}, and will reach destination in {1} year".format(self.spacecraft[craft].location.name, self.spacecraft[craft].ttoken))
        
        elif self.spacecraft[craft].mass == 0:
            print("This spacecraft is empty and cannot move") 
        
        elif not destination in locations.keys():
            print("{0} doesn't exist in this universe".format(destination))
           
        else:
            
            # 2) check if destination is accessible from position
            position = self.spacecraft[craft].location.name
            possible_maneuvers = locations[position].maneuvers
            if not destination in possible_maneuvers:
                print("Are you a fool ? You cannot go there!")
            else:
                    
                # 3) get difficulty, time_travel and hazards
                diff = possible_maneuvers[destination][0]
                time_travel = possible_maneuvers[destination][1]
                hazards = [] # by default
                if len(possible_maneuvers[destination]) > 2:
                    hazards = possible_maneuvers[destination][2:] # the rest of the list 
                
                # 4) thrust
                mass = self.spacecraft[craft].mass
                necessary_thrust = mass*diff
                print("For this maneuver, the difficulty is {0}".format(diff))
                print("For a mass of {0}, you need to provide a thrust of {1}".format(mass, necessary_thrust))
                    
                rockets = []
                for elem in self.spacecraft[craft].component:
                    if type(elem) == Rocket and elem.state == 1:
                        rockets.append(elem) # list of rockets
                    if type(elem) == Thruster and elem.state == 1 and time_travel >0 :
                        rockets.append(elem) # add ion thruster only if time traval is not 0
                total_thrust = 0
                for elem in rockets:
                    if type(elem) == Rocket:
                        total_thrust += elem.thrust
                    if type(elem) == Thruster:
                        total_thrust += 5*(time_travel) # in case there is a trhsuter, it's thrust is 5*timetravel 
                if total_thrust < necessary_thrust:
                    print("what are you thinking? You will never get enough thrust")
                    print("You could consider watching Interstellar, the movie, instead of playing this game.")
                    print(".. Sorry it was a joke")
                    print("Don't be too hard on yourself, even the best scientists make mistakes.")
                    print("Take a look at the Mars Climate Orbiter for example, a 327 million $ spacecraft from Nasa that was lost due to a simple unit conversion error." )
                else:
                    
                    move_ok = True
                    for haz in hazards:
                         if haz in ["landing"]:
                             if haz not in self.advancements:
                                 print("\nfor this maneuver, {0} technology is necessary".format(haz))
                                 print("if I was you, i would try to buy it from another space agency")
                                 move_ok = False
                    
                    if move_ok == True:
                            
                        # 5) choose rockets
                        thrust = 0
                        stop = False
                        print("available rockets")
                        while(thrust<necessary_thrust and craft in self.spacecraft and len(rockets) >0 and stop == False):
                            i=0
                                    
                            for elem in rockets:
                                if type(elem) == Thruster:
                                    peryear = "per year, meaning " + str(elem.thrust*time_travel)
                                else: 
                                    peryear = ""
                                print("Rocket ", i, ":", elem.name, " provinding a thrust of", elem.thrust, peryear)
                                i+=1
                            
                            FirstChoice = True
                            if time_travel >= 1 and FirstChoice:
                                print("100: advanced travel: slower and faster maneuvers")
                            
                            print("200 : abort")
                            n = i
                            i=-1
                             # to authorize to adapt the time_travel only BEFORE burning rockets/ion thrusters
                            while i not in list(range(0,n))+[100, 200]: # to prevent if user give an out of range index, a letter, etc
                                temp_i = input("Which rocket are you burning? :")
                                try: i=int(temp_i)
                                except: pass
                            
                            
                            
                            if not i == 200: # 200 = abort
                                
                                if i == 100 and time_travel >=1 and FirstChoice :
                                    print("Corones! Your balls are big enough to perform advanced travel")
                                    duration = False
                                    
                                    while type(duration) != int:
                                        duration= int(input('How much years will take your travel ?: '))
                                    
                                    if duration > time_travel:
                                        time_travel = duration # time_travel is now bigger, so the effect of a ion thruster is more thrust
                                    
                                    while duration < time_travel: 
                                        time_travel = math.ceil(time_travel/2) # time divided by 2, rounded up
                                        necessary_thrust = necessary_thrust*2  # new thrust to provide
                                        print("You double the thrust to divide the time travel by two, rounded up")
                                        print("For this maneuver, you need to provide a thrust of {0}".format(necessary_thrust))
                                
                                elif not i == 100: # rocket is used
                                    result = self.draw_outcome(rockets[i].name)
                                    if result == 'minor failure' or (type(rockets[i]) == Thruster and result == 'major failure'):
                                        print("ROCKET DAMAGED, PROVIDES NO THRUST")
                                        self.spacecraft[craft].component[i].state = 0  # component damaged
                                        del rockets[i]  # delete from available for thrust rockets list
                                    elif result == 'major failure':
                                        print("EXPLOSION DESTROYS SPACECRAFT")
                                        self.DestroySpacecraft(craft)
                                        move_ok = False
                                    else:   # in case of success                                         
                                        if type(rockets[i]) == Thruster:
                                            thrust = thrust + rockets[i].thrust*time_travel
                                            print("ion thruster is used, and will provide 5 thrust force each year for this travel. You will still be able to use it for future travels")
                                            print("You still need {0} more".format(necessary_thrust-thrust))
                                            # ion thruster are reusable, so not deleted from the craft
                                        else:
                                            self.spacecraft[craft].mass -= rockets[i].mass
                                            thrust = thrust + rockets[i].thrust
                                            print("{0} is burn, providing {1} thrust".format(rockets[i].name, rockets[i].thrust))
                                            if necessary_thrust - thrust > 0:
                                                print("You still need {0} more thrust".format(necessary_thrust - thrust))
                                            del self.spacecraft[craft].component[i] # rocket is burn and deleted
                                                                                        
                                        del rockets[i] # even if ion thruster is used, it cannot be burn again during the same year
                                
                                FirstChoice = False # to late to adapt time_travel
                            
                            else: stop = True
                                        
                        
                        # 6) check hazards
                        # (optional) landing
                        # atmospheric entry
                        # solar radiation
                        # reentry ?
                        
                        if thrust >= necessary_thrust:  # move occurs
                            if not hazards == False:
                                for haz in hazards:
                                    print(haz, 'is encountered')
                                    if haz == "optionnal landing" and 'landing' in self.advancements:
                                        answer = '-'
                                        while answer not in ['y', 'n', 'yes', 'no']:
                                            answer = input("Do you intend to test landing technlogy during this move?:(y/n)")
                                        if answer == 'y' or answer == 'yes':                    
                                            haz = "landing"
                                            
                                    if haz == "landing":
                                        print("\nfor this maneuver, landing technology is necessary")
                                        
                                        result = self.draw_outcome("landing")  # draw and ask if pay to remove
                                        
                                        # check if a pilot can improve the result
                                        outcome_improved = False
                                        for comp in self.spacecraft[craft].component:
                                            if type(comp) == Astronaut:
                                                if comp.skill == 'pilot':
                                                    outcome_improved = True
                                        if outcome_improved:
                                            if result == 'minor failure':
                                                result == 'success'
                                                print("Hopefully, you have a very skilled pilot on board, saving the ship")
                                            if result == 'major failure':
                                                result == 'minor failure'
                                                print("Hopefully, you have a very skilled pilot on board, limiting the damage")
                                        
                                        # apply results of outcome
                                        if result == 'major failure':
                                            print("IMPACT WITH SURFACE: SPACECRAFT DESTROYED")
                                            self.DestroySpacecraft(craft)
                                            move_ok = False
                                            
                                        elif result == "minor failure":
                                            print("ROUGH LANDING...")
                                            i = 0
                                            for elem in self.spacecraft[craft].component:
                                                print(i, ": ", elem.name)
                                                i+=1
                                            damaged = False
                                            while not (type(damaged) == int and damaged <= len(self.spacecraft[craft].component)):
                                                try:
                                                    damaged = int(input("which component is damaged ?:"))
                                                except ValueError:
                                                    pass
                                            
                                            print(self.spacecraft[craft].component[damaged].name, "is damaged")
                                            self.spacecraft[craft].component[damaged].state = 1
                                        
                                        
                                    
                                    elif haz == "reentry":
                                        for elem in self.spacecraft[craft].component:
                                            if type(elem) == Capsule:
                                                if elem.state == 0 or elem.heatshield == False:
                                                    self.spacecraft.mass = self.spacecraft.mass - elem.mass
                                                    del elem
                                                if elem.heatshield == True:
                                                    result = self.draw_outcome("reentry")
                                                    if result == 'major failure':
                                                        self.spacecraft.mass = self.spacecraft.mass - elem.mass
                                                        del elem
                                                        if self.spacecraft[craft].availableSeats() < 0 :
                                                            killAstronauts(players[p])
                                                    if result == 'minor failure':
                                                        elem.state == 0
                                    
                                    elif haz == "solar radiation": # ajouter aldrin capsule effect
                                        for elem in self.spacecraft[craft].component:
                                            if type(elem) == Astronaut:
                                                print("During the travel, {0} faces to solar radiation at a level of {1}".format(elem.name, radiation_level))
                                                print("You roll a dice....")
                                                time.sleep(2)
                                                luck = random.choice([1,2,3,4,5,6,7,8])
                                                print("...  ", luck)
                                                if luck <= (radiation_level)*time_travel:
                                                    elem.state = 0
                                                    print("Your {0} becomes incapacitated".format(elem.name))
                                                    
                                                
                                                
                            else: 
                                result = "success" # because no hazard encountered # unused
                        else:
                            print("no move")
                            move_ok = False
                                                                        
                                
                        if move_ok == True: # to change
                        # 7) move the spacecraft ! 
                            self.spacecraft[craft].location = locations[destination]
                            print("{0} is moved to {1}".format(craft, destination))
                            
                            self.spacecraft[craft].ttoken = time_travel
                            if time_travel > 0:
                                print("This maneuver will take {0} years".format(time_travel))
                                print("Each end of year, a time token will be removed")
                                print("Fly safe!")
                                    
                                
                            #8) add the location to the history of an astronaut
                                
                            for elem in self.spacecraft[craft].component:
                                if type(elem) == Astronaut:
                                    elem.route.append(destination)
                                    
            
                            
                            if time_travel == 0:
                                
                            # 9) exploration
                            # written in the if time travel == 0 condition, 
                            # but it is actually always the case in case of exploration
                            # but we never know in future expansion of the game
                            
                                # very particular case of suborbital flight, also when pass through when going to earthorbit    
                                if locations[destination].name == 'suborbitalflight' or (position == 'earth' and locations[destination].name == 'earthorbit'):
                                    
                                    astronauts = self.spacecraft[craft].astronautsOnBoard() # get the number of astronauts on board
                                    if len(astronauts) > 0:
                                    
                                        # a) first exploration
                                        if locations['suborbitalflight'].explored == False:
                                             
                                                print("Congratulation, you are the first manned space flight to reach suborbital flight alive, let's discover what happens")
                                                explo_type = 'exploration'
                                                explo = get_exploration_results(explo_type, radiation_level, locations, destination)
                                                answer = ask_for_sharing_explo(explo_type)
                                            
                                                if answer == "y":
                                                    locations['suborbitalflight'].explored = True
                                                    
                                                elif answer == "n":
                                                    print("\n your spacecraft is destroyed.")
                                                    self.DestroySpacecraft(craft)
                                        
                                        # b) already explored
                                        elif locations['suborbitalflight'].explored == True:
                                            
                                            if explo == "roll 1 : atronaut incapacited":
                                                target = 1
                                                unca = True
                                            
                                            elif explo == "roll 1-3 : atronaut incapacited":
                                                target = 3
                                                unca = True
                                        
                                            if unca == True:
                                            # a die is roll to check if astronaut take too much radiations
                                                
                                                for elem in self.spacecraft[craft].component:
                                                    if type(elem) == Astronaut:
                                                        print("At this location, {0} faces to solar radiation".format(elem.name))
                                                        print("You roll a dice....")
                                                        time.sleep(2)
                                                        luck = random.choice([1,2,3,4,5,6,7,8])
                                                        print("...  ", luck)
                                                        if luck <= target:
                                                            elem.state = 0
                                                            print("Your {0} becomes incapacitated".format(elem.name))
                                                
                                        
                                # other exploration (than suborbital flight)
                                elif (locations[destination].explorable == True and locations[destination].explored == False):
                                
                                    print("Congratulation, you are the first agency to reach {0}, let's discover what happens")
                                    explo_type = 'exploration' # and not 'survey'
                                    explo = get_exploration_results(explo_type, radiation_level, locations, destination)
                                    answer = ask_for_sharing_explo(explo_type)
                                        
                                    if answer == "y":
                                        locations[destination].explored = True
                                                
                                    elif answer == "n":
                                        print("\n your spacecraft is destroyed.")
                                        self.DestroySpacecraft(craft)
                                        
                                if locations[destination].explorable == True and locations[destination].explored == True:
                                    explo = locations[destination].exploration
                                    print("Exploration on this planet shows: ", explo)
                                    unca = False
                                    
                                    if explo == "spacecraft destroyed": 
                                        self.DestroySpacecraft(craft)
                                        print("Sorry, your spacecraft is destroyed")
                                    elif explo == 'alien origin':
                                        print("Here you can get special sample that will yield new scientific knowledge when turned in on Earth at the start of the year.")
                                        print("You would gain a new advancement with no outcome cards on it, or you would be able to remove all outcome cards from any one of your existing advancements.")
                                    elif type(explo) == dict: # {"minerals" : 25} or {"minerals" : 50} 
                                        print("Samples taken here will give you {0}$ if you bring it back on Earth".format(explo["minerals"]))
                                    elif explo == 'life' or explo == ("life", "supplies"):
                                        print("If the extraterrestrial life mission is available, bringing a sample from here back on Earth will complete the mission")
                                    elif explo == 'supplies' or explo == ("life", "supplies"):
                                        print("Supplies used for feeding astronaut and repairing damage may be collected here")
                        
                    #10) check if a mission is accomplished
                    players, missions, accomplished_missions = check_missions(locations, missions, players, p, accomplished_missions)
                                
                    
                    
    def ACTION_rendezvous(self, spacecraft1, spacecraft2, players, p, locations):
            
            #Check if the player has the rendez vous technology
            if "rendezvous" in players[p].advancements.keys():
				
                #Initialize checking variables
                end_action = False
                spacecraft_1 = True
                spacecraft_2 = True
                
                #Check if the entered spacecrafts exists
                try:
                    players[p].spacecraft[spacecraft1]
                    
                except:    
                    spacecraft_1 = False
                    
                try:
                    players[p].spacecraft[spacecraft2]
                    
                except:    
                    spacecraft_2 = False
				
				#check for time tokens.	
                if spacecraft_1 == True and spacecraft_2 == True:
                    
                    if self.spacecraft[spacecraft1].ttoken > 0 or self.spacecraft[spacecraft2].ttoken > 0:
                        
                        print("You cannot rendez-vous a spacecraft with another spacecraft that still has time tokens on it.")
                        end_action = True
				
				#if both spacecraft exists and there are no time tokens on them proceed with the next checks.
                if end_action == False:
						
					#At least 1 spacecraft from the 2 spacecrafts entered needs to exist to be able to use the Rendez-vous action.
                    if spacecraft_1 == False and spacecraft_2 == False:
						
                        print("Both spacecrafts, {0} and {1}, do not exist. Enter at least one existing spacecraft to use Rendez-Vous.".format(spacecraft1, spacecraft2))
					
					
                    elif spacecraft_1 == True and (self.spacecraft[spacecraft1].location.name == "earth" or self.spacecraft[spacecraft1].location.name == "suborbital_flight" ) :
						
                        print("You cannot rendez-vous on Earth or on a Suborbital Flight")
					  
                    elif spacecraft_2 == True and (self.spacecraft[spacecraft2].location.name == "earth" or self.spacecraft[spacecraft2].location.name == "suborbital_flight" ) :
						
                        print("You cannot rendez-vous on Earth or on a Suborbital Flight")                        
						
					
					#If only 1 spacecraft exists, ask if the player wants to create the other one. (In case player wants to split a spacecraft in 2 spacecrafts)
                    elif spacecraft_1 == False: 
						
                        answer = input("Spacecraft {0} do not exist yet, do you want to create a new one in this location? : (y/n)".format(spacecraft1))
						
                        if answer == 'y':
							
							#inverse spacecraft 1 (new one) and spacecraft 2 (existing one)
                            spacecraft1, spacecraft2 = spacecraft2, spacecraft1
							
							#create new spacecraft at the same location.
                            self.spacecraft[spacecraft2] = Spacecraft(spacecraft2, locations[self.spacecraft[spacecraft1].location.name])
                            self.spacecraft[spacecraft2].ttoken = self.spacecraft[spacecraft1].ttoken
                            print("What an amazing spacecraft ! {0} is ready for a great space travel".format(spacecraft2))
                            spacecraft_1 = True
							#spacecraft 1 is now the existing one and spacecraft 2 is now the new one.
							
							
                        else :
                            print("Ok maybe next time.")
							
						
                    elif spacecraft_2 == False:
						
                        answer = input("Spacecraft {0} do not exist yet, do you want to create a new one in this location? : (y/n)".format(spacecraft2))
						
                        if answer == 'y':
							#create new spacecraft at the same location.
                            self.spacecraft[spacecraft2] = Spacecraft(spacecraft2, locations[self.spacecraft[spacecraft1].location.name])
                            self.spacecraft[spacecraft2].ttoken = self.spacecraft[spacecraft1].ttoken
                            print("What an amazing spacecraft ! {0} is ready for a great space travel".format(spacecraft2))
                            spacecraft_2 = True
							
                        else :
                            print("Ok maybe next time.")
							
						
					#If both spacecraft exists, a rendez-vous action may take place.
                    if spacecraft_1 == True and spacecraft_2 == True:
						
						#check if both spacecrafts are on the same location.
                        if self.spacecraft[spacecraft1].location != self.spacecraft[spacecraft2].location:
							
                            print("{0} and {1} are not on the same location".format(self.spacecraft[spacecraft1].name, self.spacecraft[spacecraft2].name))
							
                            
                        #Drawing outcomes

                        else:
                            
                            outcome_improved = False
							
                            for comp in self.spacecraft[spacecraft1].component:
                                
                                if type(comp) == Astronaut:
                                    
                                    if comp.name == "pilot" and comp.state == 1:
                                        
                                        outcome_improved = True
                            
                            
                            result = self.draw_outcome("rendezvous", outcome_improved)
							
                            if result =="minor failure":
								
                                failure = True
								
                            elif result == "major failure":
							
                                failure = True
								
                            else:
                                failure = False
                                rendez_vous = True
							
								
                            #En cas de failure - choisir un composant à endommager.
                            if failure == True:
								
                                print("\nDOCKING ADAPTOR FAILED...\n")
								#l'action rendez-vous est annulée par la failure.
                                rendez_vous = False
                                #initialisations de variables pour la selection du component à endommager.
                                i = 0
                                verification_list = []
                                unbreakable_components_1 = 0
                                number_damaged_elements = 0
                                spacecraft_2_size = 0
								
                                #setup variable boucle
                                boucle = True
                                
                                #préordonnement des composants pour être certain que l'ordre est bon.
                                self.spacecraft[spacecraft1].arrangeComponents()
                                self.spacecraft[spacecraft2].arrangeComponents()
								
                                #Composants du spacecraft 1
                                print("From {0}:".format(self.spacecraft[spacecraft1].name))
								
                                for elem in self.spacecraft[spacecraft1].component:
									
                                    #Supply et Samples ne peuvent pas être endommagés.
                                    if type(elem) != Supply and type(elem) != Sample :
                                        
                                        #afficher si le component est déjà damaged. + compteur d'éléments endommagés (dans le cas où tout les éléments sont damaged, le spacecraft est détruit.)
                                        if elem.state == 0:
                                            print(i, ": ", elem.name, " - status : damaged")
                                            number_damaged_elements += 1
                                            verification_list.append(i)
                                            i += 1
                                        
                                        elif elem.state == 1:
                                            print(i, ": ", elem.name)
                                            verification_list.append(i)
                                            i += 1
                                    else:
                                        unbreakable_components_1 += 1
                                                
										
                                #Composants du spacecraft 2
                                print("\nFrom {0}:".format(self.spacecraft[spacecraft2].name))
										
                                for elem in self.spacecraft[spacecraft2].component:
                                    
                                    #Supply et Samples ne peuvent pas être endommagés.
                                    if type(elem) != Supply and type(elem) != Sample :
                                        #afficher si le component est déjà damaged. + compteur d'éléments endommagés (dans le cas où tout les éléments sont damaged, le spacecraft est détruit.)
                                        if elem.state == 0:
                                            print(i, ": ", elem.name, " - status : damaged")
                                            number_damaged_elements += 1
                                            
                                        
                                        elif elem.state == 1:
                                            print(i, ": ", elem.name)
                                            
                                            
                                        verification_list.append(i)
                                        i += 1
                                        spacecraft_2_size += 1

								#si tout les éléments sont endommagés, endommager un nouvel élément détruira le spacecraft.
                                if number_damaged_elements == i:
                                    #boucle de choix du composant à endommager est annulée, ainsi que la boucle rendez_vous
                                    boucle = False
                                    rendez_vous = False
                                    boucle_destroy = True
                                    
                                    if spacecraft_2_size > 0:
                                    
                                        while boucle_destroy == True:
                                            print("\nUnfortunately all the components of both spacecraft are already damaged.")
                                            print("The damage from your rendez-vous failure will destroy one spacecraft. \n")
                                            
                                            print("1 : ", self.spacecraft[spacecraft1].name)
                                            print("2 : ", self.spacecraft[spacecraft2].name)
                                            
                                            answer_destroyed_spacecraft = input("\nWhich spacecraft will be destroyed ? :")
                                            
                                            if answer_destroyed_spacecraft == "1":
                                                
                                                print("Message from {0} : MAYDAY, MAYDfrshhhh ... bip .. bip . bip .... \n".format(self.spacecraft[spacecraft1].name))
                                                print(self.spacecraft[spacecraft1].name , "is destroyed.")
                                                self.DestroySpacecraft(spacecraft1)
                                                boucle_destroy = False
                                                
                                            elif answer_destroyed_spacecraft == "2":
                                                
                                                print("Message from {0} : MAYDAY, MAYDfrshhhh ... bip .. bip . bip .... \n".format(self.spacecraft[spacecraft2].name))
                                                print(self.spacecraft[spacecraft2].name , "is destroyed.")
                                                self.DestroySpacecraft(spacecraft2)
                                                boucle_destroy = False
                                                
                                            else:
                                                print("Please answer '1' or '2'.")
                                                
                                    else:
                                        print("\nUnfortunately all the components on the spacecraft are already damaged.")
                                        print("The damage from your rendez-vous failure will destroy it. \n")
                                        
                                        print("Message from {0} : MAYDAY, MAYDfrshhhh ... bip .. bip . bip .... \n".format(self.spacecraft[spacecraft1].name))
                                        print(self.spacecraft[spacecraft1].name , "is destroyed.")
                                        self.DestroySpacecraft(spacecraft1)
								
                                #Choix du component à endommager.
                                while boucle == True:
									
                                    damaged = "nothing currently"
                                    
                                    try:
                                        damaged = int(input("\nWhich component is damaged? :"))
										
                                    except:
                                        pass
								
                                    #verification si l'input est correct.
                                    if damaged in verification_list:
								
										
                                        #Si c'est un composant du spacecraft 1
                                        if damaged < (len(self.spacecraft[spacecraft1].component)-unbreakable_components_1):
                                            
                                            #vérification si le composant n'est pas déjà endommagé.
                                            if self.spacecraft[spacecraft1].component[damaged].state == 0:
                                                
                                                print("\n{0} has already suffered damage.".format(self.spacecraft[spacecraft1].component[damaged].name))
                                                print("Please choose an undamaged component.")
                                                
                                            else:
                                                
                                                #sortie de boucle
                                                boucle = False
                                                
                                                #endommager le composant
                                                print("\n", self.spacecraft[spacecraft1].component[damaged].name, "is damaged")
                                                self.spacecraft[spacecraft1].component[damaged].state = 0
											
											
                                        #Si c'est un composant du spacecraft 2
                                        else:
											
                                            damaged = damaged - (len(self.spacecraft[spacecraft1].component)-unbreakable_components_1)
											
                                            #vérification si le composant n'est pas déjà endommagé.
                                            if self.spacecraft[spacecraft2].component[damaged].state == 0:
                                                
                                                print("\n{0} has already suffered damage.".format(self.spacecraft[spacecraft2].component[damaged].name))
                                                print("Please choose an undamaged component.")
                                                
                                            else:
                                                
                                                #sortie de boucle
                                                boucle = False
                                                
                                                #endommager le composant
                                                print("\n", self.spacecraft[spacecraft2].component[damaged].name, "is damaged")
                                                self.spacecraft[spacecraft2].component[damaged].state = 0
											
                                    #En cas d'erreur d'input
                                    else:
                                        print("\nPlease enter a correct number.\n")
								
											
							
							#Réalisation de l'action rendez-vous.
                            while rendez_vous == True:
								
								#setup variables de boucles
                                boucle2 = True
                                answer = "interstellar"
								
                                #choix des composant à transférer
                                while boucle2 == True:
								
                                    print("\nWhich component would you like separate from {0} and attach to {1}?".format(self.spacecraft[spacecraft1].name, self.spacecraft[spacecraft2].name))
									
                                    #setup variables de liste de composants, la liste de verification sers à vérifier si l'input est valable par rapport à la liste de composants.
                                    i = 0
                                    verification_list = []
                                    number_astronauts = 0
								
                                    for comp in self.spacecraft[spacecraft1].component:
                                        print(i, ": ", comp.name)
                                        verification_list.append(i)
                                        i+= 1
                                        #compte le nombre d'astronautes, information nécéssaire en cas de séparation de capsules.
                                        if type(comp) == Astronaut:
                                            number_astronauts += 1
                                            
									
                                    if i != 0:
										
                                        answer_component = input("Which component would you like to detach? :")
										
                                        try:
                                            answer_component = int(answer_component)
											
                                        except:
                                            pass
											
                                        #vérifier si l'input i fait partie de la liste des components affichés.
                                        if answer_component in verification_list:
                                            
                                            component_detach = True
                                            
                                            #vérifier si le composant est une capsule ou un astronaute
                                            if type(self.spacecraft[spacecraft1].component[answer_component]) == Capsule:
                                                
                                                #le nombre de places qu'il resterait après séparation
                                                leftover_seats = self.spacecraft[spacecraft1].availableSeats() - self.spacecraft[spacecraft1].component[answer_component].capacity
                                                
                                                
                                                if leftover_seats < 0 :
                                                    
                                                    #le nombre d'astronautes qui se retrouveront sans siège en cas de séparation d'une capsule.
                                                    floating_astronauts = 0 - leftover_seats
                                                    
                                                    b = True
                                                    
                                                    while b == True:
                                                        
                                                        print("The seat capacity of {0} without the {1} capsule, will be to small for the {2} astronauts currently on board.".format(self.spacecraft[spacecraft1].name, self.spacecraft[spacecraft1].component[answer_component].name, number_astronauts ))
                                                        answer_transfer = input("Would you like to transfer {0} astronauts with the {1} capsule to {2}? : (y/n)".format(floating_astronauts, self.spacecraft[spacecraft1].component[answer_component].name, self.spacecraft[spacecraft2].name))
                                                        
                                                        if answer_transfer == 'y':
                                                            #demander si et quels astro déplacer avec la capsule.
                                                            print("Which astronaut would you like to transfer to {0}?".format(self.spacecraft[spacecraft2].name))
                                                            
                                                            #tant qu'il y a des astronautes sans sièges.
                                                            while floating_astronauts > 0:
                                                                j = 0
                                                                j_verification_list = []
                                                                
                                                                #choisir un astronaute à déplacer.
                                                                for astronaut in self.spacecraft[spacecraft1].component:
                                                                    if type(astronaut) == Astronaut:
                                                                        print(j, ": ", astronaut.name)
                                                                        j_verification_list.append(j)
                                                                        j += 1
                                                                        
                                                                if j != 0:
                                                                
                                                                    answer_astronaut = input("Which astronaut would you like to transfer to {0}? :".format(self.spacecraft[spacecraft2].name))
                                                                    
                                                                    try:
                                                                        answer_astronaut = int(answer_astronaut)
                                                                        
                                                                    except:
                                                                        pass
                                                                    
                                                                    detach_astronaut = -1
                                                                    
                                                                    #vérifier si l'input answer_astronaut fait partie de la liste des astronautes affichés.
                                                                    if answer_astronaut in j_verification_list:
                                                                        
                                                                        floating_astronauts -= 1
                                                                        
                                                                        number_components = -1
                                                                        number_astronauts = 0
                                                                        number_supplies = 0
                                                                        number_samples = 0
                                                                        
                                                                        #compte le nombre de components, d'astronautes, supplies et samples à bord.
                                                                        for comp in self.spacecraft[spacecraft1].component:
                                                                            
                                                                            number_components += 1
                                                                            
                                                                            if type(comp) == Astronaut:
                                                                                number_astronauts += 1
                                                                            elif type(comp) == Supply:
                                                                                number_supplies += 1
                                                                            elif type(comp) == Sample:
                                                                                number_samples += 1                                                                                
                                                                                                                                              
                                                                        """Pour lier le bon astronaute.
                                                                        L'indice de l'astronaute dans le spacecraft = 
                                                                        nombre composants - nombre samples - nombre supplies - (nombre d'astronautes - astronaute selectionné dans la liste - 1)
                                                                        """
                                                                        detach_astronaut = number_components - number_samples - number_supplies - (number_astronauts - answer_astronaut - 1)
                                                                        
                                                                        print("You transfer astronaut {0} together with {1} capsule.".format(self.spacecraft[spacecraft1].component[detach_astronaut].name , self.spacecraft[spacecraft1].component[answer_component].name))
                                                                        
                                                                        #ajouter component (astronaute) au spacecraft 2
                                                                        self.spacecraft[spacecraft2].component.append(self.spacecraft[spacecraft1].component[detach_astronaut])
                                                                        #supprimer l'astronaute du spacecraft 1
                                                                        del self.spacecraft[spacecraft1].component[detach_astronaut]
                                                                        #Reordonner les composants
                                                                        self.spacecraft[spacecraft1].arrangeComponents()
                                                                    
                                                                    #en cas d'erreur d'input
                                                                    else:
                                                                        print("Please enter a correct number.")
                                                                   
                                                            
                                                            b = False
                                                            component_detach = True
                                                            
                                                        elif answer_transfer == 'n' :
                                                            print("\nUndocking {0} capsule aborted.".format(self.spacecraft[spacecraft1].component[answer_component].name))
                                                            b = False
                                                            component_detach = False
                                            
                                            #Si le composant est un astronaute
                                            elif type(self.spacecraft[spacecraft1].component[answer_component]) == Astronaut:
                                                
                                                if self.spacecraft[spacecraft2].availableSeats() <= 0:
                                                    
                                                    print("\nThere are no available seats for an astronaut on {0}".format(self.spacecraft[spacecraft2].name))
                                                    print("You cannot transfer {0}".format(self.spacecraft[spacecraft1].component[answer_component].name))
                                                    component_detach = False
                                                    
                                                else:
                                                    component_detach = True
       
                                                
                                            if component_detach == True:
                                                
                                                print("You detach {0} from {1} and transfer it to {2}".format(self.spacecraft[spacecraft1].component[answer_component].name ,self.spacecraft[spacecraft1].name, self.spacecraft[spacecraft2].name ))
    											
                                                #ajouter component au spacecraft 2
                                                self.spacecraft[spacecraft2].component.append(self.spacecraft[spacecraft1].component[answer_component])
                                                #Corriger la modification de masse
                                                self.spacecraft[spacecraft2].mass += self.spacecraft[spacecraft1].component[answer_component].mass
                                                self.spacecraft[spacecraft1].mass -= self.spacecraft[spacecraft1].component[answer_component].mass
                                                #supprimer le component dans le spacecraft 1
                                                del self.spacecraft[spacecraft1].component[answer_component]
                                                #Reordonner les composants des 2 spacecrafts
                                                self.spacecraft[spacecraft1].arrangeComponents()
                                                self.spacecraft[spacecraft2].arrangeComponents()
                                            
                                            #sortie de boucle
                                            boucle2 = False
											
											
										#en cas d'erreur d'input
                                        else:
                                            print("Please enter a correct number.")
											
                                    else: #if i == 0  --- if there are no components anymore in the spacecraft, cancel the loop.
										
                                        rendez_vous = False
                                        boucle2 = False
                                        answer = 'n'
										
                                        print("There are no components left in {0}, the spacecraft doesn't exist anymore.".format(self.spacecraft[spacecraft1].name) )
								
                                
                                
								#transférer un autre component?
                                while answer != 'y' and answer != 'n':
									
                                    answer = input("\nWould you like to detach / attach another component? (y/n) : ")
									
                                    answer = answer.lower() # set every character in lower case
                                    answer = answer.replace("yes", "y") #replace yes by y
                                    answer = answer.replace("no" , "n") #replace no by n
									
								
                                    if answer == 'n':
									
                                        rendez_vous = False
									
                                    elif answer != 'y':
                                        print("Please, answer the question with yes or no.")
										

						#Del empty spacecrafts
                        
                        try:
                            if self.spacecraft[spacecraft1].component == []:
							
                                print("{0} has no components on board, it has been deleted from your spacecraft list.".format(self.spacecraft[spacecraft1].name))
                                self.DestroySpacecraft(spacecraft1)
							
                        except:
                            pass
                        
                        try:
                            if self.spacecraft[spacecraft2].component == []:
							
                                print("{0} has no components on board, it has been deleted from your spacecraft list.".format(self.spacecraft[spacecraft2].name))
                                self.DestroySpacecraft(spacecraft2)
                            
                        except:
                            pass
					

                    
            #Si tu n'as pas la techno; afficher message d'erreur.                    
            else:
                print("You can't initiate a Rendez-vous, you first need to acquire the technology.")                
                        
    def ACTION_survey(self, loc, craft, locations, players, p, missions, accomplished_missions, radiation_level):
            """ survey (if possible) in loc with craft
            outcome is drawn
            ask if information is shared"""
            
            able_to_survey = False
                      
            # 1) check if player has develop surveying
            if not "surveying" in self.advancements:
                print("You first need to start researching the surveying technology")
                
            # check if spacecraft exists
            elif not craft in self.spacecraft.keys():
                print("You don't have such a spacecraft")
            
            # 2) check if there's something to survey from the location of the spacecraft
            
                
            elif locations[loc].name not in self.spacecraft[craft].location.surveying:
                print("You can not survey {0} from {1} ".format(loc, craft) )
            
               
            elif self.spacecraft[craft].ttoken > 0:
                print("This spacecraft is currently traveling to {0}, and will reach destination in {1} year".format(self.spacecraft[craft].location.name, self.spacecraft[craft].ttoken))
                print("You'll need to wait untill then to be able to Survey with {0}.".format(self.spacecraft[craft].name))
                
            else:
                # 3) check if spacecraft is correctly equiped to survey
                for comp in self.spacecraft[craft].component:
                    if type(comp) in [Probe, Capsule] and comp.state == 1:
                        able_to_survey = True    
                
                if not able_to_survey:
                    print("Your spacecraft is not equiped to survey, you need a working probe or capsule for this operation")
                else:
                    
                    # 4) check if it is need to draw an outcome
                    # (no more outcome --> automatic success)
                    result = self.draw_outcome("surveying")
                            
                    # 5) action
                    if result == "success":
                        
                        explo_type = 'survey'
                        exploration = get_exploration_results(explo_type, radiation_level, locations, loc)
                        if len(players) > 1:
                            sharing = ask_for_sharing_explo('survey')
                        else:
                            sharing = 'yes' # if only one player, it's considered shared
                        
                        if sharing in ['yes', 'y']:
                            locations[loc].explored = True
                            players, missions, accomplished_missions = check_missions(locations, missions, players, p, accomplished_missions)
                                                          
                    else:
                        print("Luckily the probes cannot be damaged in case a survey fails")  
                        
    def ACTION_collect(self, loc, locations):
            """ collect a sample (if possible) and add it into player's spacecraft"""
            
            if not locations[loc].explorable or locations[loc].name == "suborbitalflight":
                print("There is nothing to collect here, where do you think you are??")
            else:
                craft_in_situ = []
                for key in self.spacecraft:
                    if self.spacecraft[key].location.name == loc:
                        craft_in_situ.append(self.spacecraft[key])
                if len(craft_in_situ) == 0 :
                    print("You don't have a spacecraft here")
                
                else:
                    able_to_collect = False
                    elligible = []
                    
                    for craft in craft_in_situ:
                        if craft.ttoken == 0:
                            for comp in craft.component:
                                if type(comp) in [Probe, Capsule, Astronaut] and comp.state == 1:
                                    able_to_collect = True
                                    elligible.append(craft)
                    
                    if not able_to_collect:
                        print("You need an undamaged probe or a capsule, or a healtly astronaut to collect something")
                        print("Or maybe your spacecraft is not at destination yet")
                        action = False
                    elif len(elligible)>1:
                        print("It seemls you have different spacecrafts able to collect a sample here")
                        i = 0
                        for elem in elligible:
                            print(i, " :", elem.name)
                            i+=1
                        i = int(input("Which one is taking the sample? :"))
                        spacecraft_chosen = elligible[i]
                        action = True
                    else: 
                        spacecraft_chosen = elligible[0]
                        action = True
                    
                    if action:
                        #print(locations[choice[1]].exploration)
                        try: 
                            value = locations[loc].exploration["minerals"]
                            
                        except: 
                            value = 0
                        
                        if locations[loc].exploration == "alien origin":
                            
                            research = True
                            
                        else:
                            research = False
                            
                        if locations[loc].exploration == "life" or locations[loc].exploration == ('life', 'supplies'):
                            
                            life = True
                            
                        else: 
                            life = False
                        
                        sam = Sample(locations[loc].name, value, research, life)
                        
                        if locations[loc].exploration == 'supplies' or locations[loc].exploration == ("life", "supplies"):
                            what = 'noword'
                            
                            while what not in ['supply', 'sample']:
                                what = input("There are supplies available here, would you like to take one supply or a normal sample ? (supply/sample): ")
                            
                            if what == 'supply':
                                spacecraft_chosen.component.append(obj('supply'))
                                print("supply collected and taken on {0} board".format(spacecraft_chosen.name))
                        else:
                            spacecraft_chosen.component.append(sam)
                            print("sample collected and taken on {0} board".format(spacecraft_chosen.name))
                        
                            if sam.value > 0:
                                print("This sample will give you {0}$ if you bring it back on Earth".format(sam.value))
                                    
                            if sam.research == True:
                                print("This sample will yield new scientific knowledge when turned in on Earth at the start of the year.")
                                print("You may gain a new advancement with no outcome cards on it, or you may remove all outcome cards from any one of your existing advancements.")
                                
                            if sam.life == True:
                                print("This sample contains extraterrestrial life")