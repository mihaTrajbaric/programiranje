#!/usr/bin/env python
# coding: utf-8

# # Rekurzivne funkcije - rodbina
#   
# 
# ## Novakovi
# 
# Najstarejši član rodbine Novakovih, Adam, 111 let, ima štiri otroke: Matjaža, Cilko, Danieka in Erika. Matjaž ima enega, namreč Viljema. Danijel ima Elizabeto in Hansa (kasneje se je Daniel namreč preselil v predmestje Graza, kjer ima manjše podjetje, in se poročil z Avstrijko), Cilka in Erik pa nimata otrok. In tako naprej. Vse skupaj je nabrano v spodnjem slovarju.

# In[1]:


otroci = {
    "Adam": ["Matjaž", "Cilka", "Daniel"],
    "Aleksander": [],
    "Alenka": [],
    "Barbara": [],
    "Cilka": [],
    "Daniel": ["Elizabeta", "Hans"],
    "Erik": [],
    "Elizabeta": ["Ludvik", "Jurij", "Barbara"],
    "Franc": [],
    "Herman": ["Margareta"],
    "Hans": ["Herman", "Erik"],
    "Jožef": ["Alenka", "Aleksander", "Petra"],
    "Jurij": ["Franc", "Jožef"],
    "Ludvik": [],
    "Margareta": [],
    "Matjaž": ["Viljem"],
    "Petra": [],
    "Tadeja": [],
    "Viljem": ["Tadeja"],
}


# Znane so tudi starosti vseh teh ljudi. V teh zapiskih jih sicer ne bomo potrebovali, uporabne pa so za kakšne druge naloge.

# In[2]:


starost = {
    "Adam": 111, "Matjaž": 90, "Cilka": 88, "Daniel": 85, "Erik": 83,
    "Viljem": 58, "Tadeja": 20, "Elizabeta": 68, "Hans": 64, "Ludvik": 50,
    "Jurij": 49, "Barbara": 45, "Herman": 39, "Mihael": 32, "Franc": 30,
    "Jožef": 29, "Margareta": 3, "Alenka": 9, "Aleksander": 5, "Petra": 7}


# Celoten rodovnik je takšen:
# 
# <img src="data:image/.png;base64,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"/>

# Napišimo, takole, za preprosto vajo, funkcijo, ki ji podamo osebo in pove,
# koliko otrok ima.

# In[3]:


def stevilo_otrok(oseba):
    return len(otroci[oseba])
    
stevilo_otrok("Jožef")


# Kako pa bi izvemo število vnukov posamezne osebe? Tako da gremo prek vseh otrok in seštevamo število njihovih otrok, recimo z

# In[4]:


def stevilo_vnukov(oseba):
    v = 0
    for otrok in otroci[oseba]:
        v += len(otroci[otrok])
    return v

stevilo_vnukov("Daniel")


# ali, brez velike razlike,

# In[5]:


def stevilo_vnukov(oseba):
    v = 0
    for otrok in otroci[oseba]:
        v += stevilo_otrok(otrok)
    return v

stevilo_vnukov("Daniel")


# Uh, kaj kompliciramo, saj znamo tudi:

# In[6]:


def stevilo_vnukov(oseba):
    return sum(stevilo_otrok(otrok) for otrok in otroci[oseba])


# ## Velikost rodbine
# 
# Do sem - nič posebnega. Zdaj pa pridejo zanimive reči: za nekoga nas zanima, velika je njegova rodbina, skupaj z njim, njegovimi otroki, vnuki, pravnuki in tako naprej. Recimo, da ima rojstni dan in bo povabil vso svojo rodbino na večerjo. Koliko krožnikov za juho potrebuje.
# 
# 
# Kaj mu je storiti? Vse svoje otroke, bo vprašal, kako velike so njihove rodbine. To bo seštel in prištel še sebe. Kako bodo ti otroci izvedeli velikosti svojih rodbin? Tako, da bodo vprašali vse svoje otroke po velikosti njihovih rodbin, to sešteli in prišteli še sebe. Pa njihovi otroci? Enako.
# 
# Spremenimo to v funkcijo. Velikost rodbine dobimo tako, da gremo prek otrok in seštevamo velikosti njihovih rodbin.

