import math

from matplotlib import animation
from matplotlib import pyplot as plt

from oscillator import Oscillator

fig = plt.figure()
ax = plt.axes(xlim=(-0.1, 0.1), ylim=(-0.2, 1))

pendulum_bob, = ax.plot([], [], lw=2, marker='o', color="r", markersize=30)
pendulum_rod, = ax.plot([], [], lw=2, color="black")

time_steps = 400
time_max = 10.0
pendulum = Oscillator()

trajectory = pendulum.get_trajectory(time_max, time_steps)
y = [position for position, velocity in trajectory]
x_coord = [math.sin(position) for position, velocity in trajectory]
y_coord = [(1-math.cos(position)) for position, velocity in trajectory]


def init():
    pendulum_bob.set_data([], [])
    plt.title("Damped Pendulum Motion")
    plt.xlabel("X")
    plt.ylabel("Y")
    return pendulum_bob,


def animate(i):
    pendulum_bob.set_data(x_coord[i], y_coord[i])
    pendulum_rod.set_data([x_coord[i], 0], [y_coord[i], 1])
    return pendulum_bob, pendulum_rod

animation_coordinates = animation.FuncAnimation(fig, animate, init_func=init,
                                                frames=400, interval=10,
                                                blit=True)
animation_coordinates.save('coordinate_animation.mp4', fps=60,
                           extra_args=['-vcodec', 'libx264'])
