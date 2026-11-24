# diskret2

[Åpne nettsiden](https://tariknh.github.io/diskret2/) · [Aktiver automatisk publisering med GitHub Pages](PAGES.md)

Nettsiden blir tilgjengelig når Pages er aktivert. Deretter oppdateres den automatisk ved endringer på `main`.

## MA-224-eksamen

[Last ned eksamensarket for utskrift (24 sider)](helpsheets/final-exam/MA224_EKSAMEN_PAPIR.pdf). Side 1 viser hvor du finner framgangsmåten til hver oppgavetype. Side 2–15 har eksempler fra de gamle eksamenene og tidslogikk. Side 16–24 dekker flere Canvas-varianter innen relasjoner, rekurrenser, grupper, RSA og kodeteori.

[Last ned oppslagsarket til de andre papirene (4 sider)](helpsheets/final-exam/MA224_FORSIDE_OPPSLAG.pdf). Her finner du sidetall i hovedarket, gamle eksamensfasiter fra 2021–2025 og handin-vedlegget. Side 4 viser også hvilke Canvas-oppgaver som passer.

Bygg eksamensarket med `python helpsheets/final-exam/build.py` og førstesiden med `python helpsheets/final-exam/build_front_index.py`. Byggerne bruker DejaVu Sans, DejaVu Sans Mono og Python-avhengighetene i [requirements-filen](helpsheets/test4/requirements.txt).

## Delprøve 4

- [Søkbart hjelpeark V3 – 43 sider](helpsheets/test4/TEST4DOCSV3.pdf)
- RSA-eksemplet med Casio og n=2747 står på side 12.
- De enkle kodeeksemplene viser G, H og syndrom på side 22 og retting av én bit på side 33.
- [Les hjelpearket som tekst](helpsheets/test4/TEST4DOCSV3.md)
- [Last ned øvingsprøven med forhåndsvisning](test4-med-preview.html) – åpne den lagrede HTML-filen i nettleseren.
- [Bruk av øvingssiden og kontroller](practice/TEST4.md)
- [Kilder og gjenoppbygging av hjelpearket](helpsheets/test4/README.md)

Dekker alle 96 regneoppgavene i de 32 ulike prøvefilene i `Delprove_4`: RSA, Hamming-avstand, bitfeilsannsynlighet (høyst 1, 2 eller 3 feil), G/H-matriser, kodeavstand, feildeteksjon og syndromdekoding. Øvingssiden har åtte oppgavetyper, kildeprøver med de konkrete tallene, eksakte modulokalkulatorer og automatisk innlevering etter 30 minutter.

## Delprøve 3

- [Last ned øvingsprøven med forhåndsvisning](test3-med-preview.html) – åpne HTML-filen i nettleseren. Velg «Nye prøvevarianter» for de siste tilleggene.
- [Om øvingssiden og kontroller av fasit](practice/README.md)
- [Sjekkliste for rekurrensflervalg – 3 sider](helpsheets/test3/REKURRENS_SJEKKLISTE.pdf)
- [Gruppeflervalg – finn gruppen og match påstanden](helpsheets/test3/GRUPPER_SVARPROFILER.pdf)
- [Last ned søkbart hjelpeark – versjon 10](helpsheets/test3/TEST3DOCSV10.pdf)
- [Les hjelpearket som tekst](helpsheets/test3/TEST3DOCSV10.md)
- [Kilder og instruksjoner for å bygge PDF-en på nytt](helpsheets/test3/README.md)

Første side viser nøyaktig hva du skal krysse av i de to spørsmålene om gruppen med orden 3 og rekurrensen `−4a[n]+8a[n−1]−12a[n−2]=0`.

Side 2–4 har en sjekkliste som forklarer hvordan du velger for alle påstandstypene vi har funnet i rekurrensflervalgene. Tidligere [versjon 5](helpsheets/test3/TEST3DOCSV5.pdf) er beholdt.

Side 5–15 har gruppeoppslaget: match «Consider G = …», gå til riktig svarprofil, og følg «KRYSS AV / LA STÅ TOM» for hver engelsk påstand. Det er åtte profiler, inkludert den nye S2-varianten, og egne regler for nye tall. [Versjon 6](helpsheets/test3/TEST3DOCSV6.pdf) er også beholdt.

Versjon 9 har en gjennomgått oppgave om parenteser og fortegn på side 23–24, med `a0=-2`, `a1=4` og svaret `(-2+4*n)*2^n`. Den forklarer når parenteser er nødvendige eller valgfrie, og forskjellen på `(-2)^n`, `-2^n` og `-2*2^n`.

De seks siste prøvene er gjennomgått på side 64–67. Alle 147 regneoppgaver i de 49 ulike PDF-prøvene er koblet til et oppslag. Tidligere [versjon 7](helpsheets/test3/TEST3DOCSV7.pdf) og [versjon 8](helpsheets/test3/TEST3DOCSV8.pdf) er beholdt.

Versjon 10 har en tydelig «Husk a[n]=»-påminnelse på side 27–28, særlig øverst på «Ordoppgaven: ferdige tall og generell løsning». Begge fullstendige likningsformer vises. Øvingssiden har samme påminnelse ved feltet og en konkret feilmelding når bare høyresiden er skrevet. Versjon 9 er beholdt.