# In[7]:


def velikost_rodbine(oseba):
    v = 0
    for otrok in otroci[oseba]:
        v += velikost_rodbine(otrok)
    return v + 1

velikost_rodbine("Elizabeta")


# Za tiste, ki znajo snov izpred dveh tednov:

# In[8]:


def velikost_rodbine(oseba):
    return sum(velikost_rodbine(otrok) for otrok in otroci[oseba]) + 1

velikost_rodbine("Elizabeta")


# Tule je primeren trenutek, da povemo nekaj pomembnega - kar je pravzaprav očitno, ampak vam malo kasneje morda ne bo: **vsaka funkcija ima svoje lokalne spremenljivke**. To vemo že nekaj časa. A tudi, ko funkcija kliče samo sebe, **ima vsaka "inkarnacija" funkcije svoje spremenljivke**. Funkcija `velikost_rodbine` si pripravi `v = 0`. Nato ga povečuje. A ko kliče samo sebe, in si v (rekurzivnih) klicih funkcija pripravi `v = 0`, je to **drug in ne isti `v`**.

# ## Poišči osebo
# 
# Kako odkriti, ali je v rodbini določene osebe oseba s takšnim in takšnim imenom?
# 
# Storiti nam je tole: če je tako ime ravno vprašani osebi, bo odgovorila `True`. Sicer bo enega za drugim spraševala otroke, dokler prvi ne odgovori `True`; tedaj vrnemo `True`. Če noben otrok nima takšnega potomca - in torej noben otrok ne odgovori `True`, odgovorimo `False`. Z drugimi besedami,

# In[9]:


def obstaja_ime(oseba, ime):
    if oseba == ime:
        return True
    for otrok in otroci[oseba]:
        if obstaja_ime(otrok, ime):
            return True
    return False

obstaja_ime("Elizabeta", "Franc")


# S snovjo izpred dveh tednov:

# In[10]:


def obstaja_ime(oseba, ime):
    return oseba == ime or any(obstaja_ime(otrok, ime) for otrok in otroci[oseba])


# In[11]:


obstaja_ime("Elizabeta", "Franc")


# In[12]:


obstaja_ime("Elizabeta", "Herman")


# ## Največja družina
# 
# Kako velika je največja družina v rodbini neke osebe - s tem mislimo le otroke, brez staršev? Tu osebe razmišljajo tako: najprej predpostavijo, da je to njihova družina - največ otrok je torej toliko otrok, kolikor jih imajo oni. Potem vprašajo vsakega od otrok, kako velika je največja družina v njegovi rodbini. Če naleti na koga z večjo družino, si to zapomni. Na koncu vrne največ, kar je videl.

# In[13]:


def najvec_otrok(oseba):
    najvec = len(otroci[oseba])
    for otrok in otroci[oseba]:
        koliko = najvec_otrok(otrok)
        if  koliko > najvec:
            najvec = koliko
    return najvec


# Največja družina v Danielovi rodbini ima tri otroke, zato

# In[14]:


najvec_otrok("Daniel")


# Kdor zna, zna takole:

# In[15]:


def najvec_otrok(oseba):
    return max([len(otroci[oseba])] + [najvec_otrok(otrok) for otrok in otroci[oseba]])

najvec_otrok("Daniel")


# Ob reševanju te naloge znajo študenti pogosto zagrešiti hud greh. Več o njem na koncu zapiskov.
# 
# ## Najdaljše ime v rodbini
# 
# Katero je najdaljše ime v rodbini neke osebe? Tole je precej podobno največjemu številu otrok: najdaljše je moje, razen če je daljše katero od imen v rodbini katerega od otrok.

# In[16]:


def najdaljse_ime(oseba):
    najdaljse = oseba
    for otrok in otroci[oseba]:
        naj_pod = najdaljse_ime(otrok)
        if len(naj_pod) > len(najdaljse):
            najdaljse = naj_pod
    return najdaljse
    
najdaljse_ime("Adam")


