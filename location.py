# -*- coding: utf-8 -*-


class Location:
    
    def __init__(self, name, dict_maneuvers, surveying = [], auto_maneuver = "no auto maneuver",  exploration = ["no effect"], explorable = False, explored = False):         # class constructor
        """Location is initialized"""
        self.name = name
        self.maneuvers = dict_maneuvers         
            #Encoder sous forme de dictionnaire de listes 
            #[difficulté, time tokens, "hasards: no hasard, solar radiation, atmospheric_entry, landing, optionnal landing"]
        
        self.auto_maneuver = auto_maneuver
        self.exploration = exploration
            #No effect, spacecraft destroyed, minerals, supplies, sickness, radiation, life, alien origin 
        self.explorable = explorable    
            #boolean, True if the location is explorable
        self.surveying = surveying
            #list of locations that we can survey from this location.
        self.explored = explored
       
            
        # self.outcomes  # to adapt if advancement is already tested 