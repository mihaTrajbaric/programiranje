# Naloge: Čisti začetek
## Pretvarjanje iz Fahrenheitov v Celzije
Napiši program, ki mu uporabnik vpiše temperaturo v Fahrenheitovih stopinjah, program pa
jo izpiše v Celzijevih. Med temperaturama pretvarjamo po formuli C = 5/9 (F – 32). Za potrebe
Američanov napiši še program, ki računa v nasprotno smer.
Če se k tej nalogi vračaš, da jo uporabiš za vajo iz pisanja funkcij, pa napiši funkciji `celsius(f)`
in `fahrenheit(c)`. Prva prejme temperaturo v Fahrenheitih in vrne temperaturo v Celzijevih
stopinjah, druga pa ravno obratno.
## Pitagorov izrek
Napiši program, ki uporabnika vpraša po dolžinah katet pravokotnega trikotnika in izpiše
dolžino hipotenuze. (Da ponagajamo pokojnemu prof. Križaniču, ki je sovražil dlakocepce,
dodajmo "dolžino hipotenuze taistega trikotnika".)
Če nalogo uporabljaš za vajo iz pisanja funkcij, napiši funkcijo pitagora(a, b), ki prejme
dolžini katet in vrne dolžino hipotenuze.
## Topologija
Napiši program za izračun dolžine strela s topom (ki brez trenja izstreljuje točkaste krogle v
brezzračnem prostoru, a pustimo trivio). Program od uporabnika ali uporabnice zahteva, da
vnese hitrost izstrelka (to je, omenjene točkaste krogle) in kot, pod katerim je izstreljen.
Program naj izračuna in izpiše, kako daleč bo letela krogla.
Pomoč za fizično nebogljene: s = v2 sin(2)/g, kjer je s razdalja, v hitrost izstrelka,  je kot, g pa
osma črka slovenske abecede.
Preveri tole: krogla leti najdalj, če jo izstrelimo pod kotom 45 stopinj. Poskusi, kako daleč gre
pod kotom 45 in kako daleč pod 46 stopinj -- po 45 mora leteti dlje. Preveri tudi kot 50 stopinj:
če pod tem kotom leti nazaj (razdalja je negativna), si ga gotovo nekje polomil.
Če boš napisal rešitev v obliki funkcije, naj bo to funkcija top(v, fi).
## Ploščina trikotnika
Ploščino trikotnika s stranicami a, b in c lahko izračunamo po Heronovem obrazcu:
p = s(s − a)(s − b)(s − c) , kjer je s velikost polobsega, s = (a + b + c) / 2 . Napiši program,
ki uporabnika vpraša po dolžinah stranic in izpiše (njegovo) ploščino.
Program naj popazi na nepravilne podatke. Če uporabnik zatrdi, da ima trikotnik stranice 1, 2
in 5 (takšnega trikotnika – razmisli – pač ni), naj ga program pozove k resnosti.
Če nalogo rešuješ s funkcijo, naj se imenuje ploscina_trikotnika, prejme naj dolžine stranic
in ne pazi na nič. Če so podatki čudni, naj se pač sesuje.