# (Z izpeljanimi seznami bi šlo enako kot prej. A pustimo.)
# 
# ## Globina rodbine
# 
# Kako globoka je rodbina določene osebe? Torej, nekdo, ki nima otrok, ima rodbino globine 0. Če ima otroke, nima pa vnukov, ima rodbino globine 1. Če ima tudi kakega vnuka, vendar nobenega pravnuka, ima rodbino globine 2.
# 
# Globino rodbine izračunamo tako, da vprašamo vse otroke po globinah njihovih rodbin in k največji globini, ki jo dobimo, prištejemo 1. Začetna največja globina pa bo `-1`; če oseba nima otrok, bo tudi ostala -1, in ko bomo prišteli 1, bo 0. Kot mora biti.

# In[17]:


def globina(oseba):
    najvecja = -1
    for otrok in otroci[oseba]:
        g = globina(otrok)
        if g > najvecja:
            najvecja = g
    return najvecja + 1

globina("Elizabeta")


# Ali, krajše

# In[18]:


def globina(oseba):
    return max([globina(otrok) for otrok in otroci[oseba]], default=-1) + 1    

globina("Elizabeta")


# ## Velikost potomstva
# 
# Pripadnike Novakove rodbine smo nato spraševali, koliko potomstva imajo. S potomci mislimo nekaj takšnega kot rodbino, a brez te osebe same. Jurij (ki ima dva otroka in tri vnuke) ima pet potomcev, čeprav je velikost njegove rodbine enaka 6.
# 
# Tale zahteva malo razmisleka. Navidez bi jo lahko ugnali tako, kot smo velikost rodbine, le 1 ne smemo prišteti na koncu, saj oseba ne sme šteti sebe.

# In[19]:


def stevilo_potomcev(oseba):
    v = 0
    for otrok in otroci[oseba]:
        v += stevilo_potomcev(otrok)
    return v


# Zoprna reč je, da je ta funkcija nekoliko napačna. No, precej napačna. Vedno vrne 0 - ker nihče nikoli ničesar ne prišteje, vse seštevajo samo ničle. In iz ničel nikoli ne boš dobil ničesar, pa jih seštevaj, kolikor dolgo hočeš.

# In[20]:


stevilo_potomcev("Elizabeta")


# Ena rešitev je, da vsak vrne število svojih otrok, ki čemur morajo otroci prišteti število svojih otrok, in vnuki število svojih...

# In[21]:


def stevilo_potomcev(oseba):
    potomcev = len(otroci[oseba])
    for otrok in otroci[oseba]:
        potomcev += stevilo_potomcev(otrok)
    return potomcev
    
stevilo_potomcev("Elizabeta")


# Ali isto, le na drug način:

# In[22]:


def stevilo_potomcev(oseba):
    potomcev = 0
    for otrok in otroci[oseba]:
        potomcev += 1 + stevilo_potomcev(otrok)
    return potomcev

stevilo_potomcev("Elizabeta")


# Lahko pa si pomagamo tudi z rodbino:

# In[23]:


def stevilo_potomcev(oseba):
    return velikost_rodbine(oseba) - 1
    
stevilo_potomcev("Elizabeta")


# ## Izpis vseh članov rodbine
# 
# Rešimo nekoliko preprostejšo nalogo od gornjih - ker bo vodila v nekoliko zahtevnejšo spodnjo. Izpisali bi radi vse člane rodbine določene osebe.
# 
# Naloga je res preprosta: vsak izpiše svoje ime in pozove svoje otroke, naj storijo isto.

# In[24]:


def izpis(oseba):
    print(oseba)
    for otrok in otroci[oseba]:
        izpis(otrok)
        
izpis("Adam")


# ## Seznam potomcev
# 
# Zdaj pa napišimo funkcijo `rodbina(oseba)`, ki vrne seznam imen vseh članov rodbine podane osebe. Funkcija je nadvse poučna zato, ker jo študenti zelo vztrajno programirajo narobe. Na vsak način si jo namreč želijo sprogramirati tako, da bi sestavili seznam, v katerega mora vsak dopisati sebe in nato k temu povabiti še svoje otroke. 
# 
# Slediti želijo gornji funkciji, le `print` bi zamenjali z `append`. Tako naredijo tole.
# 
# ```python
# def rodbina(oseba):
#     clani.append(oseba)
#     for otrok in otroci[oseba]:
#         rodbina(otrok)
# ```
# 
# Ideja je, da se vsi dopisujejo v seznam `clani`. In to - kot je vsem, ki to napišejo, jasno na prvi pogled, ne deluje, ker nimamo seznama `clani`. Zato v resnici naredijo tole.

