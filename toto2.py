#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileLiczb = int(input("Podaj ilosc typowanych liczb: "))
maksLiczba = int(input("Podaj maksymalna losowana liczbe: "))



wyniki = []
i = 0

while i < ileLiczb:
    liczba = random.randint(1, maksLiczba)
    if wyniki.count(liczba) == 0:
        wyniki.append(liczba)
        i = i + 1


print(f"Wytypuj {ileLiczb} z {maksLiczba} liczb: ")
j = 0
for j in range(3):
    typy = set()
    i=0
    while i < ileLiczb:
        typ = int(input(f"Podaj liczbe {i + 1}: "))
        if typ not in typy:
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