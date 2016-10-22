import numpy

from matplotlib import pyplot as plt
from matplotlib import lines as mlines

from oscillator import Oscillator


def plot_underdamped_pendulum():
    pendulum = Oscillator(alpha=0.8, radius=1)
    time_steps = 400
    time_max = 10.0
    time = numpy.linspace(0, time_max, time_steps + 1)
    plt.axes(xlim=(0, 10), ylim=(-0.2, 0.2))
    trajectory = pendulum.get_trajectory(time_max, time_steps)
    theta = [position for position, velocity in trajectory]
    plt.plot(time, theta, "r")


def plot_overdamped_pendulum():
    pendulum = Oscillator(alpha=30, radius=1)
    time_steps = 400
    time_max = 10.0
    time = numpy.linspace(0, time_max, time_steps + 1)
    plt.axes(xlim=(0, 10), ylim=(-0.2, 0.2))
    trajectory = pendulum.get_trajectory(time_max, time_steps)
    theta = [position for position, velocity in trajectory]
    plt.plot(time, theta, "b")


def plot_critically_damped_pendulum():
    pendulum = Oscillator(alpha=6, radius=1)
    time_steps = 400
    time_max = 10.0
    time = numpy.linspace(0, time_max, time_steps + 1)
    plt.axes(xlim=(0, 10), ylim=(-0.2, 0.2))
    trajectory = pendulum.get_trajectory(time_max, time_steps)
    theta = [position for position, velocity in trajectory]
    plt.plot(time, theta, "g")

plot_underdamped_pendulum()
plot_overdamped_pendulum()
plot_critically_damped_pendulum()

plt.xlabel("Time")
plt.ylabel("Angular Displacement")

red_line = mlines.Line2D([], [], color='red',
                          markersize=15, label='Underdamped Pendulum')
blue_line = mlines.Line2D([], [], color='blue',
                          markersize=15, label='Overdamped Pendulum')
green_line = mlines.Line2D([], [], color='green',
                           markersize=15, label='Critically Damped Pendulum')

plt.legend(handles=[red_line, blue_line, green_line])

plt.savefig("pendulum.png")
