import math

try:
    print("Searching for class Kalman in file Kalman.py...")
    from Kalman import Kalman

    kalman_implemented = True
except ModuleNotFoundError:
    kalman_implemented = False
    print("No implementation of class Kalman found, running simulation without it.")

import random

import numpy as np


class Target:
    def __init__(self, y_t):
        self.x_t = random.randint(8, 208)
        self.y_t = y_t
        self.vx_t = 0.4 + 0.6 * random.randint(0, 1)
        self.ax_t = 0.003 * random.randint(0, 1)

    def move(self):
        self.vx_t += self.ax_t
        self.x_t += self.vx_t

    def noisy_x_pos(self, noise_scale=150):
        return self.x_t + np.random.normal(0, noise_scale)


class Player:
    def __init__(self, y_t, kalman=None):
        self.x_p = 808
        self.y_p = 708
        self.vx_p = 0
        self.vy_p = -1.0
        self.ax_p = 0.02
        self.vx_p_desired = 0
        self.kalm = kalman

        self.x_t = self.x_p
        self.vx_t = 0
        self.y_t = y_t
        self.t_impact = (self.y_t - self.y_p) / self.vy_p

    def move(self, x_target_meas):
        if self.kalm:
            self.x_t, self.vx_t = self.kalm.estimate_current_position_and_velocity(x_target_meas)
        else:
            self.vx_t = x_target_meas - self.x_t
            self.x_t = x_target_meas

        self.t_impact = (self.y_t - self.y_p) / self.vy_p

        if self.t_impact:
            self.vx_p_desired = (self.x_t - self.x_p) / self.t_impact + self.vx_t

        if self.vx_p < self.vx_p_desired:
            self.vx_p += self.ax_p
        else:
            self.vx_p -= self.ax_p

        self.x_p += self.vx_p
        self.y_p += self.vy_p


def main():

    kalman_score = 0
    reg_score = 0
    iters = 0
    y_t = 74

    while True:
        target = Target(y_t)
        missile = Player(y_t)
        if kalman_implemented:
            k_miss = Player(y_t, kalman=Kalman())
        trial = True
        iters += 1
        coll = 0
        k_coll = 0

        while trial:

            # Get latest (noisy) target position
            last_x_pos = target.noisy_x_pos()

            # Move target and missile(s)
            target.move()
            missile.move(last_x_pos)
            if kalman_implemented:
                k_miss.move(last_x_pos)

            if math.dist((missile.x_p, missile.y_p), (target.x_t, target.y_t)) < 16:
                coll = 1
                reg_score += 1

            if kalman_implemented:
                if math.dist((k_miss.x_p, k_miss.y_p), (target.x_t, target.y_t)) < 16:
                    k_coll = 1
                    kalman_score += 1

            # End trial if missile(s) hit, or missile is sufficiently high up
            oob = missile.y_p < 20
            if oob or coll or (kalman_implemented and k_coll):
                trial = False

        # Print hit rates
        print("Hit rate after " + str(iters) + " iterations:")
        print("Without filter: " + str(round((reg_score / iters) * 100, 1)) + " %")
        if kalman_implemented:
            print("With filter:    " + str(round((kalman_score / iters) * 100, 1)) + " %")


if __name__ == "__main__":
    main()
