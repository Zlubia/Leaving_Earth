# -*- coding: utf-8 -*-


from location import*
from advancements import*
from missions import*


print("Which challenge for this game? \n 1: Easy \n 2: Normal \n 3: Hard \n 4: Very Hard \n 5: All missions active")
i = input("enter your choice : ")
    
    
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
         
missions = []
    
#Easy Missions

missions.append( Mission("mars_survey", "easy" , 5 , "survey" , "mars"))

missions.append( Mission("man_in_space", "easy" , 2 , "man return" , "suborbital_flight"))

missions.append( Mission("sounding_rocket" , "easy" , 1 , "probe" , "suborbital_flight"))

missions.append( Mission("artificial_satellite" , "easy" , 2 , "probe" , "earth_orbit"))

missions.append( Mission("lunar_survey" , "easy" , 4 , "survey" , "moon"))

missions.append( Mission("man_in_orbit" , "easy" , 4 , "man return", "earth_orbit"))


#Medium missions

missions.append( Mission("phobos_sample_return", "medium" , 12 , "sample return" , "phobos"))

missions.append( Mission("space_station" , "medium" , 6 , "outpost" , "earth_orbit"))

missions.append( Mission("mercury_lander" , "medium" , 13 , "probe" , "mercury"))

missions.append( Mission("venus_lander" , "medium" , 11 , "probe" , "venus"))

missions.append( Mission("mars_lander" , "medium" , 7 , "probe", "mars"))

missions.append( Mission("mercury_survey" , "medium" , 7 , "survey" , "mercury"))

missions.append( Mission("ceres_lander" , "medium" , 8 , "probe" , "ceres"))

missions.append( Mission("man_on_the_moon" , "medium" , 12 , "man return" , "moon"))

missions.append( Mission("venus_survey" , "medium" , 6 , "survey" , "venus"))

missions.append( Mission("lunar_lander" , "medium" , 6 , "probe" , "moon"))

missions.append( Mission("lunar_sample_return" , "medium" , 10 , "sample return" , "moon"))


#Hard missions

missions.append( Mission("mars_sample_return" , "hard" , 16 , "sample return" , "mars"))

missions.append( Mission("ceres_sample_return" , "hard" , 14 , "sample return" , "ceres"))

missions.append( Mission("mercury_sample_return" , "hard" , 19 , "sample return" , "mercury"))

missions.append( Mission("venus_station" , "hard" , 27 , "outpost" , "venus"))

missions.append( Mission("man_on_mars" , "hard" , 24 , "man return" , "mars"))

missions.append( Mission("lunar_station" , "hard" , 15 , "outpost" , "moon"))

missions.append( Mission("mars_station" , "hard" , 20 , "outpost" , "mars"))

missions.append( Mission("extraterrestrial_life" , "hard" , 40 , "sample return" , "life"))

missions.append( Mission("man_on_venus" , "hard" , 32 , "man return" , "venus"))

missions.append( Mission("venus_sample_return" , "hard" , 24 , "sample return" , "venus"))


# make lists of easy, medium and hard missions

easy_missions = [element for element in missions if element.difficulty == "easy"]

medium_missions = [element for element in missions if element.difficulty == "medium"]

hard_missions = [element for element in missions if element.difficulty == "hard"]


# shuffle the lists of easy, medium and hard missions

random.shuffle(easy_missions)
random.shuffle(medium_missions)
random.shuffle(hard_missions)


#drawing the missions according to the chosen challenge level

if i == '1': 
    # Easy challenge has been chosen : 5 easy missions will de drawn.
    
    index = len(easy_missions) - 5
    #number of missions that will be removed from the easy_missions list.
    
    while index > 0:
    #remove the spare easy missions 
        del easy_missions[index + 4] # + 4 to remove the last items from the list
        index -= 1
    
    missions = easy_missions

    
elif i == '2':
    # Normal challenge has been chosen : 4 easy and 2 medium missions will be drawn
    
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
    
    
elif i == '3':    
    # Hard challenge has been chosen : 3 easy, 3 medium and 2 hard missions will be drawn
    
    
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
    
    
    
elif i == '4':    
    # Very Hard challenge has been chosen : 1 easy, 4 medium and 4 hard missions will be drawn
    
    
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
    
    
elif i =='5':
    #All missions are available
    
    missions = easy_missions + medium_missions + hard_missions
    
else:
    
    print("Please read the instructions carefully and answer something plausible")
        
index = len(missions) -1

while index >= 0:
    print(missions[index].name)
    index -= 1



