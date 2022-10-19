import pygame as pg
from datetime import datetime, timedelta
import random
import numpy as np
from rich import print
import os

"""
OBS!
Denne filen er en omskriving av HitTheTarget.py. Den skal fungere på samme måte, bare uten
grafikken og de problemer det fører til med kjøring på Mac. Det vil også være lettere
å kjøre et høyere antall iterasjoner, da det kun er kalkulering som kjøres.

def main_2() vil kjøre én test med de parameter som settes.
def main() vil kjøre en lengre test med et utvalg av alpha-beta-gamma verdier.

"""

try:
    print("\nSearching for class Kalman in file Kalman.py...")
    from Kalman import Kalman

    print("Found it!")

    kalman_implemented = True

except ModuleNotFoundError:
    kalman_implemented = False
    print("No implementation of class Kalman found, running simulation without it.")


class Target:
    def __init__(self, y_t):
        self.y_t = y_t
        self.vx_t = 0.4 + 0.6 * random.random()
        self.ax_t = 0.003 * random.random()

        target_left = 200 * random.random()  # Randomized starting position
        target_top = 50
        self.rect = pg.Rect(target_left, target_top, 16, 16)

        # Initialize position, speed and acceleration
        self.x_t = self.rect.centerx
        self.y_t = self.rect.centery

    def move(self):
        self.vx_t += self.ax_t
        self.x_t += self.vx_t
        self.rect.centerx = int(self.x_t)

    def noisy_x_pos(self, noise_scale=150):
        return self.rect.x + np.random.normal(0, noise_scale)


class Player:
    def __init__(self, y_t, kalman=None):
        self.rect = pg.Rect(800, 700, 16, 16)
        self.x_p = self.rect.centerx
        self.y_p = self.rect.centery
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

        self.rect.centerx = int(self.x_p)
        self.rect.centery = int(self.y_p)


test_no = 1


def hit_the_target(kal_alpha: float, kal_beta: float, kal_gamma: float, x_0: float, v_0: float, a_0: float, iterations: int):
    global test_no

    kalman_score = 0
    reg_score = 0
    iters = 0
    y_t = 66

    start = datetime.now()

    print(f"{test_no} | Running iterations", end="")
    test_no += 1
    breakflag = False

    while iters < iterations:

        target = Target(y_t)
        missile = Player(y_t)
        if kalman_implemented:
            k_miss = Player(y_t, kalman=Kalman(alpha=kal_alpha, beta=kal_beta, gamma=kal_gamma, x_0=x_0, v_0=v_0, a_0=a_0))
        trial = True
        iters += 1
        coll = 0
        k_coll = 0

        if iters % (iterations / 100) == 0:
            print(".", end="")

        while trial:

            # Get latest (noisy) target position
            last_x_pos = target.noisy_x_pos()

            # Move target and missile(s)
            target.move()
            missile.move(last_x_pos)
            if kalman_implemented:
                k_miss.move(last_x_pos)

            coll = missile.rect.colliderect(target.rect)
            if coll:
                reg_score += 1

            if kalman_implemented:
                k_coll = k_miss.rect.colliderect(target.rect)  # kommenter inn denne linjen naar Kalman er implementert#
                if k_coll:
                    kalman_score += 1

            # End trial if missile(s) hit, or missile is sufficiently high up
            oob = missile.rect.y < 20
            if oob or coll or (kalman_implemented and k_coll):
                trial = False

        # End trial if score(%) <= 80 after 50% of iterations.
        if iters == iterations / 2:
            if (kalman_score / iters) * 100 <= 80:
                breakflag = True
                break

    endtime = datetime.now()

    # Print hit rates
    print("\n\nHit rate after " + str(iters) + " iterations:")
    print("Without filter: " + str(round((reg_score / iters) * 100, 1)) + " %")
    if kalman_implemented:
        print("With filter:    " + str(round((kalman_score / iters) * 100, 1)) + " %")
        print(f"Initial values: Position {x_0} Velocity {v_0} Acceleration {a_0}")
        print(f"Kalman Gaines: Alpha {kal_alpha} Beta {kal_beta} Gamma {kal_gamma}")

    tid = endtime - start
    print(f"Time for trial: {str(timedelta(seconds=tid.seconds))} {'Aborted!' if breakflag else ''}")
    print("-" * 100)

    return round((kalman_score / iters) * 100, 1), breakflag


def test_different_kalman_gains():
    """
    OBS, denne kan ta lang tid å kjøre. 40000 iterasjoner gir test-tid på ca 20 timer.
    Vil lage en fil, output.txt, med resultatet av testing. Filen skrives kun på slutten av kjøring.
    Så om programmet kræsjer midtveis, eller strømmen går så er resultatet så langt tapt...
    """

    NUM_OF_ITERATIONS = 40000

    A = 2e-2  # Har valgt å ikke kjøre alphaverdier, men beholde denne som konstant.

    b = 7e-5  # Startverdi
    b_inc = 0.05e-5  # Inkrementeres med...
    b_end = 9e-5  # Sluttverdi

    G = g = 2.5e-7  # Startverdi
    g_inc = 0.1e-7  # Inkrementeres med
    g_end = 3.5e-7  # Sluttverdi

    x = 0  # Startpos
    v = 0  # Startfart
    a = 0  # Startacc.

    results = []

    while b <= b_end:
        while g <= g_end:
            prosentage, breakflag = hit_the_target(A, b, g, x, v, a, NUM_OF_ITERATIONS)
            results.append([prosentage, A, b, g, breakflag])
            g += g_inc
        g = G
        b += b_inc

    path = os.path.dirname(__file__)
    with open(os.path.join(path, "output.txt"), mode="w") as file:
        for elem in results:
            output = f"% {elem[0]} | a {elem[1]:.2e} b {elem[2]:.2e} g {elem[3]:.2e} {'Aborted' if elem[4] else ''}\n"
            file.write(output)


def main():
    hit_the_target(kal_alpha=2e-2, kal_beta=8.15e-5, kal_gamma=2.8e-7, x_0=0, v_0=0.007, a_0=0.01, iterations=40_000)
    # hit_the_target(kal_alpha=0.1, kal_beta=0.0001, kal_gamma=0.0000001, x_0=0, v_0=0, a_0=0, iterations=1_000)
    # hit_the_target(kal_alpha=0.02, kal_beta=0.0005, kal_gamma=0.0000005, x_0=0, v_0=0, a_0=0, iterations=1_000)
    # hit_the_target(kal_alpha=0.02, kal_beta=0.00007, kal_gamma=0.0000002, x_0=0, v_0=0, a_0=0, iterations=1_000)


if __name__ == "__main__":
    # test_different_kalman_gains()  # Kjør denne om du har god tid ;)
    main()
