# Komentarze
![cc-by-shield](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)

Korpus ręcznie sklasyfikowanych komentarzy do uczenia maszynowego (filtrowanie komentarzy obraźliwych)

## Skąd? 

Korpus został zgromadzony na przełomie roku 2015 i 2016 na potrzeby mojej pracy magisterskiej.
Wszystkie komentarze pochodzą z róznych działów portalu Wirtualna Polska.

## Jak używać?

### R
```r
source("komentarze.R")

load_komentarze(".")

# A tibble: 7,023 x 4
   klasa        komentarz                                                                                          nie   tak
   <chr>        <chr>                                                                                            <int> <int>
 1 Groźby kara… Dziwię się, że Niemcy działają opieszale w sprawie gwałtów przecież nie wyszli chyba z wprawy z…     3    28
 2 Groźby kara… Przywalić atomem tej islamskiej dziczy. Merkel powinna być powieszona publicznie.                    2     7
 3 Groźby kara… Tu trzeba jasno powiedzieć,wracasz albo kulka.                                                       0    40
 4 Groźby kara… umrzesz za tydzień                                                                                  16     0
 5 Groźby kara… wybic do nogi prawie wszystkich arabów , pozostawiając kilku jako eksponaty                          1     1
 6 Groźby kara… SPALIĆ MECZETY                                                                                       1     1
 7 Groźby kara… Czas odpalic piece i komory gazowe, szybko zboczencow muzulmanskich osądzać i w dym obracać.         1    14
 8 Groźby kara… Stryczek !                                                                                          11     4
 9 Groźby kara… Bohater narodowy szkalowany przez prawicę która tylko nienawidzi! Śmierć popierającym PiS to an…     4     2
10 Groźby kara… Proponuję wysłać do niego pluton specjalny z polonem.                                               12     6
# … with 7,013 more rows

```

### Python
```python
from komentarze import Komentarze
k = Komentarze('path/to/Komentarze').load()
df = k.get_dataframe()

print df

          klasa                                          komentarz  nie  tak
0       Krytyka  Myślę, że Petru jest z tej samej bajki co Tymi...   57   27
1       Krytyka  Tvp już się nie da oglądać! Porównajcie wiadom...   15    2
2       Krytyka  Akt wandalizmu to stawianie tych wstrętnych po...   13   12
3       Krytyka  Najgorsze jest to, że politycy europejscy nie ...   82   46
4       Krytyka  A co cbos ma podawać.jak kaczor kazał 39 dla P...    4    1
5       Krytyka  Podsłuchy były zlecone przez PIS. Dlatego bron...    4    1
6       Krytyka  Sondaże poparcia mówią coś całkiem innego niż ...    2    1
7       Krytyka  CBOS jest finansowany przez Beatę Szydło , wię...    6    4
8       Krytyka  I tu się Niemiaszek myli, bowiem krytykowanie ...   85   49
9       Krytyka  Europa ma dwa wyjścia, albo wyrzucić emigrantó...   82   49
10      Krytyka  Do czego to doszło żeby Niemiec, upominał się ...    2    0
11      Krytyka             Nie chcę słuchać ani oglądać posłów PO    2    1
12      Krytyka  Panie Dębski proszę POdać ile obietnic za osie...    2    1
28      Krytyka  zobaczyłam i jestem bardzo zadowolona z tego c...    0    2
29      Krytyka  Po upływie 3 miesięcy od przejęcia rządów prze...   25    4
...         ...                                                ...  ...  ...
6993  Obraźliwe  Juz wczoraj pilismy szampana.Mialam dosc tych ...    3    2
6994  Obraźliwe  ty tepa blondynko religija w szkolach jest fin...    1    0
7020  Obraźliwe  skad sie biora ludzie ktorym przeszkadza repor...    3    0
7021  Obraźliwe  ONI SAMI ZŁOZYLI DYMISJE BO  CHODZI O KASE BYŁ...    0    1
7022  Obraźliwe  NO PO  MARNIE SIE STARACIE ,MUSICIE SKLADAC SK...   64   28

[7023 rows x 4 columns]
```

