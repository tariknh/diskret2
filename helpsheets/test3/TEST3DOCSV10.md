# MA-224 – Delprøve 3 – Hjelpeark versjon 10

Gjenoppbygd 6. november 2026. Søk med Cmd+F / Ctrl+F. Sidetall viser til PDF-en.

## Side 1: Din prøve: dette skal du krysse av

Søk: KRYSS AV • G = ⟨x⟩ ⊆ S6 • order 3 • a5=a6=a7=0 • a5=b5

### GRUPPER: KRYSS AV 1, 2, 3 OG 5

**G=⟨x⟩ ⊆ S6, x har orden 3.** Da er G={e,x,x²} og |G|=3.

| Nr. | Påstand i prøven | Dette velger du |
| --- | --- | --- |
| 1 | There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| 2 | The only subgroups of G are the trivial subgroup {e}, and G itself. | **KRYSS AV** |
| 3 | The order of G is divisible by 3. | **KRYSS AV** |
| 4 | There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| 5 | The group G is finite. | **KRYSS AV** |
| 6 | None of the above | **LA STÅ TOM** |

### REKURRENS: KRYSS AV 1, 3 OG 5

**−4*x[n]+8*x[n-1]−12*x[n-2]=0**, altså a[n]=2*a[n-1]−3*a[n-2]. a[n] betyr aₙ.

| Nr. | Påstand i prøven | Dette velger du |
| --- | --- | --- |
| 1 | If a[n] is a solution, and a5=a6=a7=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 2 | If a0=3, a1=0, then a[n] can not be a solution. | **LA STÅ TOM** |
| 3 | If a[n] is a solution, and a0=−3 and a1=0, then a[n] is an integer for each n≥1. | **KRYSS AV** |
| 4 | If a0=0, a1=3 then a[n] can not be a solution. | **LA STÅ TOM** |
| 5 | If a[n] is a solution and b[n] = −a[n], for each n, then b[n] is also a solution. | **KRYSS AV** |
| 6 | a[n] and b[n] are solutions, and if a5=b5, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 7 | None of the above | **LA STÅ TOM** |

**Match teksten hvis alternativene flyttes.** Rekurrensfasiten gjelder likningen over. **Rekurrenssjekkliste: side 2–4. Parenteser og fortegn: side 23–24. Gruppeoppslag: start på side 5. Seks nye prøver: side 64–67.** Forklaringer: side 38 og 20. Innhold: side 16.

## Side 2: Sjekkliste 1: finn de faste svarene

Søk: recurrence relation • Select every statement • zero sequence • cannot be a solution • also a solution

Bruk sjekklisten på hver påstand. Den dekker alle påstandstypene vi har funnet i rekurrensflervalgene. Du trenger ikke lage en lang tallfølge. **En sann påstand = KRYSS AV. En falsk påstand = LA STÅ TOM.**

### START: kontroller at denne malen passer

```text
A*a[n] + B*a[n-1] + C*a[n-2] = 0
```

A, B og C er tallene foran de tre a-leddene. **A og C må ikke være 0.** Følgene er numeriske: brøkverdier er lov. Oppgavene i prøvesamlingen har disse vilkårene. Hvis høyresiden ikke er 0, gjelder ikke de faste svarene automatisk.

### 1. Skriv én gang hvordan du finner neste tall

```text
a[n] = P*a[n-1] + Q*a[n-2]
P = -B/A
Q = -C/A

Din likning: 4*a[n]-16*a[n-1]+12*a[n-2]=0
P = -(-16)/4 = 4
Q = -12/4 = -3
Neste tall = 4*siste tall - 3*nest siste tall
```

### 2. Kryss av eller la stå tom direkte

| Ser du denne påstanden? | Gjør dette |
| --- | --- |
| The zero sequence a[n]=0 is a solution. | **KRYSS AV.** Bare nuller gir 0=0. |
| The zero sequence … is not a solution. | **LA STÅ TOM.** «Not» gjør påstanden feil. |
| To gitte starttall a0=u,a1=v: could be a solution. | **KRYSS AV.** Du kan fortsette fra alle to starttall. |
| To gitte starttall a0=u,a1=v: can not / cannot be a solution. | **LA STÅ TOM.** Brøker senere er også tillatt. |
| If a is a solution, then b[n]=k*a[n] is also a solution. | **KRYSS AV** for et fast tall k. Dette gjelder også −a[n]. |
| If a and b are solutions, then u*a[n]+v*b[n] is also a solution. | **KRYSS AV** når u og v er faste tall. Omfatter a[n]+3*b[n]. |
| Bare én lik verdi, f.eks. a4=b4, betyr at hele følgene er like. | **LA STÅ TOM.** Ett felles tall er ikke nok. |
| Bare ett nullledd, f.eks. a5=0, betyr at hele følgen er null. | **LA STÅ TOM.** Ett nulltall er ikke nok. |

**Gjenstår det tall, indekser eller heltall?** Bruk neste side. Les hele påstanden: «could» og «cannot» gir motsatte valg. Ord som «not» og «at least one» kan endre svaret.

## Side 3: Sjekkliste 2: tall, indekser og heltall

Søk: could be a solution • a1=b1 and a3=b3 • consecutive • integer for each n • at least one index

Bruk regelen du skrev på forrige side: **a[n]=P*a[n-1]+Q*a[n-2]**, med Q≠0. Hos deg er P=4 og Q=−3.

### 3. Er tre starttall oppgitt? Regn bare tredje tall

```text
Gitt a0=u, a1=v og foreslått a2=w:
Riktig tredje tall = P*v + Q*u

Din påstand: u=2, v=-2, w=-14
4*(-2)-3*2 = -14  → stemmer
```

**«Could be a solution»:** Kryss av hvis tallet stemmer; ellers la stå tom. **«Cannot be a solution»:** Gjør motsatt. To starttall kan alltid videreføres, men et tredje foreslått tall kan bryte oppskriften.

### 4. Er to løsninger like på bestemte plasser?

| Se på indeksene | Gjør dette |
| --- | --- |
| To naboplasser: a4=b4 OG a5=b5 | **KRYSS AV** på «hele følgene er like». Samme to tall gir samme neste tall, og Q≠0 lar deg regne bakover. |
| To nabonuller, f.eks. a5=a6=0; også a5=a6=a7=0 | **KRYSS AV** på «hele følgen er null». To nuller ved siden av hverandre er nok. |
| Ett hull: a1=b1 OG a3=b3 | Se på P. **P≠0: KRYSS AV. P=0: LA STÅ TOM.** Her kan mellomtallet finnes fra a2=(a3-Q*a1)/P. |
| Større avstand enn ett hull | Regn d=avstanden mellom indeksene. Lag H0=0,H1=1 med samme P,Q. **H[d]≠0: KRYSS AV. H[d]=0: LA STÅ TOM.** |

Eksempel: mellom a1 og a4 er avstanden d=3. H2=P og H3=P²+Q. Bruk samme test hvis påstanden gir to nullledd på atskilte plasser og hevder at hele følgen er null.

### 5. Påstår den at alle ledd er heltall?

For heltallige a0,a1: **Er P og Q begge heltall? Da er alle ledd heltall.** Hos deg: P=4,Q=−3. Uansett hvilke heltall du starter med, gir 4*siste−3*nest siste et heltall.

Når alle ledd er heltall:
«is an integer for each n» → **KRYSS AV**.
«there exists at least one index … not an integer» → **LA STÅ TOM**.
Har P eller Q en brøk? Bruk neste side før du velger.

## Side 4: Sjekkliste 3: brøker og siste kontroll

Søk: rational coefficients • integer • None of the above • 4*a[n]-16*a[n-1]+12*a[n-2]=0

### 6. Brøkkoeffisienter: ikke gjett fra bare a2

Denne testen gjelder når **P,Q er rasjonale tall, Q≠0, a0,a1 er heltall og minst én av P,Q ikke er et heltall**. Start med å regne a2. En brøk der beviser at ikke alle ledd er heltall. Hvis a2 er heltall, bruker du testen under:

| Gjør dette i rekkefølge | Er alle ledd heltall? |
| --- | --- |
| a0=0 OG a1=0 | **JA.** Hele følgen er null. |
| a0=0, men a1≠0 | **NEI.** Minst ett senere ledd blir en brøk. |
| a0≠0: Regn r=a1/a0. Er r et heltall OG r*r=P*r+Q? | **JA hvis begge krav stemmer.** Ellers **NEI**. |

Eksempel: P=5/2,Q=−1,a0=1,a1=2. Da er r=2 og 2*2=(5/2)*2−1. Begge krav stemmer, så alle ledd er heltall, selv med brøk i P. Derfor er «brøkkoeffisient → falskt» en feil snarvei.

**JA** gir KRYSS AV på «alle heltall», og LA STÅ TOM på «minst ett ikke heltall». **NEI** gir motsatte valg. Hvis startverdiene ikke er heltall, passer ikke denne testen; undersøk de oppgitte indeksene og likningen direkte.

### 7. Avslutt med «None of the above»

Har du krysset av på minst én annen påstand? **LA «NONE» STÅ TOM.**
Er alle de andre påstandene falske? **KRYSS AV PÅ «NONE».**
Svarnumre kan flyttes. Match teksten, ikke plasseringen.

### Din siste oppgave: slik brukes sjekklisten

For 4*a[n]−16*a[n−1]+12*a[n−2]=0 får du P=4,Q=−3. Startverdiene i heltallspåstanden er a0=4,a1=1.

| Påstand | Sjekk / grunn | Velg |
| --- | --- | --- |
| 1. Zero sequence is not a solution | Bare nuller gir 0=0. «Not» er feil. | **LA STÅ TOM** |
| 2. a0=2,a1=−2,a2=−14 could be a solution | 4*(−2)−3*2=−14. Tredje tall passer. | **KRYSS AV** |
| 3. a4=b4 ⇒ hele følgene like | Bare én felles verdi. | **LA STÅ TOM** |
| 4. a1=b1 OG a3=b3 ⇒ hele følgene like | Ett hull; P=4 er ikke 0. | **KRYSS AV** |
| 5. a4=b4 OG a5=b5 ⇒ hele følgene like | To like naboverdier. | **KRYSS AV** |
| 6. a0=4,a1=1 ⇒ alle senere ledd heltall | Starttallene, P=4 og Q=−3 er heltall. | **KRYSS AV** |
| 7. None of the above | Du har allerede sanne påstander. | **LA STÅ TOM** |

## Side 5: Gruppeflervalg: velg profil og match teksten

Søk: Consider G • order • cyclic • abelian • proper • non-trivial

**1. Les hele «Consider G = …».
2. Finn nøyaktig samme gruppe i tabellen.
3. Gå til siden og match hver engelsk påstand.
4. Følg «KRYSS AV» eller «LA STÅ TOM».**

| Dette står i første linje | Gå til side |
| --- | --- |
| G=S2, symmetric group of permutations of 2 symbols | 11 |
| G=⟨x⟩, x has order 3 | 6 |
| G=⟨x⟩, x has order 6 | 7 |
| G=P5, multiplication modulo 5 | 8 |
| G=Z/7 × Z/10, med addisjon | 9 |
| G=Z/3 × Z/10, med addisjon | 10 |
| G=S3, symmetric group of permutations of 3 symbols | 12 |
| G=S6, symmetric group of permutations of 6 symbols | 13 |

### Det viktige skillet: hele S3 eller bare gruppen x lager?

**G=S3:** hele gruppen har 3!=6 elementer. **G=⟨x⟩, x har orden 3:** gruppen som x lager har 3 elementer. Disse får forskjellige avkryssinger. Les også teksten etter «generated by», selv om det står ⊆ S6 eller ⊆ S7 foran.

### Tallet etter «order» eller n er endret?

Bruk oppskriften på side 14 og 15. Den gjelder endelige grupper av typene som står der. En profil for P5 gjelder ikke automatisk P8, og S3 gjelder ikke automatisk alle S_n.

**Nummeret på alternativet er ikke en fasit.** De kan flytte påstandene. Match teksten, også ordene «not», «for each», «there exists», «proper» og «non-trivial». «None of the above» velges bare hvis alle de andre i DIN liste er falske.

Dette oppslaget dekker alle gruppene og påstandstypene vi har funnet i prøvene, pluss regler for endrede tall. Hvis oppgaven gjelder en annen operasjon, en uendelig gruppe eller en ny påstand, må de oppgitte vilkårene undersøkes før du bruker et ferdig svar.

## Side 6: Svarprofil: ⟨x⟩ med orden 3

Søk: G=⟨x⟩, x has order 3 • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=⟨x⟩, x has order 3.

**Antall elementer |G| = 3.**
«The order of G is k»: KRYSS AV akkurat når k=3.
«Divisible by k»: KRYSS AV akkurat når 3/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **LA STÅ TOM** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **KRYSS AV** |
| The order of G is divisible by 3. | **KRYSS AV** |

G er syklisk og abelsk. Tallet etter «order» bestemmer størrelsen på G, uansett hvilken S_n den ligger inni.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 7: Svarprofil: ⟨x⟩ med orden 6

Søk: G=⟨x⟩, x has order 6 • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=⟨x⟩, x has order 6.

**Antall elementer |G| = 6.**
«The order of G is k»: KRYSS AV akkurat når k=6.
«Divisible by k»: KRYSS AV akkurat når 6/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **KRYSS AV** |

G er syklisk og abelsk. Bruk denne profilen også om den oppgitte omgivelsesgruppen er S7 eller en annen S_n.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 8: Svarprofil: G=P5

Søk: G=P5, multiplication modulo 5 • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=P5, multiplication modulo 5.

**Antall elementer |G| = 4.**
«The order of G is k»: KRYSS AV akkurat når k=4.
«Divisible by k»: KRYSS AV akkurat når 4/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **LA STÅ TOM** |

P5={1,2,3,4}. Gruppen er syklisk og abelsk. Profilen gjelder P5, ikke alle P_m.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 9: Svarprofil: G=Z/7 × Z/10

Søk: G=Z/7 × Z/10, med addisjon • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=Z/7 × Z/10, med addisjon.

**Antall elementer |G| = 70.**
«The order of G is k»: KRYSS AV akkurat når k=70.
«Divisible by k»: KRYSS AV akkurat når 70/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **LA STÅ TOM** |

Dette er gruppen av par. Den er syklisk fordi gcd(7,10)=1, og abelsk.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 10: Svarprofil: G=Z/3 × Z/10

Søk: G=Z/3 × Z/10, med addisjon • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=Z/3 × Z/10, med addisjon.

**Antall elementer |G| = 30.**
«The order of G is k»: KRYSS AV akkurat når k=30.
«Divisible by k»: KRYSS AV akkurat når 30/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **KRYSS AV** |

Dette er gruppen av par. Den er syklisk fordi gcd(3,10)=1, og abelsk.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 11: Svarprofil: HELE S2

Søk: G=S2 • symmetric group of permutations of 2 symbols • cyclic • abelian

**Bruk denne siden når første linje sier:** G=S2, the symmetric group of permutations of 2 symbols.

**Antall elementer |G| = 2!=2.**
«The order of G is k»: KRYSS AV akkurat når k=2.
«Divisible by k»: KRYSS AV akkurat når 2/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **KRYSS AV** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| The group G is not abelian. | **LA STÅ TOM** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| The group G is cyclic. | **KRYSS AV** |
| The group G is not cyclic. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **LA STÅ TOM** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **KRYSS AV** |
| The order of G is divisible by 3. | **LA STÅ TOM** |

S2 har identiteten og byttet av de to symbolene. Gruppen er syklisk og abelsk, men har ingen ikke-triviell ekte undergruppe. I N05 er bare påstanden «The group G is cyclic» sann (alternativ 5 i den filen).

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 12: Svarprofil: HELE S3

Søk: G=S3, symmetric group of permutations of 3 symbols • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=S3, symmetric group of permutations of 3 symbols.

