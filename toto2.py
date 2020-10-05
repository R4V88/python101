#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

try:
    ileLiczb = int(input("Podaj ilosc typowanych liczb: "))
    maksLiczba = int(input("Podaj maksymalna losowana liczbe: "))

    if ileLiczb > maksLiczba:
        print("Niepoprawne dane!")
        exit()
except ValueError:
    print("Błędne dane!")
    exit()


wyniki = []
i = 0

while i < ileLiczb:
    liczba = random.randint(1, maksLiczba)
    if wyniki.count(liczba) == 0:
        wyniki.append(liczba)
        i = i + 1


for j in range(3):
    print(f"Wytypuj {ileLiczb} z {maksLiczba} liczb: ")
    typy = set()
    i=0
    while i < ileLiczb:
        try:
            typ = int(input(f"Podaj liczbe {i + 1}: "))
        except ValueError:
            print("Błędne dane")
            continue

        if 0 < typ <= maksLiczba and typ not in typy:
            typy.add(typ)
            i = i + 1

    trafione = set(wyniki) & typy
    if trafione:
        print(f"\nIlość trafień: {len(trafione)}")
        print(f"\nTrafione liczby: {trafione}")
    else:
        print("Brak trafien. \nTry again!")

    print("\n" + "x" * 40 + "\n")


print(f"\n****** Wyniki {wyniki}, tak dla pewności ******\n")

# | - suma zbirow
# - - różnica od A dla B
# & - część wspólna zbiorów