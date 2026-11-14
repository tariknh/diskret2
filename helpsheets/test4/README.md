# Delprøve 4 – søkbart hjelpeark

- [TEST4DOCSV1.pdf](TEST4DOCSV1.pdf) – 40 sider med oppskrifter, engelske søkeord og konkrete talloppslag.
- [Samme innhold som tekst](TEST4DOCSV1.md).
- [Øvingsprøven](../../test4-med-preview.html) – last ned HTML-filen og åpne den i nettleseren.

Kontrollert 14. november 2026 mot `tariknh/diskret`, mappen `Delprove_4`, revisjon `dcbf1e4e8597e1a80a445f1df91bf8864f74d836`.

Mappen inneholder 44 PDF-er: 36 prøvekopier og 8 notatkopier. Fire prøvekopier er byte-identiske med andre prøver. De 32 ulike prøvefilene har til sammen 96 regneoppgaver. Alle er knyttet til et oppslag på side 36–38. Notatene er kontrollert separat på side 39. Studentinnsendte svar er ikke behandlet som fasit; svarene er regnet ut på nytt, også der gamle dekodingsnotater har feil.

Åtte oppgavetyper er dekket:

1. Velge gyldige RSA-nøkkelpar, inkludert primtallsfeller.
2. Bryte svak RSA, finne privat eksponent og dekryptere.
3. Finne minste og største Hamming-avstand.
4. Binær symmetrisk kanal: ingen feil, høyst 1/2/3 feil og en bestemt mottatt streng.
5. Finne generator G, kontrollmatrise H og syndrom fra koderegler.
6. Minsteavstand, ikke-null kodeord og ikke-kodeord.
7. Garantert feildeteksjon og kodeord.
8. Syndrom, 8-bit-feilmønster og korrigert kodeord fra en 4×8-generator.

`source/guide.json` er den redigerbare teksten og oppslagstabellene. `source/cases.json` har matematiske oppgavetall og nyberegnede svar. `source/rsa-options.json` har de 30 ulike RSA-alternativene, hvorav 10 er gyldige etter phi-konvensjonen i prøvene. `source/catalog.json` har kildestier og SHA-256 for å identifisere kopier. Det er ikke publisert studentnavn eller signeringskoder.

De 40 sidene kan bygges fra disse filene uten original-PDF-ene:

```sh
python -m pip install -r helpsheets/test4/requirements.txt
python helpsheets/test4/build.py
python helpsheets/test4/verify.py
```

Byggingen bruker DejaVu Sans og DejaVu Sans Mono fra `/usr/share/fonts/truetype/dejavu`. PDF-en har ekte søkbar tekst, bokmerker og en klikkbar innholdsfortegnelse på siste side. Sidetallene i øvingssiden følger `build-manifest.json`; oppdater dem hvis rekkefølgen i arket endres.

Kontrollen beregner svarene uavhengig: alle mottatte 7-bitstrenger for sannsynlighetene, alle kodeord og paravstander, nullrommet til H, nærmeste kodeord og RSA-kontroll ved tilbakekryptering. Den sjekker også at tabelltekst og nuller først er med i PDF-en og at tekst ikke ligger utenfor siden. Dekningen gjelder kildematerialet; nye prøver kan inneholde nye varianter.