**Antall elementer |G| = 6.**
«The order of G is k»: KRYSS AV akkurat når k=6.
«Divisible by k»: KRYSS AV akkurat når 6/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **LA STÅ TOM** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **LA STÅ TOM** |
| The group G is not abelian. | **KRYSS AV** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **KRYSS AV** |
| The group G is cyclic. | **LA STÅ TOM** |
| The group G is not cyclic. | **KRYSS AV** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **LA STÅ TOM** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **KRYSS AV** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **KRYSS AV** |

Dette er HELE S3. Den er verken syklisk eller abelsk. Sammenlign første linje: G=⟨x⟩ med ord(x)=3 bruker en annen profil.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 13: Svarprofil: HELE S6

Søk: G=S6, symmetric group of permutations of 6 symbols • Select every statement • subgroup

**Bruk denne siden når første linje sier:** G=S6, symmetric group of permutations of 6 symbols.

**Antall elementer |G| = 720.**
«The order of G is k»: KRYSS AV akkurat når k=720.
«Divisible by k»: KRYSS AV akkurat når 720/k er et heltall (k>0).

| Finn denne påstandsteksten | Dette velger du |
| --- | --- |
| The order of G is 7. | **LA STÅ TOM** |
| The group G is finite. | **KRYSS AV** |
| The group G is infinite. | **LA STÅ TOM** |
| The group G is abelian. | **LA STÅ TOM** |
| For all elements a,b ∈ G, the following is true: ab = ba. | **LA STÅ TOM** |
| The group G is not abelian. | **KRYSS AV** |
| There exist elements g,h ∈ G such that gh ≠ hg. | **KRYSS AV** |
| The group G is cyclic. | **LA STÅ TOM** |
| The group G is not cyclic. | **KRYSS AV** |
| There exists an element g ∈ G such that ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **LA STÅ TOM** |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **KRYSS AV** |
| For each element g ∈ G, ⟨g⟩=G. | **LA STÅ TOM** |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **KRYSS AV** |
| The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| The order of G is divisible by 3. | **KRYSS AV** |

Dette er HELE S6. Den er verken syklisk eller abelsk. G=⟨x⟩ ⊆ S6 er en egen undergruppe og bruker profilen bestemt av ordenen til x.

**None of the above:** Kryss av bare når alle de andre alternativene i den aktuelle oppgaven er falske. En sann rad på denne siden teller bare hvis den faktisk står i oppgaven din.

## Side 14: Nye tall: finn tre opplysninger om G

Søk: G=<x> • order d • S_n • Z/m × Z/n • P_m • gcd • finite

Når første linje ikke matcher en profil: finn **N=antall elementer**, **syklisk?** og **abelsk?** med tabellen. Bruk deretter neste side. Reglene her gjelder endelige grupper med de vanlige operasjonene angitt nedenfor.

| Dette står i oppgaven | Finn N | Syklisk og abelsk? |
| --- | --- | --- |
| G=⟨x⟩, x has finite order d | N=d | Alltid syklisk og abelsk. S_n den ligger inni endrer ikke dette. |
| G=S_n, hele permutasjonsgruppen | N=n! | For n≥3: verken syklisk eller abelsk. S1 og S2: begge deler. |
| G=Z/m × Z/n, addisjon | N=m*n | Alltid abelsk. Syklisk akkurat når gcd(m,n)=1. m,n er positive heltall. |
| G=P_m, multiplikasjon modulo m (m≥2) | Tell 1≤a<m med gcd(a,m)=1 | Alltid abelsk. Bruk testen under for syklisk. |

### P_m: slik tester du «cyclic» med nye m

1. Skriv tallene som er med: 1≤a<m og gcd(a,m)=1. Antallet er N.
2. Velg et tall g i gruppen. Start med 1, og gang med g om igjen modulo m.
3. Teller du N forskjellige tall før du er tilbake? Da er gruppen syklisk.
4. Hvis ingen av tallene g gjør dette, er gruppen ikke syklisk.

Ved primtall m=p vet du direkte at P_p er syklisk, med N=p−1. For sammensatte m må du undersøke; P8 er et moteksempel til at alle P_m er sykliske.

### Eksempler med endrede tall

| Gruppe | N | Syklisk? | Abelsk? |
| --- | --- | --- | --- |
| ⟨x⟩ med ord(x)=9 | 9 | Ja | Ja |
| S4 | 4!=24 | Nei | Nei |
| Z/4 × Z/2 | 4*2=8 | Nei: gcd(4,2)≠1 | Ja |
| P8={1,3,5,7} | 4 | Nei: ingen lager alle fire | Ja |

Neste side oversetter opplysningene til avkryssinger. Bruk ikke bare størrelsen N: S3 og ⟨x⟩ med ord(x)=6 har begge seks elementer, men får ulike svar fordi bare den ene er syklisk.

## Side 15: Nye tall: oversett til riktig avkryssing

Søk: for each • there exists • non-trivial proper • only subgroups • order • prime • composite

For en **endelig gruppe med N>1**: finn N, syklisk og abelsk på forrige side. I tabellen betyr «når» at du krysser av hvis kravet stemmer; ellers lar du stå tom.

| Påstand / betydning | KRYSS AV når … |
| --- | --- |
| The group G is finite. | Alltid her. «Infinite»: la stå tom. |
| The order of G is k. | N=k nøyaktig. |
| The order of G is divisible by k. | N/k er et heltall (k>0). |
| The group G is cyclic. | G er syklisk. «Not cyclic»: motsatt. |
| There exists g such that ⟨g⟩=G, eller \|⟨g⟩\|=\|G\|. | G er syklisk. |
| For each g, ⟨g⟩ is a proper subgroup of G. | G IKKE er syklisk. |
| For each g, ⟨g⟩=G. | Aldri når N>1. g=e gir bare {e}. |
| There exists g such that ⟨g⟩ is proper. | Alltid når N>1: velg g=e. |
| The group G is abelian; eller ab=ba for all a,b. | G er abelsk. |
| The group G is not abelian; eller there exist g,h with gh≠hg. | G IKKE er abelsk. |
| The group G has a non-trivial and proper subgroup. | N er sammensatt (ikke primtall). |
| The only subgroups are {e} and G. | N er et primtall. |
| None of the above. | Alle de andre alternativene i DIN liste er falske. |

### Sjekk disse ordene før du leverer

**Prime:** primtall som 2,3,5,7. **Composite:** sammensatt tall som 4,6,8,9. For endelige grupper gir primtallsorden bare undergruppene {e} og G; sammensatt orden gir minst én undergruppe med 1<|H|<N.

**Proper** betyr H≠G. **Non-trivial** betyr H≠{e}. Begge samtidig krever 1<|H|<N. «There exists» trenger ett eksempel. «For each» må også virke for e.

**Hvis N=1:** G={e}, syklisk og abelsk. Den eneste undergruppen er G selv; den er verken ekte eller ikke-triviell. Hvert g genererer hele G. Det finnes ingen g som genererer en ekte undergruppe. Ikke bruk N>1-radene over direkte.

## Side 16: Innhold 1: klikk på oppgaven

Søk: Cmd+F • Ctrl+F • søkbar • innhold

Ferdige avkryssinger til dine to spørsmål står på **side 1**. Klikk på en rad for å gå direkte til oppslaget. Du kan også søke på engelske ord fra oppgaveteksten.

- Sjekkliste 1: finn de faste svarene: side 2
- Sjekkliste 2: tall, indekser og heltall: side 3
- Sjekkliste 3: brøker og siste kontroll: side 4
- Gruppeflervalg: velg profil og match teksten: side 5
- Svarprofil: ⟨x⟩ med orden 3: side 6
- Svarprofil: ⟨x⟩ med orden 6: side 7
- Svarprofil: G=P5: side 8
- Svarprofil: G=Z/7 × Z/10: side 9
- Svarprofil: G=Z/3 × Z/10: side 10
- Svarprofil: HELE S2: side 11
- Svarprofil: HELE S3: side 12
- Svarprofil: HELE S6: side 13
- Nye tall: finn tre opplysninger om G: side 14
- Nye tall: oversett til riktig avkryssing: side 15
- Din rekurrensoppgave: kryss av 1, 3 og 5: side 20
- Lukket form: finn røtter, så tallene foran: side 21
- Like røtter og ferdige startverdi-eksempler: side 22
- Parenteser: oppgaven din med startverdi −2: side 23
- Parenteser: når trengs de, og når er de valgfrie?: side 24

## Side 17: Innhold 2: klikk på oppgaven

Søk: Cmd+F • Ctrl+F • søkbar • innhold

Ferdige avkryssinger til dine to spørsmål står på **side 1**. Klikk på en rad for å gå direkte til oppslaget. Du kan også søke på engelske ord fra oppgaveteksten.

- En gitt p[n]: lag en annen løsning og finn a1: side 25
- Gitt p[n]: alle koeffisient- og a1-variantene: side 26
- Ordoppgaven: tell A og X, så bruk malen: side 27
- Ordoppgaven: ferdige tall og generell løsning: side 28
- Rekurrensflervalg: finn den konkrete regelen: side 29
- Like ledd: ett treff er ikke nok: side 30
- Heltall og tre startverdier: ferdige kontroller: side 31
- Alle rekurrensflervalgene: match din likning: side 32
- Ferdig avkryssing: B03, B05: side 33
- Ferdig avkryssing: B15, B16: side 34
- Ferdig avkryssing: B27, B33: side 35
- Ferdig avkryssing: B35, B36: side 36
- Ferdig avkryssing: N04: side 37
- Din gruppeoppgave: kryss av 1, 2, 3 og 5: side 38
- Finn gruppen først: da finner du riktig svar: side 39
- Gruppetabell: endelig, abelsk og syklisk: side 40
- Gruppetabell: generatorer og undergrupper: side 41
- Gruppetabell: alle ordenstallene i prøvene: side 42
- Ferdig avkryssing: orden 3 og P5: side 43

## Side 18: Innhold 3: klikk på oppgaven

Søk: Cmd+F • Ctrl+F • søkbar • innhold

Ferdige avkryssinger til dine to spørsmål står på **side 1**. Klikk på en rad for å gå direkte til oppslaget. Du kan også søke på engelske ord fra oppgaveteksten.

- Ferdig avkryssing: grupper av par: side 44
- Ferdig avkryssing: hele S3 og hele S6: side 45
- Ferdig avkryssing: generator med orden 6: side 46
- Permutasjoner: først venstre, så høyre: side 47
- Invers permutasjon: finn hvor tallene kom fra: side 48
- D3: hva id, r1, r2 og t1,t2,t3 betyr: side 49
- D3: ferdig multiplikasjonstabell: side 50
- Undergruppe i Z/n: start på 0 og legg til: side 51
- Grupper av par: samme antall hopp i begge: side 52
- Generatorpar: alle de ferdige svarene: side 53
- Modulo-produkt: gang og behold resten: side 54
- Invers modulo m: finn tallet som gir rest 1: side 55
- Ferdige multiplikasjons- og inverstabeller: P5 og P7: side 56
- Ferdige multiplikasjons- og inverstabeller: P8 og P9: side 57
- Konkrete prøvesvar: produkter og inverser modulo 45–49: side 58
- Konkrete prøvesvar: alle kjente P50-variantene: side 59
- Indeks i (Z/2)^k: tell og del: side 60
- Kvadratgruppen D4: ferdige indekssvar: side 61
- Casio fx-9860GIII: raske, kontrollerbare regninger: side 62

## Side 19: Innhold 4: klikk på oppgaven

Søk: Cmd+F • Ctrl+F • søkbar • innhold

Ferdige avkryssinger til dine to spørsmål står på **side 1**. Klikk på en rad for å gå direkte til oppslaget. Du kan også søke på engelske ord fra oppgaveteksten.

- Svarfelt: skriv dette, og sjekk disse fellene: side 63
- Seks nye prøver: dette er nyttig å øve på: side 64
- Nye ordvarianter: p=4 med q=4 eller q=6: side 65
- Nye partikulære løsninger: kopier p[n] og finn fortegnet: side 66
- Nye rekurrensflervalg: ferdige valg for N05 og N07: side 67
- Kildesjekk: prøvefilene 1: side 68
- Kildesjekk: prøvefilene 2: side 69
- Kildesjekk: prøvefilene 3: side 70
- Kildesjekk: prøvefilene 4: side 71
- Kildegrunnlag og rettelser til gamle notater: side 72

## Side 20: Din rekurrensoppgave: kryss av 1, 3 og 5

Søk: Consider the recurrence relation • −4*x[n]+8*x[n-1]−12*x[n-2]=0 • a5=b5

**KRYSS AV: 1, 3 OG 5.**
**LA STÅ TOM: 2, 4, 6 OG «NONE OF THE ABOVE».**

```text
-4*x[n]+8*x[n-1]-12*x[n-2]=0
a[n]=2*a[n-1]-3*a[n-2]
```

Dette er likningen fra skjermbildet ditt. x[n], a[n] og b[n] er ulike navn på følger som skal følge samme regel. a[n] betyr aₙ.

| Hele påstanden | Velg | Kort grunn |
| --- | --- | --- |
| 1. If a[n] is a solution, and a5=a6=a7=0, then a[n]=0 for each n≥1. | **KRYSS AV** | To nabonuller er nok. Her har du tre. |
| 2. If a0=3, a1=0, then a[n] can not be a solution. | **LA STÅ TOM** | To startverdier kan alltid videreføres i denne likningen. |
| 3. If a[n] is a solution, and a0=−3 and a1=0, then a[n] is an integer for each n≥1. | **KRYSS AV** | Regelen bruker bare heltallene 2 og −3. |
| 4. If a0=0, a1=3 then a[n] can not be a solution. | **LA STÅ TOM** | Også disse to startverdiene gir en løsning. |
| 5. If a[n] is a solution and b[n] = −a[n], for each n, then b[n] is also a solution. | **KRYSS AV** | Du kan gange hele den homogene likningen med −1. |
| 6. a[n] and b[n] are solutions, and if a5=b5, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** | Én lik verdi er ikke nok til å bestemme en følge av orden 2. |
| 7. None of the above | **LA STÅ TOM** | Påstand 1, 3 og 5 er sanne. |

**Fellen var påstand 6.** Nullfølgen har a5=0 og a6=0. En annen løsning med b0=11,b1=12 har b5=0 og b6=243. Følgene møtes ved 5 og skiller lag ved 6. Regning og andre indekser: 30.

## Side 21: Lukket form: finn røtter, så tallene foran

Søk: Find the solution to the initial value problem • distinct roots • initial conditions

Når oppgaven gir en rekurrens med a[n], a[n-1], a[n-2] og to startverdier, skal du finne en formel som bare bruker **n**.

```text
A*a[n]+B*a[n-1]+C*a[n-2]=0
A*r^2+B*r+C=0
```

Behold fortegnene. Casio fx-9860GIII: **MENU → EQUA → POLY → grad 2**. Skriv A, B, C. Eller regn r=(−B±sqrt(B²−4*A*C))/(2*A).

**To ulike røtter r1,r2:** a[n]=U*r1^n+V*r2^n.
**Én rot r to ganger:** a[n]=(U+V*n)*r^n. Se 22.

### Gjennomregnet eksempel B19

```text
a[n]+2*a[n-1]-8*a[n-2]=0, a0=2, a1=10
r^2+2*r-8=(r-2)*(r+4)=0
r1=2, r2=-4
a[n]=U*2^n+V*(-4)^n
n=0: U+V=2
n=1: 2*U-4*V=10
U=3, V=-1
```

**Skriv som svar:** 3*2^n-(-4)^n

Rask kontroll: n=0 gir 3−1=2. n=1 gir 6+4=10. Begge stemmer med startverdiene.

### Hvis du vil regne U og V direkte

```text
U=(a1-r2*a0)/(r1-r2)
V=a0-U
```

Ikke la U,V stå igjen når oppgaven har gitt bestemte startverdier. Finn tallene. I en **general solution** kan frie konstanter stå igjen hvis oppgaven tillater det.

## Side 22: Like røtter og ferdige startverdi-eksempler

Søk: repeated root • double root • Find the solution to the initial value problem • negative base

