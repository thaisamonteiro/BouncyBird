import pygame
from code.Const import WIN_WIDHT, WIN_HEIGHT
from code.Menu import Menu

class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WIN_WIDHT, WIN_HEIGHT)

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get()
            #    if event.type == pygame.QUIT:
            #       pygame.quit() # Closer window
            #       quit()
