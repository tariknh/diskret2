# MA-224 – Delprøve 4 – Hjelpeark versjon 3

Gjenoppbygd 20. november 2026. Søk med Cmd+F / Ctrl+F. Sidetall viser til PDF-en.

## Side 1: Delprøve 4: finn oppgaven din

Søk: RSA • Coding theory • Applications of Lagrange's theorem • Hamming • generator • parity check • syndrome

Start med den engelske setningen. Finn raden nedenfor. Følg oppskriften, eller bruk talloppslaget når ALLE tallene stemmer.

| Ser du dette i oppgaven? | Gå til |
| --- | --- |
| Select all options … valid key pair | RSA-flervalg: side 3. Ferdige tall: 5–7. |
| Bob’s RSA key is weak / Find the unencrypted message | Privat nøkkel og klartekst: 8. Talloppslag: 10. Casio-eksempel 2747: 12. |
| minimal and maximal Hamming distance | Tell ulike bit: 13. Oppslag: 14–15. |
| noisy binary symmetric channel / at most | Sannsynlighet: 16. Oppslag: 18. |
| Find the generator matrix / parity check matrix | G, H og syndrom: 19–21. Enkelt 5-biteksempel: 22. Matriseoppslag: 23. |
| minimum distance / always able to detect | Kodeord og minsteavstand: 27. Oppslag: 28. |
| Compute the error pattern / encoded message | Dekoding med 8 bit: 31–33. Eksemplet med r=10110001 står på side 33. Fasiter: 37. |

Dette arket dekker de 96 regneoppgavene i de 32 byte-ulike prøvefilene i Delprove_4, pluss supplerende regneeksempler fra notatene. Mappen har 44 PDF-er: 36 prøvekopier og 8 notatkopier. Kildesjekken bakerst viser hver fil.

Søk med Cmd+F / Ctrl+F. Oppgavene og tallene kan endres i nye prøver; bruk fremgangsmåten hvis oppslaget ikke matcher. Øvingssiden heter test4-med-preview.html.

## Side 2: Hurtigsjekk før du svarer

Søk: quick checklist • syntax • leading zero • rounded off to three decimals

| Oppgavetype | Dette må du huske |
| --- | --- |
| RSA-flervalg | p og q må være primtall. Test x*y modulo (p−1)*(q−1), ikke modulo n. Resten skal være 1. |
| Privat nøkkel | y er inversen til x modulo phi. Klartekst er M^y modulo n. |
| Hamming | Sammenlign ulike strenger. Fire strenger gir seks par. Ikke ta med avstand fra en streng til seg selv. |
| Sannsynlighet | Les tallet etter «at most». Høyst 2 inkluderer 0, 1 og 2 feil. Rund bare sluttsvaret. |
| En bestemt mottatt streng | Tell d ulike posisjoner. Bruk p^d*(1−p)^(n−d). Ingen binomialfaktor. |
| G og H | G har én rad per meldingsbit. H har én rad per kontrollbit. Alt regnes modulo 2. |
| Minimum distance / detect | d_min er minste vekten til et ikke-null kodeord. «Always detect» spør etter d_min−1. |
| Syndrom / error pattern | Ved 8-bit-oppgavene: syndrom har 4 bit. Feilmønster og korrigert kodeord har 8 bit. |

Behold nuller først: skriv 0010, ikke 10. Matrise: mellomrom mellom tall, linjeskift mellom rader. Bitstreng: skriv bare bitene uten komma eller klammer.

Flervalg: «None of the above» krysses bare av når ingen vanlige alternativer er riktige. Rekkefølgen på alternativene kan endres. Match hele tallsettet, ikke alternativnummeret.

## Side 3: RSA-flervalg: hva skal krysses av?

Søk: valid RSA keys • valid key pair • Select all options • public and private key • x y p q n

Du får x, y, p, q, n i hvert alternativ. Her brukes læreboktesten phi=(p−1)*(q−1).

| Steg | Gjør dette | Hvis testen feiler |
| --- | --- | --- |
| 1 | Kontroller at p og q er ulike primtall. | LA ALTERNATIVET STÅ TOMT. |
| 2 | Kontroller n=p*q. | LA DET STÅ TOMT. |
| 3 | Regn phi=(p−1)*(q−1). | Dette er modulen i neste steg. |
| 4 | Bruk produktkalkulatoren: Factor 1=x, Factor 2=y, Modulus=phi. | Hvis resten ikke er 1: LA DET STÅ TOMT. |
| 5 | Alle testene bestått? | KRYSS AV. |

Kalkulatorens «Modulus» skal være phi, selv om oppgaven kaller RSA-modulen n. Ikke skriv x*y mod n i denne testen.

Hvis gcd(x,phi)>1, kan x ikke ha en invers. Det er en rask måte å forkaste et alternativ på. Et partall x forkastes når p og q er odde primtall, fordi phi da er partall.

Men x og y kan gi rest 1 i kontrollen selv om p er et sammensatt tall. Derfor kan du ikke hoppe over primtallstesten.

De 30 tallalternativene som faktisk forekommer, står på side 5–7.

## Side 4: RSA: to konkrete feller

Søk: prime numbers • composite • gcd • 7637383 • 20271383 • Factor 1 • Modulus

### Et gyldig alternativ

```text
x=20271383, y=22663367
p=3557, q=7741, n=27534737
phi=3556*7740=27523440
(20271383*22663367) mod 27523440 = 1
```

p og q er primtall, og p*q=n. Dette alternativet skal krysses av.

### Et alternativ som lurer deg hvis du bare sjekker resten

```text
x=7637383, y=15705847
p=3921, q=5531, n=21687051
3921=3*1307
```

3921 er ikke primtall. Alternativet skal stå tomt selv om produktkontrollen med (3921−1)*(5531−1) gir rest 1.

### Hvordan sjekker du et nytt tall?

Prøv divisjon med primtallene opp til kvadratroten av tallet. Hvis én divisjon gir et heltall, er tallet sammensatt. Du kan stoppe når primtallets kvadrat er større enn tallet.

```text
Primtall opp til 89:
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89
```

Snarveier: partall >2 er ikke primtall. Siffersum delelig på 3 betyr delelig på 3. Tall som slutter på 0 eller 5 og er >5 er ikke primtall.

## Side 5: RSA-oppslag 1 av 3: eksakte alternativer

Søk: valid RSA keys • 682183 • 2124966 • 2497423 • 2846781 • 3008046 • 3872401 • 3975723 • 5066098 • 6058577 • 7057729

Match alle fem tall: x, y, p, q og n. «KRYSS AV» betyr gyldig. Alle andre rader skal stå tomme.

| x og y | p, q og n | Velg slik |
| --- | --- | --- |
| x=682183<br>y=22904887 | p=6163, q=4217<br>n=25989371 | KRYSS AV |
| x=2124966<br>y=1889417 | p=5477, q=2437<br>n=13347449 | gcd(x,phi)=6 |
| x=2497423<br>y=16962307 | p=7231, q=2687<br>n=19429697 | p er ikke primtall |
| x=2846781<br>y=2055541 | p=2709, q=2861<br>n=7750449 | p er ikke primtall |
| x=3008046<br>y=2067287 | p=3881, q=2549<br>n=9892669 | gcd(x,phi)=2 |
| x=3872401<br>y=5158441 | p=7247, q=4261<br>n=30879467 | KRYSS AV |
| x=3975723<br>y=862787 | p=7901, q=3209<br>n=25354309 | KRYSS AV |
| x=5066098<br>y=11977289 | p=6709, q=5641<br>n=37845469 | gcd(x,phi)=2 |
| x=6058577<br>y=8054977 | p=5303, q=6473<br>n=34326319 | KRYSS AV |
| x=7057729<br>y=1240783 | p=6007, q=3271<br>n=19648897 | gcd(x,phi)=7 |

