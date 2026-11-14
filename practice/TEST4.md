# Delprøve 4 – øvingsside

[Last ned test4-med-preview.html](../test4-med-preview.html). Bruk nedlastingsknappen på GitHub og åpne den lagrede filen i nettleseren. GitHubs filvisning viser kildekoden.

Siden er én fil og fungerer uten internett. Den har åtte oppgavetyper med norske hint, forklaringer og koblinger til [hjelpeark V1](../helpsheets/test4/TEST4DOCSV1.pdf). Bare hjelpearklenkene krever nett.

- Fullprøve: én RSA-oppgave, én Hamming-/sannsynlighetsoppgave og én kodeteorioppgave. Automatisk levering etter 30 minutter.
- Kildeprøve T01–T36: de konkrete tallene fra én av de 32 ulike prøvefilene, med 30-minutters grense. Filkopiene T15, T34, T35 og T36 er representert ved sine originaler T14, T28 og T24.
- Blandet øving, alle åtte typer eller én valgt type uten tidsgrense.
- Tilfeldige oppgaver bruker både kjente oppsett og nye tall/koderegler. RSA-flervalgene bruker de 30 kontrollerte tallalternativene i tilfeldig utvalg og rekkefølge.
- Eksakte moduloprodukt- og modulopotenskalkulatorer, som i kildetestene. De bruker heltallsaritmetikk og beholder riktig rest også for store RSA-produkter.
- Matematisk forhåndsvisning med innebygd MathML, også for matriser og bitstrenger med nuller først. Den viser formatet uten å røpe fasit.
- Delpoeng, poengtrekk ved feil RSA-avkryssing og forklaring etter innlevering. Alternative gyldige kodeord godtas. I G/H-oppgaven godtas enhver fullverdig kontrollmatrise; syndromet sjekkes mot den gyldige H-en brukeren skrev.
- Siste forsøk lagres lokalt i denne nettleseren når lokal lagring er tilgjengelig. Ny prøve eller endret modus erstatter forsøket. En utløpt prøve leveres ved gjenåpning. Test 3 har en separat lagringsnøkkel.

I 8-bit-dekodingsoppgaven brukes den uttrykkelig oppgitte konvensjonen `H=(Pᵀ|I₄)`, med kontrollbitene i samme rekkefølge som i G. Dette fastsetter rekkefølgen på syndrombitene. Kildeeksemplene og de nye generatoroppgavene har én entydig nærmeste løsning med én feil.

Kontroller:

```sh
python helpsheets/test4/verify.py
node practice/tests/test4-core.cjs
node practice/tests/test4-browser.cjs
```

Nettlesertesten bruker Playwright fra `practice/package.json` og Chromium (`/usr/bin/chromium`, eventuelt `CHROMIUM_PATH`). Den starter en lokal HTTP-server og blokkerer eksterne forespørsler. Den kontrollerer forhåndsvisning, begge kalkulatorene, retting av alle typer, lokal lagring, tidsutløp og mobilvisning.

HTML-filen er appens redigerbare kilde. Ingen byggeprosess eller eksterne biblioteker trengs for å bruke den. De matematiske kildeoppgavene er også lagret som JSON under `helpsheets/test4/source`.
