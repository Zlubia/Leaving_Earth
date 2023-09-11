# -*- coding: utf-8 -*-
    

"""
TABLE DES MATIERES
------------------

Class Rocket

Class Thruster

Class Astronaut

Class Probe

Class Capsule

Class Supply

Class Sample

"""

class Rocket:
    """
    - (name)
    - thrust
	- outcomes (knew or not)
    """
    
    def __init__(self, name, cost, mass, thrust):         # class constructor
        """Rocket is initialized"""
        self.name = name
        self.cost = cost
        self.thrust = thrust
        self.mass = mass
        self.state = 1
        # self.location = 0 #will set to a location if component is disassembled in space
        self.counter = 1
        self.damaged = 0
        self.requirements = [name] # list of advancements required to buy the component. For Rocket, it's the name
            
        # self.outcomes  # to adapt if advancement is already tested 
        
class Thruster:
    """
    - (name)
    - thrust
	- outcomes (knew or not)
    """
    
    def __init__(self, name = "ionthruster", cost=10, mass=1, thrust=5):         # class constructor
        """Rocket is initialized"""
        self.name = name
        self.cost = cost
        self.state = 1
        self.thrust = thrust
        self.mass = mass
        self.counter = 1
        self.damaged = 0
        self.requirements = ["ionthruster"] # list of advancements required to buy the component. For Rocket, it's the name
            
        # self.outcomes  # to adapt if advancement is already tested 
        
class Astronaut:
    """
    - competence
    - healt status
    """
    
    def __init__(self, name, skill, cost=5, mass=0):         # class constructor
        """Astronaut is initialized"""
        self.name = name
        self.cost = cost
        self.mass = mass
        self.skill = skill      # Mechanic, Doctor or Pilot
        self.state = 1    # can be incapacitated
        #self.location = 0 #will set to a location if component is disassembled in space
        self.requirements = []
        self.route = []
    
class Probe:
    """
    - name
    - cost
    - mass
    """
    
    def __init__(self, name = "probe", cost=2, mass=1):         # class constructor
        """Probe is initialized"""
        self.name = name
        self.cost = cost
        self.mass = mass
        self.state = 1
        #self.location = 0 #will set to a location if component is disassembled in space
        self.requirements = []

class Capsule:
    """
    - capacity
    - state ? (damaged etc)
    """
    def __init__(self, name, cost, mass, capacity, heatshield, requirement):         # class constructor
        """Probe is initialized"""
        self.name = name
        self.cost = cost
        self.mass = mass
        self.state = 1
        self.capacity = capacity                #number of astronauts it can carry
        self.heatshield = heatshield    #can be true or false, can re-enter atmosphere if true.
        #self.location = 0 #will set to a location if component is disassembled in space
        self.requirements = requirement

class Supply:
    """
    
    """
    
    def __init__(self, name = "supply", cost=1, mass=1):         # class constructor
        """Supply is initialized"""
        self.name = "supply"
        self.cost = cost
        self.mass = mass
        self.state = 1
        #self.location = 0 #will set to a location if component is disassembled in space
        self.requirements = ["lifesupport"]

class Sample:

    def __init__(self, location_name, value = 0, mass = 1, research = False, life = 0):
        
        self.name = "sample"
        self.location = location_name
        self.value = value
        self.mass = mass
        self.state = 1
        self.research = research
        self.life = life