**Dobbel rot:** bruk (U+V*n)*r^n.
U=a0, V=a1/r−a0 når r≠0. Leddet V*n må være med.

Parenteser og fortegn: se den gjennomgåtte oppgaven med a0=−2,a1=4 på side 23, og skrivereglene på side 24.

```text
N03: a[n]+6*a[n-1]+9*a[n-2]=0, a0=1,a1=-9
(r+3)^2=0 → r=-3
U=1, V=(-9)/(-3)-1=2
Svar: (1+2*n)*(-3)^n
```

Her er kontrollerte svar fra prøvemappen. **a0,a1 må også stemme med din oppgave.** Kilde-ID-ene står i kildeoversikten.

| Kilde / likning | a0 ; a1 | Svar som kan skrives inn |
| --- | --- | --- |
| B06<br>a[n]-2*a[n-1]-8*a[n-2]=0 | 1 ; -8 | -4^n+2*(-2)^n |
| B07<br>a[n]+2*a[n-1]-3*a[n-2]=0 | 1 ; -7 | 2*(-3)^n-1 |
| B08/B49<br>a[n]-a[n-1]-6*a[n-2]=0 | 1 ; -12 | -2*3^n+3*(-2)^n |
| B09<br>a[n]+4*a[n-1]+4*a[n-2]=0 | -2 ; 6 | (-2-n)*(-2)^n |
| B19<br>a[n]+2*a[n-1]-8*a[n-2]=0 | 2 ; 10 | 3*2^n-(-4)^n |
| B21<br>a[n]-4*a[n-1]+4*a[n-2]=0 | 1 ; 10 | (1+4*n)*2^n |
| B23<br>a[n]+a[n-1]-6*a[n-2]=0 | -1 ; 8 | 2^n-2*(-3)^n |
| B26<br>a[n]+3*a[n-1]-4*a[n-2]=0 | 7 ; -13 | 4*(-4)^n+3 |
| B39<br>a[n]+4*a[n-1]+3*a[n-2]=0 | 5 ; -13 | (-1)^n+4*(-3)^n |
| N01<br>a[n]-2*a[n-1]-3*a[n-2]=0 | 0 ; -4 | -3^n+(-1)^n |

**−3^n betyr −(3^n). (−3)^n har −3 som grunntall.** Dette gir forskjellige svar når n er partall. Dobbel rot 0 må behandles direkte: a[n]=0 for n≥2, startverdiene står separat.

## Side 23: Parenteser: oppgaven din med startverdi −2

Søk: a[n]-4*a[n-1]+4*a[n-2]=0 • a0=-2 • a1=4 • parentheses • (-2+4*n)*2^n

```text
a[n]-4*a[n-1]+4*a[n-2]=0
a0=-2, a1=4
```

### 1. Finn grunntallet fra likningen

```text
r^2-4*r+4=(r-2)^2=0
r=2 to ganger
```

**Grunntallet er +2. Derfor bruker du 2^n.**
Startverdien a0=−2 forteller ikke at grunntallet er −2. Grunntallet kommer fra rotlikningen.

### 2. Dobbel rot: grupper hele uttrykket foran potensen

```text
a[n]=(U+V*n)*2^n
a0=-2 → U=-2
a1=4 → (-2+V)*2=4
        -2+V=2
        V=4
```

**Skriv i svarfeltet:**
(-2+4*n)*2^n

Parentesen grupperer -2+4*n. HELE dette uttrykket skal ganges med 2^n.

### 3. Slik leser du svaret ved n=1

| Skrivemåte | Regning ved n=1 | Passer med a1=4? |
| --- | --- | --- |
| (-2+4*n)*2^n | (-2+4)*2=2*2=4 | **JA** |
| -2+4*n*2^n | -2+4*1*2=-2+8=6 | **NEI** |
| (-2+4*n)*(-2)^n | (-2+4)*(-2)=-4 | **NEI** |

Uten parentes rundt -2+4*n blir bare 4*n ganget med 2^n. Med (-2)^n har du byttet grunntallet til et annet tall. Det endrer følgen.

### 4. Kontroller begge startverdiene

```text
n=0: (-2+4*0)*2^0=-2
n=1: (-2+4*1)*2^1=4
```

Du kan også skrive (-2+4*n)*(2)^n. Parentesen rundt det positive tallet 2 er valgfri. Parentesen rundt summen -2+4*n må være med i denne skrivemåten.

## Side 24: Parenteser: når trengs de, og når er de valgfrie?

Søk: negative base • minus • brackets • parentheses • 2^n • (-2)^n • (U+V*n) • denominator

**Sett parentes rundt ALT som skal behandles som én samlet del.**
Se særlig på grunntallet før ^, hele uttrykket foran en potens, og hele nevneren etter /.

| Det du mener | Skriv slik | Hvorfor? |
| --- | --- | --- |
| Positiv rot 2 opphøyd i n | 2^n<br>(2)^n er også riktig | Ett positivt tall trenger ikke parentes. |
| Negativ rot −2 opphøyd i n | (-2)^n | Minustegnet er en del av grunntallet. Det må med inni parentesen. |
| Minus FORAN potensen 2^n | -2^n<br>eller -(2^n) | Her regnes potensen først, og deretter settes minus foran. |
| −2 som faktor foran 2^n | -2*2^n<br>(-2)*2^n er også riktig | Stjernen betyr gange. Dette gjør ikke grunntallet negativt. |
| Hele U+V*n skal ganges med r^n | (U+V*n)*(r)^n | Dobbel rot: parentesen holder hele frontleddet samlet. |
| Brøken 2/3 er grunntallet | (2/3)^n | 2/3^n betyr 2 delt på 3^n. Det er et annet uttrykk. |
| Hele 2+2*sqrt(5) er grunntallet | (2+2*sqrt(5))^n | Hele summen skal opphøyes i n. |
| Hele n+1 er eksponenten | 2^(n+1) | 2^n+1 betyr at du legger til 1 etter at potensen er regnet ut. |
| Hele 10*3^n står under brøkstreken | 1/(10*3^n) | 1/10*3^n betyr (1/10)*3^n. Hele nevneren må grupperes. |

### To minustegn som betyr forskjellige ting

```text
Ved n=2:
(-2)^2 = (-2)*(-2) = 4
-2^2   = -(2*2)    = -4
-2*2^2 = (-2)*4    = -8
```

Derfor må du finne røttene først. At en startverdi eller en koeffisient er negativ, er ikke alene en grunn til å skrive (-2)^n.

### Sjekk før du leverer

1. Er grunntallet en negativ verdi, brøk eller sum? Sett parentes rundt hele grunntallet.
2. Har du dobbel rot? Behold (U+V*n) samlet foran potensen.
3. Har nevneren flere faktorer eller ledd? Grupper hele nevneren.
4. Sett n=0 og n=1 i det du faktisk har skrevet. Begge skal gi startverdiene.
5. Bruk forhåndsvisningen: se hva som står inni potensen og under brøkstreken.

## Side 25: En gitt p[n]: lag en annen løsning og finn a1

Søk: The following sequence • particular solution • special solution • Find another solution • Given the initial condition

Når oppgaven allerede gir én løsning p[n], kopierer du den nøyaktig og legger til én potens. Du trenger ikke finne p[n] på nytt.

```text
A*a[n]+B*a[n-1]=f(n)
r=-B/A
En annen løsning: p[n]+r^n
```

Flytt alle a-ledd til venstre før du leser A og B. Høyresiden kan være alt som bare avhenger av n. Formelen her brukes med A≠0 og r≠0, som i disse prøvevariantene.

**Del a:** svar med p[n]+r^n, uten frie konstanter. Bare p[n] er samme løsning og er derfor ikke nok når det står «another … not equal to p[n]».
**Del b:** bruk den nye startverdien a0 og sett n=1 rett inn i likningen.

### N02: brøk foran a[n]

```text
a[n]/2+4*a[n-1]=(-3)^n
p[n]=2*(-3)^(n+1)/5
A=1/2, B=4 → r=-4/(1/2)=-8
Del a: 2*(-3)^(n+1)/5+(-8)^n
```

### N02: a0=4/5, finn a1

```text
a1/2+4*(4/5)=-3
a1/2=-3-16/5=-31/5
a1=-62/5
```

**Del b: skriv −62/5.** Det er ikke nødvendig å bruke formelen fra del a.

Hvis du vil finne hele løsningen som også passer med a0: a[n]=p[n]+C*r^n, der **C=a0−p[0]**. For N02 blir C=2. Del a og del b trenger ikke bruke samme C.

## Side 26: Gitt p[n]: alle koeffisient- og a1-variantene

Søk: special solution • another solution • a[n]/3 • a[n]/2 • 5*a[n] • a1

Finn raden med dine a-ledd og din a0. **I del a: kopier hele den oppgitte p[n], og legg til potensen i midtkolonnen.** Midtkolonnen er bare tillegget, ikke hele svaret.

| Kilde / a-ledd / startverdi | Tillegg til p[n] | Riktig a1 |
| --- | --- | --- |
| B02: a[n]/3+3*a[n-1]<br>a0=-20/17 | (-9)^n | 309/34 |
| B11: 4*a[n]-5*a[n-1]<br>a0=11/6 | (5/4)^n | 29/12 |
| B13: 4*a[n]+2*a[n-1]<br>a0=13/10 | (-1/2)^n | -7/5 |
| B14: 5*a[n]+3*a[n-1]<br>a0=7/4 | (-3/5)^n | -67/60 |
| B17: -a[n]+a[n-1]/2<br>a0=-3/2 | (1/2)^n | -1/4 |
| B18/B48: -a[n]/3-a[n-1]<br>a0=1/8 | (-3)^n | -123/8 |
| B20: -5*a[n]+2*a[n-1]<br>a0=23/13 | (2/5)^n | 7/65 |
| B22: 3*a[n]-2*a[n-1]<br>a0=-2 | (2/3)^n | -7/6 |
| B25: -a[n]/2+a[n-1]/2<br>a0=-9/2 | 1 | -29/2 |
| B29/B30: -5*a[n]-4*a[n-1]<br>a0=2/3 | (-4/5)^n | -2/15 |
| B31: a[n]/2+2*a[n-1]<br>a0=-3 | (-4)^n | 8 |
| B37: a[n]/2-a[n-1]/2<br>a0=1/3 | 1 | -11/3 |
| B38: 5*a[n]-a[n-1]/3<br>a0=167/76 | (1/15)^n | -973/1140 |
| B43: 5*a[n]-a[n-1]/2<br>a0=37/31 | (1/10)^n | -149/310 |
| N02: a[n]/2+4*a[n-1]<br>a0=4/5 | (-8)^n | -62/5 |
| N09: -a[n]/3-a[n-1]<br>a0=7 | (-3)^n | -15 |
| N10: -2*a[n]+4*a[n-1]<br>a0=-9/10 | 2^n | -59/30 |

B38: tillegget er **(1/15)^n**, ikke (1/5)^n. Her må også den oppgitte brøken 167/76 leses riktig. Tabellen er regnet fra likningene; feil elevsvar i originalfilene er rettet.

## Side 27: Ordoppgaven: tell A og X, så bruk malen

Søk: Let A and X be the sets • valid words • starts with • ends with • adjacent letters • Find a recurrence relation

**Husk a[n]= i rekurrensfeltet.** Skriv hele likningen: neste tall = regelen som bruker de to forrige. Bare p*a[n-1]+p*q*a[n-2] er høyresiden, ikke en full likning.

Denne malen gjelder de tre reglene i prøvene: ordet starter med et A-tegn, slutter med et A-tegn og kan ikke ha to X-tegn ved siden av hverandre.

```text
p=antall tegn i A
q=antall tegn i X
```

| Dette legger du til et gyldig ord | Antall valg | Bidrag |
| --- | --- | --- |
| Én A-bokstav | p | p*a[n-1] |
| Én X-bokstav og deretter én A-bokstav | q*p | p*q*a[n-2] |

**Rekurrens for n≥3:**
a[n]=p*a[n-1]+p*q*a[n-2]
**Skriv som likning:** a[n]-p*a[n-1]-p*q*a[n-2]=0

### De korte ordene kan telles rett frem

```text
a1=p
a2=p^2
a3=p^3+p^2*q
```

Ved lengde 1 kan du bare velge ett A-tegn. Ved lengde 3 er de eneste mønstrene **AAA** og **AXA**: p³ valg og p²q valg. Legg sammen.

### Eksempel: A har 3 tegn og X har 6 tegn

```text
a[n]-3*a[n-1]-18*a[n-2]=0
a1=3
a3=3^3+3^2*6=27+54=81
```

Hvert tegn teller én gang. Mengden {!,*,+,−} har fire tegn. Ikke kopier likningen i oppgavens syntax help; den viser bare hvordan svar skrives.

## Side 28: Ordoppgaven: ferdige tall og generell løsning

Søk: Find the general solution to the reccurence relation • general solution • a1 • a3

**DEL a: HUSK a[n]= – SKRIV HELE LIKNINGEN!**
Eksempel når A har 3 tegn og X har 6:
Riktig: a[n]=3*a[n-1]+18*a[n-2]
Også riktig: a[n]-3*a[n-1]-18*a[n-2]=0
Ufullstendig: 3*a[n-1]+18*a[n-2]
Tallene på høyresiden er riktige. Legg a[n]= foran, så uttrykker du hva neste tall er.

**Del a ber om en likning. Del d ber om en formel i n.** I del d kan du kopiere U- og V-formlene under uten å skrive a[n]= foran.

For den samme ordregelen blir den karakteristiske likningen r²−p*r−p*q=0. De to røttene er alltid forskjellige når p,q er positive.

```text
r1=(p+sqrt(p^2+4*p*q))/2
r2=(p-sqrt(p^2+4*p*q))/2
Generell løsning: U*r1^n+V*r2^n
```

| p ; q | Rekurrens | a1 ; a3 | Røtter r1 og r2 |
| --- | --- | --- | --- |
| 3 ; 3 | a[n]=3*a[n-1]+9*a[n-2] | 3 ; 54 | (3±sqrt(45))/2 |
| 3 ; 4 | a[n]=3*a[n-1]+12*a[n-2] | 3 ; 63 | (3±sqrt(57))/2 |
| 3 ; 6 | a[n]=3*a[n-1]+18*a[n-2] | 3 ; 81 | 6 og −3 |
| 4 ; 3 | a[n]=4*a[n-1]+12*a[n-2] | 4 ; 112 | 6 og −2 |
| 5 ; 4 | a[n]=5*a[n-1]+20*a[n-2] | 5 ; 225 | (5±sqrt(105))/2 |
| 6 ; 3 | a[n]=6*a[n-1]+18*a[n-2] | 6 ; 324 | 3±sqrt(27) |
| 4 ; 4 | a[n]=4*a[n-1]+16*a[n-2] | 4 ; 128 | 2±2*sqrt(5) |
| 4 ; 6 | a[n]=4*a[n-1]+24*a[n-2] | 4 ; 160 | 2±2*sqrt(7) |

### Svar som kan kopieres når p=3,q=6

```text
U*6^n+V*(-3)^n
```

### Svar som kan kopieres når p=3,q=4

```text
U*((3+sqrt(57))/2)^n+V*((3-sqrt(57))/2)^n
```

«General solution» tillater frie konstanter når oppgaven sier det. **Begge røttene skal opphøyes i n.** Bruk sqrt(...) og eksakte brøker, ikke avrundede desimaltall.

## Side 29: Rekurrensflervalg: finn den konkrete regelen

Søk: Select every statement below which is true • zero sequence • cannot be a solution • is also a solution

Reglene nedenfor gjelder **A*a[n]+B*a[n-1]+C*a[n-2]=0**, for n≥2, med **A≠0 og C≠0**, over numeriske følger. Høyresiden 0 er viktig: likningen er homogen.

