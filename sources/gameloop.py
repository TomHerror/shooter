from textures import *
from window import *
from shooter import *

def gameLoop(window, pygame):
    BLACK = ( 0, 0, 0)
    WHITE = ( 255, 255, 255)
    GREEN = ( 0, 255, 0)
    RED = ( 255, 0, 0)

    shooter_texture = load_shooter(pygame)

    # The clock will be used to control how fast the screen updates
    clock = pygame.time.Clock()

    dim = get_size_window()
    shooter = Shooter(dim)
    
    # The loop will carry on until the user exit the game (e.g. clicks the close button).
    quit = False
    # -------- Main Program Loop -----------
    while quit == False:
        # --- Main event loop
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                    quit = True # Flag that we are done so we exit this loop
 
        # --- Game logic should go here
 
        # --- Drawing code should go here
    
        #The you can draw different shapes and lines or add text to your background stage.
        # First, clear the screen to white. 
        window.fill(BLACK)
        window.blit(shooter_texture, (shooter.x, shooter.y))


        #if cube[1] <= 430:
        #    cube[1] += 1
        
        pygame.time.wait(100)
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
     
        # --- Limit to 60 frames per second
        clock.tick(60)