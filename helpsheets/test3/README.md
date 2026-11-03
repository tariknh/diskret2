# Hjelpeark til delprøve 3

[Last ned PDF – versjon 5](TEST3DOCSV5.pdf) · [Les den søkbare teksten](TEST3DOCSV5.md)

Gjenoppbygd 3. november 2026 fra `tariknh/diskret/Delprove_3`, fire opplastede prøver og rettelsene i samtalen. Første side gir de konkrete avkryssingene til spørsmålene om `G=⟨x⟩ ⊆ S6`, der `x` har orden 3, og rekurrensen `−4a[n]+8a[n−1]−12a[n−2]=0`.

Hjelpearket dekker rekurrensrelasjoner, gyldige ord, permutasjoner, D3, undergrupper, gruppeflervalg, multiplikasjon og invers modulo m, og indeks. De konkrete tabellene gjelder vilkårene og tallene som står ved dem.

Alle filer som trengs for å lage PDF-en, ligger her i GitHub. Originalprøver og personlige forsøksdata kopieres ikke inn i dette repositoriet. `source/catalog.json` dokumenterer kilder, filhash og oppgavetyper.

For å bygge på Linux med Python 3.10 eller nyere og DejaVu-fontene installert:

```sh
python -m pip install -r helpsheets/test3/requirements.txt
python helpsheets/test3/build.py
python helpsheets/test3/verify.py
```

Rediger innholdet i `source/*.json`, og bygg på nytt. Byggingen lager PDF, Markdown og `build-manifest.json`. Kontrollprogrammet sjekker matematiske tabeller, svarene på første side, at sidene er søkbare, og at innhold og lenker får plass.
