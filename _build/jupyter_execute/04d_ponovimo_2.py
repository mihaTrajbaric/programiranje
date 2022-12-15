#!/usr/bin/env python
# coding: utf-8

# # Ponovitev - seznami, funkcije, moduli
# 
# Namen tega poglavja je, da ponovimo delovanje naprednejših konstruktov, ki nam bodo pomagali pri reševanju daljših nalog

# 

# ## Seznami
# 
# Seznam je način, kako v eno spremenljivko shranimo več podatkov:
# ```python
# # definicija seznama
# moj_sez = [1, 2, 3, 4, 5, 6, 7]
# seznam_seznamov = [
#     ["Miha", 25],
#     ["Marko", 40],
#     ["Gašper", 30]
# ]
# prazen = []
# ```
# elemente seznama ali terke lahko razpakiramo (stevilo spremenljivk in elementov se mora ujemati!)
# ```python
# # razpakiravanje v elemente
# ime, teza = ["Lojze", 80]
# 
# # menjava spremenljivk
# i = 6
# j = 7
# i, j = j, i
# ```
# ## Zanka for po seznamu
# ```python
# sez = [1,4,7,3,4,7,4]
# 
# # zanka po seznamu
# for el in sez:
#     # naredi nekaj na trenutnem elementu, recimo
#     print(el)
# 
# # tudi po stringu
# moj_string = "Mihael"
# for crka in moj_string:
#     # naredi nekaj
#     pass
# 
# # zanko lahko prekinemo z `break`
# for el in sez:
#     if el == 4:
#         print("nasel 4")
#         break
# 
# 
# # else po zanki (se izvede samo, ce zanka pride do konca brez breaka)
# for el in sez:
#     if el == 8:
#         print("nasel 8")
#         break
# else:
#     print("v seznamu ni stevilke 8")
# 
# # zanka po vec seznamih
# imena = ["Miha", "Marko", "Gašper"]
# starosti = [67, 34, 76]
# 
# for ime, starost in zip(imena, starosti):
#     # naredi nekaj
#     print(ime, starost)
# 
# ```
# 

# ## Range
# 
# Range nam vrne zaporedje elementov od `0` do `n-1` (funkcijo list dodamo zgolj, da jo prisilimo, da bo kaj prikazala na zaslon. V zankah tega ne delamo):
# ```python
# print(list(range(5)))
# [0, 1, 2, 3, 4]
# ```
# 
# Določimo lahko do tri parametre: `začetek`, `konec` in `korak`:
# ```python
# # korak 2: vsak 2. element
# my_range = range(1, 10, 2)
# print(list(my_range))
# [1, 3, 5, 7, 9]
# ```
# 
# Če je korak negativen, lahko štejemo nazaj (pri tem mora biti začetek zgornja meja in konec spodnja):
# ```python
# my_range = range(5, 0, -1)
# print(list(my_range))
# [4, 3, 2, 1]
# ```
# 
# S pomočjo `range` in zanke `for` lahko štejemo:
# ```python
# for i in range(5):
#     print(i)
# ```
# 
# > Veliko ljudi takole uporablja zanko za cez sezname. To ni lepo, v pythonu se to ne dela:
# ```python
# # tole ni lepo
# sez = [3,5,3,3,2,6,3]
# for i in range(len(sez)):
#     print(sez[i])
# ```
# 

# ## Seznami - napredno
# **Dolžina seznama**
# ```python
# sez = [2,3,4,5]
# print(len(sez))
# ```
# 
# dodajanje elementa seznamu (na konec)
# ```python
# sez = [3,5,2,4]
# sez.append(7)
# ```
# ### Dostop - Indeksiranje elementov
# 
# Kako dostopamo do podatkov? Lahko z indeksi (prvi element ima indeks `0`, zadnji pa `n-1`):
# ```python
# >>> moj_sez[0]
# 1
# ```
# Indeksiramo lahko tudi od zadaj:
# ```python
# # zadnji element
# >>> moj_sez[-1]
# 7
# 
# # predzadnji element
# >>> moj_sez[-2]
# 6
# ```
# 
# Lahko pa tudi zajemamo celotne podsezname. Pazi: element spodnje meje je vključen, zgorenje pa ne.
# ```python
# >>> moj_sez[2:5]
# [3,4]
# ```
# 
# kako dostopamo do elementov v gnezdenem seznamu?
# 
# indeks_vrstice, indeks_stolpca
# 
# ```python
# seznam_seznamov = [
#     ["Miha", 25],
#     ["Marko", 40],
#     ["Gašper", 30]
# ]
# >>> seznam_seznamov[2][0]
# "Gašper"
# ```
# 
# ### Rezine
# 
# ```python
# >>> sez = [3,5,3,5,6,2]
# # prvi, zadnji (ni vkljucen)
# >>> sez[1:5]
# [5,3,5,6]
# 
# # vsak drug element
# >>> sez[1:6:2]
# [5,5,2]
# 
# # od drugega elementa naprej
# >>> sez[1:]
# [5,3,5,6,2]
# 
# # do vkljucno 4. elementa
# >>> sez[:4]
# [3,5,3,5]
# 
# # obrni seznam
# >>> sez[::-1]
# [2,6,5,3,5,3]
# ```
# 
# ### spreminjanje elementov
# 
# ```python
# sez = [2,7,6,5,3,7]
# 
# # en element
# >>> sez[2] = 99
# >>> sez
# [2,7,99,5,3,7]
# 
# # celo rezino
# >>> sez[2:5] = [-1, -1, -1]
# >>> sez
# [2,7,-1,-1,-1,7]
# 
# # lahko tudi odstranimo celo rezino
# >>> sez[2:5] = []
# >>> sez
# [2,7,7]
# ```
# 
# ### Operacije na seznamih
# ```python
# # sestevanje seznamov
# >>> [1,2,3] + [4,5,6]
# [1,2,3,4,5,6]
# 
# # mnozenje seznamov
# >>> [1,2,3] * 2
# [1,2,3,1,2,3]
# 
# # element v seznamu?
# >>> 5 in [1,2,3]
# False
# >>> 5 not in [1,2,3]
# True
# 
# # dodajanje elementa v seznam
# sez = [1,2,3]
# >>> sez.append(4)
# >>> sez
# [1,2,3,4]
# ```

