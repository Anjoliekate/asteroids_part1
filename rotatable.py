import movable
import math

class Rotatable(movable.Movable):
    
    def __init__(self, x, y, dx, dy, rotation, world_width, world_height):
        super().__init__(x, y, dx, dy, world_width, world_height)
        self.mRotation = rotation
        
    def getRotation(self):
        return self.mRotation
    
    def rotate(self, delta_rotation):
        self.mRotation += delta_rotation
        self.mRotation %= 360
        
        
    def splitDeltaVIntoXAndY(self, rotation, delta_velocity):
        rotation = math.radians(rotation)
        delta_x = delta_velocity * math.cos(rotation)
        delta_y = delta_velocity * math.sin(rotation)
        return (delta_x, delta_y)
        
    def accelerate(self, delta_velocity):
        (delta_x, delta_y) = self.splitDeltaVIntoXAndY(self.mRotation, delta_velocity)
        self.mDX += delta_x
        self.mDY += delta_y
        
    def rotatePoint(self, x, y):
        d = math.sqrt(x*x + y*y)
        phi = math.atan2(y, x)
        new_angle = phi + math.radians(self.mRotation)
        
        new_x = d * math.cos(new_angle)
        new_y = d * math.sin(new_angle)
        
        return (new_x, new_y)
        
    def translatePoint(self, x, y):
        x += self.mX
        y += self.mY
        return (x, y)
    
    def rotateAndTranslatePoint(self, x, y):
        (x, y) = self.rotatePoint(x,y)
        (x, y) = self.translatePoint(x,y)
        return (x, y)
        
    def rotateAndTranslatePointList(self, point_list):
        new_point_list = []
        for (x,y) in point_list:
            new_point_list.append(self.rotateAndTranslatePoint(x,y))
        
        return new_point_list
        
        
        
        

