# -*- coding: utf-8 -*-


class Mission:
    
    def __init__(self, name, difficulty, reward, mission_type, goal):         # class constructor
        """Mission is initialized"""
        self.name = name
        self.difficulty = difficulty    
        #Difficulty can either be easy, medium or hard
        self.reward = reward
        #amount of victory points awarded after the completion of the mission
        self.type = mission_type
        #There are 5 types of missions: survey, sample return, probe, manned return, outpost
        self.goal = goal
        #the location of the goal of the mission.
        #if it's a survey; the location to reveal
        #sample return; the location the sample is from
        #probe; the location the working probe or capsule needs to be
        #manned return; the location the man visited
        #outpost; the location where an astronaut needs to be at the start of the year
         