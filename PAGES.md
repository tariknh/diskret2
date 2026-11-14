# Nettsiden på GitHub Pages

Forsiden er `index.html`. Øvingsprøvene og PDF-ene åpnes fra knappene der.

Aktiver publisering én gang:

1. Åpne [Settings → Pages](https://github.com/tariknh/diskret2/settings/pages).
2. Under **Build and deployment**, velg **Source: Deploy from a branch**.
3. Velg **Branch: main** og mappen **/(root)**.
4. Trykk **Save**.

Når GitHub er ferdig med første publisering, ligger nettsiden på:

**https://tariknh.github.io/diskret2/**

Etter dette publiserer GitHub nye endringer på `main` automatisk. Det kan ta noen minutter før en oppdatering vises på nettsiden. Ingen egen byggekommando eller server trengs; `.nojekyll` lar GitHub levere HTML- og PDF-filene direkte.

Ved oppdatering av hjelpeark til et nytt versjonert filnavn må lenken i `index.html` oppdateres sammen med hjelpearket. Øvingsprøvene beholder de samme filnavnene og nettadressene.
