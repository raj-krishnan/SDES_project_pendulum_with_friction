import matplotlib.lines as mlines
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

from oscillator.oscillator import Oscillator

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-0.22, 0.22))

theta_line, = ax.plot([], [], lw=2, color="green")
theta_dash_line, = ax.plot([], [], lw=2, color="blue")

time_steps = 400
time_max = 10.0
osc = Oscillator()

x = np.linspace(0, time_max, time_steps + 1)
trajectory = osc.get_trajectory(time_max, time_steps)

y = [position for position, velocity in trajectory]
y_dash = [velocity for position, velocity in trajectory]


def init():
    theta_line.set_data([], [])
    plt.xlabel("Time")
    plt.ylabel("Angular Displacement, Angular Velocity")
    plt.title("Angular Displacement and Angular Velocity v/s Time")
    blue_line = mlines.Line2D([], [], color='green',
                              markersize=15, label='Theta')
    green_line = mlines.Line2D([], [], color='blue',
                               markersize=15, label='Angular Velocity')
    plt.legend(handles=[blue_line, green_line])
    return theta_line,


def animate(i):
    theta_line.set_data(x[:i], y[:i])
    theta_dash_line.set_data(x[:i], y_dash[:i])
    return theta_line, theta_dash_line

animation_time = animation.FuncAnimation(fig, animate, init_func=init,
                                         frames=400, interval=10, blit=True)
animation_time.save('time_animation.mp4', fps=60,
                    extra_args=['-vcodec', 'libx264'])
