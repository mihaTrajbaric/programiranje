#!/usr/bin/env python
# coding: utf-8

# # Ponovitev - osnove
# V času krožka smo vzeli že kar nekaj konstruktov in se naučili pisanja preprostih programov. Ker sem med reševanjem nalog opazil ponavljanje enakih osnovnih napak, je nastopil čas, da še enkrat ponovimo, kar smo se naučili do sedaj. Počitnice pretekli teden pa so še dodaten razlog, da še enkrat pogledamo, kaj vse imamo zaenkrat na voljo v našem programerskem arzenalu.

# ## Osnovne operacije
# Python lahko uporabljamo kot navaden kalkulator.
# ```
# >>> (1 + 2 - 2) * 6 / 3
# 2.0
# ```
# **Navadno deljenje**
# ```
# >>> 5 / 3
# 1.6666666666666667
# ```
# **Celoštevilsko deljenje**
# ```
# >>> 5 // 3
# 1
# ```
# **Ostanek pri deljenju**
# ```
# >>> 5 % 3
# 2
# ```
# **Potenciranje**
# ```
# >>> 5 ** 2
# 25
# ```
# **Korenjenje** (potenciranje na 0.5)
# ```
# >>> 4 ** 0.5
# 2.0
# ```
# 
# 

# ## Podatkovni tipi
# Ko števila zapisujemo v računalniku, je važno, kakšnega tipa je podatek. Do sedaj smo spoznali **4 podatkovne tipe**. \
# **int** -> cela števila
# ```Python
# >>> 2 + 3
# 5
# >>> type(2)
# int
# ```
# **float** -> realna števila
# ```Python
# >>> 4 / 3
# 1.3333333333333333
# >>> type(0.5)
# float
# ```
# **string** -> besedilo (nizi) -> enojni ali dvojni narekovaji
# ```Python
# >>> "Danes je lepo vreme"
# 'Danes je lepo vreme'
# >>> type("Danes")
# str
# ```
# **bool** -> logične vrednosti 
# ```Python
# >>> True and False
# True
# >>> type(True)
# bool
# ```
# 

# ## Nekaj uporabnih funkcij
# 
# `int(arg)`, `float(arg)`, `str(arg)`, `bool(arg)` -> pretvarjanje med podatkovnimi tipi
# 
# ```Python
# >>> int(2.0)
# 2
# >>> float("2.34")
# 2.34
# >>> str(3232)
# '3232'
# ```
# 
# `round(stevilo, decimalk)` -> zaokroži število na podano število decimalk
# ```Python
# >>> round(2.3456, 2)
# 2.35
# >>> round(2.34343)
# 2
# ```
# 
# `abs(st)` -> absolutna vrednost
# ```Python
# >>> abs(-2)
# 2
# ```
# 

# ## Operacije na nizih
# `+` -> Lepljenje nizov
# ```Python
# >>> "Danes " + "je" + " lepo vreme"
# 'Danes je lepo vreme'
# ```
# `*` -> ponavljanje niza
# ```Python
# >>> "ha" * 3
# 'hahaha'
# ```

# ## Spremenljivke
# Spremenljivko deklariramo / ji dodelimo vrednost, nato pa jo lahko pokličemo, ko želimo uporabiti vrednost.
# ```Python
# # deklaracija
# >>> stevilo = 4
# 
# # klic
# >>> stevilo
# 4
# ```
# Spremenljivko lahko nato uporabimo v računanju
# ```
# >>> 5 + stevilo
# 9
# ```
# Vrednost lahko spreminjamo
# ```
# >>> stevilo
# 4
# >>> stevilo = 7
# >>> stevilo
# 7
# >>> stevilo = stevilo + 5
# >>> stevilo
# 12
# ```

# ## Print
# Vrednosti na zaslon prikažemo z ukazom `print()`

# In[23]:


print("hello, world!")


# Izraz znotraj printa se bo najprej poračunal, nato pa prikazal na zaslonu.

# In[24]:


print(4 + 5 / 3)


# Izpise lahko oblikujemo na dva načina. Prvi način je, da posamezne dele ločimo z vejico. Na ta način lahko tiskamo **različne podatkovne tipe**, vendar bo python vmes avtomatsko **dodal presledek**.

# In[26]:


print("Danes", "je", 5, "stopinj.")


# Če želimo več nadzora nad izpisom, uporabimo **lepljenje nizov**. Vsi elementi izpisa morajo biti tipa `str`, zato jih **ustrezno pretvorimo**.

# In[29]:


print("Danes " + "je " + str(5) + "°C.")


# ## Input
# Podatke od uporabnika dobimo z ukazom `input(prompt)`. Znotraj oklepajev napišemo **iztočnico**, ki se bo uporabniku prikazala na zaslonu. Kar dobimo, moramo nujno nato **shraniti v spremenljivko**.