| Engelsk påstand / ord å søke etter | Hva velger du her? |
| --- | --- |
| The zero sequence a[n]=0 is a solution. | **KRYSS AV.** Bare nuller gir 0=0. |
| The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM.** Ordet «not» gjør påstanden falsk. |
| If a is a solution, then b[n]=k*a[n] is also a solution. | **KRYSS AV** for et fast tall k, også −1,4,9,13,18. |
| If a and b are solutions, then d[n]=a[n]+3*b[n] is also a solution. | **KRYSS AV.** Summer og faste multipler virker. |
| If a0=u and a1=v, then a[n] can not be a solution. | **LA STÅ TOM.** Alle to numeriske startverdier kan videreføres. Brøker er lov. |
| If a0=u, a1=v and a2=w, then a[n] could be a solution. | **KRYSS AV akkurat når A*w+B*v+C*u=0.** Ellers la stå tom. |
| If a[k]=b[k], then a[n]=b[n] for each n≥1. | **LA STÅ TOM.** Én felles verdi er ikke nok. |
| Two consecutive values equal / consecutive zero terms | **KRYSS AV.** Se 30. |
| a[n] is an integer / at least one term is not an integer | Bruk koeffisientene og startverdiene: 31. |
| None of the above | Kryss bare av hvis **alle** de andre påstandene er falske. |

Nøyaktige avkryssinger for alle de observerte rekurrensflervalgene står fra 33. Hvis alternativene flyttes, match påstandsteksten og vilkårene, ikke bare nummeret.

## Side 30: Like ledd: ett treff er ikke nok

Søk: a1=b1 and a3=b3 • a4=b4 and a5=b5 • a2=b2 and a4=b4 • a5=b5

Skriv rekurrensen som **a[n]=P*a[n-1]+Q*a[n-2]**. Her gjelder reglene for Q≠0. Se de små tallene under bokstavene.

| Dette er oppgitt | Blir hele følgene like? |
| --- | --- |
| Bare a5=b5 | **NEI.** Ett ledd gir bare én betingelse. |
| a4=b4 OG a5=b5 | **JA.** To naboverdier bestemmer resten begge veier. |
| a1=b1 OG a3=b3 | **JA når P≠0.** Finn a2 fra a3=P*a2+Q*a1. |
| a2=b2 OG a4=b4 | **JA når P≠0.** Finn a3 fra a4=P*a3+Q*a2. |
| a5=a6=a7=0 | **JA, hele følgen er null.** a5=a6=0 er allerede nok. |

### Moteksempel til din påstand 6

| n | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| a[n] | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| b[n] | 11 | 12 | −9 | −54 | −81 | 0 | 243 |

Begge følger oppfyller a[n]=2*a[n-1]−3*a[n-2]. De har samme verdi ved 5, men forskjellig verdi ved 6. Derfor skal «a5=b5 ⇒ alle like» stå tom.

### Hvis de oppgitte indeksene har større avstand

La d være avstanden mellom de to indeksene. Lag H0=0,H1=1 og **samme** regel H[n]=P*H[n-1]+Q*H[n-2].

**H[d]≠0:** de to like verdiene bestemmer hele følgen.
**H[d]=0:** de er ikke nok.
Eksempler: H2=P og H3=P²+Q. Dette krever Q≠0.

Hvis P=0, er to ledd med ett hull mellom ikke nok. Eksempel a[n]=a[n-2]: a1 og a3 bestemmer ikke a2. Hvis Q=0, kan regelen om å regne bakover svikte.

## Side 31: Heltall og tre startverdier: ferdige kontroller

Søk: an is an integer for each n • at least one index • not an integer • could be a solution

### 1. Isoler a[n], og se på tallene foran

```text
A*a[n]+B*a[n-1]+C*a[n-2]=0
a[n]=P*a[n-1]+Q*a[n-2]
P=-B/A, Q=-C/A
```

Hvis **P,Q,a0,a1 er heltall**, blir alle ledd heltall.
Da: «is an integer for each n» = **KRYSS AV**.
«At least one … is not an integer» = **LA STÅ TOM**.

| Kilde og startverdier | Riktig a2 / test | Påstanden i prøven |
| --- | --- | --- |
| B03: a0=3,a1=3 | −3/2 | Minst ett ikke heltall: **KRYSS AV** |
| B27: a0=5,a1=4 | −31/30 | Alle heltall: **LA STÅ TOM** |
| B35: a0=2,a1=2 | −6/5 | Minst ett ikke heltall: **KRYSS AV** |
| B36: a0=5,a1=5 | −25/14 | Minst ett ikke heltall: **KRYSS AV** |
| N04: a0=5,a1=3 | −9/7 | Alle heltall: **LA STÅ TOM** |
| B15: a0=48,a1=−256,foreslått a2=−1165 | Riktig a2=−1168 | Could be a solution: **LA STÅ TOM** |
| B33: a0=0,a1=−128,foreslått a2=−253 | Riktig a2=−256 | Could be a solution: **LA STÅ TOM** |

En brøk i selve koeffisientene er et signal om å undersøke, ikke et automatisk bevis. Ett brøkledd er nok til å bevise «minst ett ledd er ikke heltall». Ett heltallig a2 beviser ikke alle ledd: a[n]=(a[n-1]+a[n-2])/2,a0=0,a1=2 gir a2=1, men a3=3/2.

Tre gitte startverdier: sett u,v,w inn i **A*w+B*v+C*u**. Resultat 0 betyr at de passer. To startverdier alene kan alltid videreføres når A≠0.

## Side 32: Alle rekurrensflervalgene: match din likning

Søk: Consider the recurrence relation • coefficients • integer • 12 • 30 • 14 • -4

Her er alle de elleve forskjellige normaliserte rekurrensene vi har funnet i flervalg. N05 har halvparten av koeffisientene i B15 og gir samme regel. x[n] og a[n] betyr det samme her. Heltallskolonnen forutsetter heltallige startverdier.

| Kilde og likning | a[n]=P*a[n-1]+Q*a[n-2] | Heltall? |
| --- | --- | --- |
| B03<br>12*a[n]+2*a[n-1]+4*a[n-2]=0 | P=-1/6, Q=-1/3 | Undersøk startverdiene |
| B05<br>4*a[n]-12*a[n-1]-12*a[n-2]=0 | P=3, Q=3 | **ALLE** |
| B15 / N05 (lik etter deling)<br>4*a[n]-16*a[n-1]+12*a[n-2]=0 | P=4, Q=-3 | **ALLE** |
| B16<br>3*a[n]-9*a[n-1]+6*a[n-2]=0 | P=3, Q=-2 | **ALLE** |
| B27<br>30*a[n]+4*a[n-1]+3*a[n-2]=0 | P=-2/15, Q=-1/10 | Undersøk startverdiene |
| B33<br>4*a[n]-8*a[n-1]+8*a[n-2]=0 | P=2, Q=-2 | **ALLE** |
| B35<br>10*a[n]+1*a[n-1]+5*a[n-2]=0 | P=-1/10, Q=-1/2 | Undersøk startverdiene |
| B36<br>14*a[n]+1*a[n-1]+4*a[n-2]=0 | P=-1/14, Q=-2/7 | Undersøk startverdiene |
| N04<br>14*a[n]+1*a[n-1]+3*a[n-2]=0 | P=-1/14, Q=-3/14 | Undersøk startverdiene |
| Din prøve<br>-4*a[n]+8*a[n-1]-12*a[n-2]=0 | P=2, Q=-3 | **ALLE** |
| N07<br>3*a[n]+6*a[n-1]-6*a[n-2]=0 | P=-2, Q=2 | **ALLE** |

### Full heltallstest hvis nye tall gir brøkkoeffisienter

For **rasjonale P,Q, Q≠0 og heltallige a0,a1**, når minst én av P,Q ikke er et heltall:

a0=a1=0 → alle ledd er heltall.
a0=0,a1≠0 → minst ett ledd er ikke heltall.
Ellers: regn r=a1/a0. Alle ledd er heltall **akkurat når r er et heltall og r²−P*r−Q=0**. Da er a[n]=a0*r^n. Hvis testen feiler, kommer det minst ett brøkledd.

Eksempel: P=5/2,Q=−1,a0=1,a1=2. r=2 og 4−5+1=0, så følgen er 2^n og har bare heltall selv om P er en brøk.

## Side 33: Ferdig avkryssing: B03, B05

Søk: Consider the recurrence relation • 12*a[n]+2*a[n-1]+4*a[n-2]=0 • 4*a[n]-12*a[n-1]-12*a[n-2]=0

Match **likningen og påstandsteksten**. Numrene gjelder rekkefølgen i disse kildefilene. a[n] betyr aₙ. Flyttes alternativene, følger svaret teksten.

### B03: KRYSS AV 1, 2, 5

```text
12*a[n]+2*a[n-1]+4*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] and b[n] are two solutions, then d[n]=a[n]+3*b[n] is also a solution. | **KRYSS AV** |
| 2. If a[n] is a solution, and a0=3 and a1=3, then there exists at least one index n such that a[n] is not an integer. | **KRYSS AV** |
| 3. If a0=3, a1=−5, then a[n] can not be a solution. | **LA STÅ TOM** |
| 4. a[n] and b[n] are solutions, and if a3=b3, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 5. If a[n] is a solution, and a3=a4=a5=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 6. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |

**None of the above: LA STÅ TOM.**

### B05: KRYSS AV 1, 3, 4

```text
4*a[n]-12*a[n-1]-12*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] and b[n] are solutions, and if a1=b1 and a3=b3, then a[n]=b[n] for each n≥1. | **KRYSS AV** |
| 2. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |
| 3. If a[n] is a solution, and a1=a2=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 4. If a[n] is a solution, then b[n]=4*a[n] is also a solution. | **KRYSS AV** |
| 5. If a[n] is a solution, and a0=−1 and a1=−2, then there exists at least one index n such that a[n] is not an integer. | **LA STÅ TOM** |
| 6. If a0=0, a1=3, then a[n] can not be a solution. | **LA STÅ TOM** |

**None of the above: LA STÅ TOM.**

## Side 34: Ferdig avkryssing: B15, B16

Søk: Consider the recurrence relation • 4*a[n]-16*a[n-1]+12*a[n-2]=0 • 3*a[n]-9*a[n-1]+6*a[n-2]=0

Match **likningen og påstandsteksten**. Numrene gjelder rekkefølgen i disse kildefilene. a[n] betyr aₙ. Flyttes alternativene, følger svaret teksten.

### B15: KRYSS AV 1, 4, 5, 6

```text
4*a[n]-16*a[n-1]+12*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] is a solution, and a1=a2=a3=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 2. If a0=−3, a1=−1 then a[n] can not be a solution. | **LA STÅ TOM** |
| 3. If a0=48, a1=−256, and a2=−1165, then a[n] could be a solution. | **LA STÅ TOM** |
| 4. If a[n] and b[n] are solutions, and if a1=b1 and a3=b3, then a[n]=b[n] for each n≥1. | **KRYSS AV** |
| 5. If a[n] is a solution, and a0=0 and a1=−3, then a[n] is an integer for each n≥1. | **KRYSS AV** |
| 6. If a[n] is a solution, then b[n]=9*a[n] is also a solution. | **KRYSS AV** |

**None of the above: LA STÅ TOM.**

### B16: KRYSS AV 1, 2, 4, 6

```text
3*a[n]-9*a[n-1]+6*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] is a solution, and a0=−1 and a1=−3, then a[n] is an integer for each n≥1. | **KRYSS AV** |
| 2. If a[n] is a solution, and a4=a5=a6=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 3. If a0=−1, a1=0 then a[n] can not be a solution. | **LA STÅ TOM** |
| 4. If a[n] is a solution and b[n]=−a[n], for each n, then b[n] is also a solution. | **KRYSS AV** |
| 5. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |
| 6. If a[n] and b[n] are solutions, and if a4=b4 and a5=b5, then a[n]=b[n] for each n≥1. | **KRYSS AV** |

**None of the above: LA STÅ TOM.**

## Side 35: Ferdig avkryssing: B27, B33

Søk: Consider the recurrence relation • 30*a[n]+4*a[n-1]+3*a[n-2]=0 • 4*a[n]-8*a[n-1]+8*a[n-2]=0

Match **likningen og påstandsteksten**. Numrene gjelder rekkefølgen i disse kildefilene. a[n] betyr aₙ. Flyttes alternativene, følger svaret teksten.

### B27: KRYSS AV 1, 3

```text
30*a[n]+4*a[n-1]+3*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] is a solution, and a2=a3=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 2. a[n] and b[n] are solutions, and if a2=b2, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 3. If a[n] is a solution and b[n]=−a[n], for each n, then b[n] is also a solution. | **KRYSS AV** |
| 4. If a0=1, a1=−1, then a[n] can not be a solution. | **LA STÅ TOM** |
| 5. If a0=−1, a1=1 then a[n] can not be a solution. | **LA STÅ TOM** |
| 6. If a[n] is a solution, and a0=5 and a1=4, then a[n] is an integer for each n≥1. | **LA STÅ TOM** |

**None of the above: LA STÅ TOM.**

### B33: KRYSS AV 3, 4, 6

```text
4*a[n]-8*a[n-1]+8*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. a[n] and b[n] are solutions, and if a1=b1, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 2. If a0=0, a1=−128, and a2=−253, then a[n] could be a solution. | **LA STÅ TOM** |
| 3. If a[n] is a solution, and a1=a2=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 4. If a[n] is a solution, and a0=2 and a1=−2, then a[n] is an integer for each n≥1. | **KRYSS AV** |
| 5. If a0=−2, a1=1, then a[n] can not be a solution. | **LA STÅ TOM** |
| 6. If a[n] is a solution, then b[n]=18*a[n] is also a solution. | **KRYSS AV** |

**None of the above: LA STÅ TOM.**

## Side 36: Ferdig avkryssing: B35, B36

Søk: Consider the recurrence relation • 10*a[n]+1*a[n-1]+5*a[n-2]=0 • 14*a[n]+1*a[n-1]+4*a[n-2]=0

Match **likningen og påstandsteksten**. Numrene gjelder rekkefølgen i disse kildefilene. a[n] betyr aₙ. Flyttes alternativene, følger svaret teksten.

### B35: KRYSS AV 2, 5, 6

```text
10*a[n]+1*a[n-1]+5*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a0=3, a1=1 then a[n] can not be a solution. | **LA STÅ TOM** |
| 2. If a[n] is a solution, and a0=2 and a1=2, then there exists at least one index n such that a[n] is not an integer. | **KRYSS AV** |
| 3. a[n] and b[n] are solutions, and if a1=b1, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 4. If a0=1, a1=3, then a[n] can not be a solution. | **LA STÅ TOM** |
| 5. If a[n] is a solution, and a1=a2=a3=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 6. If a[n] is a solution and b[n]=−a[n], for each n, then b[n] is also a solution. | **KRYSS AV** |

**None of the above: LA STÅ TOM.**

### B36: KRYSS AV 1, 2, 4, 5

```text
14*a[n]+1*a[n-1]+4*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] is a solution, and a0=5 and a1=5, then there exists at least one index n such that a[n] is not an integer. | **KRYSS AV** |
| 2. If a[n] is a solution, and a2=a3=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 3. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |
| 4. If a[n] is a solution and b[n]=−a[n], for each n, then b[n] is also a solution. | **KRYSS AV** |
| 5. If a[n] and b[n] are solutions, and if a2=b2 and a4=b4, then a[n]=b[n] for each n≥1. | **KRYSS AV** |
| 6. If a0=3, a1=−4 then a[n] can not be a solution. | **LA STÅ TOM** |

**None of the above: LA STÅ TOM.**

## Side 37: Ferdig avkryssing: N04

Søk: Consider the recurrence relation • 14*a[n]+1*a[n-1]+3*a[n-2]=0

Match **likningen og påstandsteksten**. Numrene gjelder rekkefølgen i disse kildefilene. a[n] betyr aₙ. Flyttes alternativene, følger svaret teksten.

### N04: KRYSS AV 1, 3, 6

