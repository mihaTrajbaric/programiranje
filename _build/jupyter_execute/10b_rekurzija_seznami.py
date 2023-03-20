#!/usr/bin/env python
# coding: utf-8

# # Rekurzivne funkcije na seznamih
# 
# Tole je običajen način poučevanja rekurzije. Strinjam se z argumenti, zakaj je zgrešen. Vendar sem pogosto naletel na študente, ki jim je bilo tole lažje kot karkoli drugega. Zategadelj poskušam tudi tako; nekateri doživijo razsvetljenje po tej poti.
# 
# 
# ## Palindrom
# 
# Niz je palindrom, če se naprej in nazaj bere enako.
# 
# Očitno obstaja kup načinov, da preverimo, ali je niz palindrom. Najlažji v Pythonu je, da ga pač obrnemo in pogledamo, ali ostane pri tem enak, `s[::-1] == s`.
# 
# Vendar nas danes zanima rekurzivna rešitev. Zato se moramo najprej domisliti rekurzivne definicije palindroma: niz je palindrom, če sta prvi in zadnji znak enaka, vse, kar je vmes, pa je palindrom. Obenem moramo pristaviti, da so tudi prazni nizi palindromi.
# 
# Kar smo napisali, "*niz je palindrom, če je prazen ali pa je prvi znak enak zadnjemu in je vse, kar je vmes palindrom*" dobesedno prevedemo v Python.

# In[1]:


def palindrom(s):
    return s == "" or s[0] == s[-1] and palindrom(s[1:-1])


# In[2]:


palindrom("pericarežeracirep")


# In[3]:


palindrom("abcba")


# In[4]:


palindrom("abccba")


# In[5]:


palindrom("abcdba")


# Študente tole pogosto zbega. Funkcija `palindrom` je definirana s funkcijo `palindrom`. Sama s sabo. Je to sploh dovoljeno? Deluje?
# 
# Če bi napisali
# 
# ```python
# def palindrom(s):
#     return palindrom(s)
# ```
# 
# to seveda ne bi delovalo. Razlog, da gornje deluje, pa je v tem da je niz vedno krajši.
# 
# - Ko se vprašamo, ali je `"abccba"` palindrom, funkcija ugotovi, da sta prvi in zadnji znak enaka in pokliče neko funkcijo, ki bo preverila, ali je `"bccb"` palindrom. Ta "neka funkcija" je slučajno ravno taista funkcija, a s tem ni nič narobe.
# - Funkcija, katere naloga je preveriti, ali je `"bccb` palindrom, ugotovi, da sta prvi in zadnji znak enaka, nato pa pokliče neko funkcijo, ki bo preverila, ali je `"cc"` palindrom.
# - Funkcija, katere naloge je preveriti, ali je `"cc"` palindrom, ugotovi, da sta prvi in zadnji znak enaka, nato pa pokliče neko funkcijo, ki bo preverila, ali je `""` palindrom.
# - Funkcija, katere naloge je preveriti, ali je `""` palindrom, odgovori, da je.
# 
# Kako Python zmore slediti temu? Kako se ne zgubi v tem, do kje je prišel, kaj preverja, kaj bo rezultat tega preverjanja? To naj vas ne skrbi. Zna pač. Da bi razložili, moramo vedeti več, kot bomo izvedeli pri tem predmetu.
# 
# Funkcijam, ki kličejo same sebe, rečemo "rekurzivne funkcije".
# 
# ## Vsota elementov seznama
# 
# Kako bi izračunali vsoto elementov seznama. Z zanko seveda znamo. Pa poskusimo še s trikom, kakršnega smo uporabili zgoraj. Za to spet potrebujemo rekurzivno definicijo vsote seznama - definicijo, ki se nanaša sama nase.
# 
# Takole lahko rečemo: vsoto elementov seznama dobimo tako, da k prvemu elementu prištejemo vsoto ostalih. Če je seznam prazen, pa je vsota 0.

# In[6]:


def vsota(s):
    if not s:
        return 0
    return s[0] + vsota(s[1:])

vsota([5, 8, 2])


# ## Vsebuje seznam sama soda števila?
# 
# Seznam vsebuje sama soda števila, če je prazen ali pa je prvi element sod in vsebuje preostanek seznama sama soda števila.

# In[7]:


def soda(s):
    return not s or s[0] % 2 == 0 and soda(s[1:])


# In[8]:


soda([4, 8, 6, 1, 2, 4])


# In[9]:


soda([4, 8, 6, 2, 4])


# ## Vsota sodih števil v seznamu
# 
# Napisati želimo funkcijo, ki vrne vsoto vseh sodih elementov v podanem seznamu.
# 
# Recimo tako:
# 
# - Če je seznam prazen, je vsota enaka 0.
# - Če je ničti element sod, vrnemo vsoto ničtega elementa in vsote ostalih.
# - Sicer vrnemo le vsoto ostalih.

# In[10]:


def vsota_sodih(s):
    if not s:
        return 0
    if s[0] % 2 == 0:
        return s[0] + vsota_sodih(s[1:])
    else:
        return vsota_sodih(s[1:])
        
vsota_sodih([4, 2, 5, 11, 6])


# ## Prvi sodi element seznama
# 
# Napisati želimo funkcijo, ki vrne prvi sodi element seznama.
# 
# Če je ničti element sod, vrnemo tega. Sicer vrnemo prvega sodega med ostalimi.

# In[11]:


def prvi_sodi(s):
    if s[0] % 2 == 0:
        return s[0]
    else:
        return prvi_sodi(s[1:])
        
prvi_sodi([5, 11, 3, 4, 8, 7, 12])


# Ta funkcija ima manjšo težavo, kadar v seznamu ni nobenega sodega elementa. Ker prvi ni sod, išče sodega v preostanku. Ker prvi iz preostanka ni sod, išče sodega v preostanku. Ker prvi v tem preostanku ni sod ... in tako naprej, dokler ne pride do praznega seznama. Takrat bomo v prvi vrstici funkcije spraševali po prvem (no, ničtem) elementu, `s[0]` in Python bo javil napako, `Index out of range`.
# 
# Recimo, da naj funkcija v takšnem primeru vrne `None`.

# def prvi_sodi(s):
#     if not s:
#         return None
#     if s[0] % 2 == 0:
#         return s[0]
#     else:
#         return prvi_sodi(s[1:])

# ## Vsi sodi elementi seznama
# 
# Funkcija, ki vrne vse sode elemente seznama je železna klasika napačnih rešitev. Tipični prvi poskus je

# In[12]:


def vsi_sodi(s):
    if s == []:
        return []
    
    t = []
    if s[0] % 2 == 0:
        t.append(s[0])
    vsi_sodi(s[1:])
    return t

vsi_sodi([4, 2, 5, 11, 6])


# To ne deluje, ker vsaka funkcija naredi svoj seznam `t`, vanj doda en sem element in ga vrne. Na koncu dobimo le seznam, ki ga ustvari najbolj zunanja funkcija.
# 
# V drugem poskusu poskusimo zagotoviti, da bodo vse funkcije uporabljale isti `t` tako, da ga postavimo pred funkcijo - tako da postane globalna spremenljivka.

# In[13]:


t = []

def vsi_sodi(s):
    if s == []:
        return []
    
    if s[0] % 2 == 0:
        t.append(s[0])
    vsi_sodi(s[1:])
    return t


# To deluje - vendar le enkrat. Če tole poskusimo poklicati večkrat, bo funkcija vedno dodajale elemente v ta seznam - in to ne bo dobro.

# In[14]:


vsi_sodi([4, 2, 5, 11, 6])


# In[15]:


vsi_sodi([4, 2, 5, 11, 6])


# In[16]:


vsi_sodi([4, 2, 5, 11, 6])


# To lahko poskušamo rešiti na vse žive načine. Recimo tako, da seznam praznimo na začetku funkcije.

# In[17]:


t = []

def vsi_sodi(s):
    t.clear()
    
    if s == []:
        return t
    
    if s[0] % 2 == 0:
        t.append(s[0])
    vsi_sodi(s[1:])
    return t

vsi_sodi([4, 2, 5, 11, 6])


# To ne deluje, ker se seznam sprazni ob *vsakem* klicu. Obupani študenti potem pišejo maile, kako narediti, da se bo seznam spraznil samo prvič.
# 
# Ne gre. Tu ni problem v tem, da ne znamo prav sprogramirati, temveč v tem, da narobe razmišljamo. Kakšna je rekurzivna definicija vseh sodih elementov seznama? To je seznam, ki vsebuje prvi element, če je le-ta sod, poleg tega pa vse sode elemente iz ostanka. Recimo tako:

# def vsi_sodi(s):
#     if s == []:
#         return []
#         
#     if s[0] % 2 == 0:
#         return [s[0]] + vsi_sodi(s[1:])
#     else:
#         return vsi_sodi(s[1:])

# Obstajajo tudi elegantnejši načini, obstajajo tudi hitrejši načini. A za nas je tale dovolj dober.
# 
# ## Sodolihi in lihosodi
# 
# Seznam je sodolih, če se v njem izmenjujejo sodi in lihi elementi, začenši s sodim.
# 
# Seznam je lihosod, če se v njem izmenjujejo lihi in sodi elementi, začenši z lihim.
# 
# Napisati moramo funkciji `sodolih` in `lihosod`, ki preverita, ali je seznam tak, kot pravi ime funkcije.

# In[18]:


def sodolih(s):
    return s == [] or s[0] % 2 == 0 and lihosod(s[1:])
    
def lihosod(s):
    return s == [] or s[0] % 2 == 1 and sodolih(s[1:])
    
sodolih([4, 5, 8, 13, 2, 7, 0])


# Tu vidimo primer, ko se dve funkciji kličeta med sabo. Tudi to je rekurzija in tudi za takšno obliko ni razloga, da ne bi delovala.
