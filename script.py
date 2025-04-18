from engine import *
# Create a simple animation
anim = SimpleAnimation(width=1280, height=720, duration=5, fps=30)

# Create objects
circle = anim.add_object(Circle(x=2, y=5, radius=1, color='blue'))
text = anim.add_object(Text(text="Simple Animation Engine", x=5, y=7, color='white', size=36))

# Create animations
anim.add_animation(FadeIn(circle, start_time=0, end_time=0.3))
anim.add_animation(Move(circle, start_pos=(2, 5), end_pos=(8, 5), start_time=0.3, end_time=0.8))
anim.add_animation(FadeIn(text, start_time=0.5, end_time=0.8))
anim.add_animation(FadeOut(circle, start_time=0.8, end_time=1.0))

# Render
anim.render("first_animation.mp4")