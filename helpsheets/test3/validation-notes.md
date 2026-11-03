# Kontroller ved gjenoppbygging

Hjelpearket ble gjenoppbygd 3. november 2026. Innholdet er kontrollert mot 50 PDF-er i originalmappen, fire opplastede prøver og spørsmålene fra studentens skjermbilde. Identiske forsøk er merket som kopier. Det gir 43 forskjellige PDF-prøver og 129 regneoppgaver.

- Alle 12 oppgavefamilier har oppslag. `source/coverage.csv` kobler hver oppgave til sidetall. Flervalg peker direkte til avkryssingskortene for akkurat kildefilen.
- De 13 valgene på første side og 42 valg i de sju gruppevariantene er kontrollert mot ordlyden, inkludert «not», «there exists» og «for each». Den utydelige overskriften i B08 er visuelt kontrollert: oppgaven gjelder hele S6.
- De 54 påstandene i de ni rekurrensvariantene, 11 initialverdieksempler og 15 partikulære eksempler er kontrollert uavhengig. Brøkregning ble gjort eksakt; formler ble satt inn i både rekurrens og startverdier.
- Heltallsregelen for rasjonale koeffisienter er kontrollert mot 5 250 små tilfeller og begrunnet generelt med determinanten `D[n]=a[n]*a[n+2]−a[n+1]^2`.
- Gruppeegenskapene ble kontrollert ved å telle elementer og elementordener, inkludert alle 720 permutasjoner i S6. Alle 36 D3-produkter følger kursets konvensjon om å bruke venstre faktor først.
- Multiplikasjons- og inverstabellene samt modulære regneeksempler ble regnet ut uavhengig. Indekser og ordener til potenser ble kontrollert mot gruppeordenen.
- `verify.py` kontrollerer den publiserte PDF-en, søkbar påstandstekst, bokmerker, lenker, avkryssinger, marger, kildekoblinger og numeriske tabeller på nytt.

Gamle elevsvar og prosenttall er ikke alene brukt som fasit. Svarnumre gjelder rekkefølgen i det viste spørsmålet; hvis alternativene flyttes, må teksten matches. En tabell for én oppgitt likning eller gruppe må brukes med de samme vilkårene.
