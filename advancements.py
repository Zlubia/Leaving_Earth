# -*- coding: utf-8 -*-

import random

class Advancement:
    """when an advancement is created and add to player.advancement{}, it as a number of outcomes
    - name
	- outcomes (randomly set)
    """

    def __init__(self, name, chance):         # class constructor
        """Advancement is initialized"""
        self.name = name
        self.outcomes = []
        
        if name in ["juno", "atlas", "soyuz", "saturn", "ionthruster", "rendezvous" \
                    , "reentry", "landing", "lifesupport"]: 
            #draw 3 random outcomes
            if not chance: # normal situation 
                self.outcomes.append(random.choice(["success" , "success" , "success" , "success" , "minor failure" , "major failure"])) 
                self.outcomes.append(random.choice(["success" , "success" , "success" , "success" , "minor failure" , "major failure"]))
                self.outcomes.append(random.choice(["success" , "success" , "success" , "success" , "minor failure" , "major failure"]))
            
            if chance:
            #developper mode:
                self.outcomes.append(random.choice(["success"]))
                self.outcomes.append(random.choice(["success"]))
                self.outcomes.append(random.choice(["success"]))
                #self.outcomes.append(random.choice(["minor failure"]))
                #self.outcomes.append(random.choice(["major failure"]))
            
        elif name == "surveying": 
            if not chance:
            #draw 1 random outcomes
                self.outcomes.append(random.choice(["success" , "success" , "success" , "success" , "minor failure" , "major failure"]))
            if chance:
                self.outcomes.append(random.choice(["success"]))
            
        else:
            raise NameError("Invalid name") # je lève manuellement une exception, pour forcer une erreur
            # en fait elle ne produit pas d'erreur si la boucle entière est dans un try. en effet, le code "try"
            # de créer l'object, mais n'y parvient pas (Invalid name), et donc, il demande un autre input.
            # Je sais pas si c'est très propre mais bon :D
        