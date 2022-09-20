class Movable:
    
    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY = y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
     
    def getX(self):
        return self.mX
    
    def getY(self):
        return self.mY
    
    def getDX(self):
        return self.mDX
    
    def getDY(self):
        return self.mDY
    
    def getWorldWidth(self):
        return self.mWorldWidth
    
    def getWorldHeight(self):
        return self.mWorldHeight
    
    
    def move(self, dt):
        self.mX += self.mDX * dt
        self.mY += self.mDY * dt
        
        if self.mX >= self.mWorldWidth: #going off the right edge
            self.mX -= self.mWorldWidth
            
        elif self.mX < 0: #going off left edge
            self.mX += self.mWorldWidth
            
        self.mY %= self.mWorldHeight
        
        
    def accelerate(self, delta_velocity):
        raise NotImplementedError("accelerate method required in child class")
    
    def evolve(self, dt):
        raise NotImplementedError("evolve method required in child class")
    
    def draw(self, surface):
        raise NotImplementedError("draw method required in child class")
    
    
    
    
    