Nye tall? Bruk sjekklisten på side 3. Disse radene er sortert etter x, ikke etter rekkefølgen i prøven.

## Side 6: RSA-oppslag 2 av 3: eksakte alternativer

Søk: valid RSA keys • 7637383 • 8000356 • 9017582 • 9657491 • 12903033 • 14024123 • 14907077 • 17570399 • 20271383 • 21226837

Match alle fem tall: x, y, p, q og n. «KRYSS AV» betyr gyldig. Alle andre rader skal stå tomme.

| x og y | p, q og n | Velg slik |
| --- | --- | --- |
| x=7637383<br>y=15705847 | p=3921, q=5531<br>n=21687051 | p er ikke primtall |
| x=8000356<br>y=277063 | p=4177, q=3851<br>n=16085627 | gcd(x,phi)=28 |
| x=9017582<br>y=3606439 | p=6673, q=4093<br>n=27312589 | gcd(x,phi)=2 |
| x=9657491<br>y=10246811 | p=2721, q=4021<br>n=10941141 | p er ikke primtall |
| x=12903033<br>y=3215451 | p=6113, q=2437<br>n=14897381 | gcd(x,phi)=3 |
| x=14024123<br>y=3588467 | p=3879, q=6529<br>n=25325991 | p er ikke primtall |
| x=14907077<br>y=8920973 | p=7177, q=2843<br>n=20404211 | KRYSS AV |
| x=17570399<br>y=30362099 | p=7451, q=6451<br>n=48066401 | KRYSS AV |
| x=20271383<br>y=22663367 | p=3557, q=7741<br>n=27534737 | KRYSS AV |
| x=21226837<br>y=3434893 | p=5119, q=5563<br>n=28476997 | KRYSS AV |

Nye tall? Bruk sjekklisten på side 3. Disse radene er sortert etter x, ikke etter rekkefølgen i prøven.

## Side 7: RSA-oppslag 3 av 3: eksakte alternativer

Søk: valid RSA keys • 21749249 • 23095092 • 26924209 • 27087494 • 35131943 • 35413787 • 35519203 • 36661763 • 36784094 • 42185665

Match alle fem tall: x, y, p, q og n. «KRYSS AV» betyr gyldig. Alle andre rader skal stå tomme.

| x og y | p, q og n | Velg slik |
| --- | --- | --- |
| x=21749249<br>y=17859389 | p=5335, q=6571<br>n=35056285 | p er ikke primtall |
| x=23095092<br>y=2157127 | p=7027, q=3917<br>n=27524759 | gcd(x,phi)=12 |
| x=26924209<br>y=43485577 | p=7239, q=7789<br>n=56384571 | p er ikke primtall |
| x=27087494<br>y=8924683 | p=7331, q=4231<br>n=31017461 | gcd(x,phi)=2 |
| x=35131943<br>y=15273131 | p=7579, q=7583<br>n=57471557 | p er ikke primtall |
| x=35413787<br>y=22470071 | p=5575, q=7919<br>n=44148425 | p er ikke primtall |
| x=35519203<br>y=9772867 | p=5471, q=7351<br>n=40217321 | KRYSS AV |
| x=36661763<br>y=31000091 | p=5783, q=6553<br>n=37895999 | KRYSS AV |
| x=36784094<br>y=14173807 | p=6833, q=6823<br>n=46621559 | gcd(x,phi)=2 |
| x=42185665<br>y=31377985 | p=7249, q=6329<br>n=45878921 | p er ikke primtall |

Nye tall? Bruk sjekklisten på side 3. Disse radene er sortert etter x, ikke etter rekkefølgen i prøven.

## Side 8: Svak RSA: finn y og klarteksten

Søk: Bob is using the RSA encryption scheme • weak • private key • unencrypted plain text message • 1349 527 1209

Oppgaven gir offentlig nøkkel (n,x) og kryptert melding M. Du skal finne privat eksponent y og klartekst m.

| Steg | Regel | Eksempel |
| --- | --- | --- |
| 1 | Faktoriser n=p*q i to primtall. | 1349=19*71 |
| 2 | phi=(p−1)*(q−1) | 18*70=1260 |
| 3 | Finn y slik at x*y mod phi=1. | 527*y mod 1260=1 gir y=263. |
| 4 | m=M^y mod n | 1209^263 mod 1349=1148. |

I potens-kalkulatoren: Base=1209, Exponent=263, Modulus=1349. Resultatet 1148 er klarteksten. Ikke bruk x i stedet for y når du dekrypterer.

Privatnøkkelen er (n,y)=(1349,263), men når svarfeltet allerede sier y=, skriver du bare 263.

Sjekk gjerne ved å kryptere tilbake: 1148^527 mod 1349 skal gi 1209. I noen eksempler blir m=M; det er mulig og betyr ikke automatisk regnefeil.

For de kjente tallene kan du slå opp på side 10. For nye tall finner du inversen på neste side.

Se hele Casio-eksemplet med n=2747, x=1933 og M=1076 på side 12. Der brukes «powers mod» både for y og m.

## Side 9: Finn inversen y uten å gjette

Søk: modular inverse • Euclid • extended Euclidean algorithm • x*y=1 mod phi • 527 1260

Målet er x*y+phi*k=1. Da er y inversen til x modulo phi. Først deler du med rest, deretter regner du bakover.

```text
1260 = 2*527 + 206
 527 = 2*206 + 115
 206 = 1*115 + 91
 115 = 1*91 + 24
  91 = 3*24 + 19
  24 = 1*19 + 5
  19 = 3*5 + 4
   5 = 1*4 + 1
```

### Tabellmetoden: behold bare r og t

Start med (r,t)=(phi,0) og (x,1). Hver ny rad: q=heltallsdelen av r_forrige/r_siste, ny r=r_forrige−q*r_siste, ny t=t_forrige−q*t_siste.

| r | t |
| --- | --- |
| 1260 | 0 |
| 527 | 1 |
| 206 | −2 |
| 115 | 5 |
| 91 | −7 |
| 24 | 12 |
| 19 | −43 |
| 5 | 55 |
| 4 | −208 |
| 1 | 263 |

Når r=1, er t inversen. Her y=263. Hvis t er negativ, legg til phi til du får 0<y<phi. Sjekk x*y mod phi=1.

## Side 10: RSA: alle kjente svake nøkler og meldinger

Søk: private key • plain text • 1333 • 2501 • 3139 • 5293 • 3713 • 1121 • 3233 • 1541 • 1121 • 1541 • 3763 • 1349 • 1357 • 1537 • 3337 • 2537

Match n, x OG den krypterte meldingen M. Samme nøkkel kan brukes med flere forskjellige M. y er samme for nøkkelen, men m kan endres.

| n ; x | p ; q ; phi | M → m | y |
| --- | --- | --- | --- |
| 1333 ; 1091 | 31 ; 43 ; 1260 | 739 → 285 | 671 |
| 2501 ; 2023 | 41 ; 61 ; 2400 | 633 → 37 | 1687 |
| 3139 ; 883 | 43 ; 73 ; 3024 | 3121 → 3121 | 1387 |
| 5293 ; 3875 | 67 ; 79 ; 5148 | 4275 → 1708 | 1379 |
| 3713 ; 613 | 47 ; 79 ; 3588 | 3398 → 2055 | 2113 |
| 1121 ; 115 | 19 ; 59 ; 1044 | 575 → 55 | 463 |
| 3233 ; 1969 | 53 ; 61 ; 3120 | 1220 → 1220 | 2689 |
| 1541 ; 475 | 23 ; 67 ; 1452 | 1002 → 1064 | 1183 |
| 1121 ; 115 | 19 ; 59 ; 1044 | 1093 → 925 | 463 |
| 1541 ; 475 | 23 ; 67 ; 1452 | 1227 → 1232 | 1183 |
| 3763 ; 2029 | 53 ; 71 ; 3640 | 2873 → 170 | 2029 |
| 1349 ; 527 | 19 ; 71 ; 1260 | 1209 → 1148 | 263 |
| 1357 ; 277 | 23 ; 59 ; 1276 | 1228 → 49 | 281 |
| 1537 ; 155 | 29 ; 53 ; 1456 | 1496 → 1462 | 883 |
| 3337 ; 1257 | 47 ; 71 ; 3220 | 1096 → 825 | 3033 |
| 2537 ; 1615 | 43 ; 59 ; 2436 | 1791 → 921 | 451 |

