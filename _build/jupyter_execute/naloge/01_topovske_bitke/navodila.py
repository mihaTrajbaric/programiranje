#!/usr/bin/env python
# coding: utf-8

# # Topovske bitke
# 
# ## Nekaj dejstev o šahu 
# 
# <img float="right" src="data:image/.png;base64,iVBORw0KGgoAAAANSUhEUgAAAYYAAAGICAMAAAByVLenAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAMxQTFRFBwcHQEBAv7+/c3NzgICATU1NJiYmg4ODwcHBRUVFUFBQf39/LCwsEBAQdXV17+/vICAgYGBgMDAwFxcXz8/P39/fcHBwn5+fZGRkNjY2j4+P0dHR8PDwk5OTr6+v4ODgoqKiOTk5HR0dExMTVVVVYmJiVlZWsrKyPj4+dHR0CgoKh4eHQ0NDKioqfn5+kJCQNTU1IiIiR0dHY2NjHh4eJSUlOzs7WVlZkZGRWFhYMjIyYWFhFRUVDw8PGRkZGBgYAAAA////mZmZ////2ISPqQAAAER0Uk5T/////////////////////////////////////////////////////////////////////////////////////////wBx0o8SAAAOxklEQVR42uzdCXuiyBYGYKBnVCDV7GA0apJO0tusd+6+nm7//3+6gAuGRU4Qq0j8zjw9XeMzqYiv1EYt2hoxgNDwEYABAQYwIMAABgQYwIAAAxgQYAAD4iwMOiH6jK4Mxjdm0HduEDdLY8TN8scfuHn+8CM3zxH70vV37EsHAxjAAAYwtDDMJ2msdokitQKDTIZAS2O8SxSpMRhkMmjTyST7U/oXGCQzjCs3QpYCg3yGVV4tZP+1T4FBfqFUE2BQUEXXBBjkNlgDbVG5F6ba9c0lM0SJPYvkdt/mQfCxpLAoFC6SIc5HAGO5veh5pXo4ULhEhpisaB36ZMsdzNjXA3UvXB6DQyIvmMgFg0IGg/T87/KDCTBIZYhIOLmGDwaVdYNFfrSOfDLAoJLBsYh0cpdrMChtsNqC0n9sMChl8Mhz1olLHhgUMiRk5UWToBAM6hisbd0cl/pvYJDKoG8ZbDCoZIi3lYIru1Ayx89D+3zR3TdBcbQOLclV9Fi7LWVjBqtLbimFuoIR1kkwmlQGuh9WFz1PKUxsw5H7vCE4+vANT98kMdQ+jAaDdIZxTUZgkMow384Qq9wN0930STBIYGial1FUD2CQwNAwS+mgegADGFAooVCSyLCaNAdaSljtAwYwgGHIDDODGfSOG8TNcnbPzfLO4+bp3XHzvGdfuv/EvvSuDPcjZpDODeJmeS+4Wbof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"/>
# 
# - Šahovska polja označimo s kombinacijo črke (stolpec) in številke (vrstica). c2 je tretje polje v drugi vrstici.
# - V šahu se trdnjava (AKA top) pomika po stolpcih in vrsticah, ne pa diagonalno ali kako drugače. Dve trdnjavi se torej napadata, če ste v isti vrstici in stolpcu.
# - Šahovske trdnjave lahko, tako kot šahovski konji, tudi preskakujejo figure. O tem dejstvu sicer nisem povsem prepričan, ampak Donald je tako napisal na Twitterju, torej mora biti res.
# 
# Običajno se v šahu napadajo bele in črne figure (tidve barvi bodo sicer nekoč zamenjali s čim nevtralnim, saj se to, da je beli lovec požrl črnega kmeta, sliši rasistično). V naši nalogi pa se bodo med seboj napadale kar bele trdnjave.
# 
# 

