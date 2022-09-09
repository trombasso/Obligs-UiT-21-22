from random import uniform
import time


def estimate_PI(hits, print_info):
    totalhits = 0
    for i in range(0, hits):
        x = uniform(-1.00, 1.00)
        y = uniform(-1.00, 1.00)

        if x**2 + y**2 - 1**2 < 0:
            totalhits += 1
            if print_info == "y":
                print(f"{'Inside:':<10} X= {x:<25} Y= {y:<25}")
            else:
                pass
        elif (x**2 + y**2 - 1**2 > 0) and print_info == "y":
            print(f"{'Outside:':<10} X= {x:<25} Y= {y:<25}")
    print("-" * 68)
    print(f"PI estimates to {(4 * totalhits) / hits } based on {totalhits} points of calculation.")
    print("--------------------------------------------------------------------")


def main():
    print("--------------------------------------------------------------------")
    print("\nCalculate PI by dividing number of random hits within a circle by number of reference points.\n")
    print("--------------------------------------------------------------------")
    user_input = int(input("How many reference points? "))
    to_screen = input("Print points to screen?\n(Warning, takes at lot longer with high numbers!) (Y / N) ").lower()

    start_time = time.time()
    estimate_PI(user_input, to_screen)
    print(f"\n(Time to calculate: {(time.time() - start_time):.4f} seconds)")


if __name__ == "__main__":
    main()