Eksempel: n=1121,x=115 gir y=463. M=575 gir m=55, mens M=1093 gir m=925. Ikke kopier m fra feil rad.

## Side 11: Store RSA-tall: bruk modulokalkulatoren

Søk: modular product • modular exponentiation • Factor 1 • Factor 2 • Base • Exponent • Modulus • repeated squaring

I prøvene ligger det kalkulatorer for moduloprodukt og modulopotens. Øvingssiden har de samme to verktøyene. Bruk dem direkte; ikke regn ut en enorm potens først.

| Hva skal finnes? | Verktøy | Feltene |
| --- | --- | --- |
| Er x og y inverse? | Produkt modulo | Factor 1=x<br>Factor 2=y<br>Modulus=(p−1)*(q−1) |
| Dekryptert melding m | Potens modulo | Base=M<br>Exponent=y<br>Modulus=n |
| Krypter tilbake og sjekk | Potens modulo | Base=m<br>Exponent=x<br>Modulus=n |

Mange vanlige kalkulatorer avrunder når x*y har 15–16 sifre. Da kan den avgjørende resten 1 forsvinne. Bruk den eksakte modulokalkulatoren i oppgaven / øvingssiden.

### Hvis du må regne en potens manuelt

Kvadrer med rest i hvert steg: b^1 mod n, b^2 mod n, b^4 mod n, b^8 mod n, osv. Del eksponenten i en sum av 1,2,4,8,… og multipliser de valgte restene, med modulo etter hvert produkt.

```text
Eksempel: 7^13 mod 33
7^1 → 7; 7^2 → 16; 7^4 → 25; 7^8 → 31
13=8+4+1
31*25 mod 33=16
16*7 mod 33=13
```

Svar derfor 13. Oppskriften virker fordi du kan ta resten etter hver multiplikasjon uten å endre sluttresten.

Du kan også bruke potens modulo til å finne y når phi er lett å faktorisere. Se eksemplet på side 12.

## Side 12: Svak RSA på Casio med n=2747

Søk: Bob's RSA key is weak • find the unencrypted message • 2747 • 1933 • 1076 • Casio fx-9860GIII • powers mod

Oppgaven gir (n,x)=(2747,1933) og kryptert melding M=1076. Finn den private eksponenten y i a) og klarteksten m i b). Bruk TABLE på Casioen og «powers mod» i oppgaven.

### 1. Finn faktorene til n med TABLE

Trykk MENU → TABLE. Skriv 2747 ÷ X i Y1 (bruk X,θ,T-knappen), og trykk EXE. Velg F5 (SET) og sett Start=2, End=52, Step=1. 52 er heltallsdelen av √2747. Trykk EXIT → F6 (TABL).

Raden X=41 gir Y1=67. Dermed er 2747=41×67, og phi=(41−1)×(67−1)=2640.

### 2. Finn eksponenten som gir y

Del 2640 helt ned til 1. Når divisjonen går opp, prøv samme primtall på det nye tallet. Når den gir desimaler, behold tallet og prøv neste primtall.

```text
2640 ÷ 2 = 1320 → ÷ 2 = 660 → ÷ 2 = 330 → ÷ 2 = 165
 165 ÷ 3 =   55 → ÷ 5 =  11 → ÷ 11 = 1
```

De ulike primtallene er 2, 3, 5 og 11. Bruk (p−1)/p for hvert av dem. Ta med 2 én gang, selv om det var fire divisjoner med 2.

```text
2640 × (1÷2) × (2÷3) × (4÷5) × (10÷11) = 640
640 − 1 = 639
```

640 er Eulers phi-verdi for 2640. Derfor gir 1933^640 rest 1 modulo 2640. Da gir 1933^639 den private eksponenten y, siden én ekstra gang med 1933 gir rest 1.

### 3. Bruk «powers mod» i oppgaven to ganger

| Det du finner | Base | Exponent | Modulus | Resultat |
| --- | --- | --- | --- | --- |
| a) Privat eksponent y | 1933 | 639 | 2640 | 997 |
| b) Klartekst m | 1076 | 997 | 2747 | 2314 |

Skriv 997 i feltet y og 2314 i feltet m. Resultatet fra a) blir eksponenten i b). Bruk phi=2640 som modulus i a) og n=2747 i b).

Med andre tall kan du bruke denne metoden når phi er lett å faktorisere. Euklid-tabellen på side 9 finner y direkte fra x og phi.

## Side 13: Hamming-avstand: tell ulike posisjoner

Søk: Compute the minimal and maximal Hamming distance • bitstrings • lmin • lmax • minimum maximum

Avstanden mellom to strenger er antall plasser der bitene er forskjellige. Ikke tolk strengene som vanlige heltall.

```text
000111
000011
   ↑
Bare posisjon 4 er ulik: avstanden er 1.
```

Kall de fire strengene A,B,C,D. Du trenger bare seks sammenligninger: AB, AC, AD, BC, BD, CD.

| Par i eksemplet | Avstand |
| --- | --- |
| A=000111, B=000011 | 1 |
| A=000111, C=100101 | 2 |
| A=000111, D=010011 | 2 |
| B=000011, C=100101 | 3 |
| B=000011, D=010011 | 1 |
| C=100101, D=010011 | 4 |

l_min=1 og l_max=4. Se over ALLE seks par før du velger maksimum. Ikke ta med AA,BB,CC,DD: de ville alltid gitt 0.

Med XOR: like bit gir 0, ulike bit gir 1. Antall 1-ere i XOR-resultatet er avstanden. Behold ledende nuller.

## Side 14: Hamming: kjente tallsett 1

Søk: Hamming • 001011 • 000110 • 001111 • 110101 • 000111 • 111110 • 101010 • 000100 • 000010 • 001010

| De fire strengene (A,B,C,D) | AB AC AD BC BD CD | min ; max |
| --- | --- | --- |
| 001011<br>110000<br>000010<br>000111 | 5 2 2 3 5 2 | 2 ; 5 |
| 000110<br>000101<br>000000<br>101010 | 2 2 3 2 5 3 | 2 ; 5 |
| 001111<br>111111<br>000101<br>001000 | 2 2 3 4 5 3 | 2 ; 5 |
| 110101<br>010101<br>001110<br>001100 | 1 5 4 4 3 1 | 1 ; 5 |
| 000111<br>000011<br>100101<br>010011 | 1 2 2 3 1 4 | 1 ; 4 |
| 111110<br>110111<br>110100<br>100101 | 2 2 4 2 2 2 | 2 ; 4 |
| 101010<br>011001<br>001001<br>100100 | 4 3 3 1 5 4 | 1 ; 5 |
| 000100<br>001010<br>011010<br>001000 | 3 4 2 1 1 2 | 1 ; 4 |
| 000010<br>010000<br>001001<br>000100 | 2 3 2 3 2 3 | 2 ; 3 |
| 001010<br>110010<br>110000<br>010001 | 3 4 4 1 3 2 | 1 ; 4 |

Strengenes rekkefølge kan være endret. Minste og største avstand er likevel den samme for samme sett.

