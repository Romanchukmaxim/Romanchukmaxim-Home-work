import pygame

class Button:
    def __init__(self, x, y, width, height, text=None, colour=(70, 70, 70), highlitedColour=(180, 180, 180), function=None, params=None):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.downleft = self.pos
        self.text = text
        self.colour = colour
        self.highlitedColour = highlitedColour
        self.function = function
        self.params = params
        self.highlited =False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlited = True
        else:
            self.highlited = False

    def draw(self, window):
        if self.highlited:
            self.image.fill(self.highlitedColour)
        else:
            self.image.fill(self.colour)
        window.blit(self.image, self.pos)