# Hjelpeark til delprøve 3

[Gruppeflervalg – svarprofiler](GRUPPER_SVARPROFILER.pdf) · [Sjekkliste for rekurrensflervalg](REKURRENS_SJEKKLISTE.pdf) · [Last ned PDF – versjon 8](TEST3DOCSV8.pdf) · [Les den søkbare teksten](TEST3DOCSV8.md)

Gjenoppbygd 3. november 2026 fra `tariknh/diskret/Delprove_3`, fire opplastede prøver og rettelsene i samtalen. Første side gir de konkrete avkryssingene til spørsmålene om `G=⟨x⟩ ⊆ S6`, der `x` har orden 3, og rekurrensen `−4a[n]+8a[n−1]−12a[n−2]=0`.

Oppdatert 5. november 2026: en trinnvis sjekkliste på side 2–4 dekker faste svar, tre gitte tall, like ledd, heltall og «None of the above». Den inneholder et gjennomgått eksempel med `4a[n]−16a[n−1]+12a[n−2]=0`, og eksporteres også som eget ark på tre sider. [Versjon 5](TEST3DOCSV5.pdf) er beholdt.

Gruppeoppslaget på side 5–15 har en inngangstabell som matcher første linje i oppgaven, én egen svarside for hver av de åtte kjente gruppevariantene og regler for endrede tall. Hver engelsk påstand har «KRYSS AV / LA STÅ TOM». Reglene har eksplisitte vilkår; de gir ikke en garanti for enhver ny oppgavetype. Oppslaget finnes også i [en egen PDF](GRUPPER_SVARPROFILER.pdf). [Versjon 6](TEST3DOCSV6.pdf) er beholdt.

Versjon 8, 6. november 2026, legger til seks nye prøver: S2 som egen profil, to nye ordvarianter, to rekurrensflervalg, nye partikulære løsninger og P49-tall. Side 62–65 forklarer endringene. Det er nå 60 PDF-kilder, 49 ulike forsøk og 147 regneoppgaver. N08 heter «100%», men viser delpoeng selv om de fire viste ordsvarene er matematisk riktige; poengtapet kan ikke forklares ut fra PDF-en alene. [Versjon 7](TEST3DOCSV7.pdf) er beholdt.

Hjelpearket dekker rekurrensrelasjoner, gyldige ord, permutasjoner, D3, undergrupper, gruppeflervalg, multiplikasjon og invers modulo m, og indeks. De konkrete tabellene gjelder vilkårene og tallene som står ved dem.

Alle filer som trengs for å lage PDF-en, ligger her i GitHub. Originalprøver og personlige forsøksdata kopieres ikke inn i dette repositoriet. `source/catalog.json` dokumenterer kilder, filhash og oppgavetyper.

For å bygge på Linux med Python 3.10 eller nyere og DejaVu-fontene installert:

```sh
python -m pip install -r helpsheets/test3/requirements.txt
python helpsheets/test3/build.py
python helpsheets/test3/verify.py
```

Rediger innholdet i `source/*.json`, og bygg på nytt. Byggingen lager PDF, Markdown og `build-manifest.json`. Kontrollprogrammet sjekker matematiske tabeller, svarene på første side, at sidene er søkbare, og at innhold og lenker får plass.
