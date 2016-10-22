from matplotlib import pyplot as plt

from oscillator import Oscillator


def plot_theta_vs_theta_dash():
    pendulum = Oscillator(alpha=0.8, radius=1)
    time_steps = 400
    time_max = 10.0
    plt.axes(xlim=(-0.1, 0.1), ylim=(-0.25, 0.25))
    trajectory = pendulum.get_trajectory(time_max, time_steps)
    theta = [position for position, velocity in trajectory]
    theta_dash = [velocity for position, velocity in trajectory]
    plt.plot(theta, theta_dash, "b")

plot_theta_vs_theta_dash()

plt.xlabel("Angular Displacement", fontsize=13, family='monospace')
plt.ylabel("Angular Velocity", fontsize=13, family='monospace')
plt.title("Angular Displacement v/s Angular Velocity", fontsize=13, family='monospace')

plt.savefig("theta_vs_theta_dash.png")
# plt.show()
