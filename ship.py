import polygon

class Ship(polygon.Polygon):
    
    def __init__(self, x, y, world_width, world_height):
        super().__init__(x, y, 0, 0, 0,  world_width, world_height)
        self.setPolygon([(0, 0),(-15, -5),(-15, 5)])
        
    def evolve(self, dt):
        self.move(dt)