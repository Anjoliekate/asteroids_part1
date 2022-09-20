import rotatable
import pygame

class Polygon(rotatable.Rotatable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, rotation, world_width, world_height)
        self.mOriginalPolygon = []
        self.mColor = (255, 255, 255)
    
    def getPolygon(self):
        return self.mOriginalPolygon
    
    def getColor(self):
        return self.mColor
        
    def setPolygon(self, point_list):
        self.mOriginalPolygon = point_list
    
    def setColor(self, color):
        self.mColor = color
    
    def draw(self, surface):
        rt_point_list = self.rotateAndTranslatePointList(self.mOriginalPolygon)
        pygame.draw.polygon(surface, self.mColor, rt_point_list, 1)
        
    
    