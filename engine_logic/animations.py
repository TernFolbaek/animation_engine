class Animation:
    def __init__(self,target,start_time=0, end_time=1):
        self.target = target
        self.start_time = start_time
        self.end_time = end_time

    def update(self, t):
        pass

class Move(Animation):
    def __init__(self, target, start_pos, end_pos, start_time=0, end_time=1):
        super().__init__(target, start_time, end_time)
        self.start_pos = start_pos
        self.end_pos = end_pos
    
    def update(self, t):
        # Linear interpolation
        self.target.x = self.start_pos[0] + t * (self.end_pos[0] - self.start_pos[0])
        self.target.y = self.start_pos[1] + t * (self.end_pos[1] - self.start_pos[1])

class FadeIn(Animation):
    def __init__(self,target, start_time=0, end_time=1):
        super().__init__(target, start_time, end_time)
    
    def uodate(self, t):
        self.target.opacity = t

class FadeOut(Animation):
    def __init__(self, target, start_time=0, end_time=1):
        super().__init__(target, start_time, end_time)
    
    def update(self, t):
        self.target.opacity = 1 -t 