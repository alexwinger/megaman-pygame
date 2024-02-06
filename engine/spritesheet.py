import os
import pygame
import json

class SpriteSheet:
    def __init__(self, def_filename):
        self.spriteGroups = {}
        self.animations = {}

        with open(def_filename,'r') as deffile:
            sheetdefinition=json.load(deffile)
        
        self.sprite_sheet = pygame.image.load(sheetdefinition["imagefile"])
        self.colorkey = (sheetdefinition["colorkey"][0],sheetdefinition["colorkey"][1],sheetdefinition["colorkey"][2])
        spriteGroups = sheetdefinition["SpriteGroups"]
        for groupName,frameAreas in spriteGroups.items():
            self.createSpriteGroup(groupName,frameAreas)

        for animationName,stepDefinition in sheetdefinition["Animations"].items():
            self.createAnimation(animationName, stepDefinition)

    def createSpriteGroup(self, name, areas):
        self.spriteGroups[name] = []
        for area in areas:
            image = pygame.Surface((area['width'], area['height'])).convert_alpha()
            image.blit(self.sprite_sheet, (0, 0), (area['startx'], area['starty'], area['width'], area['height']))
            image.set_colorkey(self.colorkey)
            self.spriteGroups[name].append(image)
    
    def createAnimation(self, name, steps):
        self.animations[name] = []
        for step in steps:
            self.animations[name].append(Frame(step['spriteGroup'], step['spriteNumber'], step['duration'], step['nextFrame']))

    def getImage(self, groupName, frameNumber, flipx, flipy):
        group = self.spriteGroups[groupName]
        image = pygame.transform.flip(group[frameNumber], flipx, flipy).convert_alpha()
        image.set_colorkey(self.colorkey)
        return image

class Frame:
    def __init__(self, spriteGroup, spriteNumber, frameDuration, nextStep):
        self.spriteGroup   = spriteGroup
        self.spriteNumber  = spriteNumber
        self.frameDuration = frameDuration
        self.nextStep = nextStep
