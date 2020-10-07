#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


def ustawienia():
    """Funkcja pobiera ilość losowanych liczb, maksymalną losowaną wartość
    oraz ilość prób. Pozwala określić stopień trudności gry."""
    while True:
        try:
            ileLiczb = int(input("Podaj ilosc typowanych liczb: "))
            maksLiczba = int(input("Podaj maksymalna losowana liczbe: "))

            if ileLiczb > maksLiczba:
                print("Niepoprawne dane!")
                continue
            ileLosowan = int(input("Ile losowań: "))
            return (ileLiczb, maksLiczba, ileLosowan)
        except ValueError:
            print("Błędne dane!")
            continue


def losujliczby(ileLiczb, maksLiczba):
    """Funkcja losuje ile unikalnych liczb całkowitych od 1 do maks"""
    wyniki = []
    i = 0

    while i < ileLiczb:
        liczba = random.randint(1, maksLiczba)
        if wyniki.count(liczba) == 0:
            wyniki.append(liczba)
            i = i + 1
    return wyniki


def pobierztypy(ileLiczb, maksLiczba):
    """Funkcja pobiera od użytkownika jego typy wylosowanych liczb"""
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
    return typy


def wyniki(liczby, typy):
    """Funkcja porównuje wylosowane i wytypowane liczby,
    zwraca ilość trafień"""
    trafione = set(liczby) & typy
    if trafione:
        print("\nIlość trafień: %s" % len(trafione))
        trafione = ", ".join(map(str, trafione))
        print("Trafione liczby: %s" % trafione)
    else:
        print("Brak trafień. Spróbuj jeszcze raz!")

    print("\n" + "x" * 40 + "\n")  # wydrukuj 40 znaków x
    return len(trafione)
