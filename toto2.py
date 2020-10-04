#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

ileLiczb = int(input("Podaj ilosc typowanych liczb: "))
maksLiczba = int(input("Podaj maksymalna losowana liczbe: "))

print(f"Wytypuj {ileLiczb} z {maksLiczba}, liczb: ")

wyniki = []
i = 0

while i < ileLiczb:
    liczba = random.randint(1, maksLiczba)
    if wyniki.count(liczba) == 0:
        wyniki.append(liczba)
        i = i + 1


print(f"Wyniki {wyniki}")