# Delprøve 3 – øvingssiden

[Last ned test3-med-preview.html](../test3-med-preview.html), lagre filen og åpne den i nettleseren. Oppgaver, retting og matematisk forhåndsvisning fungerer uten internett. Lenker til hjelpearket krever nett. GitHub viser kildekoden; last ned selve filen for å bruke prøven.

Oppdatert 6. november 2026:

- S2 og de manglende gruppeformuleringene er med, blant annet «The only subgroups …».
- Ordvariantene p=4,q=4 og p=4,q=6 er med, med eksakte rotuttrykk og fire separat rettede delsvar.
- De nye rekurrenskoeffisientene, null- og negative startverdier og begge heltallspåstandene er med.
- Partikulære oppgaver inkluderer brøkkoeffisienten −1/3 og fortegnsfellen der riktig tillegg er +2^n.
- Binære undergrupper kan ha blandede koordinater, slik de nye indeksoppgavene har.
- «Nye prøvevarianter» gir sju målrettede oppgaver fra de seks nye filene. Dette er øving på de nye variantene, ikke seks komplette kopier av prøvene. De øvrige oppgavefamiliene finnes i de vanlige modusene.
- Hint og forklaringer viser til hjelpeark V9, inkludert parentesforklaringen på side 23–24. De 11 oppgavetypene, 30-minutters fullprøve, automatisk innlevering, poengtrekk ved feil avkryssing og forhåndsvisning er beholdt.

Den oppdaterte generatoren bruker en ny lokal lagringsnøkkel. Tidligere v1-data slettes ikke, men et gammelt forsøk kan ikke gjenopptas med den endrede generatoren. Bare siste forsøk fra denne versjonen lagres. Ny prøve eller nytt modusvalg starter et nytt forsøk.

Filen `../test3-med-preview.html` er hele appen; ingen byggeprosess eller eksterne biblioteker er nødvendig for bruk. For å kontrollere generator og retting med Node:

```sh
node practice/tests/test3-core.cjs
```

For nettleserkontroll med Playwright og Chromium:

```sh
npm install --prefix practice
npm run test:browser --prefix practice
```

Testen bruker `/usr/bin/chromium`, eller banen satt i `CHROMIUM_PATH`. Den starter en midlertidig HTTP-server på localhost, blokkerer eksterne forespørsler og kontrollerer forhåndsvisning, retting, lagring, tidsutløp og mobilvisning.
