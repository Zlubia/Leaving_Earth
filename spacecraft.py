# -*- coding: utf-8 -*-


"""
TABLE DES MATIERES
------------------

class Spacecraft:
   
    def __init__(self, name, location)
    
    def addComponent(self, component, player)
    
    def arrangeComponents (self)
    
    def availableSeats (self)
    
    def astronautsOnBoard(self)
    
    def killAstronauts(self, player)
    
    def killAstronauts_bis(self, player, amount=1)
    
    def suppliesOnBoard(self)
    
    def samplesOnBoard(self)
    
    
"""



from components import *

class Spacecraft:                # class definition
    """class to define the spacecrafts, with
    - position
    - total mass
    - time tokens on it
    - list of components"""
    
    def __init__(self, name, location):         # class constructor
        """spacecraft is initialized empty and on earth"""
        self.name = name
        self.location = location       # spacecraft is initialised on earth or elsewhere (rendez vous)
        self.mass = 0      # spacecraft is initialized empty
        self.ttoken = 0         # no time token on it
        self.component = []    # empty list of component
        
    def addComponent(self, component, player):
        """Add a list of component to the spacecraft
        (use [elem, elem,.. ] to define, the list)
        adapt the spacecraft mass
        """
        
        player.component.remove(component) # component is remove from player's stock
        self.component.append(component) # component is added to spaceship's components
        print(component.name, "is taken from your stock and added to spacecraft")
        self.mass += component.mass
        print("spacecraft mass is equal to ", self.mass)
        
    def arrangeComponents (self):
        """ arrange components: Rockets, Trhuster, Probe, Capsule, Astronauts, Supplies, sample"""
        rocket=[]
        thruster=[]
        probe=[]
        capsule=[]
        astronaut=[]
        supply=[]
        sample=[]
        
        for comp in self.component:
            if type(comp) == Rocket: rocket.append(comp)
            elif type(comp) == Thruster: thruster.append(comp)
            elif type(comp) == Probe: probe.append(comp)
            elif type(comp) == Capsule: capsule.append(comp)
            elif type(comp) == Astronaut: astronaut.append(comp)
            elif type(comp) == Supply: supply.append(comp)
            elif type(comp) == Sample: sample.append(comp)
        
        rocket.sort(key = lambda x: x.thrust)
        
        self.component = rocket + thruster + probe + capsule + astronaut + supply + sample

    def availableSeats (self):
        """Number of available seats in the spacecraft"""
        available_seats = 0
        
        for comp in self.component:
            
            if type(comp) == Capsule:
                
                available_seats += comp.capacity
                
            elif type(comp) == Astronaut:
                
                available_seats -= 1
                
        return available_seats
    
    def astronautsOnBoard(self):
        """ lists astronauts in the spacecraft"""
        astronauts_list = []
        
        for comp in self.component:
            
            if type(comp) == Astronaut:
                
                astronauts_list.append(comp)
        
        return astronauts_list
    
    def killAstronauts(self, player):
        """ ask which astronauts to kill"""
        
        onboards = self.astronautsOnBoard()
        seats = self.availableSeats()
        deads = len(onboards) - seats
        
        print("Unfortunately, only {0} astronauts have seats still available on board".format(seats))
        print("{0} will die".format(deads))
        
        for astronaut in onboards:
            print('-', astronaut.name)
        
        goodbye = ''
        while(self.availableSeats > 0):
            goodbye = input('Which astronaut is dying?: ')
            
            for i in range(0, len(self.component)-1):
                if goodbye == self.component[i].name:
                    print('{0} die'.format(goodbye))
                    del self.component[i]
                    player.points =- 2
                    print(player.name, "loses 2 points.")
                    
    def killAstronauts_bis(self, player, amount=1):
        """ kill a number of astronauts """
        
        if amount == 1:
        
            print("\nUnfortunately an astronaut passed away \n")
        
        else:
            print("\nUnfortunately {0} astronauts have died \n".format(amount))
            
            
        while amount > 0:
            
            astronauts_on_board = self.astronautsOnBoard()
            supply_sample_amount = self.suppliesOnBoard() + self.samplesOnBoard()
            i = 0
            verification_list = []
            
            for astro in astronauts_on_board :
            
                print(i , ":" , astro.name)
                verification_list.append(i)
                i =+ 1
            
            try:
                killed = int(input("Which astronaut died ? :"))
            except:
                pass
            
            if killed in verification_list:
                
                #Formule pour obtenir l'indice du composant.
                killed = len(self.component) - supply_sample_amount - len(verification_list) + killed
                
                #Killing astronaut
                print("\n{0}, you will be missed. May you rest in space.".format(self.component[killed].name))
                del self.component[killed]
                self.arrangeComponents()
                player.points =- 2
                
                print(player.name, "loses 2 points.")
                
                amount = amount - 1

            else:
                print("Please enter a correct number.")
                
        return player
    
                

            
    def suppliesOnBoard(self):
        """ amount of supplies on board """
        
        supplies_on_board = 0        
        
        for comp in self.component:
            
            if type(comp) == Supply:
                
                supplies_on_board =+ 1
                
        return supplies_on_board
    
    def samplesOnBoard(self):
        """ amount of supplies on board """
        
        samples_on_board = 0
        
        for comp in self.component:
            
            if type(comp) == Sample:
                
                samples_on_board =+ 1
                
        return samples_on_board
    
                
            
            
            