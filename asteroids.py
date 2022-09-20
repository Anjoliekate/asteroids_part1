import pygame
import ship
import rock
NUM_ROCKS = 10

class Asteroids:
    
    def __init__(self, world_width, world_height):
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        self.mShip = ship.Ship(self.mWorldWidth/2, self.mWorldHeight/2, self.mWorldWidth, self.mWorldHeight)
        self.mRocks = []
        for i in range(NUM_ROCKS):
            self.mRocks.append(rock.Rock(0, 0, self.mWorldWidth, self.mWorldHeight))
        self.mObjects = [self.mShip] + self.mRocks
      
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    def getShip(self):
        return self.mShip
    
    def getRocks(self):
        return self.mRocks
    
    def getObjects(self):
        return self.mObjects
    
    def turnShipLeft(self, delta_rotation):
        self.mShip.rotate(-delta_rotation)
    
    def turnShipRight(self, delta_rotation):
        self.mShip.rotate(delta_rotation)
    
    def accelerateShip(self, delta_velocity):
        self.mShip.accelerate(delta_velocity)
        
    def evolve(self, dt):
        for ob in self.mObjects:
            ob.evolve(dt)
              
    def draw(self, surface):
        surface.fill((0,0,0))
        for ob in self.mObjects:
            ob.draw(surface)
