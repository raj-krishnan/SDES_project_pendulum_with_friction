import numpy as np
from matplotlib import pyplot as plt
import math
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
from oscillator.oscillator import Oscillator

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-0.1, 0.1))
line, = ax.plot([], [], lw=2)

time_steps = 400
time_max = 10.0
osc = Oscillator()
x = np.linspace(0, time_max, time_steps + 1)
trajectory = osc.get_trajectory(time_max, time_steps)
y = [position for position, velocity in trajectory]
y_dash = [velocity for position, velocity in trajectory]

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    plt.xlabel("Time")
    plt.ylabel("Theta")
    return line,


# animation function.  This is called sequentially
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=400, interval=10, blit=True)
anim.save('position_animation.mp4', fps=60, extra_args=['-vcodec', 'libx264'])

plt.show()
