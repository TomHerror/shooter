import os.path

yes = "yesyesyes"

def load_shooter(pygame):
    """
    redimensionne une image a la taille souhaitée
    """
    shooter = load_texture(pygame, '../img/whiteShooter.png')
    shooter = pygame.transform.scale(shooter, (64, 64))
    return shooter

def load_texture(pygame, PATH):
    """
    charge une texture,
    path vers l'image,
    """
    filepath = os.path.dirname(__file__)
    texture = pygame.image.load(os.path.join(filepath, PATH)).convert_alpha()

    return texture