# Programiranje

Ta repozitorij vsebuje skripto, ki jo uporabljamo pri krožku Začetnega programiranja na Škofijski klasični gimnaziji v Ljubljani. Skripta je dostopna na https://programiranje-skg.github.io/skripta/


## Namestitev paketov
```
pip install -r requirements.txt
```

## Generiranje html-ja
Iz mape projekta:
```
jupyter-book clean .
jupyter-book build .
```

Nato s svojim najljubšim internetnim brskalnikom odpremo datoteko `_build/html/index.html` in si lahko lokalno ogledamo stran.

## Objava nove verzije
Če smo zadovoljni z novo verzijo strani, vse skupaj (vključno z avtomatsko generiranimi datotekami) porinemo v glavni branch (`git commit...`, `git push...`).

Nato stran posodobimo z ukazom:
```
ghp-import -n -p -f _build/html
```

## FAQ
### Ukaz 'jupyte-book' ali 'ghp-import' ne dela

Če ukaz poganjamo takoj po instalacij, (in paketov nismo namestili na PATH), jih Linux terminal ne bo našel. Po ponovnem zagonu računalnika bi moralo vse spet delovati.