## Side 15: Hamming: kjente tallsett 2

Søk: Hamming • 110010

| De fire strengene (A,B,C,D) | AB AC AD BC BD CD | min ; max |
| --- | --- | --- |
| 110010<br>011110<br>001001<br>000000 | 3 5 3 4 4 2 | 2 ; 5 |

Strengenes rekkefølge kan være endret. Minste og største avstand er likevel den samme for samme sett.

Ekstra fra T41: [001010,110010,110000,010001] gir AB,AC,AD,BC,BD,CD = 3,4,4,1,3,2. Min=1, max=4.

## Side 16: Bitfeil: velg riktig sannsynlighetsformel

Søk: noisy binary symmetric channel • probability • no errors • at most 1 2 3 bit errors • receiving • rounded off

p er feilrisiko per bit, n er antall bit. Bitfeilene er uavhengige. Skriv q=1−p. I kildene er n=7.

| Oppgaven spør om | Regn ut |
| --- | --- |
| no errors | q^n |
| exactly 1 bit error | n*p*q^(n−1) |
| at most 1 bit error | q^n+n*p*q^(n−1) |
| at most 2 bit errors | q^n+n*p*q^(n−1)+n*(n−1)/2*p^2*q^(n−2) |
| at most 3 bit errors | Samme som høyst 2, pluss n*(n−1)*(n−2)/6*p^3*q^(n−3) |
| transmitting w and receiving en bestemt r | p^d*q^(n−d), der d er Hamming-avstanden mellom w og r. |

«At most» = høyst: inkluder 0 feil. «Receiving r» = akkurat denne strengen: IKKE gang med n eller en binomialkoeffisient.

For n=7 er faktorene for akkurat 0,1,2,3 feil: 1,7,21,35. Eksempel høyst 3: q^7+7*p*q^6+21*p^2*q^5+35*p^3*q^4.

Regn med alle desimaler underveis. Rund bare hvert ferdige svar til tre desimaler. 0.010 kan skrives 0.01, og 1.000 kan være et riktig avrundet svar selv om den eksakte sannsynligheten er litt mindre enn 1.

## Side 17: Bitfeil: et helt gjennomregnet eksempel

Søk: p=0.069 • 1000111 • 1000010 • at most 2 • specific received string

```text
p=0.069, q=0.931, n=7
w=1000111
r=1000010
```

w og r er ulike på to plasser, så d=2.

| Del | Skriv dette i kalkulatoren | Tre desimaler |
| --- | --- | --- |
| a) Ingen feil | (1−0.069)^7 | 0.606 |
| b) Høyst 2 feil | (1−0.069)^7 + 7*0.069*(1−0.069)^6 + 21*0.069^2*(1−0.069)^5 | 0.991 |
| c) Akkurat r | 0.069^2*(1−0.069)^5 | 0.003 |

I c finnes det bare én bestemt feilplassering som gjør 1000111 til 1000010. I «akkurat 2 feil hvor som helst» finnes det 21 feilplasseringer. Derfor er dette to forskjellige spørsmål.

Hvis b i stedet sier «at most 1», fjern leddet med 21. Hvis b sier «at most 3», ta også med 35*p^3*(1−p)^4.

Den gamle prøven viser et studentinnsendt svar 0.03 på c. Det er ikke fasit. Riktig avrundet svar er 0.003.

## Side 18: Bitfeil: alle kjente oppsett og svar

Søk: no errors • at most • probability • 0.069 • 0.074 • 0.149 • 0.148 • 0.077 • 0.113 • 0.091 • 0.078 • 0.074 • 0.097 • 0.116 • 0.051 • 0.052

Svarrekkefølge: a=ingen feil, b=høyst k feil, c=akkurat den mottatte strengen r. Match p, w, r OG k.

| p ; k | w → r | d | a ; b ; c |
| --- | --- | --- | --- |
| 0.069 ; 2 | 1000111 →<br>1000010 | 2 | 0.606 ; 0.991 ; 0.003 |
| 0.074 ; 1 | 1110101 →<br>1100100 | 2 | 0.584 ; 0.910 ; 0.004 |
| 0.149 ; 1 | 1111001 →<br>1111010 | 2 | 0.323 ; 0.719 ; 0.010 |
| 0.148 ; 2 | 1101110 →<br>1111111 | 2 | 0.326 ; 0.929 ; 0.010 |
| 0.077 ; 1 | 1111111 →<br>1011101 | 2 | 0.571 ; 0.904 ; 0.004 |
| 0.113 ; 1 | 0000010 →<br>0000001 | 2 | 0.432 ; 0.817 ; 0.007 |
| 0.091 ; 1 | 0010110 →<br>1000110 | 2 | 0.513 ; 0.872 ; 0.005 |
| 0.078 ; 2 | 0011110 →<br>1001110 | 2 | 0.566 ; 0.987 ; 0.004 |
| 0.074 ; 2 | 1010000 →<br>0010001 | 2 | 0.584 ; 0.989 ; 0.004 |
| 0.097 ; 2 | 0000101 →<br>0000000 | 2 | 0.490 ; 0.976 ; 0.006 |
| 0.116 ; 1 | 0010101 →<br>0011100 | 2 | 0.422 ; 0.809 ; 0.007 |
| 0.051 ; 2 | 1011010 →<br>1000010 | 2 | 0.693 ; 0.996 ; 0.002 |
| 0.052 ; 3 | 0110101 →<br>1110001 | 2 | 0.688 ; 1.000 ; 0.002 |

«At most 3» ved p=0.052 gir 1.000 etter avrunding. Det betyr ikke at den eksakte sannsynligheten er 1.

## Side 19: Lag G: send 100, 010 og 001 gjennom regelen

Søk: Find the generator matrix • encoding function • E(w1w2w3) • generator matrix G

Alle kodereglene her bruker tre meldingsbit og to kontrollbit: E(w1w2w3)=w1w2w3w4w5. Regn kontrollbitene modulo 2.

| Regneregel | Svar |
| --- | --- |
| 0+0 | 0 |
| 0+1 eller 1+0 | 1 |
| 1+1 | 0 |
| 1+1+1 | 1 |

Eksempel: w4=w1+w2, w5=w2+w3. Finn de tre radene slik:

| Input | w4 | w5 | Hele kodeordet = rad i G |
| --- | --- | --- | --- |
| 100 | 1+0=1 | 0+0=0 | 10010 |
| 010 | 0+1=1 | 1+0=1 | 01011 |
| 001 | 0+0=0 | 0+1=1 | 00101 |

```text
G =
1 0 0 1 0
0 1 0 1 1
0 0 1 0 1
```

Skriv ALLE tre radene og ALLE fem kolonnene. De tre første kolonnene er identitetsmatrisen. De to siste er kontrollbitene.

Hvis w4=0, blir hele kontrollkolonne 4 null. Hvis en melding påvirker begge kontrollbitene, får den raden to 1-ere til høyre.

## Side 20: Lag H fra G: snu kontrollblokken

Søk: Find the parity check matrix • H • G=(I|P) • H=(P transpose|I) • binary field F2

G har en identitetsblokk til venstre. Kall resten P. H får kontrollblokken P snudd fra rader til kolonner, og en ny identitetsblokk til høyre.

```text
G = [ I3 | P ]          P =
1 0 0 | 1 0            1 0
0 1 0 | 1 1            1 1
0 0 1 | 0 1            0 1

H = [ P^T | I2 ] =
1 1 0 | 1 0
0 1 1 | 0 1
```

### Enda enklere: les kontrollreglene direkte

w4=w1+w2 gir w1+w2+w4=0. Sett 1 på posisjon 1,2,4. Det gir første H-rad 1 1 0 1 0.
w5=w2+w3 gir w2+w3+w5=0. Sett 1 på posisjon 2,3,5. Det gir andre H-rad 0 1 1 0 1.