```text
14*a[n]+1*a[n-1]+3*a[n-2]=0
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] and b[n] are solutions, and if a1=b1 and a2=b2, then a[n]=b[n] for each n≥1. | **KRYSS AV** |
| 2. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |
| 3. If a[n] is a solution, then b[n]=13*a[n] is also a solution. | **KRYSS AV** |
| 4. If a[n] is a solution, and a0=5 and a1=3, then a[n] is an integer for each n≥1. | **LA STÅ TOM** |
| 5. If a0=−5, a1=−1, then a[n] can not be a solution. | **LA STÅ TOM** |
| 6. If a[n] is a solution, and a1=a2=0, then a[n]=0 for each n≥1. | **KRYSS AV** |

**None of the above: LA STÅ TOM.**

### N04: rask kontroll av heltallspåstanden

```text
14*a2+a1+3*a0=0
14*a2+3+3*5=0
a2=-18/14=-9/7
```

a2 er ikke et heltall. Derfor skal påstand 4 stå tom. «There exists at least one … not an integer» ville derimot være sann med de samme startverdiene.

Din egen variant med −4 foran x[n] har **andre koeffisienter**, og dermed en annen heltallsvurdering: se 20.

## Side 38: Din gruppeoppgave: kryss av 1, 2, 3 og 5

Søk: Consider G = ⟨x⟩ ⊆ S6 • generated by a permutation x of order 3 • The only subgroups

**KRYSS AV: 1, 2, 3 OG 5.**
**LA STÅ TOM: 4 OG «NONE OF THE ABOVE».**

Consider G = ⟨x⟩ ⊆ S6, the subgroup of the symmetric group of permutations of 6 symbols, generated by a permutation x of order 3.

Recall that a subgroup H ⊆ G is called non-trivial if H ≠ {e}, and proper if H ≠ G.

| Nr. / påstand | Velg | Kort grunn |
| --- | --- | --- |
| 1. There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **KRYSS AV** | Velg g=x. Da er ⟨g⟩=G. |
| 2. The only subgroups of G are the trivial subgroup {e}, and G itself. | **KRYSS AV** | \|G\|=3 er et primtall; en undergruppe kan bare ha 1 eller 3 elementer. |
| 3. The order of G is divisible by 3. | **KRYSS AV** | \|G\|=3, og 3/3=1. |
| 4. There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** | G er syklisk og abelsk. Her er alltid gh=hg. |
| 5. The group G is finite. | **KRYSS AV** | G har bare tre elementer. |
| 6. None of the above | **LA STÅ TOM** | Flere av påstandene over er sanne. |

```text
G={e,x,x^2}, fordi x^3=e
|G|=3
```

**Orden 3 gjelder x og dermed gruppen G som x lager.** Hele S6 har 720 elementer. I denne oppgaven velger du svar for G, som har 3.

## Side 39: Finn gruppen først: da finner du riktig svar

Søk: order of G • generated by • symmetric group • proper • non-trivial

| Dette står i oppgaven | Bruk dette |
| --- | --- |
| G=⟨x⟩, x has order d | **\|G\|=d.** G er endelig, syklisk og abelsk. Hvilken S_n den ligger inni endrer ikke dette. |
| G=S_n | **\|G\|=n!** Hele permutasjonsgruppen. For n≥3 er den ikke abelsk og ikke syklisk. |
| G=Z/m × Z/n, med addisjon | **\|G\|=m*n.** Alltid abelsk. Syklisk akkurat når gcd(m,n)=1. |
| G=P_m, med multiplikasjon modulo m | Bare 1≤a<m med gcd(a,m)=1 er med. Alltid abelsk. Ved primtall m=p er ordenen p−1 og gruppen syklisk. |

### Orden, generator og undergruppe

**Orden til G:** antall elementer i hele G. **Orden til x:** antall ganger du bruker x før du får identiteten. **⟨x⟩:** alle elementene du kan lage ved å bruke x om igjen.

**Non-trivial:** undergruppen skal ha mer enn bare identiteten. **Proper:** undergruppen skal være mindre enn G. Begge samtidig betyr **1<|H|<|G|**.

### Når G=⟨x⟩ og x har endelig orden d

| Påstand | Konkrete regler |
| --- | --- |
| Finite / cyclic / abelian | **KRYSS AV** på alle tre. |
| There exist g,h with gh ≠ hg | **LA STÅ TOM.** En syklisk gruppe er abelsk. |
| There exists g with ⟨g⟩=G | **KRYSS AV.** Velg g=x. |
| Only subgroups {e} and G | For d>1: **KRYSS AV hvis d er primtall**, ellers la stå tom. |
| Non-trivial and proper subgroup | For d>1: **KRYSS AV hvis d er sammensatt**, ellers la stå tom. |
| Order divisible by 3 | **KRYSS AV hvis d/3 er et heltall.** |

d=1 er særtilfellet G={e}. Ingen ikke-triviell ekte undergruppe finnes da. P_m er ikke alltid syklisk når m er sammensatt: P8={1,3,5,7} er et moteksempel.

## Side 40: Gruppetabell: endelig, abelsk og syklisk

Søk: The group G is abelian • not abelian • finite • infinite • cyclic • not cyclic • ab = ba • gh ≠ hg

**JA = KRYSS AV. NEI = LA STÅ TOM.**
Velg kolonnen som matcher hele gruppeteksten. ⟨x⟩ med orden 3 er en annen kolonne enn hele S6.

| Påstand | ⟨x⟩<br>ord 3 | ⟨x⟩<br>ord 6 | P5 | Z7 ×<br>Z10 | Z3 ×<br>Z10 | S3 | S6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| The group G is finite. | **JA** | **JA** | **JA** | **JA** | **JA** | **JA** | **JA** |
| The group G is infinite. | NEI | NEI | NEI | NEI | NEI | NEI | NEI |
| The group G is abelian. | **JA** | **JA** | **JA** | **JA** | **JA** | NEI | NEI |
| For all elements a,b ∈ G, the following is true: ab = ba. | **JA** | **JA** | **JA** | **JA** | **JA** | NEI | NEI |
| The group G is not abelian. | NEI | NEI | NEI | NEI | NEI | **JA** | **JA** |
| There exist elements g,h ∈ G such that gh ≠ hg. | NEI | NEI | NEI | NEI | NEI | **JA** | **JA** |
| The group G is cyclic. | **JA** | **JA** | **JA** | **JA** | **JA** | NEI | NEI |
| The group G is not cyclic. | NEI | NEI | NEI | NEI | NEI | **JA** | **JA** |

### Ord som betyr det samme her

**Abelian / commutative / ab=ba for all a,b** betyr at rekkefølgen ikke spiller noen rolle. **There exist g,h with gh≠hg / not abelian** sier det motsatte.

**Cyclic** betyr at ett bestemt element kan lage hele gruppen. Det betyr ikke at hvert element kan lage hele gruppen. Identiteten e lager bare {e}.

For Z7×Z10 og Z3×Z10 er operasjonen addisjon. Påstanden skrevet ab=ba leses som at gruppeoperasjonen er kommutativ; i additiv skrivemåte er dette a+b=b+a.

## Side 41: Gruppetabell: generatorer og undergrupper

Søk: The only subgroups • non-trivial and proper subgroup • For each element • There exists an element

**JA = KRYSS AV. NEI = LA STÅ TOM.** «There exists» trenger ett eksempel; «for each» må også virke for g=e.

| Påstand | ⟨x⟩<br>ord 3 | ⟨x⟩<br>ord 6 | P5 | Z7 ×<br>Z10 | Z3 ×<br>Z10 | S3 | S6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| There exists an element g ∈ G such that ⟨g⟩=G. | **JA** | **JA** | **JA** | **JA** | **JA** | NEI | NEI |
| There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **JA** | **JA** | **JA** | **JA** | **JA** | NEI | NEI |
| For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | NEI | NEI | NEI | NEI | NEI | **JA** | **JA** |
| For each element g ∈ G, ⟨g⟩=G. | NEI | NEI | NEI | NEI | NEI | NEI | NEI |
| There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G. | **JA** | **JA** | **JA** | **JA** | **JA** | **JA** | **JA** |
| The group G has a non-trivial and proper subgroup. | NEI | **JA** | **JA** | **JA** | **JA** | **JA** | **JA** |
| The only subgroups of G are the trivial subgroup {e}, and G itself. | **JA** | NEI | NEI | NEI | NEI | NEI | NEI |

### To feller i formuleringen

«For each element» i rad 4 er feil i alle disse gruppene: g=e lager bare {e}. «There exists ... proper» i rad 5 er derimot riktig: g=e er ett gyldig valg. Den raden sier ikke non-trivial.

**None of the above:** Kryss bare av hvis alle de andre alternativene i akkurat din liste er falske. Hvis minst ett annet alternativ er riktig, lar du «None» stå tomt.

## Side 42: Gruppetabell: alle ordenstallene i prøvene

Søk: The order of G is 3 • 4 • 6 • 12 • 30 • 70 • 720 • divisible by 3

**JA = KRYSS AV. NEI = LA STÅ TOM.** Les alltid raden med riktig tall; «order 6» er en annen påstand enn «divisible by 3».

| Påstand | ⟨x⟩<br>ord 3 | ⟨x⟩<br>ord 6 | P5 | Z7 ×<br>Z10 | Z3 ×<br>Z10 | S3 | S6 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Riktig antall elementer \|G\| | 3 | 6 | 4 | 70 | 30 | 6 | 720 |
| The order of G is 3. | **JA** | NEI | NEI | NEI | NEI | NEI | NEI |
| The order of G is 4. | NEI | NEI | **JA** | NEI | NEI | NEI | NEI |
| The order of G is 6. | NEI | **JA** | NEI | NEI | NEI | **JA** | NEI |
| The order of G is 12. | NEI | NEI | NEI | NEI | NEI | NEI | NEI |
| The order of G is 30. | NEI | NEI | NEI | NEI | **JA** | NEI | NEI |
| The order of G is 70. | NEI | NEI | NEI | **JA** | NEI | NEI | NEI |
| The order of G is 720. | NEI | NEI | NEI | NEI | NEI | NEI | **JA** |
| The order of G is divisible by 3. | **JA** | **JA** | NEI | NEI | **JA** | **JA** | **JA** |

### Hvis tallet i oppgaven blir endret

**G=⟨x⟩, ord(x)=d:** antall elementer er d. Eksempel d=5 gir en gruppe på 5 elementer med bare {e} og G som undergrupper. d=9 gir også en undergruppe på 3 elementer.

**S_n:** orden n!. S3 har 6 og S6 har 720. **Z/m×Z/n:** orden m*n. **P_p for primtall p:** orden p−1; P5 har 4.

«Divisible by k» betyr at |G|/k blir et heltall. Eksempel: 70 er ikke delelig med 3, mens 30, 6, 3 og 720 er det. Et «not» foran en egenskap snur svaret.

## Side 43: Ferdig avkryssing: orden 3 og P5

Søk: B05 • B22 • subgroup of S7 • P5 • For each element

### B05: generator med orden 3

**G=⟨x⟩ ⊆ S7, x har orden 3.** G har 3 elementer.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. The group G is infinite. | **LA STÅ TOM** |
| 2. The group G is cyclic. | **KRYSS AV** |
| 3. The group G has a non-trivial and proper subgroup. | **LA STÅ TOM** |
| 4. The order of G is 6. | **LA STÅ TOM** |
| 5. There exist elements g,h ∈ G such that gh ≠ hg. | **LA STÅ TOM** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 2.** Kilde: B05, oppgave 2. Numrene gjelder denne rekkefølgen.

### B22: P5 med multiplikasjon modulo 5

**P5={1,2,3,4}.** Orden 4, syklisk og abelsk.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G. | **LA STÅ TOM** |
| 2. The group G is infinite. | **LA STÅ TOM** |
| 3. The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| 4. The order of G is 4. | **KRYSS AV** |
| 5. For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 3, 4, 5.** Kilde: B22, oppgave 2. Numrene gjelder denne rekkefølgen.

## Side 44: Ferdig avkryssing: grupper av par

Søk: B07 • B35 • Z7 × Z10 • Z3 × Z10

### B07: Z7×Z10

**|G|=70.** Abelsk og syklisk, fordi gcd(7,10)=1.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| 2. The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| 3. The group G is infinite. | **LA STÅ TOM** |
| 4. The order of G is 70. | **KRYSS AV** |
| 5. The group G is cyclic. | **KRYSS AV** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 1, 4, 5.** Kilde: B07, oppgave 2. Numrene gjelder denne rekkefølgen.

### B35: Z3×Z10

**|G|=30.** Abelsk og syklisk, fordi gcd(3,10)=1.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. For all elements a,b ∈ G, the following is true: ab = ba. | **KRYSS AV** |
| 2. The group G is finite. | **KRYSS AV** |
| 3. The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| 4. The order of G is 30. | **KRYSS AV** |
| 5. The group G is not cyclic. | **LA STÅ TOM** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 1, 2, 3, 4.** Kilde: B35, oppgave 2. Numrene gjelder denne rekkefølgen.

## Side 45: Ferdig avkryssing: hele S3 og hele S6

Søk: B18 • B48 • B08 • B49 • symmetric group

### B18 / B48: G=S3

**Hele S3 har 6 elementer.** Gruppen er ikke abelsk og ikke syklisk.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. The group G is not abelian. | **KRYSS AV** |
| 2. The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| 3. There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **LA STÅ TOM** |
| 4. The order of G is 12. | **LA STÅ TOM** |
| 5. The group G is infinite. | **LA STÅ TOM** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 1, 2.** Kilde: B18 og den identiske B48, oppgave 2. Numrene gjelder denne rekkefølgen.

### B08 / B49: G=S6

**Hele S6 har 720 elementer.** Her står det G=S6, ikke G=⟨x⟩ med x av orden 3.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. The order of G is divisible by 3. | **KRYSS AV** |
| 2. The group G is finite. | **KRYSS AV** |
| 3. The only subgroups of G are the trivial subgroup {e}, and G itself. | **LA STÅ TOM** |
| 4. There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G. | **LA STÅ TOM** |
| 5. There exist elements g,h ∈ G such that gh ≠ hg. | **KRYSS AV** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 1, 2, 5.** Kilde: B08 og den identiske B49, oppgave 2. Numrene gjelder denne rekkefølgen.

## Side 46: Ferdig avkryssing: generator med orden 6

Søk: B34 • G = ⟨x⟩ ⊆ S5 • order 6 • non-trivial and proper

### B34: G=⟨x⟩ ⊆ S5, ord(x)=6

**G={e,x,x²,x³,x⁴,x⁵}.** Orden 6, syklisk, abelsk og endelig.

| Nr. / nøyaktig påstand | Dette velger du |
| --- | --- |
| 1. The group G is finite. | **KRYSS AV** |
| 2. The group G has a non-trivial and proper subgroup. | **KRYSS AV** |
| 3. The order of G is divisible by 3. | **KRYSS AV** |
| 4. The group G is abelian. | **KRYSS AV** |
| 5. There exists an element g ∈ G such that ⟨g⟩=G. | **KRYSS AV** |
| 6. None of the above | **LA STÅ TOM** |

**Kryss av 1, 2, 3, 4, 5.** Kilde: B34, oppgave 2. Numrene gjelder denne rekkefølgen.

### Hvorfor er alle de fem første riktige?

x er selv en generator for hele G. Fordi |G|=6 er gruppen endelig og ordenen delelig med 3. Alle elementene er potenser av x, så gruppen er abelsk.

```text
⟨x^3⟩={e,x^3}          har orden 2
⟨x^2⟩={e,x^2,x^4}      har orden 3
```

Begge disse undergruppene er større enn {e} og mindre enn G. Derfor er de både non-trivial og proper.

Sammenlign med orden 3: da finnes bare orden 1 og 3. Påstanden om en ikke-triviell ekte undergruppe blir da **falsk**. Det er ord(x), ikke tallet i S5 eller S7, som bestemmer størrelsen til ⟨x⟩.

## Side 47: Permutasjoner: først venstre, så høyre

Søk: computing with elements in the symmetric group of permutations • products • 2 × 5 matrix

**I disse prøvene leses produktet fra venstre mot høyre.** For P*Q bruker du først P og deretter Q. Dette står uttrykkelig i D3-oppgavene og bekreftes av fullscore-svarene.

En kolonne med 1 øverst og 4 nederst betyr **1→4**. Øverste rad i svaret skal være 1 2 3 4 5. Finn nederste rad ved å gjøre ett starttall om gangen.

|  | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| P sender til | 4 | 2 | 1 | 3 | 5 |
| Q sender til | 5 | 4 | 3 | 1 | 2 |

| Start | Først P | Deretter Q | Skriv |
| --- | --- | --- | --- |
| 1 | 1→4 | 4→1 | 1 |
| 2 | 2→2 | 2→4 | 4 |
| 3 | 3→1 | 1→5 | 5 |
| 4 | 4→3 | 3→3 | 3 |
| 5 | 5→5 | 5→2 | 2 |

**P*Q har nederste rad: 1 4 5 3 2.**

```text
Svar som matrise:
1 2 3 4 5
1 4 5 3 2
```

### Superkort fremgangsmåte

Les nederste rad i P: 4,2,1,3,5. Slå hvert tall opp i Q. Da får du **Q(4),Q(2),Q(1),Q(3),Q(5)** = 1,4,5,3,2.

Hver rad må ha tallene 1–5 én gang. For et produkt av flere permutasjoner følger du hele kjeden fra venstre mot høyre. Hvis en ny oppgave oppgir en annen konvensjon, bruker du den oppgitte konvensjonen.

## Side 48: Invers permutasjon: finn hvor tallene kom fra

Søk: inverse permutation • inverses • symmetric group • 2 x 5 matrix

P⁻¹ skal reversere P. Hvis P sender 1 til 4, må P⁻¹ sende 4 tilbake til 1. Finn hvor 1,2,3,4,5 står nederst i P.

```text
P:
1 2 3 4 5
4 2 1 3 5
```

| Tall du skal tilbake fra | Hvor står det nederst i P? | Inversen sender til |
| --- | --- | --- |
| 1 | Under 3 | 3 |
| 2 | Under 2 | 2 |
| 3 | Under 4 | 4 |
| 4 | Under 1 | 1 |
| 5 | Under 5 | 5 |

**P⁻¹:**
1 2 3 4 5
3 2 4 1 5

### Ny feil fra Test 3 54.65%.pdf, oppgave 2c

```text
Den gitte permutasjonen:
1 2 3 4 5
5 2 1 4 3

