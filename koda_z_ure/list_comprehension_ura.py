# koda iz ure o izpeljanih seznamih

# zaradi preglednosti, so vsi printi zakomentirani. Po potrebi odkomentiraj.
# celotno vrstico v pycharm (od)komentiras s ctrl + / (poševnica nad numpadom na slovenski tipkovnici)

k = [9, 16, 81, 25, 196]

# seznam kvadratov
# print([x ** 2 for x in k])


imena = ["Ana", "Berta", "Cilka", "Dani", "Ema"]

# povprecna dolzina imena
# print(sum([len(x) for x in imena]) / len(imena))

podatki = [
    (74, "Anže", False),
    (82, "Benjamin", False),
    (58, "Cilka", True),
    (66, "Dani", False),
    (61, "Eva", True),
    (84, "Franc", False)]



vsota = 0
for teza, ime, je_zenska in podatki:
    vsota += teza

# povrpecna teza, ki jo odpakiramo iz podatkov
# print(vsota / len(podatki))

# povprecna teza z izpeljanim seznamom
# print(sum([teza for teza, _, _ in podatki]) / len(podatki))


kvadrati = [x ** 2 for x in range(10)]
# if stavek kot 'filter': samo kvadrati, ki so manjsi od 50
# print([k for k in kvadrati if k < 50])

# if-else v izrazu, s katerim sestavimo drugačen izraz za eno ali drugo skupino.
# if na koncu je filter
# print([x / 2 if x % 2 else x for x in kvadrati if x < 50])

def delitelji(n):
    return [x for x in range(1,n + 1) if not n % x ]


def prastevilo(n):
    return delitelji(n) == [1, n]

def vsa_prastevila(n):
    return [i for i in range(1,n) if prastevilo(i) ]

from itertools import groupby

# groupby naredi slovar k: [vrednosti] glede na key, ki mu ga dolocimo.
# v nasem primeru je key za vsak element x // 100 (954 postane 9, 324 postane 3 itd.)
# groupby tako zlozi skupaj vse elemente, ki imajo isti kljuc.
# Rezultat groupby je slovar, zato se sprehodimo cez, in obrdzimo samo vrednost (vrednost je seznam teh stevil).
# ker groupby vraca nek cuden obejtk, ga z list(g) prisilimo, da vrne navaden list
def zlozi(m):
    return [list(g) for k,g in groupby([i for i in vsa_prastevila(m)], key=lambda x: x // 100)]


# print(zlozi(1000))


# izpeljana mnozica, nic posebnega, samo vrstni red ne drzi
# print({i ** 2 for i in range(10)})

# izpeljani slovar, tukaj pa od Python 3.6 naprej velja vrstni red
# print({i: i ** 2 for i in range(100)})

k = [9, 16, 81, 25, 196]

# kaj ce hocemo indeks? Lahko naredimo 'po starem' z zanko cez range
# print({i: k[i] for i in range(len(k))})

# ali pa uporabimo 'enumerate', ki nam poda indeksiranje seznama
# print({i: x for i, x in enumerate(k)})

b1 = "MELODIJA"
# b1 = "DELODAJALEC"
b2 = "DELODAJALEC"

# na koliko mestih se besedi ujemata? ce sestevamo booleane, je True 1, False pa 0
# print(sum([el1 == el2 for el1, el2 in zip(b1, b2)]))

# ce nas zanima mesta neujemanja, je potrebno pristet se razliko v dolzinah. Zip gre samo do dolzine krajsega...
# print(sum([el1 != el2 for el1, el2 in zip(b1, b2)]) + abs(len(b1) - len(b2)))

# na voljo sta nam besedici 'all' (ali so vsi True) in 'any' (ali je vsaj en True)
# print(all([el1 == el2 for el1, el2 in zip(b1, b2)]))
# print(any([el1 == el2 for el1, el2 in zip(b1, b2)]))

from itertools import chain

# itertools ima kar nekaj uporabnih funkcij za delo s seznami, izpeljanimi seznami itd.
# chain nam skupaj 'zlepi' vse tri besede, da se sprehodimo po njih zaporedno
# v tem primeru obdrzimo samo vsak drug element, kar naredimo s pomocjo indeksov

# print([c for ind,c in enumerate(chain("Ana", "Berta", "Cilka")) if ind % 2])