# In[25]:


def rodbina(oseba):
    clani = []
    clani.append(oseba)
    for otrok in otroci[oseba]:
        rodbina(otrok)
    return clani

rodbina("Adam")


# Kot je jasno vsakemu, ki ve vsaj kaj malega o eni od treh razširjenih religijah, namreč judovski, krščanski in muslimanski (in order of appearance), je zgolj število trenutno živečih članov Adamove rodbine okrog sedem milijard in pol (število vseh ljudi, ki so bili kdaj na svetu, pa okrog sto milijard). No, v našem rodovniku pa jih je, skupaj z Adamom, 19. Funkcija pa vrne le Adama.
# 
# Zakaj? Logično. Kaj počnemo s seznamom člani? Pripravimo prazen seznam, vanj dodamo osebo in ga vrnemo. Tisti dve vrstici, ki sta vmes (zanka in klic v njej) se seznama `clani` ne dotikata. Vsaka funkcija ima *svoje* lokalne spremenljivke. Vsi ti klici funkcij si ne delijo *istega* seznama `clani`, saj ima - kot smo se ponovno spomnili precej na začetku, ob funkciju `velikost_rodbine`, vsaka funkcija **svoje lokalne spremenljivke**.
# 
# Študent, ki napiše gornje, je naredil zgolj napako. V obupu pa se zatečejo iz *napake* naravnost v *greh*. Naredijo pogodbo s hudičem (v obliki globalne spremenljivke) in mislijo, da jih bo to rešilo.

# In[26]:


clani = []

def rodbina(oseba):
    clani.append(oseba)
    for otrok in otroci[oseba]:
        rodbina(otrok)
    return clani

rodbina("Adam")


# Nasvet nekoga, ki rad bere ljudske zgodbe in pripovedke: pogodbe s hudičem se nikoli ne splačajo. Kratkoročno izgleda, da je junak zgodbe uspel, potem pa pride tvist, kjer hudič zmaga. (Edina znana izjema v zgodovini človeštva je oni nemški kovač; več o njem na [Myths and Legends](https://www.stitcher.com/show/myths-and-legnen/episode/45rumpelstiltskin-lets-make-a-deal-46489753), začetek zgodbe je pri 17:45.)
# 
# Torej: zgoraj je videti, da funkcija deluje. Za vsak slučaj poglejmo še Jožefovo rodbino, ki, kot vemo, obsega njega in njegove tri otroke.

# In[27]:


rodbina("Jožef")


# Razumemo, kaj se dogaja? Vsakič, ko pokličemo funkcijo, dodaja nove ljudi v isti seznam. Ta bo vsakič vedno daljši. Potem se grešnik domisli, da bi `clani` spraznil na začetku klica funkcije,

# In[28]:


clani = []

def rodbina(oseba):
    clani = []
    clani.append(oseba)
    for otrok in otroci[oseba]:
        rodbina(otrok)
    return clani

rodbina("Adam")


# To ne deluje iz enakega razloga, iz katerega ne deluje že prvič. `clani` je zdaj spet lokalna spremenljivka funkcije, katere ime je slučajno enako imenu globalne spremenljivke.
# 
# Grešnik išče odrešenja v tem, da v funkciji ne naredi nove, lokalne spremenljivke, temveč sprazni globalno,

# In[29]:


clani = []

def rodbina(oseba):
    clani.clear()
    clani.append(oseba)
    for otrok in otroci[oseba]:
        rodbina(otrok)
    return clani

rodbina("Adam")