Bruk kontrollbitene i oppgitt rekkefølge: først w4, så w5. Dette gir den vanlige H-matrisen og samme rekkefølge på syndrombitene som i oppslagene.

Kontroll: hver rad i G skal gi syndrom 00 med H. Ellers er H feil. I F2 er minus det samme som pluss, så det trengs ingen minustegn.

## Side 21: Syndrom: én kontrollsum per rad i H

Søk: Compute the syndrome • received message • syndrome of r • H*r transpose • 11010

Hvis H har identitetsmatrisen til høyre, kan du sammenligne kontrollbitene direkte. Regn ut hva de skal være fra starten av r. Skriv 1 for ulikt par og 0 for likt par. Se side 22.

```text
H =
1 1 0 1 0
0 1 1 0 1
r = 11010
```

Første rad bruker posisjon 1,2,4. Andre rad bruker posisjon 2,3,5. Tell 1-ere på disse posisjonene, og ta resten ved deling på 2.

| Syndrombit | Utregning | Rest modulo 2 |
| --- | --- | --- |
| s1=r1+r2+r4 | 1+1+1=3 | 1 |
| s2=r2+r3+r5 | 1+0+0=1 | 1 |

Syndromet er 11. Skriv 11 uten mellomrom eller klammer. To H-rader gir to syndrombit; fire H-rader gir fire bit.

00 betyr at r er et kodeord. Det beviser ikke at overføringen var feilfri: enkelte feil kan gjøre ett kodeord til et annet kodeord.

Bruk den H-matrisen du faktisk har valgt. Bytter du om H-radene, byttes også syndrombitene. I øvingssiden kan en annen gyldig H brukes i matriseoppgaven; syndromet rettes da mot den H-en du skrev.

## Side 22: G, H og syndrom med 5 bit

Søk: Find the generator matrix • parity check matrix • syndrome • 10111 • skal være • w4=w3+w1 • w5=w2+w1

Du har tre meldingsbit og to kontrollbit. Les kodeordet som melding | kontroll. Her er reglene w4=w3+w1 og w5=w2+w1. Husk at 1+1=0.

### a) G fyller inn de to siste bitene

| Første tre bit | Regn ut de to siste | Rad i G |
| --- | --- | --- |
| 100 | Bit 1 brukes i begge reglene → 11 | 1 0 0 1 1 |
| 010 | Bit 2 brukes bare for w5 → 01 | 0 1 0 0 1 |
| 001 | Bit 3 brukes bare for w4 → 10 | 0 0 1 1 0 |

### b) H markerer plassene som skal sjekkes

Ta med bitene på begge sider av likhetstegnet. I regelen w4=w3+w1 er det plass 1, 3 og 4. Sett 1 på de plassene i første H-rad og 0 på resten. I regelen w5=w2+w1 bruker du plass 1, 2 og 5 i andre rad.

```text
H =
1 0 1 1 0
1 1 0 0 1
```

### c) Sammenlign kontrollbitene

Du fikk r=101 | 11. Bruk starten 101 i reglene. Da skal bit 4 være 1+1=0, og bit 5 skal være 0+1=1. Sammenlign 01 med de to kontrollbitene du fikk.

| Kontrollbit | Skal være | Du fikk | Syndrombit |
| --- | --- | --- | --- |
| Bit 4 | 0 | 1 | 1 (ulike) |
| Bit 5 | 1 | 1 | 0 (like) |

Skriv syndromet 10. Ulike kontrollbit gir 1, og like kontrollbit gir 0. For denne H-en gir sammenligningen samme resultat som H·rᵀ.

## Side 23: G, H og syndrom: oppslag 1

Søk: generator matrix • parity check matrix • 11101 • 11010 • 00010

Match både kontrollreglene og r. H står med kontrollbitene i vanlig rekkefølge. Skriv matrisene med mellomrom mellom bitene.

### T02 · w4=w1+w3; w5=w3

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 0<br>0 1 0 0 0<br>0 0 1 1 1 | 1 0 1 1 0<br>0 0 1 0 1 | 11101 → 00 |

### T09 · w4=w1+w2; w5=w2+w3

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 0<br>0 1 0 1 1<br>0 0 1 0 1 | 1 1 0 1 0<br>0 1 1 0 1 | 11010 → 11 |

### T10 · w4=w1+w2+w3; w5=0

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 0<br>0 1 0 1 0<br>0 0 1 1 0 | 1 1 1 1 0<br>0 0 0 0 1 | 00010 → 10 |

## Side 24: G, H og syndrom: oppslag 2

Søk: generator matrix • parity check matrix • 11001 • 01111 • 01110

Match både kontrollreglene og r. H står med kontrollbitene i vanlig rekkefølge. Skriv matrisene med mellomrom mellom bitene.

### T12 · w4=w3; w5=w1+w2

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 0 1<br>0 1 0 0 1<br>0 0 1 1 0 | 0 0 1 1 0<br>1 1 0 0 1 | 11001 → 01 |

### T13 · w4=w2+w3; w5=w2

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 0 0<br>0 1 0 1 1<br>0 0 1 1 0 | 0 1 1 1 0<br>0 1 0 0 1 | 01111 → 10 |

### T14, T15 · w4=w1+w2+w3; w5=w1

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 1<br>0 1 0 1 0<br>0 0 1 1 0 | 1 1 1 1 0<br>1 0 0 0 1 | 01110 → 10 |

## Side 25: G, H og syndrom: oppslag 3

Søk: generator matrix • parity check matrix • 10010 • 01101 • 01001

Match både kontrollreglene og r. H står med kontrollbitene i vanlig rekkefølge. Skriv matrisene med mellomrom mellom bitene.

### T17 · w4=w1+w2; w5=w1+w3

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 1<br>0 1 0 1 0<br>0 0 1 0 1 | 1 1 0 1 0<br>1 0 1 0 1 | 10010 → 01 |

### T18 · w4=w1+w3; w5=w2

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 0<br>0 1 0 0 1<br>0 0 1 1 0 | 1 0 1 1 0<br>0 1 0 0 1 | 01101 → 10 |

### T20 · w4=0; w5=w2

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 0 0<br>0 1 0 0 1<br>0 0 1 0 0 | 0 0 0 1 0<br>0 1 0 0 1 | 01001 → 00 |

## Side 26: G, H og syndrom: oppslag 4

Søk: generator matrix • parity check matrix • 01011 • 01000

Match både kontrollreglene og r. H står med kontrollbitene i vanlig rekkefølge. Skriv matrisene med mellomrom mellom bitene.

### T26 · w4=w1+w3; w5=w1+w2+w3

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 1 1<br>0 1 0 0 1<br>0 0 1 1 1 | 1 0 1 1 0<br>1 1 1 0 1 | 01011 → 10 |

### T33 · w4=w3; w5=w1+w2

| G (3 rader) | H (2 rader) | r → syndrom |
| --- | --- | --- |
| 1 0 0 0 1<br>0 1 0 0 1<br>0 0 1 1 0 | 0 0 1 1 0<br>1 1 0 0 1 | 01000 → 01 |

## Side 27: Minimum distance, detect og kodeord

Søk: Compute the minimum distance • codewords not equal • maximum number always able to detect • non-zero codeword • not a codeword

For en lineær kode er minsteavstanden den minste vekten til et ikke-null kodeord. Vekt betyr antall 1-ere. Lag alle åtte kodeordene fra G.

```text
Eksempel G:
1 0 0 1 1
0 1 0 1 0
0 0 1 1 0
```

