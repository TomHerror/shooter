import gameloop 
from window import *
import gameloop
from allclass.shooterBullet import *
from allclass.shooter import *
from allclass.enemy import *

def draw_all(window, pygame):
    for tabs in gameloop.entity:
        for elem in tabs:
            print(elem.texture)
            if elem.alive == 1:
                if type(elem) is Shooter:
                    elem.draw_self(window)
                    if elem.isShooting: 
                        elem.shoot(pygame)
                    
                elif type(elem) is Enemy:
                    elem.draw_self(window)
                    elem.move()
                    print(elem.x, elem.y)
                
                elif type(elem) is ShooterBullet:
                    elem.draw_self(window) 
                    elem.move()
                
            else:
                for i in tabs:
                    if i == elem:
                        index = tabs.index(elem)
                        del tabs[index]