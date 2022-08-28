import pygame

from const import *

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0
    
    # BLIT METHOD

    # updates visual position of piece
    def update_blit(self, surface):
        
        # slightly enlarges dragged piece (UX)
        self.piece.set_texture(size=128)
        texture = self.piece.texture

        # piece image
        img = pygame.image.load(texture)
        # piece center
        img_center = (self.mouseX, self.mouseY)

        # displays piece by mouse position
        self.piece.texture_rect = img.get_rect(center=img_center)
        surface.blit(img, self.piece.texture_rect)

    # OTHER METHODS

    # tracks mouse position
    def update_mouse(self, position):
        self.mouseX, self.mouseY = position # (Xcor, Ycor)
    
    # tracks initial click location (as a board coordinate)
    def save_initial(self, pos):
        self.initial_row = pos[1] // SQSIZE
        self.initial_col = pos[0] // SQSIZE
    
    # piece being dragged?
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    # piece released?
    def undrag_piece(self):
        self.piece = None
        self.dragging = False