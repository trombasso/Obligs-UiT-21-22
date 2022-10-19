class Kalman:
    # Verdiene i init er de verdiene som kom best ut under testing.
    def __init__(self, dt: int = 1, x_0: float = 0, v_0: float = 0.007, a_0: float = 0.01, alpha: float = 2e-2, beta: float = 8.15e-5, gamma: float = 2.8e-7):

        self.x_prev = x_0  # Initverdi for posisjon
        self.v_prev = v_0  # Initverdi for hastighet
        self.a_prev = a_0  # Initverdi for akselerasjon
        self.alpha = alpha  # Filterparameter for posisjon
        self.beta = beta  # Filterparameter for hastighet
        self.gamma = gamma  # Filterparameter for akselerasjon
        self.dt = dt  # Tidssteg

    def estimate_current_position_and_velocity(self, zi):

        # State Update Equation, calculate current estimate
        self.x_curr = self.x_prev + self.alpha * (zi - self.x_prev)
        self.v_curr = self.v_prev + self.beta * (zi - self.x_prev)
        # self.v_curr = self.v_prev + self.beta * ((zi - self.x_prev) / self.dt)
        self.a_curr = self.a_prev + self.gamma * ((zi - self.x_prev) * 2)
        # self.a_curr = self.a_prev + self.gamma * ((zi - self.x_prev) / (0.5 * self.dt**2))

        # State Extrapolation Equation, calculate next estimate
        self.x_prev = self.x_curr + self.v_curr * self.dt + self.a_curr * ((self.dt**2) * 0.5)
        self.v_prev = self.v_curr + self.a_curr * self.dt
        self.a_prev = self.a_curr

        return self.x_curr, self.v_curr