# a tudi to ne obrodi bistveno boljši rezultatov, saj se ena in ista spremenljivka praznita ob vsakem rekurzivnem klicu in na koncu vsebuje tisto vrednost, ki jo je tja vpisala zadnja oseba, za katero smo poklicali funkcijo.
# 
# Kdor naredi pogodbo s hudičem, se zezne. Rekurzija in globalne spremenljivke so zelo slaba kombinacija.
# 
# Osnovni problem ni v tem, da ne bi znali sprogramirati, temveč že v tem, da narobe razmišljamo. Tule znotraj funkcije očitno pokličemo funkcijo `rodbina(otrok)`, ki vrne nek rezultat, mi pa s tem rezultatom na naredimo ničesar. To ne more biti prav, ne? (Picajzlasto gledano: lahko bi bilo prav. Vendar bi bilo treba sprogramirati grše in računati na "stranske efekte" funkcije, kar pa je prav tako zelo grdo.)
# 
# Razmišljati moramo z vidika igre, ki jo igramo ob učenju rekurzije v predavalnici: vsak otrok sporoči svojo rodbino in to, kar vrnejo otroci, je potrebno seštevati.

# In[30]:


def rodbina(oseba):
    clani = [oseba]
    for otrok in otroci[oseba]:
        clani += rodbina(otrok)
    return clani

rodbina("Adam")


# In[31]:


rodbina("Jožef")


# ## Globina imena
# 
# Funkcija `globina_imena(oseba, ima)` naj pove, kako globoko v rodbini podane osebe je potomec s podanim imenom. Če gre za eno in isto osebo; naj vrne 0; če za otroka, vrne 1; če za vnuka, 2; če za pravnuka, 3... Če oseba nima potomca s podanim imenom, pa naj funkcija vrne `None`.
# 
# Gre za variacijo funkcije `obstaja_ime`. Tako kot prej tudi tu vrnemo `None`, če imena ni. Če kateri od otrok pove, da je dotični potomec na globini `n`, pa je ta potomec, glede na to osebo, na globini `n + 1`.

# In[32]:


def globina_imena(oseba, ime):
    if oseba == ime:
        return 0
    for otrok in otroci[oseba]:
        n = globina_imena(otrok, ime)
        if n != None:
            return n + 1
    return None

globina_imena("Daniel", "Jožef")


# Pri `najvec_otrok` sem opozoril, da znajo študenti pri programiranju te funkcije narediti zoprno napako. Tudi `globina_imena` ponuja podobno skušnjavo. Marsikateri študent bi jo skrajšal za eno vrstico in naredil tako:

# In[33]:


def globina_imena(oseba, ime):
    if oseba == ime:
        return 0
    for otrok in otroci[oseba]:
        if globina_imena(otrok, ime) != None:
            return globina_imena(otrok, ime) + 1
    return None

globina_imena("Daniel", "Jožef")


# In[34]:


def globina_imena(oseba, ime):
    print(oseba)
    if oseba == ime:
        return 0
    for otrok in otroci[oseba]:
        n = globina_imena(otrok, ime)
        if n != None:
            return n + 1
    return None

globina_imena("Daniel", "Jožef")


# Druga funkcija - tista, ki se pokliče dvakrat.

# In[35]:


def globina_imena(oseba, ime):
    print(oseba)
    if oseba == ime:
        return 0
    for otrok in otroci[oseba]:
        if globina_imena(otrok, ime) != None:
            return globina_imena(otrok, ime) + 1
    return None

globina_imena("Daniel", "Jožef")


# Pričakovali bi dvakrat daljši spisek ... vendar je spisek očitno več kot dvakrat daljši.
# 
# Kolikokrat se na njem pojavi Jožef? Osemkrat!
# 
# Daniel dvakrat vpraša Elizabeto. To drži. Elizabeta dvakrat vpraša Jurija; vendar je sama vprašana dvakrat, torej je Jurij vprašan štirikrat. Jurij pa dvakrat vpraša Jožefa; Jurij sam je vprašaan štirikrat, torej je Jožef osemkrat. Kot je očitno iz spiska.
# 
# Število vprašanj se v vsakem nivoju podvoji. Pri drevesu globine 5, kot je naše, so nekateri vprašani 32-krat. Pri drevesu globine 10 so vprašani 1024-krat. Pri drevesu globine 20 pa že več kot milijonkrat - namesto dvajsetkrat.
# 
# V rekurziji se moramo *res* izogniti temu, da bi isto funkcijo brez potrebe klicali večkrat.