Riktig invers:
1 2 3 4 5
3 2 5 4 1
```

Forsøket svarte **3 2 5 4 3**. Det gjentar 3 og mangler 1. Riktig siste tall er **1**, fordi den gitte permutasjonen sender 1 til 5.

### Kontroll før levering

Følg et tall gjennom P og deretter P⁻¹: du skal komme tilbake til starttallet. Inversraden skal ha hvert tall én gang. En opphøyd −1 betyr invers, ikke at du skal ta 1 delt på hvert tall.

## Side 49: D3: hva id, r1, r2 og t1,t2,t3 betyr

Søk: dihedral group of symmetries of the regular triangle • counter-clockwise • reflection

D3 er symmetriene til en trekant. Den har seks elementer. Hjørnene er merket 1,2,3 mot klokken. Du trenger ikke tegne trekanten for hvert produkt; bruk tabellen på 50.

| Navn | Betydning i disse oppgavene | Sender 1,2,3 til |
| --- | --- | --- |
| id | Gjør ingenting. | 1,2,3 |
| r1 | Rotasjon 120°: 1 går til 2. | 2,3,1 |
| r2 | Rotasjon 240°: 1 går til 3. | 3,1,2 |
| t1 | Speiling som holder hjørne 1 fast. | 1,3,2 |
| t2 | Speiling som holder hjørne 2 fast. | 3,2,1 |
| t3 | Speiling som holder hjørne 3 fast. | 2,1,3 |

### Eksempel: t1*r1

```text
Start 1: t1 sender 1→1, deretter r1 sender 1→2
Start 2: t1 sender 2→3, deretter r1 sender 3→1
Start 3: t1 sender 3→2, deretter r1 sender 2→3
Resultat: 2,1,3 = t3
```

**t1*r1=t3**, fordi du bruker venstre symmetri først. Omvendt rekkefølge gir r1*t1=t2.

Hvis oppgaven beskriver r1 som 120° med 1→2 og t_i som speilingen som holder i fast, matcher dette tabellen. Oppgavene B10 og N01 har denne beskrivelsen.

## Side 50: D3: ferdig multiplikasjonstabell

Søk: Find the entire multiplication table for D3 • t3 ⋅ t1 • t1 ⋅ t2 • first applies a and then b

**Rad = den venstre / første symmetrien. Kolonne = den høyre / andre.** Finn ruten der raden og kolonnen møtes.

| Først ↓, så → | id | r1 | r2 | t1 | t2 | t3 |
| --- | --- | --- | --- | --- | --- | --- |
| id | id | r1 | r2 | t1 | t2 | t3 |
| r1 | r1 | r2 | id | t2 | t3 | t1 |
| r2 | r2 | id | r1 | t3 | t1 | t2 |
| t1 | t1 | t3 | t2 | id | r2 | r1 |
| t2 | t2 | t1 | t3 | r1 | id | r2 |
| t3 | t3 | t2 | t1 | r2 | r1 | id |

### Eksempler fra fullscore-prøven B10

| Uttrykk | Svar | Uttrykk | Svar |
| --- | --- | --- | --- |
| t3*t1 | r2 | t3*r2 | t1 |
| t1*t1 | id | t1*r2 | t2 |
| t2*t1 | r1 | t2*r2 | t3 |
| t3*t2 | r1 | t1*t2 | r2 |
| t2*t2 | id | r1*r2 | id |

### Kontroller som avslører feil

id-raden og id-kolonnen kopierer navnene. Hver speiling brukt to ganger gir id: t1*t1=t2*t2=t3*t3=id. r1*r2=r2*r1=id. Hver rad og kolonne skal ha hvert av de seks navnene én gang.

I feltet skriver du navn som **id**, **r1**, **r2**, **t1**, **t2**, **t3**. Svar id, ikke tallet 1, hvis det er denne navnelisten oppgaven bruker.

## Side 51: Undergruppe i Z/n: start på 0 og legg til

Søk: Find the subgroup generated by the element • Z/n • additive subgroup

For ⟨a⟩ i (Z/n,+): start på **0**, legg til a, og ta resten modulo n. Stopp når du er tilbake på 0. Alle forskjellige tall du fikk, er med.

```text
Eksempel: ⟨2⟩ i Z/8
0 → 2 → 4 → 6 → 0
Svar: {0,2,4,6}
```

### Alle enkelt-tall-variantene fra prøvefilene

| Oppgave | Ferdig svar | Kilde |
| --- | --- | --- |
| ⟨2⟩ i Z/4 | {0,2} | B09/B29 |
| ⟨0⟩ i Z/3 | {0} | B09/B21 |
| ⟨2⟩ i Z/5 | {0,1,2,3,4} | B21 |
| ⟨6⟩ i Z/9 | {0,3,6} | B23 |
| ⟨5⟩ i Z/10 | {0,5} | B23 |
| ⟨1⟩ i Z/3 | {0,1,2} | B29/B30 |
| ⟨2⟩ i Z/8 | {0,2,4,6} | B33 |
| ⟨2⟩ i Z/6 | {0,2,4} | B33 |

### Enda raskere med gcd

```text
d=gcd(n,a)
⟨a⟩={0,d,2*d,...,n-d}
Antall elementer = n/d
```

Er gcd(n,a)=1, blir hele Z/n med. Er a=0, blir svaret bare {0}. Z/8 betyr tall med addisjon modulo 8; det betyr ikke at du skal skrive brøker som 1/8 og 2/8.

En undergruppe må inneholde identiteten. Her er den **0**. Derfor er {[2,0]} alene ikke riktig for en ikke-null generator i en gruppe av par; startparet [0,0] skal også med.

## Side 52: Grupper av par: samme antall hopp i begge

Søk: Find the subgroup generated by [a,b] • direct product • Z/m × Z/n

For ⟨[a,b]⟩ i Z/m×Z/n: regn **[k*a mod m, k*b mod n]** for k=0,1,2,… til [0,0] kommer igjen. Bruk **samme k** i begge koordinatene.

### Gjennomregnet eksempel: [1,2] i Z/3×Z/4

| k | k*1 mod 3 | k*2 mod 4 | Par |
| --- | --- | --- | --- |
| 0 | 0 | 0 | [0,0] |
| 1 | 1 | 2 | [1,2] |
| 2 | 2 | 0 | [2,0] |
| 3 | 0 | 2 | [0,2] |
| 4 | 1 | 0 | [1,0] |
| 5 | 2 | 2 | [2,2] |
| 6 | 0 | 0 | Stopp: tilbake til start |

```text
Svar: {[0,0],[1,2],[2,0],[0,2],[1,0],[2,2]}
```

### Antall par før du starter

```text
L1 = m/gcd(m,a)
L2 = n/gcd(n,b)
Antall forskjellige par = lcm(L1,L2)
```

I eksemplet er L1=3 og L2=2. lcm(3,2)=6, så du skal få seks par. Du skal ikke automatisk kombinere alle førsteverdier med alle andreverdier. Parene må komme fra det samme k.

Ferdige svar til de andre generatorparene står på 53. Rekkefølgen i en mengde spiller ingen rolle, men hvert par skal bare stå én gang.

## Side 53: Generatorpar: alle de ferdige svarene

Søk: [2,0] in Z/4 × Z/3 • [0,2] • [6,5] • [1,2] • [2,2]

### B09: ⟨[2,0]⟩ i Z/4×Z/3 — 2 par

```text
{[0,0],[2,0]}
```

### B21: ⟨[0,2]⟩ i Z/3×Z/5 — 5 par

```text
{[0,0],[0,2],[0,4],[0,1],[0,3]}
```

### B23: ⟨[6,5]⟩ i Z/9×Z/10 — 6 par

```text
{[0,0],[6,5],[3,0],[0,5],[6,0],[3,5]}
```

### B29/B30: ⟨[1,2]⟩ i Z/3×Z/4 — 6 par

```text
{[0,0],[1,2],[2,0],[0,2],[1,0],[2,2]}
```

### B33: ⟨[2,2]⟩ i Z/8×Z/6 — 12 par

```text
{[0,0],[2,2],[4,4],[6,0],[0,2],[2,4],
 [4,0],[6,2],[0,4],[2,0],[4,2],[6,4]}
```

**Skriv en mengde av par:** {[0,0],[2,0]}, ikke bare {[2,0]}. Bruk krøllparenteser rundt hele mengden og firkantparenteser rundt hvert par.

Kontroll: [0,0] er med, generatorparet er med, antall par stemmer med lcm-formelen, og neste hopp fra siste par gir [0,0].

## Side 54: Modulo-produkt: gang og behold resten

Søk: In this problem you are tasked with computing products and inverses • integers and multiplication modulo • P50 • coprime

I P_m er tallene mellom 1 og m−1 som ikke har felles faktor med m, med i gruppen. Regneoperasjonen er **vanlig multiplikasjon, så rest etter deling på m**. Identiteten er 1.

```text
a ∙m b = (a*b) mod m
r = a*b - m*Intg((a*b)/m)
```

**Intg er gulvfunksjonen:** rund nedover til nærmeste heltall. Med positive tall betyr det å fjerne desimalene. Med negative tall må du fortsatt runde nedover, for eksempel Intg(−18/13)=−2.

### Din prøve: ferdige svar i P50

| Oppgave | Regn vanlig først | Trekk fra 50-ere | Skriv |
| --- | --- | --- | --- |
| 37 ∙50 39 | 37*39=1443 | 1443−28*50=43 | **43** |
| 39 ∙50 43 | 39*43=1677 | 1677−33*50=27 | **27** |
| 43 ∙50 29 | 43*29=1247 | 1247−24*50=47 | **47** |
| 37⁻¹ mod 50 | 37*23=851 | 851−17*50=1 | **23** |

### Kalkulator: skriv ett uttrykk

```text
37*39-50*Intg((37*39)/50)
Svaret er 43.
```

For andre oppgaver bytter du bare ut 37, 39 og 50 med tallene dine. Svaret skal ligge mellom 0 og m−1. Når begge faktorene er i P_m, ligger også svaret i P_m, så det kan ikke bli 0.

**«Coprime to m» betyr gcd(x,m)=1.**
P9={1,2,4,5,7,8}. Tallene 3 og 6 er ikke med.
P8={1,3,5,7}. Alle partall er utelatt.

## Side 55: Invers modulo m: finn tallet som gir rest 1

Søk: inverse • a^-1 • inverses • extended Euclidean algorithm • TABLE • 43 inverse mod 50

**a⁻¹ mod m er tallet x som gjør (a*x) mod m = 1.**
Det er ikke desimaltallet 1/a. En invers finnes akkurat når gcd(a,m)=1.

### Raskt på kalkulator: søk etter rest 1

Åpne **TABLE**. For å finne inversen til 43 modulo 50, bruk funksjonen under. La X gå fra 1 til 49 med steg 1. Finn raden med Y=1. **X-verdien i den raden er svaret.**

```text
Y = 43*X - 50*Intg((43*X)/50)
Ved X=7 får du Y=1. Derfor er inversen 7.
```

Du kan også prøve bare tallene i P_m. Et tall uten felles faktor med m er den eneste typen kandidat som kan gi rest 1.

### Uten tabell: utvidet Euklid, ferdig eksempel

```text
50 = 1*43 + 7
43 = 6*7 + 1

1 = 43 - 6*7
  = 43 - 6*(50-43)
  = 7*43 - 6*50
