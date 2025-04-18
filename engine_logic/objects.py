import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba

class Circle:
    def __init__(self, x=5, y=5, radius=1, color='white'):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.opacity = 1.0

    def draw(self,ax):
        circle = plt.Circle((self.x, self.y), self.radius, color=(*to_rgba(self.color)[:3], self.opacity), fill=True)
        ax.add_patch(circle)

class Text:
    def __init__(self, text="Text", x=5, y=5, color='white', size=24):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.opacity = 1.0

    def draw(self, ax):
        ax.text(self.x, self.y,self.text, color=(*to_rgba(self.color)[:3], self.opacity), fontsize = self.size, ha='center', va='center')
            