| Melding | Kodeord | Vekt |
| --- | --- | --- |
| 000 | 00000 | 0 – utelates |
| 001 | 00110 | 2 |
| 010 | 01010 | 2 |
| 011 | 01100 | 2 |
| 100 | 10011 | 3 |
| 101 | 10101 | 3 |
| 110 | 11001 | 3 |
| 111 | 11111 | 5 |

Minimum distance = 2. Always detect = 2−1 = 1. Always correct = floor((2−1)/2) = 0. Les hvilket av disse tre tallene oppgaven ber om.

Et non-zero codeword: velg en rad i G, for eksempel 10011. Et not-a-codeword: velg en 5-bitstreng som ikke finnes i tabellen, for eksempel 00001. 00000 er ALLTID et kodeord.

Ikke ta bare minste radvekt uten å sjekke XOR-kombinasjonene: to rader kan sammen gi et lettere kodeord. For systematisk G finnes en rask test for et foreslått kodeord: bruk de første tre bitene som melding, og sjekk om reglene gir de siste to.

## Side 28: Kodeavstand og deteksjon: oppslag 1

Søk: minimum distance • detect • non-zero • T01 • T04 • T05 • T06 • T07

Finn G-radene, eller lag G fra kontrollreglene. «Kodeord» og «ikke kodeord» er ett gyldig eksempel; flere svar kan være riktige.

| G-radene | d_min ; detect | Kodeord ≠ 0 | Ikke kodeord |
| --- | --- | --- | --- |
| 10010<br>01001<br>00101 | 2 ; 1 | 00101 | 00001 |
| 10010<br>01010<br>00111 | 2 ; 1 | 00111 | 00001 |
| 10011<br>01010<br>00100 | 1 ; 0 | 00100 | 00001 |
| 10011<br>01001<br>00110 | 2 ; 1 | 00110 | 00001 |
| 10000<br>01010<br>00100 | 1 ; 0 | 00100 | 00001 |

Hvis d_min=1, er «always detect» 0. Det betyr at noen enkeltbitfeil kan gå uoppdaget. 0 er da svaret, selv om koden kan oppdage andre feil.

## Side 29: Kodeavstand og deteksjon: oppslag 2

Søk: minimum distance • detect • non-zero • T11 • T16 • T19 • T21 • T22

Finn G-radene, eller lag G fra kontrollreglene. «Kodeord» og «ikke kodeord» er ett gyldig eksempel; flere svar kan være riktige.

| G-radene | d_min ; detect | Kodeord ≠ 0 | Ikke kodeord |
| --- | --- | --- | --- |
| 10001<br>01000<br>00111 | 1 ; 0 | 00111 | 00001 |
| 10000<br>01011<br>00110 | 1 ; 0 | 00110 | 00001 |
| 10011<br>01010<br>00110 | 2 ; 1 | 00110 | 00001 |
| 10000<br>01001<br>00111 | 1 ; 0 | 00111 | 00001 |
| 10011<br>01011<br>00101 | 2 ; 1 | 00101 | 00001 |

Hvis d_min=1, er «always detect» 0. Det betyr at noen enkeltbitfeil kan gå uoppdaget. 0 er da svaret, selv om koden kan oppdage andre feil.

## Side 30: Kodeavstand og deteksjon: oppslag 3

Søk: minimum distance • detect • non-zero • T25 • T31

Finn G-radene, eller lag G fra kontrollreglene. «Kodeord» og «ikke kodeord» er ett gyldig eksempel; flere svar kan være riktige.

| G-radene | d_min ; detect | Kodeord ≠ 0 | Ikke kodeord |
| --- | --- | --- | --- |
| 10011<br>01001<br>00100 | 1 ; 0 | 00100 | 00001 |
| 10010<br>01010<br>00110 | 2 ; 1 | 00110 | 00001 |

Hvis d_min=1, er «always detect» 0. Det betyr at noen enkeltbitfeil kan gå uoppdaget. 0 er da svaret, selv om koden kan oppdage andre feil.

## Side 31: Dekoding med 8 bit: finn feilposisjonen

Søk: We use the generator matrix • Compute the error pattern • encoded message • r=c+e • syndrome decoding

Her har G fire rader og åtte kolonner. Første fire kolonner er I4. Skriv H=(P^T|I4), akkurat som for 5-bit-kodene.

| Steg | Det du gjør |
| --- | --- |
| 1 | Les de fire siste G-kolonnene som kontrollregler, og bruk dem til å lage H. |
| 2 | Beregn kontrollbitene fra de fire første bitene i r. Sammenlign med de fire siste i r. Ulik gir 1, lik gir 0. Dette er syndromet. |
| 3 | Les hver KOLONNE i H ovenfra og ned. Finn kolonnen som er lik syndromet. |
| 4 | Hvis det er kolonne j, sett en 1-er på posisjon j i en ellers null 8-bitstreng. Dette er feilmønster e. |
| 5 | Korriger ved å flippe bit j i r. Resultatet er kodeord c=r XOR e. |
| 6 | Sjekk H*c^T=0000. Hvis det ikke stemmer, er c feil. |

Syndrom 0010 betyr ikke automatisk «feil på plass 3». Du må finne hvilken H-kolonne som er 0010. Kolonnen kan stå hvor som helst.

Metoden gir entydig enkeltbitkorrigering når syndromet matcher én unik, ikke-null kolonne. Alle 8-bit-eksemplene i prøvemappen har slik en unik nærmeste løsning med én feil.

Ved andre matriser kan like kolonner gi flere muligheter. Hvis ingen kolonne matcher syndromet, kan det være flere bitfeil; da må du sammenligne avstanden til kodeordene. Ikke gjett en feilposisjon.

Se hele sammenligningen «skal være» og «du fikk» med r=10110001 på side 33.

## Side 32: Dekoding: se hele eksemplet

Søk: 01100111 • 01100011 • syndrome 0100 • error pattern 00000100

| G | H |
| --- | --- |
| 1 0 0 0 1 0 0 1<br>0 1 0 0 1 1 0 1<br>0 0 1 0 1 1 1 0<br>0 0 0 1 1 0 1 1 | 1 1 1 1 1 0 0 0<br>0 1 1 0 0 1 0 0<br>0 0 1 1 0 0 1 0<br>1 1 0 1 0 0 0 1 |

```text
r=01100111
s1=r1+r2+r3+r4+r5 = 0+1+1+0+0 = 0 mod 2
s2=r2+r3+r6       = 1+1+1     = 1 mod 2
s3=r3+r4+r7       = 1+0+1     = 0 mod 2
s4=r1+r2+r4+r8    = 0+1+0+1   = 0 mod 2
s=0100
```

Kolonne 6 i H er 0100. Derfor er bit nummer 6 feil. Feilmønsteret har åtte bit og en 1-er på plass 6.

```text
e=00000100
r=01100111
c=01100011
```

Svar a) 0100, b) 00000100, c) 01100011. c er hele det korrigerte kodeordet, ikke bare de fire opprinnelige meldingsbitene.

Ønsker oppgaven også selve meldingen w, kan du lese de første fire bitene av c når G er systematisk: her w=0110.

## Side 33: Rett én bit i 10110001

Søk: We use the generator matrix • Compute the syndrome • error pattern • encoded message • 10110001 • 1010 • 00100000 • 10010001

Du får G og r=10110001. Del r i fire meldingsbit og fire kontrollbit: 1011 | 0001. I denne oppgaven finner du den ene biten som må flippes.

```text
G =
1 0 0 0 | 0 1 1 1
0 1 0 0 | 1 1 1 0
0 0 1 0 | 1 0 1 0
0 0 0 1 | 0 1 1 0
```

### a) Finn hva kontrollbitene skal være

Les kolonne 5, 6, 7 og 8 i G, ovenfra og ned. En 1-er på rad 2 betyr at du bruker meldingsbit 2. Sett inn de fire første bitene fra r, altså 1, 0, 1 og 1.