# 
# ## Predloga
# 
# Da bo reševanje šlo kar najbolj gladko, si najprej prenesi [topovske_bitke.py](https://raw.githubusercontent.com/programiranje-SKG/naloge-daljse/main/01_topovske_bitke/topovske_bitke.py) (predloga za reševanje) in [testi.py](https://raw.githubusercontent.com/programiranje-SKG/naloge-daljse/main/01_topovske_bitke/testi.py), ki vsebuje teste za avtomatsko testiranje.
# 
# Če želiš, da testi delujejo, morata biti datoteki shranjeni v isti mapi, druga zraven druge.
# 
# Datoteki odpri v svojem najljubšem IDE-ju. 
# 
# `Topovske_bitke.py` vsebuje že napisano ogrodje funkcij, ki jih moraš zgolj dopolniti, da bodo računale in vračale prave vrednosti (zamenjaj besedo `pass` s svojo kodo).
# Ko želiš preveriti pravilnost rešitve, poženi datoteko `testi.py`, ki bo preverila tvojo rešitev. V večini IDE-jev lahko tudi poženeš posamezne teste. V pyvharmu to narediš s klikom na zelen trikotnik ob določenem testu:
# 
# ![Run single test](./run-test.png)
# 
# ## Resitve
# [resitev.py](https://raw.githubusercontent.com/programiranje-SKG/naloge-daljse/main/01_topovske_bitke/resitev.py)
# 

# 
# ## Naloge
# 
# Napiši naslednje funkcije.
# 
# > Poskusite pri posameznih podnalogah uporabiti čim več že napisanih funkcij iz prejšnjih podnalog.
# 
# ### se_napadata
# 
# `se_napadata(top1, top2)` prejme koordinati dveh topov in vrne `True`, če se med seboj napadata (torej: če sta v isti vrstici ali stolpcu) in `False`, če se ne. Če gre za eno in isto trdnjavo, pa vedno vrne `False`.
# 
# Tako klica `se_napadata("a5", "a8")` in `se_napadata("c5", "f5")` vrneta `True`, klic `se_napadata("a5", "c3")` vrne `False` (ker nista ne v isti vrstici ne v istem stolpcu), klic `se_napadata("c3", "c3")` pa vrne `False`, ker gre za eno in isto trdnjavo.

# ### napadeni
# 
# `napadeni(top, topovi)` prejme koordinato enega topa in seznam koordinat vseh topov na šahovnici. Vrniti mora seznam koordinat vseh topov, ki jih napada podani top.
# 
# Klic `napadeni("c3", ["c1", "c3", "d6", "c6", "e5", "a3"])` vrne `["c1", "c6", "a3"]`. Klic `napadeni("c1", ["c1", "c3", "c4", "c5"])` vrne `["c3", "c4", "c5"]`, ker topovi lahko preskakujejo druge topove.
# 
# (Napadeni topovi naj bodo našteti v enakem vrstnem redu, v katerem se pojavijo v seznamu `topovi`. S tem se ti ni treba posebej ukvarjati: če ne boš kaj brez potrebe mešal(a), se bo zgodilo samo od sebe.)

# ### napadenost
# 
# `napadenost(top, topovi)` prejme koordinato topa in koordinate vseh topov ter vrne število topov, ki napadajo podani top. Napadenost topa f5 na sliki je 3, saj ga napadajo trije topovi (vključno s topom a5, ker lahko le-ta preskoči top c5).

# ### varen    
# 
# `varen(top, topovi)` vrne `True`, če podani top ni napaden in `False`, če je. Na sliki je le en top, za katerega bi ta funkcija vrnila `True`: top d3.

# ### Varni
# `varni(topovi)` vrne seznam varnih topov. Na sliki je varen le top d3, zato bo funkcija pri kongiguraciji, kot na sliki, vrnila samo tega.

# ### Najbolj napaden
# 
# `najbolj_napaden(topovi)` prejme seznam topov in vrne koordinati topa, ki ga napada največ drugih topov. Če je enako napadenih več, vrne tistega, ki je prej na seznamu. Če ni napaden nihče, vrne `None`.
# 
# Za topove na sliki ta funkcija vrne `"c5"`, saj ga napadajo štirje drugi topovi.

# ### vse_varno
# 
# `vse_varno(topovi)` vrne `True`, če noben top ne napada nobenega drugega. Na sliki ni vse varno. Nikakor.

# ## Dodatna naloga
# 
# Donald je priznal napako. No, v resnici je ni, fake news, ampak vseeno: topovi se ne morejo preskakovati. 
# 
# Napiši funkcijo `direkten_napad(top1, top2, topovi)`, ki prejme koordinati dveh topov in seznam vseh topov. Funkcija vrne `True`, če se `top1` in `top2` napadata - seveda tako, da med njima ni nobenega drugega topa.
# 
# Funkcija, ki smo jo napisali prej, bi za topa a5 in f5 vrnila `True`, četudi je med njima top na c5. Funkcija, ki jo pišemo zdaj, pa mora v takem primeru vrniti `False`.
