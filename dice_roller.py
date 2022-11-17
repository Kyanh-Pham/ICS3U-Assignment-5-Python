#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Oct 2022
# This program rolls a dice until you get doubles

import random


def main():

    loop_counter = 0
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)

    # Process and Output
    while dice_1 != dice_2:
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        loop_counter = loop_counter + 1
        if dice_1 == dice_2:
            break
        print(
            "Roll #{0}...Dice 1 rolled a {1} and dice 2 rolled a {2}!".format(
                loop_counter, dice_1, dice_2
            )
        )
    print(
        "Roll #{0}... hit doubles! Dice 1 and 2 are {1}!".format(loop_counter, dice_1)
    )

    print("\nDone.")


if __name__ == "__main__":
    main()
