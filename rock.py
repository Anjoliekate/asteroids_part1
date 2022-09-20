import polygon
import random
import math

class Rock(polygon.Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, random.uniform(0.0, 359.9), world_width, world_height)
        self.mSpinRate = random.uniform(-90.0, 90.0)
        self.accelerate(random.uniform(10, 20))
        self.setPolygon(self.createRandomPolygon(random.uniform(50, 100), random.randint(5, 8)))
        
    def createRandomPolygon(self, radius, number_of_points):
        point_list = []
        for i in range(number_of_points):
            theta = (360 / number_of_points) * i
            d = random.uniform(.7*radius, 1.3*radius)
            theta = math.radians(theta)
            x = d * math.cos(theta)
            y = d * math.sin(theta)
            point_list.append((x,y))
        return point_list
            
        
    def getSpinRate(self):
        return self.mSpinRate
        
    def setSpinRate(self, spin_rate):
        self.mSpinRate = spin_rate
            
    def evolve(self, dt):
        self.rotate(dt * self.mSpinRate)
        self.move(dt)
                        