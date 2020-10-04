#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


liczba = random.randint(1, 10)
# print(f"Wylosowana liczba: {liczba}")

for i in range(3):
    print(f"Proba: {i + 1}")
    odp = input("Jaka liczbe od 1 do 10 mam na mysli? ")
#   print(f"Podales liczbe {odp}")


    if liczba == int(odp):
        print("Zgadles!")
        break
    else:
        print("Sprobuj ponownie")
        print()