```

Koeffisienten foran 43 er 7. Derfor er **43⁻¹ mod 50 = 7**. Hvis koeffisienten hadde vært negativ, tar du resten modulo 50 for å få svaret mellom 0 og 49.

### Sjekk alltid med én multiplikasjon

| Invers du vil kontrollere | Kontroll | Riktig |
| --- | --- | --- |
| 37⁻¹ mod 50 = 23 | 37*23=851=17*50+1 | Ja |
| 29⁻¹ mod 46 = 27 | 29*27=783=17*46+1 | Ja |
| 25⁻¹ mod 49 = 2 | 25*2=50=49+1 | Ja |

Ferdige små tabeller står på 56 og 57. Konkrete større prøvetall står på 58 og 59.

## Side 56: Ferdige multiplikasjons- og inverstabeller: P5 og P7

Søk: Compute the missing entries in the group multiplication table • P5 • P7 • multiplication modulo 5 • modulo 7

Finn venstre faktor som **rad**, og høyre faktor som **kolonne**. Tallet der de møtes, er svaret. Tabellen er fullstendig, også når prøven bare skjuler ni ruter.

### P5 = {1,2,3,4}

| ∙5 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| 1 | 1 | 2 | 3 | 4 |
| 2 | 2 | 4 | 1 | 3 |
| 3 | 3 | 1 | 4 | 2 |
| 4 | 4 | 3 | 2 | 1 |

| a | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| a⁻¹ | 1 | 3 | 2 | 4 |

### P7 = {1,2,3,4,5,6}

| ∙7 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 2 | 3 | 4 | 5 | 6 |
| 2 | 2 | 4 | 6 | 1 | 3 | 5 |
| 3 | 3 | 6 | 2 | 5 | 1 | 4 |
| 4 | 4 | 1 | 5 | 2 | 6 | 3 |
| 5 | 5 | 3 | 1 | 6 | 4 | 2 |
| 6 | 6 | 5 | 4 | 3 | 2 | 1 |

| a | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| a⁻¹ | 1 | 4 | 5 | 2 | 3 | 6 |

Eksempler: 3 ∙5 4 = **2**, fordi 12 har rest 2 ved deling på 5.
4 ∙7 6 = **3**, fordi 24 har rest 3 ved deling på 7.
En invers er plassen der produktet blir **1**.

## Side 57: Ferdige multiplikasjons- og inverstabeller: P8 og P9

Søk: Compute the missing entries in the group multiplication table • P8 • P9 • multiplication modulo 8 • modulo 9 • 8*4

### P8 = {1,3,5,7}

| ∙8 | 1 | 3 | 5 | 7 |
| --- | --- | --- | --- | --- |
| 1 | 1 | 3 | 5 | 7 |
| 3 | 3 | 1 | 7 | 5 |
| 5 | 5 | 7 | 1 | 3 |
| 7 | 7 | 5 | 3 | 1 |

| a | 1 | 3 | 5 | 7 |
| --- | --- | --- | --- | --- |
| a⁻¹ | 1 | 3 | 5 | 7 |

### P9 = {1,2,4,5,7,8}

| ∙9 | 1 | 2 | 4 | 5 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 2 | 4 | 5 | 7 | 8 |
| 2 | 2 | 4 | 8 | 1 | 5 | 7 |
| 4 | 4 | 8 | 7 | 2 | 1 | 5 |
| 5 | 5 | 1 | 2 | 7 | 8 | 4 |
| 7 | 7 | 5 | 1 | 8 | 4 | 2 |
| 8 | 8 | 7 | 5 | 4 | 2 | 1 |

| a | 1 | 2 | 4 | 5 | 7 | 8 |
| --- | --- | --- | --- | --- | --- | --- |
| a⁻¹ | 1 | 5 | 7 | 2 | 4 | 8 |

**Feilen i Test 3 54.65%: 8 ∙9 4 = 5.**
8*4=32, og 32−3*9=5. Svaret er ikke 0.
I P8 er hvert element sin egen invers. Det betyr for eksempel 3*3 mod 8 = 1.

Ni ruter mangler: slå opp **hvert produkt** fra oppgavelisten i tabellen. Rekkefølgen på de ni produktene varierer mellom prøvene; tallene i tabellen gjelder alle variantene.

## Side 58: Konkrete prøvesvar: produkter og inverser modulo 45–49

Søk: P45 • P46 • P48 • P49 • 29 inverse • 25 inverse • 36 inverse • products and inverses

Velg først **riktig m**. Finn deretter nøyaktig samme produkt eller invers som i oppgaven din. Svarene er regnet på nytt, også der gamle forsøk hadde feil.

| mod m | Første produkt | Andre produkt | Tredje produkt | Invers |
| --- | --- | --- | --- | --- |
| 45 | 44*29 → **16** | 29*28 → **2** | 28*37 → **1** | 44⁻¹ → **44** |
| 46 | 29*41 → **39** | 41*37 → **45** | 37*31 → **43** | 29⁻¹ → **27** |
| 46 | 33*45 → **13** | 45*29 → **17** | 29*41 → **39** | 33⁻¹ → **7** |
| 46 | 27*43 → **11** | 43*39 → **21** | 39*29 → **27** | 27⁻¹ → **29** |
| 48 | 37*41 → **29** | 41*29 → **37** | 29*35 → **7** | 37⁻¹ → **13** |
| 49 | 36*27 → **41** | 27*32 → **31** | 32*31 → **12** | 36⁻¹ → **15** |
| 49 | 25*30 → **15** | 30*43 → **16** | 43*29 → **22** | 25⁻¹ → **2** |
| 49 | 39*37 → **22** | 37*26 → **31** | 26*45 → **43** | 39⁻¹ → **44** |

### To feil i eldre forsøk: disse tallene skal du skrive

**29⁻¹ mod 46 = 27**, ikke 29.
**25⁻¹ mod 49 = 2**, ikke 49.
Et svar på en invers skal gi rest 1 når du ganger tilbake.

### Slik leser du første rad

```text
44*29 mod 45 = 16
29*28 mod 45 = 2
28*37 mod 45 = 1
44^(-1) mod 45 = 44
```

Andre tall? Bruk gang-og-rest-metoden på 54. For invers bruker du søk etter rest 1 eller Euklid på 55.

## Side 59: Konkrete prøvesvar: alle kjente P50-variantene

Søk: P50 • modulo 50 • 31 inverse • 29 inverse • 43 inverse • 37 inverse • test3_0%.pdf

Her er hver kjente P50-liste med sine **tre produkter og én invers**. Match tallene fra din oppgave. Alle pilene nedenfor viser ferdig svar.

| Variant | Produkt 1 | Produkt 2 | Produkt 3 | Invers |
| --- | --- | --- | --- | --- |
| B07 | 31*33 → **23** | 33*29 → **7** | 29*41 → **39** | 31⁻¹ → **21** |
| B23/B46 | 29*27 → **33** | 27*43 → **11** | 43*37 → **41** | 29⁻¹ → **19** |
| N02 | 43*37 → **41** | 37*47 → **39** | 47*31 → **7** | 43⁻¹ → **7** |
| Din prøve | 37*39 → **43** | 39*43 → **27** | 43*29 → **47** | 37⁻¹ → **23** |

**Viktig rettelse: 31⁻¹ mod 50 = 21.**
31*21=651=13*50+1. Det gamle svaret 19 gir rest 39 og er feil.

### Alle inversene i P50: slå opp tallet ditt

| a | a⁻¹ mod 50 | a | a⁻¹ mod 50 |
| --- | --- | --- | --- |
| 1 | **1** | 27 | **13** |
| 3 | **17** | 29 | **19** |
| 7 | **43** | 31 | **21** |
| 9 | **39** | 33 | **47** |
| 11 | **41** | 37 | **23** |
| 13 | **27** | 39 | **9** |
| 17 | **3** | 41 | **11** |
| 19 | **29** | 43 | **7** |
| 21 | **31** | 47 | **33** |
| 23 | **37** | 49 | **49** |

N02 er test3_0%.pdf. B07 og B23/B46 er tidligere prøvefiler og løsningsnotater i kildeoversikten. **«Din prøve»** er skjermbildet du sendte. Produkter med nye tall løses på 54.

## Side 60: Indeks i (Z/2)^k: tell og del

Søk: What is the index of H ⊂ G • Let G = (Z/2) • subgroup • [G:H] • index

**[G:H] = antall elementer i G / antall elementer i H.**
For G=(Z/2)^k er |G|=2^k. Tell hele vektorer i H, ikke antall nuller og enere inni dem.

### Eksempel med fem plasser i hver vektor

```text
G=(Z/2)^5
H={[0,0,0,0,0], [0,0,0,0,1],
   [0,1,1,0,0], [0,1,1,0,1]}

|G|=2^5=32
|H|=4 hele vektorer
[G:H]=32/4=8
Skriv: 8
```

### Ferdig tabell for listene i prøvene

| G | Antall vektorer i H | Regning | Skriv |
| --- | --- | --- | --- |
| (Z/2)^4 | 2 | 16/2 | **8** |
| (Z/2)^4 | 4 | 16/4 | **4** |
| (Z/2)^4 | 8 | 16/8 | **2** |
| (Z/2)^5 | 2 | 32/2 | **16** |
| (Z/2)^5 | 4 | 32/4 | **8** |
| (Z/2)^5 | 8 | 32/8 | **4** |
| (Z/2)^5 | 16 | 32/16 | **2** |

Har oppgaven andre k eller flere vektorer, bruk samme formel. H er oppgitt som en undergruppe i disse oppgavene; du trenger bare å telle de forskjellige vektorene.

### Hvis H er gitt med en generator i stedet for en liste

I (Z/2)^k blir en ikke-null vektor lagt til seg selv lik null. Dermed har ⟨v⟩ bare **to** elementer: nullvektoren og v. Da er indeksen 2^k/2. Er generatoren nullvektoren, har H ett element og indeksen er 2^k.

## Side 61: Kvadratgruppen D4: ferdige indekssvar

Søk: Let D4 be the dihedral group of order 8 • symmetry that rotates • reflects around the line • Compute the index of the subgroup generated by σ

D4 har **8 elementer**. Finn hvor mange ganger symmetrien må gjentas for å komme tilbake til start. Det tallet er |⟨σ⟩|. Del så 8 på tallet.

| Dette står i oppgaven | \|⟨σ⟩\| | [D4:⟨σ⟩] — skriv |
| --- | --- | --- |
| Rotates 90°, −90° eller 270° | 4 | **2** |
| Rotates 180° eller −180° | 2 | **4** |
| Reflects around x=0, y=0, y=x eller y=−x | 2 | **4** |
| Identity / rotates 0° eller 360° | 1 | **8** |

**Gammelt forsøk med −90° svarte 4. Riktig svar er 2.**
Fire kvartomdreininger trengs for å komme tilbake: |⟨σ⟩|=4. Da blir indeksen 8/4=2.

### Hvis det står ⟨σ²⟩, ⟨σ⁴⟩ eller en annen potens

Finn først symmetrien **σ^t**, og bruk deretter tabellen. Hvis σ er en kvartomdreining, er σ² en halv omdreining og σ⁴ identiteten.

| σ er en kvartomdreining | Orden til σ^t | Skriv indeks |
| --- | --- | --- |
| t=0,4,8,… | 1 | **8** |
| t=1,3,5,7,… | 4 | **2** |
| t=2,6,10,… | 2 | **4** |

```text
Generell regel: ord(σ^t)=d/gcd(d,t), der d=ord(σ).
Indeksen er 8 / ord(σ^t).
```

For en speiling: oddetallspotens er samme speiling → indeks **4**. Partallspotens er identiteten → indeks **8**. Eksempel: ⟨σ⁴⟩ for en −90°-rotasjon er {id}, så svaret er **8**.

## Side 62: Casio fx-9860GIII: raske, kontrollerbare regninger

Søk: calculator • Casio • EQUA • POLY • Intg • TABLE • RECUR • roots • inverse

### 1. Finn røttene i en andreordens rekurrens

For A*a[n]+B*a[n-1]+C*a[n-2]=0 skal du løse **A*r²+B*r+C=0**. Åpne **MENU → EQUA → POLY → grad 2**, og tast A, B og C med fortegn.

```text
a[n]+6*a[n-1]+9*a[n-2]=0
Tast: A=1, B=6, C=9
Roten er -3 to ganger.
```

To like røtter krever formen (U+V*n)*r^n. To ulike røtter krever U*r1^n+V*r2^n. Kalkulatoren finner røttene; du må fortsatt velge riktig formel og bruke startverdiene.

### 2. Rest etter deling: ett uttrykk

```text
Rest av X ved deling på m:
X-m*Intg(X/m)

Eksempel negativt tall:
-18-13*Intg(-18/13) = 8
```

Bruk **Intg**, som runder nedover. Int er en annen funksjon og kan gi feil rest for negative tall. Resten ved positiv m skal være fra 0 til m−1.

### 3. Invers: TABLE leter etter rest 1

```text
Y=a*X-m*Intg((a*X)/m)
X fra 1 til m-1, steg 1.
Finn raden Y=1. Svaret er X i denne raden.
```

Eksempel a=37,m=50: raden X=23 gir Y=1. Derfor er inversen **23**. Fremgangsmåten og Euklid står på 55.

### 4. Kontroller noen ledd i RECUR

I RECUR kan du skrive en andreordens regel i formen a[n+2]=P*a[n+1]+Q*a[n], og angi a0,a1. For prøven din er regelen a[n+2]=2*a[n+1]−3*a[n]. Med a0=−3,a1=0 får du de neste leddene **9,18,9,−36**.

Noen riktige ledd er en **kontroll**, ikke et bevis for en påstand om alle n. For «all terms are integers» bruker du også heltallsregelen i rekurrensdelen.

## Side 63: Svarfelt: skriv dette, og sjekk disse fellene

Søk: Your last answer was interpreted as follows • answer syntax • missing entries • powers • parentheses • None of the above

| Når du skal skrive | Slik skriver du | Pass på |
| --- | --- | --- |
| Et tall eller en indeks | 8 | Ikke skriv selve regningen hvis feltet ber om ett tall. |
| En brøk | -62/5 | Eksakt brøk er sikrere enn avrundet desimaltall. |
| En potens | (-3)^n | Parentes rundt negativt grunntall. |
| Minus foran en potens | -3^n | Dette betyr −(3^n), ikke (−3)^n. |
| Gangetegn i en formel | (1+2*n)*(-3)^n | Bruk * mellom tall, n og parenteser. |
| Kvadratrot | sqrt(57) | Ikke bytt til en avrundet rot når svaret skal være eksakt. |
| Sett av vektorer | {[0,0],[1,1]} | Krøllparenteser rundt mengden; hver vektor samlet. |
| En permutasjon | 2 × 5 matrise slik feltet ber om | Hvert tall fra 1 til 5 én gang i hver rad. |
| None of the above | Kryss bare hvis alle andre påstander er falske | Ikke kombiner «None» med et sant alternativ. |

### Tre siste kontroller før du leverer

**Produkt modulo m:** er svaret mellom 0 og m−1, og i P_m når faktorene er der?
**Invers:** gir originaltallet ganger svaret rest 1?
**Indeks:** har du delt antall elementer i hele gruppen på antall i undergruppen?

Hvis nettsiden viser en forhåndsvisning, les den. Se særlig etter at minus, parenteser, eksponenter og brøkstreker er tolket slik du mente.

Ferdige avkryssinger gjelder påstandene og vilkårene de står ved. Når oppgaven bytter rekkefølge, match **teksten**. Når tall eller likning endres, bruk regelen og det nye tallet.

## Side 64: Seks nye prøver: dette er nyttig å øve på

Søk: 6. november 2026 • delprøve_3_92% • quiz3_100 • S2 • N05 • N06 • N07 • N08 • N09 • N10

De seks nye filene inneholder **18 regneoppgaver**. Ingen ny oppgavefamilie er nødvendig, men vi har fått **en ny konkret gruppeprofil, to nye ordvarianter, nye rekurrensflervalg og nye tall i partikulære løsninger**. Dette oppslaget gir de nye eksemplene; kildeoversikten kobler alle oppgavene til metode.

| Fil / kilde | Nyttig tillegg | Slå opp |
| --- | --- | --- |
| N05: Matric (1).pdf | S2 som egen gruppeprofil. Rekurrens med koeffisienter 2,−8,6. | Profil 11; flervalg 67 |
| N06: delprøve_3_92%.pdf | Ord med p=4,q=4. Røttene er ikke 4 og −4. Nye P49-produkter. | Ord 65; P49 58 |
| N07: Test 3_1_66%.pdf | Tre foreslåtte starttall: siste er tre unna riktig verdi. D3 og indeks bruker kjente tabeller. | Flervalg 67; D3 50 |
| N08: Test 3, forsøk 1, 100%.pdf | Ord med p=4,q=6. Alle fire viste ordsvar er matematisk riktige, selv om delpoeng vises. | Ord 65 |
| N09: quiz3_100.pdf | Negativ koeffisient −1/3 og a0=7. En annen løsning og a1 er to separate spørsmål. | Eksempel 66 |
| N10: Matric.pdf | 4*a[n-1]−2*a[n]. Tillegget er +2^n. Den oppgitte p[n] skal kopieres uendret. | Eksempel 66 |

### S2 er unntaket du må kjenne igjen

S2 har **to elementer**, er **syklisk og abelsk**, og har bare undergruppene {e} og S2. Den har ingen ikke-triviell ekte undergruppe. Derfor får S2 andre avkryssinger enn hele S3 og S6. Bruk den nye svarprofilen.

Filnavn og prosent er ikke fasit. Vi kontrollerer regningen. N08 heter «100%», men selve oppgave 1 viser 0.75/1. PDF-en viser ikke hvorfor poengene ble trukket; de fire viste matematiske svarene passer med ordreglene.

Permutasjoner, D3, P5 og indeks bruker metodene som allerede stod i hjelpearket. P49-varianten er lagt til i talloppslaget. Det er nå **60 PDF-kilder og 49 ulike prøveforsøk, med 147 regneoppgaver**, etter fjerning av identiske kopier.

## Side 65: Nye ordvarianter: p=4 med q=4 eller q=6

Søk: Let A and X • general solution • a1 • a3 • 128 • 160 • sqrt(5) • sqrt(7)

Reglene er de samme: start i A, slutt i A og ingen to X-tegn ved siden av hverandre. Tell **p=antall tegn i A**, **q=antall tegn i X**. Så bruker du a[n]=p*a[n-1]+p*q*a[n-2] for n≥3.

### N06: A={a,b,c,d}, X={!,*,+,−}

```text
p=4, q=4
a[n]=4*a[n-1]+16*a[n-2]
a1=4
a3=4^3+4^2*4=128