| Kolonne i G | Regel | Skal være | Du fikk | Syndrombit |
| --- | --- | --- | --- | --- |
| 5 → 0110 | w5=w2+w3 | 0+1=1 | 0 | 1 |
| 6 → 1101 | w6=w1+w2+w4 | 1+0+1=0 | 0 | 0 |
| 7 → 1111 | w7=w1+w2+w3+w4 | 1+0+1+1=1 | 0 | 1 |
| 8 → 1000 | w8=w1 | 1 | 1 | 0 |

Skal være 1011. Du fikk 0001. Skriv 1 for ulikt par og 0 for likt par. Syndromet blir 1010.

### b) Finn kolonnen i H som matcher syndromet

Legg de fire G-kolonnene fra tabellen som rader til venstre i H. Til høyre legger du identitetsmatrisen med én 1-er på diagonalen i hver rad.

```text
H =
0 1 1 0 | 1 0 0 0
1 1 0 1 | 0 1 0 0
1 1 1 1 | 0 0 1 0
1 0 0 0 | 0 0 0 1
```

Les H loddrett. Kolonne 3 er 1, 0, 1, 0, som matcher syndromet. Sett 1 på plass 3 i en streng med åtte bit. Da får du e=00100000.

### c) Flipp den tredje biten i r

Bit 3 i 10110001 er 1. Bytt den til 0 og behold de andre bitene. Da får du c=10010001. En rask sjekk er å bruke 1001 i kontrollreglene. De gir 0001, som er de fire siste bitene i c.

Svar a) 1010, b) 00100000, c) 10010001. Syndromet har fire bit. Feilmønsteret og kodeordet har åtte.

## Side 34: 8-bit-matriser: D-oppslag 1

Søk: generator matrix • D1 • D2

Først finn D-nummeret ved å matche ALLE radene i G. Gå deretter til svaretabellen på side 37.

### D1

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 1 0 1 1<br>0 1 0 0 1 0 0 1<br>0 0 1 0 0 1 0 1<br>0 0 0 1 0 0 1 1 | 1 1 0 0 1 0 0 0<br>0 0 1 0 0 1 0 0<br>1 0 0 1 0 0 1 0<br>1 1 1 1 0 0 0 1 |

H-kolonner 1–8: 1011 ; 1001 ; 0101 ; 0011 ; 1000 ; 0100 ; 0010 ; 0001

### D2

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 1 0 0 1<br>0 1 0 0 1 1 1 0<br>0 0 1 0 1 0 1 1<br>0 0 0 1 1 1 0 1 | 1 1 1 1 1 0 0 0<br>0 1 0 1 0 1 0 0<br>0 1 1 0 0 0 1 0<br>1 0 1 1 0 0 0 1 |

H-kolonner 1–8: 1001 ; 1110 ; 1011 ; 1101 ; 1000 ; 0100 ; 0010 ; 0001

## Side 35: 8-bit-matriser: D-oppslag 2

Søk: generator matrix • D3 • D4

Først finn D-nummeret ved å matche ALLE radene i G. Gå deretter til svaretabellen på side 37.

### D3

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 1 0 0 1<br>0 1 0 0 1 1 0 1<br>0 0 1 0 1 1 1 0<br>0 0 0 1 1 0 1 1 | 1 1 1 1 1 0 0 0<br>0 1 1 0 0 1 0 0<br>0 0 1 1 0 0 1 0<br>1 1 0 1 0 0 0 1 |

H-kolonner 1–8: 1001 ; 1101 ; 1110 ; 1011 ; 1000 ; 0100 ; 0010 ; 0001

### D4

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 0 1 0 1<br>0 1 0 0 1 0 1 1<br>0 0 1 0 1 0 0 1<br>0 0 0 1 1 1 1 0 | 0 1 1 1 1 0 0 0<br>1 0 0 1 0 1 0 0<br>0 1 0 1 0 0 1 0<br>1 1 1 0 0 0 0 1 |

H-kolonner 1–8: 0101 ; 1011 ; 1001 ; 1110 ; 1000 ; 0100 ; 0010 ; 0001

## Side 36: 8-bit-matriser: D-oppslag 3

Søk: generator matrix • D5 • D6

Først finn D-nummeret ved å matche ALLE radene i G. Gå deretter til svaretabellen på side 37.

### D5

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 1 0 0 1<br>0 1 0 0 1 0 1 1<br>0 0 1 0 1 1 0 1<br>0 0 0 1 0 0 1 1 | 1 1 1 0 1 0 0 0<br>0 0 1 0 0 1 0 0<br>0 1 0 1 0 0 1 0<br>1 1 1 1 0 0 0 1 |

H-kolonner 1–8: 1001 ; 1011 ; 1101 ; 0011 ; 1000 ; 0100 ; 0010 ; 0001

### D6

| G (4 × 8) | H (4 × 8) |
| --- | --- |
| 1 0 0 0 0 0 1 1<br>0 1 0 0 1 0 1 1<br>0 0 1 0 1 1 0 1<br>0 0 0 1 1 1 1 0 | 0 1 1 1 1 0 0 0<br>0 0 1 1 0 1 0 0<br>1 1 0 1 0 0 1 0<br>1 1 1 0 0 0 0 1 |

H-kolonner 1–8: 0011 ; 1011 ; 1101 ; 1110 ; 1000 ; 0100 ; 0010 ; 0001

## Side 37: 8-bit-dekoding: alle kjente svar

Søk: error pattern • encoded message • 10011010 • 11111111 • 01100111 • 01000010 • 10110101 • 11010110 • 01010110 • 10000100

D1, D2, … er G-matrisene på de foregående sidene. Match både matrisen og den mottatte strengen r. Bruk oppgitt H-rekkefølge for syndromet.

| G | r | Syndrom | Feilmønster e | Kodeord c |
| --- | --- | --- | --- | --- |
| D1 | 10011010 | 0010 | 00000010 | 10011000 |
| D2 | 11111111 | 1110 | 01000000 | 10111111 |
| D3 | 01100111 | 0100 | 00000100 | 01100011 |
| D4 | 01000010 | 1001 | 00100000 | 01100010 |
| D5 | 10110101 | 0010 | 00000010 | 10110111 |
| D3 | 11010110 | 1001 | 10000000 | 01010110 |
| D6 | 01010110 | 0011 | 10000000 | 11010110 |
| D2 | 10000100 | 1101 | 00010000 | 10010100 |

De tidligere notatene om r=11010110 inneholder feil i H/syndrom. Med G som starter med rad 10001001 og deretter 01001101,00101110,00011011, er riktig syndrom 1001, e=10000000 og c=01010110.

Hvis oppgaven endrer rekkefølgen på H-radene, endres syndromet tilsvarende. Feilposisjonen og det korrigerte kodeordet er likevel de samme.

## Side 38: Svarformat og egenkontroll

Søk: syntax guide • bitstrings • matrices • rounded off • None of the above

| Felt | Riktig form | Vanlig feil |
| --- | --- | --- |
| RSA y / m | 263 / 1148 | Bytter y og x, eller bruker phi som modul for klartekst. |
| Sannsynlighet | 0.003 | 0.03 har ti ganger for stor verdi. |
| G | Tre rader, fem tall per rad | Mangler en rad eller kontrollkolonne. |
| H i 5-bitoppgave | To rader, fem tall per rad | Kopierer P uten å transponere / uten I2. |
| Syndrom i 5-bitoppgave | 00,01,10 eller 11 | Skriver bare 0 eller 1 og mister en bit. |
| Syndrom i 8-bitoppgave | Fire bit, f.eks. 0010 | Tolker syndromet som feilplassnummer. |
| Feilmønster i 8-bitoppgave | Åtte bit, f.eks. 00000010 | Skriver «7» eller bare fire bit. |
| Korrigert kodeord | Åtte bit | Skriver bare fire meldingsbit. |

