# Programiranje

Ta repozitorij vsebuje skripto, ki jo uporabljam pri krožku Začetnega programiranja na Škofijski klasični gimnaziji v Ljubljani. Skripta je dostopna na https://mihatrajbaric.github.io/programiranje/


## Build

```
jupyter-book clean .
jupyter-book build .
```

## Publish

```
ghp-import -n -p -f _build/html
```