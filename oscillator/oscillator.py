import math
import numpy
from scipy import constants
import scipy.integrate as integrate


class Oscillator:
    """
    Variable: theta
    First Derivative: theta_dash
    Second Derivative: theta_ddash
    """

    def __init__(self, state=(5 * math.pi / 180, 0), alpha=1.0, radius=1.0):
        allowed_types = [int, float]

        if type(c) not in allowed_types \
                or type(radius) not in allowed_types \
                or type(state[0]) not in allowed_types \
                or type(state[1]) not in allowed_types:
            raise TypeError("Expected a numeric type")

        if len(state) != 2:
            raise TypeError("Expected list of length 2")

        self.alpha = alpha
        self.radius = radius
        self.state = list(state)

    def get_derivative(self, state, t):
        theta_dash = state[1]
        theta_ddash = - self.alpha * state[1] - (constants.g * state[0]) / self.radius
        return [omega, alpha]

    def update_state(self, time_step):
        self.state = integrate.odeint(self.get_derivative,
                                      self.state,
                                      [0, time_step])[1]
        return self.state

    def get_trajectory(self, simulation_time=10.0, simulation_steps=500,
                       initial_state=None):

        if initial_state is not None:
            self.state = initial_state

        y = [numpy.asarray(self.state)]
        # y = [self.state[0]]
        for i in range(simulation_steps):
            print("Iteration: " + str(i + 1))
            self.update_state(simulation_time / simulation_steps)
            y.append(self.state)
        return y