r^2-4*r-16=0
r1=2+2*sqrt(5)
r2=2-2*sqrt(5)
```

**Generell løsning – skriv:**
U*(2+2*sqrt(5))^n+V*(2-2*sqrt(5))^n

Forsøket brukte A*4^n+B*(−4)^n. Tallene 4 og −4 er ikke røtter i r²−4r−16=0. Ved r=4 får du 16−16−16=−16, ikke 0. **Bruk EQUA med koeffisientene 1,−4,−16**, eller rotformelen. Ikke velg røtter ved å se bare på tallet 16.

### N08: A har 4 tegn, X={!,%,&,*,+,−} har 6

```text
p=4, q=6
a[n]=4*a[n-1]+24*a[n-2]
a1=4
a3=4^3+4^2*6=160

r^2-4*r-24=0
r1=2+2*sqrt(7), r2=2-2*sqrt(7)
```

**Generell løsning – skriv:**
U*(2+2*sqrt(7))^n+V*(2-2*sqrt(7))^n

De fire viste svarene i N08 samsvarer med disse beregningene. Oppgaven viser likevel 0.75/1. PDF-en gir ikke nok til å fastslå årsaken til poengtapet. Beregningen over er kontrollert ved innsetting.

## Side 66: Nye partikulære løsninger: kopier p[n] og finn fortegnet

Søk: another solution • particular solution • 4*a[n-1]-2*a[n] • a[n]/3 • 2^n • -59/30

### N10: to feil i det innleverte svaret i del a

```text
4*a[n-1]-2*a[n]=1/3^n
p[n]=1/(10*3^n)

A=-2, B=4
r=-B/A=-4/(-2)=2
```

**En annen løsning – skriv:**
1/(10*3^n)+2^n

Det innleverte svaret var 1/(30*3^n)+(4/−2)^n. Her er både p[n] og fortegnet på tillegget endret. **Behold 10, ikke 30.** Regelen er −B/A, så −4/(−2) blir **+2**. Det er ikke B/A=−2.

### Del b: bruk a0=−9/10 rett i likningen

```text
4*(-9/10)-2*a1=1/3
-2*a1=1/3+18/5=59/15
a1=-59/30
```

Uttrykket som ble levert i del b, (1/3−4*(−9/10))/(−2), gir nettopp −59/30. En annen løsning valgt i del a trenger ikke ha startverdien som først innføres i del b.

### N09: −1/3 foran a[n]

```text
-a[n]/3-a[n-1]=(-2)^n
p[n]=-3*(-2)^(n+1)
A=-1/3, B=-1
r=-B/A=1/(-1/3)=-3
```

**En annen løsning:**
-3*(-2)^(n+1)+(-3)^n

**Med a0=7 i del b:**
-a1/3-7=-2  →  a1=-15

Sjekk tillegget alene: r^n skal gi 0 i venstresiden. For N10 gir 4*2^(n−1)−2*2^n=0. For N09 gir −(−3)^n/3−(−3)^(n−1)=0. Da kan tillegget legges til den oppgitte p[n].

## Side 67: Nye rekurrensflervalg: ferdige valg for N05 og N07

Søk: 2*a[n]-8*a[n-1]+6*a[n-2]=0 • 3*a[n]+6*a[n-1]-6*a[n-2]=0 • -357

Match både likningen og påstandsteksten. Valgnumrene gjelder rekkefølgen i disse to filene.

### N05: KRYSS AV 2, 5 OG 6

```text
2*a[n]-8*a[n-1]+6*a[n-2]=0
a[n]=4*a[n-1]-3*a[n-2]
```

| Hele påstanden | Velg |
| --- | --- |
| 1. The zero sequence a[n]=0 is not a solution. | **LA STÅ TOM** |
| 2. If a[n] is a solution, and a0=0 and a1=2, then a[n] is an integer for each n≥1. | **KRYSS AV** |
| 3. If a0=4, a1=−3 then a[n] can not be a solution. | **LA STÅ TOM** |
| 4. a[n] and b[n] are solutions, and if a2=b2, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 5. If a[n] is a solution, and a2=a3=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 6. If a[n] and b[n] are two solutions, then d[n]=a[n]+13*b[n] is also a solution. | **KRYSS AV** |

None of the above: **LA STÅ TOM**. Begrunnelser: heltallige koeffisienter; to nabonuller; lineær kombinasjon. Gruppeoppgaven i samme fil gjelder S2: bare «The group G is cyclic» er sann i dens alternativliste.

### N07: KRYSS AV 1 OG 3

```text
3*a[n]+6*a[n-1]-6*a[n-2]=0
a[n]=-2*a[n-1]+2*a[n-2]
```

| Hele påstanden | Velg |
| --- | --- |
| 1. If a[n] is a solution, and a4=a5=a6=0, then a[n]=0 for each n≥1. | **KRYSS AV** |
| 2. If a0=−18, a1=162, and a2=−357, then a[n] could be a solution. | **LA STÅ TOM** |
| 3. If a[n] is a solution, then b[n]=13*a[n] is also a solution. | **KRYSS AV** |
| 4. a[n] and b[n] are solutions, and if a4=b4, then a[n]=b[n] for each n≥1. | **LA STÅ TOM** |
| 5. If a0=−1, a1=0, then a[n] can not be a solution. | **LA STÅ TOM** |
| 6. If a[n] is a solution, and a0=0 and a1=0, then there exists at least one index n such that a[n] is not an integer. | **LA STÅ TOM** |

None of the above: **LA STÅ TOM**. I påstand 2 må tredje tall være −2*162+2*(−18)=**−360**, ikke −357. I påstand 6 gir to startnuller bare nuller, som er heltall.

## Side 68: Kildesjekk: prøvefilene 1

Søk: Originalprøver • kildeoversikt • coverage • B01–B50 • N01–N04

Hver regneoppgave er koblet til et oppslag. Sidetallet under oppgavetypen viser hvor du begynner. Kopier er merket.

| Kilde / fil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| B01<br>2 av 3/2 av 3___1.pdf | Antall ord<br>27, 28 | D3-tabell<br>50 | Indeks<br>60, 61 |
| B02<br>2 av 3/2 av 3___2.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| B03<br>2 av 3/2 av 3___3.pdf | Rekurrensflervalg<br>33 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B04<br>2 av 3/2 av 3___4.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B05<br>2 av 3/2 av 3___5.pdf | Rekurrensflervalg<br>33 | Gruppeflervalg<br>43 | Produkt / invers<br>54, 58, 59 |
| B06<br>2 av 3/2 av 3___6.pdf | Ulike røtter<br>21, 22 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| B07<br>2 av 3/2.08 av 3___1.pdf | Ulike røtter<br>21, 22 | Gruppeflervalg<br>44 | Produkt / invers<br>54, 58, 59 |
| B08<br>2 av 3/2.33 av 3___1.pdf | Ulike røtter<br>21, 22 | Gruppeflervalg<br>45 | Indeks<br>60, 61 |
| B09<br>2 av 3/2.42 av 3___1.pdf | Dobbel rot<br>22 | Undergrupper<br>51, 52, 53 | P_m-tabell<br>56, 57 |
| B10<br>2 av 3/2.50 av 3 ___ 5.pdf | Antall ord<br>27, 28 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B11<br>2 av 3/2.50 av 3___1.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B12<br>2 av 3/2.50 av 3___2.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B13<br>2 av 3/2.50 av 3___3.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B14<br>2 av 3/2.50 av 3___4.pdf | Gitt p[n]<br>25, 26 | D3-tabell<br>50 | Produkt / invers<br>54, 58, 59 |

## Side 69: Kildesjekk: prøvefilene 2

Søk: Originalprøver • kildeoversikt • coverage • B01–B50 • N01–N04

Hver regneoppgave er koblet til et oppslag. Sidetallet under oppgavetypen viser hvor du begynner. Kopier er merket.

| Kilde / fil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| B15<br>2 av 3/2.75 av 3___1.pdf | Rekurrensflervalg<br>34 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B16<br>2 av 3/tet 3 2.75 av 3.pdf | Rekurrensflervalg<br>34 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B17<br>3 av 3/3 av 3___1.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B18<br>3 av 3/3 av 3___10.pdf | Gitt p[n]<br>25, 26 | Gruppeflervalg<br>45 | P_m-tabell<br>56, 57 |
| B19<br>3 av 3/3 av 3___2.pdf | Ulike røtter<br>21, 22 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B20<br>3 av 3/3 av 3___3.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | Produkt / invers<br>54, 58, 59 |
| B21<br>3 av 3/3 av 3___4.pdf | Dobbel rot<br>22 | Undergrupper<br>51, 52, 53 | P_m-tabell<br>56, 57 |
| B22<br>3 av 3/3 av 3___5.pdf | Gitt p[n]<br>25, 26 | Gruppeflervalg<br>43 | Indeks<br>60, 61 |
| B23<br>3 av 3/3 av 3___6.pdf | Ulike røtter<br>21, 22 | Undergrupper<br>51, 52, 53 | Produkt / invers<br>54, 58, 59 |
| B24<br>3 av 3/3 av 3___7.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| B25<br>3 av 3/3 av 3___8.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B26<br>3 av 3/3 av 3___9.pdf | Ulike røtter<br>21, 22 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| B27<br>alt under 2 av 3/0 av 3___1.pdf | Rekurrensflervalg<br>35 | D3-tabell<br>50 | Indeks<br>60, 61 |
| B28<br>alt under 2 av 3/0.75 av 3___1.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | Produkt / invers<br>54, 58, 59 |

## Side 70: Kildesjekk: prøvefilene 3

Søk: Originalprøver • kildeoversikt • coverage • B01–B50 • N01–N04

Hver regneoppgave er koblet til et oppslag. Sidetallet under oppgavetypen viser hvor du begynner. Kopier er merket.

| Kilde / fil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| B29<br>alt under 2 av 3/1 av 3___1.pdf | Gitt p[n]<br>25, 26 | Undergrupper<br>51, 52, 53 | Indeks<br>60, 61 |
| B30 (kopi av B29)<br>alt under 2 av 3/1 av 3___2.pdf | Gitt p[n]<br>25, 26 | Undergrupper<br>51, 52, 53 | Indeks<br>60, 61 |
| B31<br>alt under 2 av 3/1 av 3___3.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| B32<br>alt under 2 av 3/1.25 av 3___1.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | Produkt / invers<br>54, 58, 59 |
| B33<br>alt under 2 av 3/1.33 av 3___1.pdf | Rekurrensflervalg<br>35 | Undergrupper<br>51, 52, 53 | Indeks<br>60, 61 |
| B34<br>alt under 2 av 3/1.40 av 3___1.pdf | Antall ord<br>27, 28 | Gruppeflervalg<br>44 | P_m-tabell<br>56, 57 |
| B35<br>alt under 2 av 3/1.42 av 3___1.pdf | Rekurrensflervalg<br>36 | Gruppeflervalg<br>46 | Indeks<br>60, 61 |
| B36<br>alt under 2 av 3/1.50 av 3___1.pdf | Rekurrensflervalg<br>36 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| B37<br>alt under 2 av 3/1.56 av 3___1.pdf | Gitt p[n]<br>25, 26 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B38<br>alt under 2 av 3/1.67 av 3___1.pdf | Gitt p[n]<br>25, 26 | D3-tabell<br>50 | Produkt / invers<br>54, 58, 59 |
| B39<br>alt under 2 av 3/1.89 av 3___1.pdf | Ulike røtter<br>21, 22 | D3-tabell<br>50 | Produkt / invers<br>54, 58, 59 |
| B43<br>regler/Test 3 100%.pdf | Gitt p[n]<br>25, 26 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| B48 (kopi av B18)<br>regler/test3_3p.pdf | Gitt p[n]<br>25, 26 | Gruppeflervalg<br>45 | P_m-tabell<br>56, 57 |
| B49 (kopi av B08)<br>regler/test3_77% (1).pdf | Ulike røtter<br>21, 22 | Gruppeflervalg<br>45 | Indeks<br>60, 61 |

## Side 71: Kildesjekk: prøvefilene 4

Søk: Originalprøver • kildeoversikt • coverage • B01–B50 • N01–N04

Hver regneoppgave er koblet til et oppslag. Sidetallet under oppgavetypen viser hvor du begynner. Kopier er merket.

| Kilde / fil | Oppgave 1 | Oppgave 2 | Oppgave 3 |
| --- | --- | --- | --- |
| N01<br>test3_100.pdf | Ulike røtter<br>21, 22 | D3-tabell<br>50 | P_m-tabell<br>56, 57 |
| N02<br>test3_0%.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | Produkt / invers<br>54, 58, 59 |
| N03<br>Test 3 54.65%.pdf | Dobbel rot<br>22 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| N04<br>Topics7-9_100%.pdf | Rekurrensflervalg<br>37 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| N05<br>Test 3 (topics 7-9_ Recurrence relations, Introduction to group theory, The multiplicative group of integers mod(n) and Lagrange's theorem)_ Attempt review _ Matric (1).pdf | Rekurrensflervalg<br>67 | Gruppeflervalg<br>11 | Indeks<br>60, 61 |
| N06<br>delprøve_3_92%.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | Produkt / invers<br>54, 58, 59 |
| N07<br>Test 3_1_66% (topics 7-9_ Recurrence relations, Introduction to group theory, The multiplicative group of integers mod(n) and Lagrange's theorem)_ Attempt review _ Matric.pdf | Rekurrensflervalg<br>67 | D3-tabell<br>50 | Indeks<br>60, 61 |
| N08<br>Test 3, forsøk 1, 100%.pdf | Antall ord<br>27, 28 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |
| N09<br>quiz3_100.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | P_m-tabell<br>56, 57 |
| N10<br>Test 3 (topics 7-9_ Recurrence relations, Introduction to group theory, The multiplicative group of integers mod(n) and Lagrange's theorem)_ Attempt review _ Matric.pdf | Gitt p[n]<br>25, 26 | Permutasjoner<br>47, 48 | Indeks<br>60, 61 |

## Side 72: Kildegrunnlag og rettelser til gamle notater

Søk: Rekursjon_Leselig • regler • source • fortegn • gamle notater

**Grunnlag:** 50 PDF-er i Delprove_3 på GitHub, ti nyere opplastede prøver og flervalgsspørsmål fra samtalen. Etter fjerning av identiske kopier: **49 ulike PDF-prøver med 147 regneoppgaver**. Signeringskode er ikke en regneoppgave.

| Støttedokument | Bruk / merknad |
| --- | --- |
| B40<br>regler/Diskre_matte_oppgave_3_eks.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B41<br>regler/Diskre_matte_oppgave_3_eks_2.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B42<br>regler/Rekursjon_Leselig.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B44<br>regler/diskre_prøve_3_oppg_1.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B45<br>regler/spm_1_eks.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B46<br>regler/spm_3_eks.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B47<br>regler/subgroups_spm_2.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |
| B50<br>regler/utvidet_euklidisk.pdf | Støttedokument; metoden er kontrollert mot prøveoppgavene. |

**Gamle tekstnotater har feil.** Én lik verdi bestemmer ikke en andreordens følge. Z/7 × Z/10 er endelig og har 70 elementer. For a[n]=2*a[n-1]−2*a[n-2], a0=0,a1=−128 blir a2=−256, ikke −253. «None of the above» avhenger alltid av de andre alternativene.

De to tekstnotatene og fire håndskrevne bildene i originalmappen er støttemateriale. Avkryssinger og prosenttall i tidligere forsøk er ikke alene brukt som fasit. Hver metode og svartabell er kontrollert matematisk.
