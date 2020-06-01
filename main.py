import pygame
from app import Application

#program execution
if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("labyrinth of mcgyver")
    application_class = Application()
    application_class.main_display()
    application_class.main_loop()
    pygame.quit()