# In[31]:


ime = input("Vnesi svoje ime: ")


# In[32]:


print(ime)


# Funkcija `input()` bo vedno podatke pridobila kot podatkovni tip `str`. Če pričakujemo število, moramo podatke ustrezno pretvoriti (`int()`, `float()`), drugače ne bomo mogli računati z njim. Največkrat to naredimo kar v isti vrstici, kot input:

# In[36]:


letnica_rojstva = int(input("Vnesi svojo letnico rojstva: "))


# In[37]:


starost = 2022 - letnica_rojstva
print("Star sem " + str(starost) + " let.")


# 
# ## Primeri pogojev
# Pogoj je lahko katerikoli izraz, ki se evaluira v `bool` (logično vrednost).
# 

# In[63]:


# primerjanje < > <= >=
4 < 5


# In[62]:


# Pozor! Enakost preverjamo z dvojnim enačajem!
# enakost == in neenakost !=
4 == 4


# In[1]:


# pogoje lahko zduzujemo s poljubnimi logičnimi vezniki
# Logični vezniki: and, or, not
a = 5
a != 4 and True


# In[2]:


# Lahko preverjamo tudi več neenakosti hkrati
a = 5
3 < a < 6


# ## Pogojni stavek
# 
# S pogojnim stavkom lahko v program dodamo pogoje. Kodo, ki se izvede pod določenim pogojem, moramo zamakniti za 4 presledke ali tabulator (vendar znotraj programa teh dveh ne mešamo!)

# In[39]:


starost = 15
if 10 < starost < 20:
    print("Najstnik")


# Dodamo lahko tudi `else` del, ki se izvede, če pogoj ni izpolnjen:

# In[40]:


starost = 21
if 10 < starost < 20:
    print("Najstnik")
else:
    print("Očitno nisi najstnik")


# Preverjamo lahko tudi več različnih možnosti. Prvo začnemo z `if`, naslednje z `elif`, če pa noben pogoj ni izpolnjen, pa zaključimo z `else`:

# In[43]:


zival = "mačka"
if zival == 'pes':
    print("hov hov!")
elif zival == "mačka":
    print("mijav!")
elif zival == "konj":
    print("ihaha")
else:
    print("Ne poznam živali!")


# Pogoje lahko tudi gnezdimo

# In[44]:


starost = 17
if  starost < 20:
    if starost > 10:
        print("najstnik")
    else:
        print("otrok")
else:
    print("ne najstnik, ne otrok")


# ## Zanka while
# Z zanko lahko dosežemo, da se del kode nekajkrat **ponovi** ali pa se **ponavalja, dokler je pogoj izpolnjen**. Spodaj je nekaj primerov uporabe.
# 
# Dostikrat zanko uporabimo skupaj s **števcem**, ki ga poimenujemo `i`. Tega nato uporabimo v **pogoju**. Znotraj zanke ga tudi povečamo / zmanjšamo.
# 
# > števec lahko povečamo `i = i + 1` ali krajše `i += 1`. Okrajšava deluje za vse osnovne operacije (`i -= 1`, `i *= 1`, `i /= 1`, `i //= 1` `i %= 1 `)
# 

# 
# ### Petkrat ponovimo `print()`:

# In[45]:


i = 0
while i < 5:
    print("hej")
    i += 1


# ### Štetje od 1 do 10

# In[47]:


i = 1
while i <= 10:
    print(i)
    i += 1


# ### Seštevanje števil
# Recimo da nam uporabnik poda 5 števil, mi pa jih moramo sešteti. Kako bi naredili to? **Izven zanke** definiramo spremenljivko vsota. Zanko moramo izvesti *5x*, pri čemer v vsaki iteraciji od uporabnika dobimo nov *input*.  Trenutni input prištejemo vsoti. Na koncu natisnemo rezultat.

# In[51]:


vsota = 0
i = 0
while i < 5:
    st = int(input("Vnesi število: "))
    vsota += st
    i += 1
print("Vsota je", vsota)


# ### Računanje povprečja
# Kako bi izračunali povprečje? Povprečje je v resnici vsota, deljena s številom elementov, ki smo jih sešteli. Kot v prejšnjem primeru z zanko seštejemo elemente, nato pa vsoto delimo s številom elementov.

# In[52]:


st_elementov = 3
vsota = 0
i = 0
while i < st_elementov:
    vsota += int(input("Vnesi število: "))
    i += 1
povprecje = vsota / st_elementov
print("Povprečje:", povprecje)


# ### Izpis lihih števil
# Z zanko se bomo sprehodili čez števila, če bo trenutno število liho, ga izpišemo.

# In[55]:


i = 0
while i < 10:
    if i % 2 == 1:
        print(i)
    i += 1

