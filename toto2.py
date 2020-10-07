#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from totomodul import ustawienia, losujliczby, pobierztypy, wyniki

def main(args):

    ileLiczb, maksLiczba, ileLosowan = ustawienia()

    liczby = losujliczby(ileLiczb, maksLiczba)

    for i in range(ileLosowan):
        typy = pobierztypy(ileLiczb, maksLiczba)
        ileTraf = wyniki(set(liczby), typy)

    print("Wylosowane liczby:", liczby)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

# | - suma zbirow
# - - różnica od A dla B
# & - część wspólna zbiorów