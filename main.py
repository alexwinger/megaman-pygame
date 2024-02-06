import pygame
from engine.spritesheet import SpriteSheet
from engine.object import Object

WIDTH, HEIGHT = 640,480
FPS = 60
SCREEN= pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Megaman")
CLOCK = pygame.time.Clock()

class Megaman(Object):
    def __init__(self, posx, posy):
        super().__init__(SpriteSheet("sprites/megaman.json"),posx, posy)

    def update(self):
        if(self.updateAnimation()):
            self.posx+= self.velx
            self.posy+= self.vely

    def Run(self, toRight):
        if(player.setAnimation("RUNNING")):
            if(toRight):
                self.velx=1
                self.flip_x=False
            else:
                self.velx=-1
                self.flip_x=True
            self.posx+=self.velx

    def Stop(self):
        player.setAnimation("STANDING")
        player.velx=0

def pollInputs():
    pressed_keys = pygame.key.get_pressed()
    if(pressed_keys[pygame.K_RIGHT]):
        player.Run(True)
    elif(pressed_keys[pygame.K_LEFT]):
        player.Run(False)
    else:
        player.Stop()

def main():
    player2.setAnimation("STANDING")
    player.setAnimation("RUNNING")

    run = True
    while run:

        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pollInputs()

        player.update()
        player2.update()
        SCREEN.fill((128,128,128))
        player.draw(SCREEN)
        player2.draw(SCREEN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    player2 = Megaman(75,50)
    player = Megaman(40, 40)
    main()