# ## Funkcije
# 
# Funkcija je nacin, kako zapakiramo blok kode, neko funkcionalnost, ki jo nato uporabimo kasneje. Tudi veckrat
# 
# ```python
# # primer funkcije
# def sestevanje(st_1, st_2):
#     vsota = st_1 + st_2
#     return vsota
# 
# ```
# 
# Funkcija ima 4 elemente
# - ime funkcije (kar kasneje poklicemo)
# - argumente (vhodni podatki, ki jih uporabimo pri racunanju)
# - blok kode ("racunanje")
# - vracanje rezultata
# 
# ```python
# def ime_funkcije(arg1, arg2,...):
#     # do something
#     ...
# 
#     return rezultat 
# ```
# 
# ### Vračanje rezultata
# 
# Return vrne rezultat
# ```python
# def dvakratnik(st):
#     return 2 * st
# ```
# Funkcija ima lahko tudi več `return` stavkov. **Izvede se samo prvi, do katerega pride izvajanje**. Return je konec funkcije.
# 
# ```Python
# def je_sodo(st):
#     if st % 2 == 0:
#         return True
#     return False
# ```
# 
# Brez return stavka, funkcija ne vraca nicesar (oz. vraca `None`)
# 
# ```python
# def pozdrav(ime):
#     print("Zivijo,",ime)
#     # ni return stavka
# ```
# 
# ### Klic funkcije
# 
# Funkcijo poklicemo takole:
# 
# ```python
# ime_funkcije(args)
# ```
# 
# Primer:
# 
# ```python
# # tole je preprosta definicija
# def vsota(a, b):
#     return a + b
# 
# # klic funkcije
# >>> vsota(4,5)
# 9
# 
# # klic je izraz. Vrednost funkcije lahko uporabimo v izrazu, shranimo, tiskamo...
# a = vsota(3,4)
# >>> a
# 7
# 
# rac = 5 + 7 - vsota(4,5)
# >>> rac
# 3
# 
# >>> print(vsota(3,4))
# 7
# ```
# 
# Uporaba funkcij v drugih funkcijah
# 
# ```python
# # prva funkcija
# def je_sodo(st):
#     return st % 2 == 0
# 
# # funckija, ki vrne sode elemente seznama
# def sodi(sez):
#     sodi_el = []
#     for el in sez:
#         if je_sodo(el):
#             sodi_el.append(el)
#     return sodi_el
# 
# # klic funkcije na neken seznamu
# 
# >>> moj_seznam = [3,4,5,2,56,7,8,3,2]
# samo_sodi = sodi(moj_sez)
# >>> samo_sodi
# [4,2,56,8,2]
# ```

# ## Moduli
# 
# Moduli so način, kako v naše datoteke uvažamo funkcionalnost od drugod.
# 
# ### Načini uvažanja
# 
# 1. `import <module>`
# ```python
# import math
# print(math.sin(math.pi))
# ```
# 
# 2. `from <module> import <function>`
# ```python
# from math import sin, pi
# print(sin(pi))
# ```
# 
# 3. `from <module> import *`
# ```python
# print(sin(pi))
# ```
# 
# Uporabljajte nacina 1 in 2, 3 vodi v nered...
# 
# 
# ### Pisanje lastnega modula
# `
# Recimo da bi radi napisali funkcijo ploscina_kroga(r), in jo spravili v modul geometrija. Preprosto naredimo datoteko `geometrija.py`, kamor shranimo funkcijo, nato pa pisemo svoj program v datoteki, ki se nahaja v isti mapi. Primer
# 
# ```bash
# project_dir
# |
# geometrija.py
# nas_program.py
# ```
# 

# 
# ## Kako naj izgleda python datoteka?
# 
# - na vrhu uvoz modulov
# - nato funkcije, konstante
# - na dnu `if __name__ == "__main__"` in koda programa
# 
# Primer:
# 

# ```python
# import math
# 
# PI_FIZIKI = 3
# 
# 
# def ploscina_kroga(r):
#     """
#     vrne ploscino kroga s polmerom r
#     """
# 
#     return math.pi * r ** 2
# 
# def ploscina_kvadrata(a):
#     """
#     ploscina kvadrata s strnico a
#     """
#     return a * a
# 
# def ploscina_kroga_fizikalno(r):
#     """
#     vrne ploscino kroga, kjer uporabi fizikalni priblizek konstante PI
#     """
# 
#     return PI_FIZIKI * r ** 2
# 
# 
# if __name__ == "__main__":
# 
#     stranica = 4
# 
#     print(ploscina_kroga(stranica))
#     print(ploscina_kroga_fizikalno(stranica))
#     print(ploscina_kvadrata(stranica))
# ```
