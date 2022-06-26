# 掷骰子
import matplotlib.pyplot as plt
from random import randrange


def roll_dice(face):
    return randrange(face)

times = 10
face = 6


for i in range(10):
    r1 = roll_dice(face)
    r2 = roll_dice(face)
    plt.scatter(r1, r2, c='r', marker=".")
plt.show()