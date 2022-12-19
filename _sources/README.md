# Programiranje

Ta repozitorij vsebuje skripto, ki jo uporabljamo pri krožku Začetnega programiranja na Škofijski klasični gimnaziji v Ljubljani. Skripta je dostopna na https://mihatrajbaric.github.io/programiranje/


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
## Objava nove verzije
Ko je v glavnem branchu že koda nove verzije knjige, iz katere smo uspešno zgenerirali html, lahko stran posodobimo kot:
```
ghp-import -n -p -f _build/html
```
