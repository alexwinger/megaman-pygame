from abc import abstractmethod
from engine.spritesheet import SpriteSheet

class Object:
    def __init__(self,spritesheet, posx, posy):
        self.spritesheet = spritesheet
        self.setAnimation()
        self.animate=True
        self.flip_x = False
        self.flip_y = False
        self.posx = posx
        self.posy = posy
        self.velx=0
        self.vely=0

    def setAnimation(self, animationName=None):
        animationUpdated = True
        if animationName == None:
            keys = list(self.spritesheet.animations.keys())
            self.currentAnimation = self.spritesheet.animations[keys[0]]
            self.currentAnimationStep = self.currentAnimation[0]
            self.currentFrameDuration = self.currentAnimationStep.frameDuration
        elif self.spritesheet.animations[animationName] != self.currentAnimation:
            self.currentAnimation = self.spritesheet.animations[animationName]
            self.currentAnimationStep = self.currentAnimation[0]
            self.currentFrameDuration = self.currentAnimationStep.frameDuration
        else:
            animationUpdated = False
        return animationUpdated

    def updateAnimation(self):
        frameChanged = False
        if(self.animate):
            self.currentFrameDuration -= 1
            if (self.currentFrameDuration <= 0):
                self.currentAnimationStep = self.currentAnimation[self.currentAnimationStep.nextStep]
                self.currentFrameDuration = self.currentAnimationStep.frameDuration
                frameChanged = True

        return frameChanged

    def getImage(self):
        spriteGroup = self.currentAnimationStep.spriteGroup
        spriteNumber = self.currentAnimationStep.spriteNumber
        image = self.spritesheet.getImage(spriteGroup, spriteNumber, self.flip_x, self.flip_y)
        return image
    
    def draw(self, screen):
        image = self.getImage()
        screen.blit(image,(int(self.posx), int(self.posy)))

    def update(self):
        self.updateAnimation()
    

