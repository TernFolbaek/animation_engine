import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Scene:
    def __init__(self, width=1280, height=720, duration=5, fps=30):
        self.width= width
        self.height = height
        self.duration = duration
        self.fps = fps
        self.frames = int(duration*fps)

        # Set up the figure and axis
        self.fig, self.ax = plt.subplots(figsize=(width/100, height/100), dpi=100)
        self.ax.set_xlim(0,10)
        self.ax.set_ylim(0,10 * height/width)
        self.ax.set_axis_off()
        self.fig.set_facecolor('black')
        self.ax.set_facecolor('black')

        # Store objects and animations
        self.objects = []
        self.animations = []

    def add_object(self,obj):
        self.objects.append(obj)
        return obj

    def add_animation(self, animation):
        self.animations.append(animation)

    def update(self, frame):
        self.ax.clear()
        self.ax.set_xlim(0,10)
        self.ax.set_ylim(0,10 * self.height/self.width)
        self.ax.set_axis_off()

        # Calculate time progress (0 to 1)
        t = frame / self.frames

        for anim in self.animations:
            if anim.start_time <= t <= anim.end_time:
                # Normalize time for this animation
                local_t = (t - anim.start_time) / (anim.end_time - anim.start_time)
                anim.update(local_t)

        # Draw all objects
        for obj in self.objects:
            obj.draw(self.ax)
        
        return []
    
    def render(self, filename="animation.mp4"):
        ani = animation.FuncAnimation(
            self.fig, self.update, frames=self.frames, interval=1000/self.fps, blit=False
        )

        #save as mp4
        writer = animation.FFMpegWriter(fps=self.fps, bitrate=5000)
        ani.save(filename, writer=writer)
        plt.close()
        print(f"Animation saved as {filename}")
        
