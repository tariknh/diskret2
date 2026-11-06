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

## Tillegg 6. november 2026

Seks nye PDF-er (N05–N10) er gjennomgått, med 18 regneoppgaver. Ingen identiske filkopier av tidligere kilder ble funnet. Kildegrunnlaget er nå 60 PDF-er, 49 ulike forsøk og 147 regneoppgaver.

S2-profilen er kontrollert mot elementordenene 1 og 2. Alle påstandene er testet mot gruppeegenskapene. De nye ordvariantene er kontrollert ved å telle alle gyldige ord av lengde tre, og de eksakte røttene er satt inn i karakteristiske polynomer. De to nye partikulære løsningene er kontrollert både med en generell koeffisientidentitet og eksakt innsetting. De nye permutasjonene, D3-produktene, P5-produktene, P49-tallene og indeksene er regnet ut uavhengig. Den testbare matematiske datalisten ligger i `source/new-2026-11-checks.json`.

N08 har fire matematisk riktige viste ordsvar, men viser 0.75/1. Det er kontrollert visuelt at de innskrevne potensene og rotuttrykkene samsvarer med tekstuttrekket. PDF-en gir ikke grunnlag for å tilskrive poengtapet en bestemt del eller endre et matematisk riktig svar.

## Parentesforklaring i versjon 9

Eksemplet med dobbel rot 2 og startverdiene −2,4 er kontrollert mot både startverdiene og rekurrensen. Det gir U=−2,V=4 og `(-2+4*n)*2^n`. Den innskrevne formen uten frontparentes gir feil a1=6; formen med negativt grunntall gir feil a1=−4. Potens-, brøk- og nevnerreglene er kontrollert med konkrete tall. Øvingssidens faktiske parser og retter godtar de riktige ekvivalente uttrykkene og avviser de tre viste grupperingene som endrer løsningen. Øvingssidens lenker og sidetall viser til V9; oppgavegeneratoren og eksisterende v2-forsøk er uendret.
