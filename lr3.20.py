# Дано дійсне число ε (> 0). Послідовність дійсних чисел AK визначається наступним чином:A1 = 1,
# A2 = 2, AK = (AK-2 + 2 • AK-1) / 3, K = 3, 4, ....Знайти перший з номерів K, для яких виконується умова |
# AK - AK-1 | <Ε, і вивести цей номер, а також числа AK-1 і AK.
from math import*
e = int(input("enter the number = "))
if e <= 1:
    exit(0)
    print("Число повинно бути більшим за 1")


def find(e):
    mass = [0]*100
    mass[1] = 1
    mass[2] = 2
    for i in range(1, 99, 1):
        mass[i] = mass[i - 2] + 2 * mass[i-1]
        if abs(mass[i] - mass[i - 1]) < e:
            print(i, mass[i], mass[i-1])
            exit(0)


find(e)
