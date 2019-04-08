import gameloop 
from window import *
import gameloop
from allclass.shooterBullet import *
from allclass.shooter import *

def draw_all(window, pygame):
    for tabs in gameloop.entity:
        for elem in tabs:
            if elem.alive == 1:
                elem.draw_self(window)
                if type(elem) is Shooter:
                    if elem.isShooting: 
                        elem.shoot(pygame)
                
                
                if type(elem) is ShooterBullet: 
                    elem.move()
            else:
                for i in tabs:
                    if i == elem:
                        index = tabs.index(elem)
                        del tabs[index]
