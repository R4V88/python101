#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileLiczb = int(input("Podaj ilosc typowanych liczb: "))
maksLiczba = int(input("Podaj maksymalna losowana liczbe: "))

print(f"Wytypuj {ileLiczb} z {maksLiczba}, liczb: ")

wyniki = []

for ileLiczb in range(ileLiczb):
    liczba = random.randint(1, maksLiczba)
    print(liczba)
    wyniki.append(liczba)


print(wyniki)