### Kontrollregler som avdekker regnefeil

RSA: x*y mod phi=1 og m^x mod n=M.
Hamming: 0≤min≤max≤strenglengden, og ulike strenger har avstand >0.
Kode: H*g^T=0 for hver rad g i G.
Dekoding: r XOR e=c, og H*c^T=0.

Øvingssiden viser hva svaret tolkes som mens du skriver. En forhåndsvisning betyr at formatet kan leses; riktig/feil vises først når du leverer.

## Side 39: Kildesjekk: prøvefiler 1

Søk: coverage • Delprove_4 • T01 • T02 • T03 • T04 • T05 • T06 • T07 • T08 • T09 • T10 • T11 • T12

Alle de tre regneoppgavene er dekket. Fullprøvemodus i HTML velger én oppgave fra hver kolonne; «Kildeprøve Txx» bruker de konkrete tallene fra den filen.

| Kildefil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| T01<br>2av3/1.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | Feildeteksjon<br>side 27 |
| T02<br>2av3/3.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | G, H og syndrom<br>side 19 |
| T03<br>2av3/4.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |
| T04<br>2av3/5.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T05<br>2av3/6.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | Feildeteksjon<br>side 27 |
| T06<br>2av3/7.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | Kodeavstand<br>side 27 |
| T07<br>2av3/8.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | Feildeteksjon<br>side 27 |
| T08<br>2av3/9.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | 8-bit-dekoding<br>side 31 |
| T09<br>3av3/1.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T10<br>3av3/10.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T11<br>3av3/11.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T12<br>3av3/12.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |

## Side 40: Kildesjekk: prøvefiler 2

Søk: coverage • Delprove_4 • T13 • T14 • T15 • T16 • T17 • T18 • T19 • T20 • T21 • T22 • T23 • T24

Alle de tre regneoppgavene er dekket. Fullprøvemodus i HTML velger én oppgave fra hver kolonne; «Kildeprøve Txx» bruker de konkrete tallene fra den filen.

| Kildefil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| T13<br>3av3/13.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T14<br>3av3/14.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T15 (kopi av T14)<br>3av3/15.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T16<br>3av3/16.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T17<br>3av3/17.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T18<br>3av3/18.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | G, H og syndrom<br>side 19 |
| T19<br>3av3/19.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | Kodeavstand<br>side 27 |
| T20<br>3av3/2.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T21<br>3av3/3.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | Feildeteksjon<br>side 27 |
| T22<br>3av3/4.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T23<br>3av3/5.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | 8-bit-dekoding<br>side 31 |
| T24<br>3av3/6.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |

## Side 41: Kildesjekk: prøvefiler 3

Søk: coverage • Delprove_4 • T25 • T26 • T27 • T28 • T29 • T30 • T31 • T32 • T33 • T34 • T35 • T36

Alle de tre regneoppgavene er dekket. Fullprøvemodus i HTML velger én oppgave fra hver kolonne; «Kildeprøve Txx» bruker de konkrete tallene fra den filen.

| Kildefil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| T25<br>3av3/9.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T26<br>diverse_scores/1.pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T27<br>diverse_scores/2.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |
| T28<br>diverse_scores/3.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |
| T29<br>diverse_scores/4.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | 8-bit-dekoding<br>side 31 |
| T30<br>diverse_scores/5.pdf | RSA-flervalg<br>side 3 | Bitfeil<br>side 16 | Kodeavstand<br>side 27 |
| T31<br>diverse_scores/6.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | Kodeavstand<br>side 27 |
| T32<br>diverse_scores/7.pdf | Svak RSA<br>side 10 | Bitfeil<br>side 16 | 8-bit-dekoding<br>side 31 |
| T33<br>diverse_scores/8.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | G, H og syndrom<br>side 19 |
| T34 (kopi av T28)<br>diverse_scores/9.pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |
| T35 (kopi av T28)<br>regler/Test 4 (1).pdf | Svak RSA<br>side 10 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |
| T36 (kopi av T24)<br>regler/Test 4 (topics 10-12_ Applications of Lagrange's theorem,Coding theory,Coding theory and group codes)_ Attempt review (1).pdf | RSA-flervalg<br>side 3 | Hamming<br>side 13 | 8-bit-dekoding<br>side 31 |

## Side 42: Kildesjekk: notater og rettelser

Søk: source notes • RSA • Hamming • parity check • wrong H • 11010110

| Notat | Innhold og kontroll |
| --- | --- |
| T37 · regler/diskre_prøve_4_oppg_1 (1).pdf | Svak RSA n=3139,x=883,M=3121. Regnet på nytt: y=1387,m=3121. |
| T38 og kopi T39 · oppg_1 (2) | Svak RSA n=1349,x=527,M=1209. Regnet på nytt: y=263,m=1148. |
| T40 · oppg_1.pdf | RSA-validering. Tallalternativene finnes i RSA-oppslaget. |
| T41 · oppg_2.pdf | Hamming for 001010,110010,110000,010001. Avstander 3,4,4,1,3,2 gir min=1,max=4. |
| T42 · oppg_3 (2).pdf | G-rader 10001,00011,01110 (ikke systematisk G). Kodeord: 00000,01110,00011,01101,10001,11111,10010,11100. d_min=2, detect=1. Gyldige eksempler: kodeord 10001, ikke-kodeord 01010. Enumering virker også uten en I-blokk. |
| T43 · oppg_3 (3).pdf og T44 · oppg_3.pdf | Dekodingsnotater har feil / blandede H-matriser og syndrom. Bruk korrigert utregning på side 37. |

Kildegrunnlag: github.com/tariknh/diskret, mappen Delprove_4. Kilderevisjon dcbf1e4e8597e1a80a445f1df91bf8864f74d836. Innhold kontrollert 14. november 2026.

Kildekatalogen i source/catalog.json inneholder filnavn og SHA-256 for å skille kopier fra ulike filer. source/cases.json inneholder bare matematiske oppgavetall og nyberegnede svar, uten studentnavn eller signeringskoder.

Dekningen gjelder materialet i denne mappen. En ny prøve kan bruke nye tall eller oppgavevarianter; derfor står både oppskrifter og konkrete oppslag i arket.

## Side 43: Innhold: klikk deg til riktig oppslag

Søk: innhold • contents • index

- Delprøve 4: finn oppgaven din: side 1
- Hurtigsjekk før du svarer: side 2
- RSA-flervalg: hva skal krysses av?: side 3
- RSA: to konkrete feller: side 4
- Svak RSA: finn y og klarteksten: side 8
- Finn inversen y uten å gjette: side 9
- RSA: alle kjente svake nøkler og meldinger: side 10
- Store RSA-tall: bruk modulokalkulatoren: side 11
- Svak RSA på Casio med n=2747: side 12
- Hamming-avstand: tell ulike posisjoner: side 13
- Bitfeil: velg riktig sannsynlighetsformel: side 16
- Bitfeil: et helt gjennomregnet eksempel: side 17
- Bitfeil: alle kjente oppsett og svar: side 18
- Lag G: send 100, 010 og 001 gjennom regelen: side 19
- Lag H fra G: snu kontrollblokken: side 20
- Syndrom: én kontrollsum per rad i H: side 21
- G, H og syndrom med 5 bit: side 22
- Minimum distance, detect og kodeord: side 27
- Dekoding med 8 bit: finn feilposisjonen: side 31
- Dekoding: se hele eksemplet: side 32
- Rett én bit i 10110001: side 33
- 8-bit-dekoding: alle kjente svar: side 37
- Svarformat og egenkontroll: side 38
- Kildesjekk: notater og rettelser: side 42
