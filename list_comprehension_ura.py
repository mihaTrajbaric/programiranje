k = [9, 16, 81, 25, 196]

# print([x ** 2 for x in k])
imena = ["Ana", "Berta", "Cilka", "Dani", "Ema"]
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

# print(vsota / len(podatki))

# print(sum([teza for teza, _, _ in podatki]) / len(podatki))
kvadrati = [x ** 2 for x in range(10)]
# print([k for k in kvadrati if k < 50])

# print([x / 2 if x % 2 else x for x in kvadrati if x < 50])

def delitelji(n):
    return [x for x in range(1,n + 1) if not n % x ]


def prastevilo(n):
    return delitelji(n) == [1, n]

def vsa_prastevila(n):
    return [i for i in range(1,n) if prastevilo(i) ]

def zlozi(m):
    return [i for i in vsa_prastevila(m)]

# print(100 < x <= 200)

# print(zlozi(100000))

# print({i ** 2 for i in range(10)})

# print({i: i ** 2 for i in range(100)})

k = [9, 16, 81, 25, 196]
# print({i: k[i] for i in range(len(k))})
# print({i: x for i, x in enumerate(k)})

b1 = "MELODIJA"
# b1 = "DELODAJALEC"
b2 = "DELODAJALEC"

# print(sum([el1 != el2 for el1, el2 in zip(b1, b2)]) + abs(len(b1) - len(b2)))

# print(all([el1 == el2 for el1, el2 in zip(b1, b2)]))

from itertools import chain



print([c for ind,c in enumerate(chain("Ana", "Berta", "Cilka")) if ind % 2])
