"""Editable content for the MA-224 printed exam guide.

Question references use the numbering in the uploaded 2021–2025 exams.
Each entry in PAGES is one A4 page. The front page is generated from INDEX.
"""


def page(key, label, title, prompt, exams, blocks, *, source=''):
    return dict(key=key, label=label, title=title, prompt=prompt, exams=exams,
                blocks=blocks, source=source)


def p(text):
    return ('p', text)


def h(text):
    return ('h', text)


def box(text):
    return ('box', text)


def code(text):
    return ('code', text)


def table(headings, rows, widths):
    return ('table', (headings, rows, widths))


INDEX = [
    ('Logikk og bevis', 'Truth table / logical inferences / find the flaws', 'logikk'),
    ('Induksjon og Peano', 'Prove by induction / Peano definitions', 'induksjon'),
    ('Grammatikk', 'Derivation / syntax tree / ambiguous / 4-tuple', 'grammatikk'),
    ('Automater', 'Translate NFA to DFA / minimize', 'dfa'),
    ('Regulære uttrykk', 'NFA to regex / right-regular grammar', 'regex'),
    ('Programkorrekthet', 'Correct implementation / refinement / JML', 'program'),
    ('Relasjoner', 'Reflexive / antisymmetric / equivalence / order', 'relasjoner'),
    ('Relasjonsmatriser', 'Relation matrix / partition / add mandatory 1s', 'relasjonsmatrise'),
    ('Relasjonsbevis', 'Union / transpose / lexicographic / least / remainder', 'relasjonsbevis'),
    ('Rekurrens', 'Initial value / double root / periodic / find a recurrence', 'rekurrens'),
    ('Flere rekurrenser', 'First order / variable coefficient / complex roots', 'rekurrensvarianter'),
    ('Grupper', 'Group table / order / cyclic / gcd / lcm', 'grupper'),
    ('Symmetri', 'Sₙ / permutation / D₄ / rotation / reflection', 'symmetri'),
    ('Lagrange', 'Coset / index / subgroup orders', 'sideklasser'),
    ('Gruppebevis', 'Prove subgroup / homomorphism / isomorphism', 'gruppebevis'),
    ('Modulo og Euklid', 'Euler totient / Pₙ / modular inverse / integer solutions', 'modulo'),
    ('RSA og potenser', 'Public/private key / encrypt / Fermat / powers mod', 'rsa'),
    ('Kodeavstand og G', 'Minimum distance / choose G / detect or correct', 'kodeavstand'),
    ('Syndrom og feilretting', 'Parity check / syndrome / codeword / coset leader', 'syndrom'),
    ('Bitfeil og sannsynlighet', 'No errors / at most k / receive a given word', 'kanal'),
    ('Kode fra regler', 'Given E / generator matrix / group code / list codewords', 'gruppekode'),
    ('Turing og løkker', 'Last 1 on the tape / watchdog / infinite loop', 'maskin'),
    ('Tidslogikk', 'Next / eventually / always / until / semantic function', 'tidslogikk'),
]


PAGES = [
    page('logikk', 'Logikk', 'Logikk og bevisfeil',
         'Truth tables · logical inferences · find the flaws', '2022 Q1 · 2024 Q1 · 2025 Q1', [
        box('**Truth table:** lag alle 2ⁿ rader. Del uttrykket i små kolonner. A⇒B er bare usann ved T⇒F. '
            'A⇔B er sann når A og B har samme verdi.'),
        h('Sannhetstabell, eksempel fra 2025'),
        p('Sett A=¬p∨¬q, B=p∧q∧r og C=p∧q. Vis at (A⇒B) og C er like på hver rad.'),
        table(['p', 'q', 'r', 'A', 'B', 'A⇒B', 'C', '(A⇒B)⇔C'], [
            ['F', 'F', 'F', 'T', 'F', 'F', 'F', 'T'],
            ['F', 'F', 'T', 'T', 'F', 'F', 'F', 'T'],
            ['F', 'T', 'F', 'T', 'F', 'F', 'F', 'T'],
            ['F', 'T', 'T', 'T', 'F', 'F', 'F', 'T'],
            ['T', 'F', 'F', 'T', 'F', 'F', 'F', 'T'],
            ['T', 'F', 'T', 'T', 'F', 'F', 'F', 'T'],
            ['T', 'T', 'F', 'F', 'F', 'T', 'T', 'T'],
            ['T', 'T', 'T', 'F', 'T', 'T', 'T', 'T'],
        ], [1, 1, 1, 1, 1, 1.25, 1, 2]),
        h('Logiske slutninger for samme uttrykk'),
        code('A⇒B ≡ ¬A∨B                        implikasjonsregelen\n'
             '    ≡ (p∧q)∨(p∧q∧r)               De Morgan og dobbel negasjon\n'
             '    ≡ X∨(X∧r) ≡ X, der X=p∧q      absorpsjon'),
        p('Hvis absorpsjon må forklares, vis begge veier. Fra X kan du slutte X∨(X∧r). '
          'Fra X∨(X∧r) får du X i begge tilfeller, siden X∧r gir X.'),
        p('**For å vise A⇒B:** start med A og vis B. I 2022 gir (p∧¬q)∧r først p∧r, '
          'deretter (p∧r)∨q. **For A⇔B:** vis begge retninger.'),
        h('Finn feilen i et bevis'),
        p('I n+n=n·n mister du n=0 hvis du deler på n med én gang. Skriv n(n−2)=0. '
          'Da får du n=0 eller n=2. Sett begge inn i den opprinnelige likningen.'),
    ]),
    page('induksjon', 'Induksjon', 'Induksjon og Peano',
         'Prove by induction · Peano axioms · define recursively',
         '2021 Q1–2 · 2022 Q2 · 2023 Q1–2, Q7 · 2024 Q2 · 2025 Q2', [
        box('**Skriv tre linjer før du regner.** 1. Vis første tilfelle. 2. Anta påstanden for k (eller t). '
            '3. Bruk definisjonen til å vise neste tilfelle. Marker hvor du bruker antakelsen.'),
        h('Peano: finn hvilken side regelen virker på'),
        p('s(x) betyr etterfølgeren til x, altså tallet etter x. '
          'Når oppgaven gir s(x)+a=s(x+a), kan du bytte ut venstresiden med høyresiden. '
          'Bruk akkurat definisjonene i oppgaven. Her er 0+a=a og 1=s(0).'),
        code('Vis n+1=s(n).\n'
             'Start:       0+1=1=s(0).\n'
             'Anta:        k+1=s(k).\n'
             'Vis for s(k): s(k)+1=s(k+1)=s(s(k)).'),
        p('**Hvis de bare sier «using the definitions»:** fold ut direkte. '
          'Med s(x)·a=x·a+a får du 3·n=2·n+n=1·n+n+n=0·n+n+n+n=n+n+n.'),
        p('For n·0=0 er starten 0·0=0. Anta k·0=0. Da gir definisjonen s(k)·0=k·0+0=0.'),
        h('Strenger: start med ε, bygg på én bokstav'),
        p('I 2025 skal l(D(s))=2·l(s). D gjentar hver bokstav to ganger. '
          'Start med l(D(ε))=0=2·l(ε). Anta l(D(t))=2·l(t). For en vilkårlig bokstav a får du:'),
        code('l(D(t◦a)) = l(D(t)◦a◦a) = l(D(t))+2\n'
             '          = 2·l(t)+2 = 2·l(t◦a).'),
        h('Følger: sjekk hvor mange starttilfeller du trenger'),
        p('I 2022 er s[0]=1, s[1]=2 og s[n+2]=s[n]+2. Vis s[0]<s[1] og s[1]<s[2]=3. '
          'Fra s[k]<s[k+1] får du s[k]+2<s[k+1]+2, altså s[k+2]<s[k+3]. '
          'Dette viser neste ulikhet med samme paritet.'),
        p('I 2023 er a[n]=2a[n−1]+3a[n−2]. For økende følge: vis 0=a[0]<a[1]=1<a[2]=2. '
          'Deretter er a[n+1] større enn a[n] fordi begge leddene i '
          '**2a[n]+3a[n−1]** er større enn de tilsvarende leddene i **2a[n−1]+3a[n−2]**.'),
        p('**«Define recursively»** betyr å skrive en startverdi og en regel for neste verdi. '
          'Eksempel fra 2021: 1,3,1,3,… skrives s[0]=1, s[n+1]=4−s[n].'),
        p('For (ab)ⁿ=aⁿbⁿ med n>0 starter du ved n=1. Splitt av siste faktor ab '
          'i (ab)ᵏ⁺¹, bruk antakelsen på (ab)ᵏ og grupper a-faktorene og b-faktorene.'),
    ]),
    page('grammatikk', 'Grammatikk', 'Derivasjon, tre og tvetydighet',
         'Find a derivation · syntax tree · ambiguous · grammar as a 4-tuple',
         '2021 Q3–4 · 2022 Q3 · 2023 Q3 · 2024 Q3 · 2025 Q3', [
        p('I regelen A→a er **A en ikke-terminal**, et symbol du kan bytte ut. '
          '**a er en terminal**, et av tegnene som står i den ferdige strengen.'),
        table(['Når de ber om', 'Gjør dette'], [
            ['Derivasjon', 'Start med startsymbolet. Bytt én ikke-terminal per pil. '
                           'Hvis du har et tre, følg barna til noden. Velg gjerne det venstre symbolet først.'],
            ['Tre fra regler / grammatikk fra tre', 'I et tre gir hver indre node regelen '
                                                  'forelder → barna fra venstre til høyre. Bladene leses som strengen.'],
            ['Ambiguous?', 'Finn én streng med to ulike trær fra startsymbolet. '
                          'Skriv gruppen med parenteser hvis det gjør treet lettere å tegne.'],
            ['4-tuple', 'Skriv (terminaler, ikke-terminaler, startsymbol, regler). '
                        'Ta med de nye symbolene når du fjerner EBNF-forkortelser.'],
        ], [1.3, 3.5]),
        h('Følg én streng som mål'),
        p('I 2025 skal A lage `cc`. A→B→C→CC→cC→cc er én derivasjon. '
          'Finn ulike trær ved å spørre **hvor de to c-ene skilles**. I dette eksemplet finnes tre muligheter:'),
        code('A → B → C → CC            del i to ved C\n'
             'A → B → CC                del i to ved B\n'
             'A → BB → CB → CC          del i to ved A'),
        p('I alle tre blir de to siste C-ene til c, men treet forgrener seg på ulike steder. '
          'Med start C har `cc` ett tre. Sjekk da `ccc`, som får både (cc)c og c(cc) med C→CC.'),
        p('**Hvis to viste derivasjoner har samme tre:** se om reglene kan lage en ny tvetydig streng. '
          'I 2024 kan R→R+R gi både (2+3)+3 og 2+(3+3) på høyre side i `1=2+3+3`.'),
        h('Tidlige og sene valg i en IF-grammatikk'),
        p('For `if A then if B then C else D` kan `else D` høre til den indre eller ytre IF-en. '
          'Tegn begge og behold de samme terminalene i samme rekkefølge.'),
        h('Gjør EBNF om til ordinære regler'),
        p('Bytt [X] med et nytt O og reglene O→ε | X. Bytt {X} med R og reglene R→ε | X R. '
          'Reglene lar deg velge null eller flere X. Fast startsymbol oppgis i 4-tuplen.'),
        box('Å erstatte venstre eller høyre symbol først kan gi samme tre. Det teller som tvetydighet '
            'først når du kan vise **samme ferdige streng med to ulike trær**.'),
    ]),
    page('dfa', 'Automater', 'Fra NFA til minimal DFA',
         'Translate NFA to DFA · subset construction · minimize', '2021 Q5 · 2023 Q4', [
        box('**Ta én rad og én bokstav av gangen.** Startmengden er ε-lukningen til start. '
            'I en rute følger du først den oppgitte bokstaven fra alle tilstandene i raden. '
            'Så legger du til alle steder du kan nå fra de nye målene med ε.'),
        p('ε er tom streng. En ε-pil flytter deg uten å lese et tegn. '
          'ε-lukningen er alle tilstandene du kan nå på den måten, også den du startet i. '
          'En ε-pil har retning. En tilstand uten pil for den aktuelle bokstaven bidrar med ingenting.'),
        h('Slik fyller du én rute, fra 2023'),
        code('A = ε-lukning({1}) = {1,2,4,6,8}.\n'
             'På symbol 1: 2→3 og 8→9, så målene er {3,9}.\n'
             'ε-lukning av målene gir {2,3,8,9}. Kall den B.'),
        p('Gi hver ny mengde én rad. Bruk det gamle navnet hvis mengden allerede finnes. '
          'Hvis ingen piler passer, gir ruten ∅, som går til ∅ på alle bokstaver. '
          'Marker sluttilstander ut fra NFA-tilstandene i mengden. Følg oppgavens prioritet for Acc1, Acc2 osv.'),
        table(['DFA-tilstand', 'NFA-mengde', 'På 1', 'På 2', 'Utfall'], [
            ['A (start)', '{1,2,4,6,8}', 'B', 'C', 'Ingen'],
            ['B', '{2,3,8,9}', 'B', 'D', 'Acc1'],
            ['C', '{4,5,6,7}', 'E', 'C', 'Acc2'],
            ['D', '{8,9}', 'D', 'D', 'Acc1'],
            ['E', '{6,7}', 'E', 'E', 'Acc2'],
        ], [1.1, 2, .65, .65, 1.15]),
        h('Minimer ved å sjekke hvilken gruppe hver pil lander i'),
        p('Fjern utilgjengelige tilstander. Start med gruppene **{A} / {B,D} / {C,E}**, '
          'én per utfall. For hver gruppe: del den hvis to tilstander går til ulike **grupper** '
          'på samme symbol. Gjenta til ingen gruppe deles. Behold start og utfall i svaret.'),
        p('B og D lander begge i {B,D} på 1 og 2. C og E lander begge i {C,E} på 1 og 2. '
          'Slå derfor sammen B+D og C+E.'),
        table(['Minimert tilstand', 'På 1', 'På 2', 'Utfall'], [
            ['A (start)', 'BD', 'CE', 'Ingen'], ['BD', 'BD', 'BD', 'Acc1'], ['CE', 'CE', 'CE', 'Acc2'],
        ], [2, 1, 1, 1.25]),
    ]),
    page('regex', 'Regulære uttrykk', 'Regulære uttrykk og grammatikk',
         'Translate NFA to a regular expression · show the steps · right-regular grammar',
         '2021 Q6 · 2022 Q4 · 2024 Q4 · 2025 Q4', [
        h('NFA → regulært uttrykk'),
        box('Legg til en ny start med ε-pil til gammel start og en ny slutt med ε-pil fra hver gammel slutt. '
            'Fjern én gammel tilstand q om gangen. Behold alle andre piler.'),
        p('For hver pil **i→q** og **q→j** legger du inn en ny vei fra i til j. '
          'Det gjelder også når i=j. Hvis q har en løkke L, kan den tas null eller flere ganger.'),
        code('Ny etikett i→j = gammel i→j | (inn til q)(løkke på q)*(ut av q)\n'
             'Ingen løkke på q → bruk ε i stedet for løkkedelen.\n'
             'Ingen gammel pil i→j → bruk bare den nye veien.'),
        p('Eksempel: i→q med a, løkke b, og q→j med c gir **ab*c**. Har du allerede d fra i til j, '
          'blir etiketten **d|ab*c**. Skriv opp de nye pilene for hvert steg.'),
        h('Fjern A, B og C i oppgaven fra 2025'),
        p('Start→A har ε, A-løkka har a, og A→B og A→C har b og c. Fjerner du A, '
          'får start nye piler a*b til B og a*c til C. Via A får B og C også nye veier '
          'a⁺b og a⁺c. De slås sammen med direkte b- og c-piler til a*b og a*c.'),
        p('Sett u=a*b og v=a*c. Fra start går u til B og v til C. '
          'B har løkke u og pil v til C. C har løkke v og pil u til B. C går til ny slutt med ε.'),
        code('Fjern B: start→C og C→C får v|uu*v = u*v.\n'
             'Fjern C: (u*v)(u*v)* = (u*v)+.\n'
             'Sett inn u og v: ((a*b)*a*c)+ = ([ab]*c)+ = [abc]*c.'),
        p('Du kan stoppe ved et korrekt uttrykk før den siste forenklingen. ε er tom streng. '
          'A* kan være tomt, A+ krever minst én A, A? betyr ε|A.'),
        h('Regulært uttrykk → høyrelineær grammatikk'),
        p('I 2024 er uttrykket `0*1 | 1?0 | (01)+`. Start S velger én av tre grener.'),
        code('Terminaler {0,1}, ikke-terminaler {S,A,B,C,D,E}, start S\n'
             'S → A | B | C     A → 0A | 1     B → 0 | 1D\n'
             'D → 0             C → 0E         E → 1 | 1C'),
        p('Hvis du starter med en NFA, gir en pil X→Y med terminal a regelen X→aY. '
          'ε-pil gir X→Y. Hver sluttilstand F får F→ε. Skriv hele 4-tuplen.'),
    ]),
    page('program', 'Programmer', 'Programkorrekthet og JML',
         'Correct implementation · refinement calculus · counterexample · extend JML',
         '2021 Q9–10 · 2022 Q5 · 2023 Q5 · 2024 Q5 · 2025 Q5', [
        p('**{pre}** sier hva som gjelder før kjøring. **x, y** er gamle verdier. **x′, y′** er nye verdier. '
          'Postbetingelsen sier hva de nye verdiene må oppfylle.'),
        table(['Regel', 'Det du skal vise eller gjøre'], [
            ['Wep · weaken precondition', 'Gammel pre ⇒ ny pre. Eksempel: x≥30 ⇒ x≥3.'],
            ['Str · strengthen postcondition', 'Gjeldende pre ∧ ny post ⇒ gammel post. Sett inn de nye verdiene og vis hver del.'],
            ['Fra · contract frame', 'Hvis x skal beholdes, vis x′=x og fjern x fra listen over variabler som skrives.'],
            ['Ass · introduce assignment', 'Fra x′=E får du oppdateringen x:=E.'],
            ['Rew · rewrite', 'Med {x=12} kan du bytte ut x med 12 i uttrykket.'],
        ], [1.45, 3.1]),
        h('Moteksempel: kjør én linje av gangen'),
        p('I 2023 skal x′=x−y og y′=y−x bruke gamle verdier. Koden x:=x−y etterfulgt av y:=y−x '
          'bruker ny x i steg 2. Start med x=y=1. Spesifikasjonen gir (0,0), mens koden gir (0,1). '
          'Fiks det ved å lagre gammel x i h og bruke y:=y−h i steg 2.'),
        p('**Str + Ass, 2022:** med x=0 og x′=x+3 får du x′=3. '
          'Sett 3 inn i kravet x′³−3x′²+3x′−9=0 og få 27−27+9−9=0. Da kan du innføre x:=x+3.'),
        p('**2025 Q5:** fasiten tester x=2 under kandidatenes pre x≥0. Da gir y′=x−3 et negativt tall '
          'og y′=x mod 3 gir y′=x. For x≥3 gir x−3 en lovlig y′ med differanse 3. '
          'Resten x mod 3 ligger i {0,1,2}, er mindre enn x, og x−y′ er delelig på 3. '
          'For b) og d) i fasiten navngir du Wep, Str og Fra. '
          'Hvis du kun sjekker den opprinnelige pre x≥30, oppfyller alle fire kodene kravet. '
          'Skriv hvilken pre du bruker.'),
        h('JML: én gren per tilfelle i den matematiske definisjonen'),
        code('/*@ requires p != null;\n'
             '  @ ensures \\result == (p == zero() ? zero()\n'
             '  @        : p == one() ? one() : mod2(pred(pred(p))));\n'
             '  @*/\n'
             'public Peano mod2(Peano p);'),
        p('Sjekk basistilfellene først, så pred kalles på gyldige verdier. '
          'For geq(x,y) tester du y=0 → true, så x=0 → false, ellers geq(pred(x),pred(y)).'),
    ]),
    page('relasjoner', 'Relasjoner', 'Relasjoner, ekvivalens og ordning',
         'Reflexive · symmetric · antisymmetric · transitive · equivalence classes',
         '2021 Q11–12 · 2022 Q6 · 2023 Q6 · 2024 Q6 · 2025 Q6', [
        p('**aRb** betyr at paret **(a,b) står i relasjonen R**. I en matrise ser du på '
          '**rad a, kolonne b**. Finn ett tilfelle som bryter kravet, slik som i høyre kolonne.'),
        table(['Egenskap', 'Det du skal vise', 'Slik ser et moteksempel ut'], [
            ['Refleksiv', '(a,a) må stå i R for alle a.', '1 er med i mengden, men (1,1) mangler i R.'],
            ['Symmetrisk', 'Hvis (a,b) står i R, må (b,a) også stå der.', '(1,2) står i R, men (2,1) mangler.'],
            ['Antisymmetrisk', 'Hvis (a,b) og (b,a) begge står i R, må a=b.', 'Både (1,2) og (2,1) står i R, og 1≠2.'],
            ['Transitiv', 'Hvis (a,b) og (b,c) står i R, må (a,c) også stå der.', '(1,2) og (2,3) står i R, men (1,3) mangler.'],
            ['Sammenlignbar', 'For alle a,b må (a,b) eller (b,a) stå i R.', 'Både (1,2) og (2,1) mangler.'],
        ], [1.15, 1.85, 2.1]),
        box('**Ekvivalens** = refleksiv + symmetrisk + transitiv. '
            '**Delvis ordning** = refleksiv + antisymmetrisk + transitiv. '
            '**Total ordning** = delvis ordning + alle par kan sammenlignes.'),
        h('Samme paritet, fra 2025'),
        p('Her betyr aRb at a+b er partall. a+a=2a gir refleksivitet. a+b=b+a gir symmetri. '
          'Hvis a+b og b+c er partall, er a+c=(a+b)+(b+c)−2b partall. Det viser transitivitet. '
          'Både (1,3) og (3,1) står i R, så antisymmetri feiler. R er en ekvivalensrelasjon.'),
        h('Delelighet, fra 2024'),
        p('a|b betyr b=ak. Refleksiv: a=a·1. Transitiv: b=ak og c=bℓ gir c=a(kℓ). '
          'Antisymmetri: anta også a=bℓ. Hvis a=0, må b=0. Ellers får du a=a·kℓ og k=ℓ=1. '
          'Det er en delvis ordning. 2|4 men ikke 4|2 viser manglende symmetri. '
          '2 og 3 kan ikke sammenlignes, så ordningen er ikke total. Med denne definisjonen er 0|0.'),
        h('Klasser: finn hva som må være likt'),
        p('Ved (a,b)R(c,d) ⇔ ab=cd har to par samme klasse når de har samme produkt. '
          'Likhet av produkt gir de tre ekvivalensegenskapene. Hvert n forekommer som (1,n), '
          'så det er uendelig mange klasser. Ved «same number of prime factors» teller du med gjentakelser. '
          '12=2·2·3 har tre faktorer.'),
        p('**Antisymmetri med «a≠b»:** Hvis a og b er forskjellige, kan ikke både (a,b) '
          'og (b,a) stå i R. Det er det samme som å si at når begge står der, må a=b. '
          'For ordning på par kan du sjekke hver koordinat separat.'),
    ]),
    page('rekurrens', 'Rekurrens', 'Fra rekurrens til formel, og tilbake',
         'Initial value problem · find a recurrence · particular solution · periodic',
         '2021 Q13 · 2022 Q7 · 2023 Q7 · 2024 Q7 · 2025 Q7', [
        box('For **a[n]−S·a[n−1]+P·a[n−2]=0** erstatter du a[n], a[n−1], a[n−2] med **r², r, 1** '
            'i den rekkefølgen. Løs **r²−S·r+P=0** for å finne røttene. Har du røttene, bruk **S=r₁+r₂** og **P=r₁r₂**.'),
        table(['Røtter', 'Formel for a[n]', 'Bruk a[0] og a[1]'], [
            ['Ulike r₁ og r₂', 'A·r₁ⁿ + B·r₂ⁿ', 'A+B=a[0], A·r₁+B·r₂=a[1]'],
            ['Dobbel rot r≠0', '(A+B·n)·rⁿ', 'A=a[0], B=a[1]/r−A'],
        ], [1.3, 1.5, 2.3]),
        p('**Initial values, 2024:** a[n]−4a[n−1]+4a[n−2]=0, a[0]=0 og a[1]=1. '
          '(r−2)²=0 gir a[n]=(A+B·n)·2ⁿ. Ved n=0 får du A=0. '
          'Ved n=1 får du 2B=1. Svar **a[n]=(n/2)·2ⁿ**.'),
        p('**Fra formel til rekurrens, 2025:** Røttene 3+√13 og 3−√13 gir S=6 og '
          'P=9−13=−4. Svar **a[n]−6a[n−1]−4a[n−2]=0**. '
          'Skriv parenteser rundt en negativ rot før du tar potensen, f.eks. (−1)ⁿ.'),
        h('Hvis høyresiden ikke er null'),
        p('De gir p[n]=n og ber deg sjekke den. Sett n, n−1 og n−2 inn i venstresiden: '
          'n−5(n−1)+6(n−2)=2n−7. Sett så høyresiden til 0 for den homogene delen. '
          'Den har røtter 2 og 3. **Alle løsninger** er A·2ⁿ+B·3ⁿ+n.'),
        h('Periodisk følge: se etter det samme paret'),
        p('I en rekurrens av orden 2 bestemmer to naboverdier resten. '
          'For a[n+2]=√3·a[n+1]−a[n] med start (1,0), regn fram til (1,0) kommer tilbake.'),
        code('n         0    1    2    3    4    5    6\n'
             'a[n]      1    0   −1  −√3   −2  −√3   −1\n\n'
             'n         7    8    9   10   11   12   13\n'
             'a[n]      0    1   √3    2   √3    1    0'),
        p('Første gang startparet gjentas er n=12. Da fortsetter hele følgen likt, '
          'så **minste positive periode er 12**. Én gjentatt verdi alene holder ikke.'),
        p('Hvis røttene er ρe^(±iθ), kan en reell løsning skrives ρⁿ(A cos(nθ)+B sin(nθ)). '
          'For bevis på at en følge øker, bruk induksjonseksemplet på side {page:induksjon}.'),
    ]),
    page('grupper', 'Grupper', 'Gruppetabell, orden og Lagrange',
         'Neutral element · order of an element · cyclic · subgroup · index',
         '2021 Q14–15, Q19 · 2022 Q8–10 · 2023 Q8, Q10 · 2024 Q8, Q10 · 2025 Q8, Q10', [
        table(['Du skal finne', 'Gjør dette'], [
            ['Finn en ugyldig gruppetabell', 'En gjentakelse i en rad eller kolonne bryter kansellering. '
                                             'Hvis xz=yz, må x=y. En tabell uten gjentakelser trenger fortsatt assosiativitet.'],
            ['Nøytralt element e', 'Finn raden og kolonnen som kopierer overskriftene. e·x=x·e=x.'],
            ['Orden til g', 'Regn g, g², g³,… til du får e. Første eksponent er ordenen. '
                          'For + bruker du 0 og g, 2g, 3g,…'],
            ['Syklisk?', 'Finn en g med orden |G|, eller vis at ingen elementer har så høy orden.'],
            ['Maksimal indeks', 'Indeks [G:H]=|G|/|H| teller sideklassene. Velg en tillatt H med minst mulig |H|.'],
        ], [1.45, 3.4]),
        h('gcd og lcm med små tall'),
        p('**gcd** er største tall som går opp i begge. 4 har divisorene 1, 2, 4. '
          '6 har 1, 2, 3, 6. Største treff er 2, så **gcd(4,6)=2**. '
          '**lcm** er minste positive tall som begge går opp i. Tell 4, 8, 12 og 6, 12. '
          'Første felles treff er 12, så **lcm(4,6)=12**.'),
        p('I Z/m er ord(a)=m/gcd(m,a). I Z/2×Z/3 legger du til (1,1) om igjen. Første koordinat '
          'er 0 hver 2. gang. Andre er 0 hver 3. gang. Begge er 0 første gang ved **6**. '
          'Da har (1,1) orden lcm(2,3)=6 og genererer alle seks elementene.'),
        p('I Z/3×Z/3 får du én undergruppe {(0,0)} og fire undergrupper {(0,0),v,2v} '
          'med v=(1,0),(0,1),(1,1),(1,2). De andre generatorene gir samme undergrupper. '
          'Alle undergrupper av orden 3 er sykliske. Hele gruppen har orden 9 og er eneste ikke-sykliske.'),
        p('**Gruppetabellen fra 2025:** i tabell 3 er x nøytral. Fra raden eller kolonnen til y får du '
          'y²=w, y³=z og y⁴=x, så y har orden 4 og genererer gruppen.'),
        h('Lagrange gir divisorer, og deretter bruker du grensene'),
        p('**|H| deler |G|.** Et element g med g²=e og g≠e gir undergruppen {e,g} av orden 2. '
          'Derfor er |G| partall. I D₄ har en refleksjon orden 2 og gir maksimal ikke-triviell indeks 8/2=4.'),
        p('Ved |G|=210 og 70<|H|<210 er indeksen et heltall mellom 1 og 3. Den er 2, så |H|=105. '
          'Ved |K|=8 vet du at 8 deler |G|. Hvis K må være **ekte** undergruppe, er neste mulighet 16. '
          'Hvis K=G er tillatt, kan |G|=8 med G=K=Z/8 og H={0,4}.'),
        p('**Inverse:** snu rekkefølgen, (ab)⁻¹=b⁻¹a⁻¹. Vis det ved å multiplisere til e. '
          'For eksempel a(b⁻¹a)⁻¹=a·a⁻¹·b=b.'),
        p('**Uendelig gruppe:** i ℝ× har alle elementer unntatt 1 og −1 uendelig orden, '
          'siden |g|ⁿ stadig endres. En endelig undergruppe kan derfor bare ha 1 eller 2 elementer.'),
    ]),
    page('modulo', 'Modulo', 'Modulo, φ og utvidet Euklid',
         'Euler totient · multiplicative group Pₙ · inverse · integer solutions',
         '2021 Q15–18, Q20 · 2022 Q9 · 2023 Q9–10 · 2024 Q9 · 2025 Q9', [
        h('Tell Pₙ eller vis at gruppen er syklisk'),
        p('**Pₙ** inneholder tallene 1≤a<n med gcd(a,n)=1, altså der 1 er eneste felles divisor. '
          '**φ(n)** er antall tall i Pₙ. '
          'Når n er primtall får du n−1. For en primpotens pᵏ er φ=pᵏ−pᵏ⁻¹. '
          'Generelt: faktoriser n og gang n med (p−1)/p for hvert **ulikt** primtall p.'),
        p('**2024:** φ(1024)=512 fordi n er en 2-potens og bare oddetallene telles. '
          '**2025:** for n=pq og uniformt valg fra 1 til n er sannsynligheten for Pₙ lik '
          'φ(n)/n=(1−1/p)(1−1/q), nær 1 når begge er store.'),
        p('**Syklisk?** Regn potenser med rest etter hvert steg. I P₅ gir 2,4,3,1 orden 4, '
          'så 2 er generator. I P₈ er gruppen {1,3,5,7}, og alle kvadrater er 1. Da finnes ingen generator.'),
        h('Invers a⁻¹ mod m, med to kolonner'),
        p('Inversen til a er tallet som gir **rest 1** når du ganger med a og deler på m. '
          'Start med (r,t)=(m,0) og (a,1). Del forrige r på siste r og ta heltallsdelen q. '
          'I begge kolonner skriver du forrige rad minus q ganger siste rad.'),
        table(['q brukt', 'r', 't'], [
            ['Start', '211', '0'], ['Start', '28', '1'], ['7', '15', '−7'], ['1', '13', '8'],
            ['1', '2', '−15'], ['6', '1', '98'],
        ], [1, 1, 1]),
        p('Første nye rad: 211−7·28=15 og 0−7·1=−7. Ved r=1 er t inversen modulo m. '
          'Her er **98** inversen fordi 28·98−211·13=1. '
          'Hvis siste ikke-null rest er større enn 1, finnes ingen invers.'),
        p('For å vise at inversen er unik, anta at ax≡ay modulo m og gang begge sider '
          'med inversen til a. Da får du x≡y. I intervallet 1 til m−1 betyr det x=y.'),
        h('Hvor mange heltallsløsninger har ax+by=c?'),
        p('Sett d=gcd(a,b). Når minst én koeffisient er ulik 0, får du **ingen** løsninger hvis d∤c '
          'og **uendelig mange** hvis d|c. For 28x+32y=4 er d=4, og (−1,1) virker. '
          'Alle fås ved x=−1+8k, y=1−7k, k et heltall.'),
        p('**Bézout.** Med siste ikke-null rest d og koeffisient t fra tabellen får du d=t·a+s·m '
          'med s=(d−t·a)/m. For store potenser, Fermat og RSA, se side {page:rsa}.'),
    ]),
    page('kodeavstand', 'Kodeteori', 'Bygg G og sjekk hva koden tåler',
         'Minimum distance · find a generator · detect or correct errors',
         '2021 Q21–22 · 2022 Q11–12 · 2023 Q11 · 2024 Q11 · 2025 Q11', [
        box('For en lineær kode er **dₘᵢₙ = minste antall 1-ere i et kodeord ulik null**. '
            'Alle feil med opptil t bit oppdages hvis dₘᵢₙ≥t+1. '
            'Alle feil med opptil t bit kan rettes hvis dₘᵢₙ≥2t+1.'),
        p('**Vekt** teller 1-ere i én streng. **Hamming-avstand** teller hvor to strenger er ulike. '
          '10100 har vekt 2, og avstanden til 11101 er 2 (plass 2 og 5). '
          'For å lage et kodeord wG, legg sammen de radene der w har 1, bit for bit (⊕). '
          '**To 1-ere blir 0.** For eksempel velger 101 rad 1 og 3. '
          'For en lineær kode er avstanden mellom c og c′ lik vekten til kodeordet c⊕c′. '
          'Derfor holder det å telle 1-ere i de sju ikke-null kodeordene ved tre meldingsbit.'),
        h('En 3×6-generator du kan bruke når du skal konstruere G'),
        p('Legg I₃ til venstre. Velg kontroll­radene 110, 101 og 111 til høyre. '
          'Dette er et gyldig valg for å rette én feil eller oppdage opptil to feil.'),
        code('G = 1 0 0 | 1 1 0\n'
             '    0 1 0 | 1 0 1\n'
             '    0 0 1 | 1 1 1'),
        table(['Melding w', '001', '010', '011', '100', '101', '110', '111'], [
            ['Kodeord wG', '001111', '010101', '011010', '100110', '101001', '110011', '111100'],
            ['Antall 1-ere', '4', '3', '3', '3', '3', '4', '4'],
        ], [1.6, 1, 1, 1, 1, 1, 1, 1]),
        p('Minste vekt er **3**. Du kan også bevise det ved å telle 1-ere i w. Ved én 1-er har '
          'kontrollraden minst to. Ved to 1-ere gir to ulike kontrollrader minst én. '
          'Ved tre 1-ere har meldingsdelen allerede tre.'),
        h('Hvis de ber om et moteksempel'),
        p('I 2025 har en annen G raden **010001** med vekt 2. Velg sendt kodeord c=000000 '
          'og feil e=010001. Da er r=c⊕e også et kodeord, og feilen blir ikke oppdaget.'),
        p('**«Exactly t»**: se etter et ikke-null kodeord med vekt t. Det er en uoppdagelig feil. '
          '**«At most t»**: bruk dₘᵢₙ. Hvis du skal velge mellom G₁,G₂,G₃, vis at vinneren '
          'har størst dₘᵢₙ. Ett lett kodeord kan være nok til å forkaste hver rival.'),
    ]),
    page('syndrom', 'Kodeteori', 'Syndrom, H og én bitfeil',
         'Parity check matrix · syndrome · is r a codeword? · coset leaders',
         '2022 Q11 · 2023 Q12 · 2024 Q11–12 · 2025 Q12', [
        p('**r** er det du fikk, **c** er kodeordet som ble sendt, og **e** har 1 på hver plass som ble endret. '
          'For G=[I|P] finner du **H=[Pᵀ|I]**. Les hver kontrollkolonne i G loddrett og legg den '
          'som én rad i H. I er matrisen med 1 på diagonalen og 0 ellers.'),
        h('Sammenlign «skal være» og «du fikk», fra 2025'),
        code('G = 1 0 0 | 1 0      H = 1 0 1 | 1 0\n'
             '    0 1 0 | 0 1          0 1 1 | 0 1\n'
             '    0 0 1 | 1 1\n\n'
             'r = 111 | 10'),
        p('Bruk de tre første bitene i r til å regne ut hva kontrollbitene skulle vært. '
          'G-kolonne 4 bruker bit 1 og 3. Kolonne 5 bruker bit 2 og 3.'),
        table(['Kontroll', 'Skal være', 'Du fikk', 'Syndrombit'], [
            ['Bit 4', '1+1=0', '1', '1 (ulike)'], ['Bit 5', '1+1=0', '0', '0 (like)'],
        ], [1, 1.25, 1, 1.5]),
        p('Syndromet **s=10** er H·rᵀ regnet modulo 2. Det er ulikt 00, så r er ikke et kodeord. '
          'Et nullsyndrom betyr at r er et kodeord. En feil kan likevel ha gjort ett kodeord til et annet.'),
        h('Finn feilposisjon, eller vis hvorfor retting kan feile'),
        p('**Én 1-er i e på plass j** gir syndrom lik H-kolonne j. Les kolonnene loddrett. '
          'Ved én feil og ett treff setter du 1 der i e og flipper den biten i r for å få c.'),
        code('H-kolonne nr.    1   2   3   4   5\n'
             'Syndrom         10  01  11  10  01'),
        p('I eksemplet matcher **både kolonne 1 og 4** syndrom 10. Dermed kan du se at '
          'r er feil, men to ulike énbitfeil kan passe. Alle kolonner må være **ikke-null** for å '
          'oppdage alle énbitfeil, og i tillegg **ulike** for å rette dem entydig.'),
        p('Med r=11111 og én feil får du s=11. Bare kolonne 3 matcher. '
          'Da er e=00100, og når du flipper bit 3 får du c=11011.'),
        h('Coset leaders, fra 2024'),
        p('For en fullrangskode med k meldingsbit og n kodebit har du 2ⁿ⁻ᵏ syndromer eller cosets. '
          'En coset leader er et feilmønster med lavest vekt i sin klasse. '
          'Ved (k,n)=(3,5) har du 4 plasser til **6 tilfeller** (ingen feil + fem énbitfeil), '
          'så du kan ikke skille alle. Generelt finner du e med H·eᵀ=s og bruker c=r⊕e.'),
    ]),
    page('maskin', 'Eldre varianter', 'Turing-maskin og løkkedeteksjon',
         'Last 1 on the tape · possible to implement · watchdog', '2021 Q7–8', [
        h('Turing-maskin: les én rute og bestem neste steg'),
        p('I 2021 starter maskinen på den første 1-eren i en sammenhengende blokk. '
          'Den skal stoppe på den siste 1-eren. Gå til høyre så lenge du leser 1, '
          'og gå én plass til venstre når du møter 0.'),
        table(['Tilstand', 'Les', 'Skriv', 'Flytt', 'Neste tilstand'], [
            ['Søk', '1', '1', 'R', 'Søk'], ['Søk', '0', '0', 'L', 'Stopp'],
        ], [1.1, .7, .7, .8, 1.4]),
        p('Skriv en kort begrunnelse ved tabellen. Den første 0-en du møter til høyre '
          'står rett etter blokken med 1-ere. Ett steg til venstre setter hodet på siste 1.'),
        h('Watchdog: hva kan du faktisk observere?'),
        p('Hvis roboten er deterministisk, har endelig mange fullstendige tilstander og '
          'samme videre input, kan du lagre besøkte tilstander. Når hele tilstanden gjentar seg, '
          'gjentar den samme utviklingen seg. En nyttig arbeidsløkke kan også gjenta seg, '
          'så beskriv hvilke løkker som skal utløse omstart.'),
        p('For vilkårlige programmer med ubegrenset minne finnes det ingen generell '
          'metode som alltid avgjør om programmet stopper. Oppgi antakelsene for roboten.'),
        h('Detaljer å passe på i de gamle løsningene'),
        table(['Oppgave', 'Bruk dette på eksamen'], [
            ['2022 Q7 · periode', 'Røttene er √3/2 ± i/2. Du kan unngå rotregningen ved å følge naboparet på side {page:rekurrens}.'],
            ['2023 Q2 · induksjon', 'Induksjonsantakelsen skal være k·0=0, samme påstand som skal bevises.'],
            ['2023 Q7 · voksende følge', 'Rekurrensen har koeffisienter 2, så 3, i den rekkefølgen. Se side {page:induksjon}.'],
            ['2025 Q5 · pre', 'Fasitens moteksempler bruker kandidatens pre. Se forklaringen på side {page:program}.'],
            ['2025 Q10 · undergruppe', 'Skillet ved |K|=8 er om K=G er tillatt. Hvis ja, bruk K=G=Z/8 i moteksemplet. Se side {page:grupper}.'],
        ], [1.35, 3.4]),
        p('Grunnlag: de fem opplastede engelske MA-224-eksamenene med løsninger '
          '(november 2021 og desember 2022, 2023, 2024 og 2025). '
          'Oppgavenumre nederst på temasidene viser hvor du kan øve videre.'),
    ]),
    page('tidslogikk', 'Tillegg', 'Tidslogikk og semantiske funksjoner',
         'Temporal logic · next · eventually · always · until · semantic function', '', [
        box('En **tilstand** forteller hva som er sant akkurat nå. En **kjøring** er en rekke tilstander '
            'i tidsrekkefølge. Finn først hvilken plass i rekka du skal starte på. Her bruker vi vanlig LTL på én kjøring.'),
        table(['Hvis du ser', 'Sjekk dette fra plassen du står på'], [
            ['X p · next · ○p', 'Gå én plass fram. Er p sann akkurat der?'],
            ['F p · eventually · ◇p', 'Finn minst én plass der p er sann. Plassen du står på teller også.'],
            ['G p · always · □p', 'p må være sann på alle plasser fra nå av, inkludert denne. Én usann er nok til å svare nei.'],
            ['p U q · until', 'Finn en plass der q er sann. p må være sann på alle plasser før treffet, fra der du starter. '
                              'Hvis q er sann nå, er kravet oppfylt nå.'],
        ], [1.5, 3.7]),
        h('Se på en tidslinje'),
        code('Plass:    0     1     2     3     4     …\n'
             'p:        0     1     0     1     1     …  (1 for alltid fra 3)'),
        p('Fra plass 0 er **X p sann** (p=1 på plass 1), **F p sann** (du finner en 1-er) og '
          '**G p usann** (p=0 på plass 0). Fra plass 1 er **X p usann**, fordi p=0 på den neste plassen, altså 2.'),
        p('**G F p** betyr at du fra hver plass kan finne en p senere eller nå. '
          '**F G p** betyr at du kan finne en plass der p fortsetter å være sann for alltid. '
          'Med p=0,1,0,1,… for alltid er **G F p sann** og **F G p usann**.'),
        h('Semantisk funksjon: hva betyr uttrykket her?'),
        p('En semantisk funksjon gir betydningen av et uttrykk i en gitt tilstand. '
          'Hvis σ gir x verdien 4, får vi **⟦x+1⟧(σ)=5**. Klammene «⟦ ⟧» betyr at du regner ut hva som står inni. '
          'I tidslogikk får du en sannhetsverdi. **⟦X p⟧(i)=⟦p⟧(i+1)** langs kjøringen.'),
        p('Hvis oppgaven bruker et diagram med flere veier ut og skriver **A** eller **E** foran en operator, '
          'les A som «på alle veier» og E som «på minst én vei». '
          'Med to neste tilstander der bare én har p, er **EX p sann** og **AX p usann**.'),
    ]),
    page('relasjonsmatrise', 'Relasjoner', 'Fyll ut en relasjonsmatrise',
         'Relation matrix · partition · add mandatory 1s · Boolean product · composition', '', [
        box('Sett **1 på rad a, kolonne b** for hvert gitt par (a,b). Merk alle radene og kolonnene '
            'i samme rekkefølge. Ved «add mandatory 1s» behold de gitte 1-erne og legg til rutene reglene krever. '
            'La resten stå 0.'),
        h('Samme start, to ulike krav'),
        p('Eksempel med mengden {1,2,3,5} og parene (2,3), (3,5). Sjekk hvilket krav som står i oppgaven.'),
        table(['Oppgaven ber om', 'Fyll ut slik'], [
            ['**Partial order**', 'Fyll diagonalen. (2,3) og (3,5) krever (2,5). '
                                   'Fortsett å sjekke slike kjeder med de nye parene til ingen flere ruter må fylles.'],
            ['**Equivalence relation**', 'Legg tallene som er koblet sammen i én gruppe, uansett pilretning. '
                                          'Her får du {1} og {2,3,5}. Sett 1 når rad og kolonne er i samme gruppe.'],
            ['**Gitt partition**', 'Gruppene er allerede oppgitt. Fyll alle rutene innen hver gruppe.'],
        ], [1.3, 3.72]),
        code('Rad / kolonne     1 2 3 5    1 2 3 5\n'
             '                    Delvis     Ekvivalens\n'
             '1                 1 0 0 0    1 0 0 0\n'
             '2                 0 1 1 1    0 1 1 1\n'
             '3                 0 0 1 1    0 1 1 1\n'
             '5                 0 0 0 1    0 1 1 1'),
        p('Ved **partial order** må par mellom ulike tall beholde retningen. Hvis du må sette 1 '
          'i både (a,b) og (b,a) for a≠b, brytes antisymmetrien. Hvis de krever både **equivalence '
          'relation og partial order**, fyller du bare diagonalen, fordi begge kravene da gjelder.'),
        h('Snu, slå sammen eller koble to matriser'),
        p('For å **transponere** bytter du rad og kolonne, så (a,b) blir (b,a). '
          'Ved **union** setter du 1 der minst én av matrisene har 1.'),
        p('I det **boolske produktet A·B** blir rute (i,j) 1 hvis minst én k har **A[i,k]=1 og B[k,j]=1**. '
          'Med (6,3) i R og (3,6) i S gir «R først, S etterpå» paret **(6,6)**. '
          'Ved R∘S bruker du rekkefølgen oppgaven definerer.'),
        p('I (A·Id)[i,j] kan bare k=j bidra, så du får A[i,j]. I (Id·A)[i,j] velges k=i, '
          'som også kopierer A[i,j]. Dermed er **Id nøytral**.'),
    ], source='Canvas · Exercise6, lysbilde 4, 8–9, 15 og 17–19 · Solutions6, lysbilde 5, 10 og 12'),
    page('relasjonsbevis', 'Relasjoner', 'Relasjonsbevis med små eksempler',
         'Relation union · transpose · NAND or NOR · lexicographic order · minimal · same remainder', '', [
        h('Hvis R og S har egenskapen, må R ∪ S ha den?'),
        table(['Egenskap', 'Det du skriver'], [
            ['Refleksiv', '**Ja.** Én refleksiv relasjon er nok. Alle (a,a) kommer med i unionen.'],
            ['Symmetrisk', '**Ja.** Hvis (a,b) kommer fra R, kommer (b,a) også fra R. Samme argument for S.'],
            ['Antisymmetrisk', '**Nei.** R={(1,2)} og S={(2,1)} på {1,2}. '
                              'Hver for seg er de antisymmetriske. Unionen har begge retninger.'],
            ['Transitiv', '**Nei.** R={(1,2)} og S={(2,3)} på {1,2,3}. Hver for seg er de transitive. '
                          'Unionen har (1,2) og (2,3), og mangler (1,3).'],
        ], [1.24, 3.75]),
        p('Når **N=Mᵀ** definerer relasjonen, velg M med radene [0 1] og [0 0]. Da er M≠Mᵀ. Paret (M,M) mangler, '
          'så refleksivitet feiler. M og Mᵀ står begge veier, så antisymmetri feiler. '
          'De to stegene M → Mᵀ → M ville også krevd (M,M) for transitivitet. Symmetri holder fordi (Mᵀ)ᵀ=M.'),
        h('Boolsk matrise og nøytralt element'),
        p('Regn operasjonen for 00, 01, 10, 11 og skriv resultatene i to rader. NAND gir '
          '**[1 1]** og **[1 0]**. NOR gir **[1 0]** og **[0 0]**. Et nøytralt e må gi '
          'op(a,e)=op(e,a)=a for begge a. NAND feiler for a=0 med begge e. NOR feiler for a=1 med begge e.'),
        h('Leksikografisk ordning og minste element'),
        p('Sammenlign første ulike bokstav. Behandle slutten av et ord som et tegn før alle bokstaver. '
          'For transitivitet, finn første forskjell i u<v og v<w. Ved den tidligste av de to posisjonene er u<w '
          'fordi én eller begge sammenligningene gir en mindre bokstav. Likhet gir refleksivitet. '
          'Forskjellige ord har én bestemt retning, så ≤ er antisymmetrisk og alle par kan sammenlignes.'),
        p('Et **minimalt** element m har ingen x≠m med x≤m. Et **minste** element har m≤x for alle x. '
          'I en total ordning er alle x sammenlignbare med m. For x≠m kan du utelukke x≤m, så m≤x.'),
        h('Samme rest, også med negative tall'),
        p('Bruk **x−m·Intg(x/m)** på Casio for positiv m. Intg runder ned, så med x=−18 og m=8 '
          'får du −18−8·(−3)=6. Tallene −18, −10, −2, 6 og 14 ligger i samme klasse på −20…20. '
          'Grupper bare tallene i oppgavens mengde. En restklasse mod 20 ligger i én restklasse mod 10. '
          'For eksempel ligger klassen med rest 14 mod 20 i klassen med rest 4 mod 10.'),
    ], source='Canvas · Exercise6, lysbilde 5–6, 11, 14, 16 og 20 · Solutions6, lysbilde 3–4, 6–9, 11 og 13'),
    page('rekurrensvarianter', 'Rekurrens', 'Første orden, brøk og komplekse røtter',
         'First order · variable coefficient · telescoping sum · complex conjugate roots', '', [
        h('Ett tidligere ledd og et fast tall'),
        p('For **a[n]=c·a[n−1]+d**, finn nivået L som oppfyller L=cL+d. Da er L=d/(1−c) for c≠1. '
          'Sett b[n]=a[n]−L. Nå ganges b med c for hvert steg. Med start ved n=k blir '
          '**a[n]=L+(a[k]−L)·c^(n−k)** for n>k. Hvis c=1, legg til d for hvert steg.'),
        code('a[n] = 2·a[n−1]+1,  a[1]=1\n'
             'L = 1/(1−2) = −1,   b[1] = 1−(−1) = 2\n'
             'b[n] = 2·2^(n−1) = 2^n,  a[n] = 2^n−1'),
        p('Hvis d=0 er L=0, så a[0]=−1 og a[n]=−0,5·a[n−1] gir a[n]=−1·(−0,5)^n. '
          'Bruk parentes rundt en negativ base.'),
        h('Brøk med n og n+1'),
        p('For a[n]=n/(n+1)·a[n−1]+1 med a[0]=1, regner du fra n=1. Gang med **n+1**. Se etter at '
          'faktoren på a[n−1] er den samme som faktoren på a[n], bare med én lavere indeks.'),
        code('(n+1)·a[n] = n·a[n−1] + (n+1)\n'
             'Sett b[n]=(n+1)·a[n]. Da er b[n]=b[n−1]+(n+1).\n'
             'b[n] = 1+2+…+(n+1) = (n+1)·(n+2)/2\n'
             'Del på n+1. Svar  a[n] = (n+2)/2.'),
        h('Negativ diskriminant i andre orden'),
        p('Regn som på side {page:rekurrens} til du har roten **u+iv** med v>0. Finn lengden '
          'ρ=√(u²+v²) og vinkelen θ fra positiv realakse. Bruk '
          '**a[n]=ρ^n·(A·cos(nθ)+B·sin(nθ))**. Startverdiene gir **A=a[0]** og '
          '**B=(a[1]−u·A)/v**, fordi ρ·cosθ=u og ρ·sinθ=v.'),
        p('For a[n]+2a[n−1]+2a[n−2]=0 er røttene −1±i. Punktet (−1,1) ligger 45° over den '
          'negative realaksen, så ρ=√2 og θ=3π/4. Med a[0]=1 og a[1]=3 får du A=1 '
          'og B=(3−(−1)·1)/1=4.'),
        box('Svaret er **a[n]=(√2)^n·(cos(3nπ/4)+4·sin(3nπ/4))**. '
            'Sett inn n=0 og n=1 som rask kontroll.'),
    ], source='Canvas · exercise7_problems og exercise7_solutions, Problem 1–3'),
    page('symmetri', 'Grupper', 'Permutasjoner og kvadratgruppen D₄',
         'G = ⟨x⟩ ⊆ Sₙ · order of a permutation · D₄ multiplication table · rotation · reflection', '', [
        h('Hva er G i første linje?'),
        table(['Oppgaven gir', 'Dette følger'], [
            ['G=⟨x⟩, ord(x)=t', '**|G|=t**. Elementene er e,x,…,x^(t−1). Gruppen er syklisk '
                                'og abelsk siden xⁱxʲ=x^(i+j)=xʲxⁱ. Ved primtall t er undergruppene {e} og G.'],
            ['G=Sₙ', '**|G|=n!**. For n≥3, bruk (1 2) og (2 3) for å vise at rekkefølgen betyr noe. '
                     'Følg 1. I forelesningens rekkefølge får du 1→2→3 og 1→1→2.'],
        ], [1.23, 3.76]),
        p('**Ordenen til én permutasjon** er lcm av lengdene til dens separate sykler. '
          'En 3-sykel og en 2-sykel kommer begge tilbake til start første gang etter 6 steg. '
          'I S₃ har elementene orden 1, 2 eller 3. Dermed kan ingen generere alle 6.'),
        h('D₄ i Canvas-øving 8'),
        p('D₄ har 8 elementer. r er rotasjon +90°, s er speiling i y=x og e er identiteten. '
          'Gjør radens operasjon først og deretter kolonnens, som i forelesning 8. '
          'r⁴=e, s²=e og rs=sr³. Bruk oppgavens rekkefølge hvis den oppgis.'),
        table(['·', 'e', 'r', 'r²', 'r³', 's', 'sr', 'sr²', 'sr³'], [
            ['e',   'e',   'r',   'r²',  'r³',  's',   'sr',  'sr²', 'sr³'],
            ['r',   'r',   'r²',  'r³',  'e',   'sr³', 's',   'sr',  'sr²'],
            ['r²',  'r²',  'r³',  'e',   'r',   'sr²', 'sr³', 's',   'sr'],
            ['r³',  'r³',  'e',   'r',   'r²',  'sr',  'sr²', 'sr³', 's'],
            ['s',   's',   'sr',  'sr²', 'sr³', 'e',   'r',   'r²',  'r³'],
            ['sr',  'sr',  'sr²', 'sr³', 's',   'r³',  'e',   'r',   'r²'],
            ['sr²', 'sr²', 'sr³', 's',   'sr',  'r²',  'r³',  'e',   'r'],
            ['sr³', 'sr³', 's',   'sr',  'sr²', 'r',   'r²',  'r³',  'e'],
        ], [1] * 9),
        p('D₄ er **ikke-abelsk** siden r·s=sr³ og s·r=sr. Den ekte undergruppen ⟨r⟩={e,r,r²,r³} '
          'har orden 4, er syklisk og abelsk. Indeksen **[D₄:⟨r⟩]=8/4=2**. '
          'For ⟨r²⟩={e,r²} er indeksen 4. For ⟨r⁴⟩={e} er indeksen 8.'),
    ], source='Canvas · lecture8, s. 5–9 og 10–12 · exercise8_solutions, Problem 1–6'),
    page('sideklasser', 'Grupper', 'Regn ut sideklasser og indeks',
         'Compute a coset · left coset · same coset · index · Lagrange’s theorem', '', [
        box('En **sideklasse gH** er mengden du får ved å regne g·h for hvert h i H. '
            'Når gruppen bruker addisjon, heter den **g+H**. Finn H først hvis du bare har fått en generator.'),
        h('Eksempel i Z/12 med H=⟨4⟩'),
        p('Start på 0 og legg til 4 til du kommer tilbake til 0. Da er H={0,4,8}. '
          'For 2+H legger du 2 til hvert av tallene og tar rest modulo 12.'),
        table(['Representant g', 'g+H i Z/12'], [
            ['0', '{0,4,8}'],
            ['1', '{1,5,9}'],
            ['2', '**{2,6,10}**'],
            ['3', '{3,7,11}'],
        ], [1.35, 3.64]),
        p('For å **liste alle sideklassene**, velg neste g blant tallene som ennå ikke er dekket. '
          'For eksempel ligger 6 allerede i 2+H, så 6+H gir samme mengde. '
          'Her gir [G:H]=|G|/|H|=12/3=4 antall sideklasser.'),
        h('Hvorfor virker tellingen?'),
        p('Hvis gH og g′H overlapper, finnes a,b i H med g·a=g′·b. Da er g′=g·(ab⁻¹), '
          'og ab⁻¹ ligger i H. Å gange alle elementene i H med ab⁻¹ gir H igjen. Derfor er g′H=gH. '
          'Så sideklassene dekker G uten overlapp mellom ulike klasser.'),
        p('Du kan sjekke om g og g′ er i samme sideklasse ved å teste **g⁻¹g′∈H**. Ved addisjon bruker du g′−g.'),
        p('Alle sideklasser har |H| elementer fordi hvert h har et unikt bilde gh, og du får h '
          'tilbake ved å gange med g⁻¹. Tell klassene og gang med |H|. Dette gir **|G|=|H|·[G:H]**.'),
        h('Hva kan jeg slutte fra Lagrange?'),
        p('Orden k til x er |⟨x⟩|. Da deler k gruppens orden n, så **x^n=e**. '
          'Hvis n er primtall, har enhver undergruppe størrelse 1 eller n. '
          'Hvis elementer har orden 5 og 7, deler begge |G|. Da deler også 35 |G|.'),
        p('For å vise at en bestemt undergruppe finnes, oppgi dens elementer eller en generator. '
          'I en **syklisk** gruppe G=⟨g⟩ av orden n finnes nøyaktig én undergruppe av orden d for '
          'hver divisor d av n, nemlig ⟨g^(n/d)⟩. For eksempel i Z/12 med addisjon gir d=3 '
          'generatoren 12/3=4.'),
    ], source='Canvas · lecture9, s. 1–3 · lecture8, s. 11–12 · Handin 9'),
    page('gruppebevis', 'Grupper', 'Bevis for grupper og avbildninger',
         'Prove it is a group or subgroup · well defined · homomorphism · isomorphism · image', '', [
        h('Hva må du bevise?'),
        table(['Oppgaven gir', 'Sjekk dette'], [
            ['**En gruppe** (G,·)', 'Regn at resultatet holder seg i G (lukkethet). '
                                    'Vis (ab)c=a(bc), finn e med ea=ae=a, og vis at alle a har en invers i G.'],
            ['**En undergruppe** H⊆G', 'Vis e∈H. For a,b∈H vis ab∈H og a⁻¹∈H. '
                                       'Assosiativiteten følger fra G.'],
            ['**Well defined**', 'Bytt representanter i samme klasse. Vis at resultatet blir i samme klasse. '
                                  'For Z/n gir a′=a+kn og b′=b+ℓn at a′+b′ og a+b har samme rest.'],
        ], [1.24, 3.75]),
        h('To korte gruppebevis'),
        p('For **SO(n) i GLₙ** har identitetsmatrisen determinant 1. For A,B med determinant 1 får '
          'vi det(AB)=det(A)·det(B)=1 og det(A⁻¹)=1/det(A)=1. Dermed ligger begge resultatene i SO(n).'),
        p('I **Pₙ med multiplikasjon modulo n**, for n≥2, kan ingen primfaktor '
          'i n dele ab når gcd(a,n)=gcd(b,n)=1. Å ta rest beholder gcd med n. 1 er nøytral. '
          'Utvidet Euklid gir ta+sn=1, så resten av t er inversen til a. '
          'Enhver felles divisor av t og n må dele 1, så denne resten ligger i Pₙ. '
          'Assosiativitet følger fra vanlig multiplikasjon.'),
        h('Vis at f bevarer gruppeoperasjonen'),
        p('For å vise **homomorfi**, ta vilkårlige a,b og vis f(ab)=f(a)f(b). '
          'Hvis gruppen til venstre bruker +, skriv f(a+b). '
          'For **isomorfi**, vis i tillegg at alle målverdier treffes nøyaktig én gang. '
          'Da kan du gå tilbake med f⁻¹.'),
        p('I Z/4 → ⟨r⟩, der r har orden 4, bruk f([k])=r^k. Å legge til 4 i eksponenten '
          'gir samme rotasjon, så funksjonen er veldefinert. f([a]+[b])=r^(a+b)=r^a·r^b. '
          'Eksponentene 0, 1, 2, 3 gir de fire rotasjonene én gang hver.'),
        p('For **bildet f(G)** får du det nøytrale elementet fra f(e_G)=f(e_G)·f(e_G) ved å kansellere. '
          'f(a)·f(b)=f(ab) ligger i bildet, og f(a)⁻¹=f(a⁻¹) ligger også der fordi f(aa⁻¹)=e.'),
    ], source='Canvas · lecture8, s. 2–5 og 9–14 · lecture9, s. 4–6 · Handin 8'),
    page('rsa', 'Modulo og RSA', 'Fermat, modulopotenser og RSA',
         'Compute ϕ · Fermat’s little theorem · private key · encrypt/decrypt · powers mod', '', [
        h('Finn ϕ(n) fra faktorer'),
        p('Prøv primtall opp til √n ved faktorisering. Hvis p går opp, del ut p og test samme p '
          'igjen på tallet som er igjen. **126=2·3²·7**, så **ϕ(126)=126·(1−1/2)·(1−1/3)·(1−1/7)=36**. '
          'Bruk hver ulik primfaktor én gang i ϕ-formelen.'),
        h('Regn en stor potens med små tall'),
        p('Ta rest av basen først, som i 2257³ mod 5 = 2³ mod 5 = 3. '
          'For **3¹³ mod 17**, skriv 13=8+4+1. Kvadrer for hver ny kolonne og ta rest.'),
        table(['Eksponent', '1', '2', '4', '8'], [
            ['3^eksponent mod 17', '3', '9', '13', '16'],
        ], [2.6, .6, .6, .6, .6]),
        p('Gang bare kolonnene for 8, 4 og 1. Tallet 16·13·3 gir **rest 12 modulo 17**. '
          'Hvis prøven gir «powers mod», er feltene Base=3, Exponent=13, Modulus=17.'),
        p('**Fermat-testen** bruker at hvis n er primtall, gir a^(n−1) rest 1 for alle 1≤a<n. '
          '**2^526 mod 527 = 64**, så 527 er sammensatt. For 1105 gir base 2 rest 1. '
          'Hvis alle oppgitte rester er 1, kan du ikke avgjøre det med de testene. '
          'Med base 5 får du **5^1104 mod 1105 = 885**, så 1105 er sammensatt.'),
        h('RSA. Skriv riktig modulus på hvert steg'),
        table(['Når de ber om', 'Regn'], [
            ['**Find private key y**', 'Finn de ulike primtallene p,q med n=p·q. Regn ϕ=(p−1)(q−1). '
                                      'Finn inversen y til x **modulo ϕ**, med tabellen på side {page:modulo}.'],
            ['Encrypt m / decrypt M', 'Regn **M=m^x mod n** for kryptering. For klartekst bruk **m=M^y mod n**.'],
            ['Valid RSA pair?', 'Sjekk ulike primtall p,q, n=p·q og at x·y gir **rest 1 modulo ϕ**. '
                                 'Følg eventuelle grenser for x og y i oppgaven.'],
        ], [1.35, 3.64]),
        p('Med **n=2747, x=1933 og M=1076** kan du bruke Casio TABLE med Y1=2747÷X og X=2…52. '
          'Ved X=41 får du 67, så ϕ=40·66=2640. Inversen er **y=997**, fordi 1933·997=730·2640+1. '
          'I «powers mod» gir Base=1076, Exponent=997, Modulus=2747 svaret **m=2314**.'),
        p('Med Euler kan du bruke «powers mod» også for y. Fra 2640=2⁴·3·5·11 får du ϕ(2640)=640. '
          'Siden gcd(1933,2640)=1, gir 1933^640 rest 1. Da er **1933^639 mod 2640 = 997**.'),
        p('**Hvorfor dekrypteringen virker.** Sjekk m^(xy)≡m modulo p og modulo q hver for seg. '
          'For en faktor ℓ som deler m, er begge rester 0. Ellers gir Fermat m^(ℓ−1)≡1. '
          'Fordi ℓ−1 deler xy−1, blir m^(xy)≡m. Da passer begge restene og dermed resten modulo p·q.'),
    ], source='Canvas · lecture10 og exercise10 · 2021 Q18, Q20 · Delprøve 4'),
    page('kanal', 'Kodeteori', 'Sannsynlighet for bitfeil',
         'Binary symmetric channel · no errors · exactly k · at most k · receive a particular word', '', [
        box('Tell antall sendte bit n. Skriv p for sannsynligheten for én bitfeil, og q=1−p for at '
            'én bit kommer riktig fram. I en binær symmetrisk kanal antar vi uavhengige bitfeil.'),
        table(['Ordene i oppgaven', 'Dette skal inn på kalkulatoren'], [
            ['**No errors**', 'q^n'],
            ['**Receive r** når w sendes', 'Tell d plasser der w og r er ulike. Regn **p^d·q^(n−d)** for dette bestemte r.'],
            ['**Exactly k errors**', '**(n nCr k)·p^k·q^(n−k)**. Plassene kan velges på n nCr k måter.'],
            ['**At most k errors**', 'Legg sammen «exactly» for 0,1,…,k. Ved høyst 2, bruk '
                                    '**q^n+n·p·q^(n−1)+(n·(n−1)/2)·p²·q^(n−2)** for n≥2.'],
            ['**At least k errors**', 'Regn 1 minus sannsynligheten for høyst k−1 feil.'],
        ], [1.37, 3.62]),
        h('Akkurat én eller to feil, Canvas 11.2'),
        p('Her sendes **6 kodebiter** med p=0,001, så q=0,999. '
          'Én feil kan ligge på 6 plasser. To feil kan ligge på **6·5/2=15** ulike par av plasser.'),
        code('Akkurat 1:  6·0,001·0,999^5   ≈ 0,005970\n'
             'Akkurat 2:  15·0,001²·0,999^4 ≈ 0,000015'),
        h('Når oppgaven gir én bestemt mottatt streng'),
        code('w = 1 0 0 1 1 0 1\n'
             'r = 0 1 0 1 0 0 1\n'
             '    ↑ ↑     ↑      d=3 av n=7'),
        p('Med p=0,111 får dette bestemte r sannsynligheten 0,111³·0,889⁴≈0,0008542. '
          'For **akkurat tre feil hvor som helst** ganger du også med 7 nCr 3=35.'),
        h('Tre desimaler fra E-visning'),
        p('8,542…E−4 betyr 8,542…·10⁻⁴, så flytt komma fire plasser til venstre. '
          '0,0008542 har 8 som fjerde desimal. Da blir svaret **0.001** med tre desimaler og punktum. '
          'Avrund først når du har regnet hele svaret.'),
        h('Kan vi oppdage feilen i øving 11.2?'),
        p('Kontrollbitene er x=w₁+w₃ og y=w₂+w₄. En feil i en meldingsbit får den tilhørende '
          'kontrollen til å feile. En feil i x eller y gir også et avvik, så **alle enkeltfeil oppdages**. '
          'E(1000)=100010 har vekt 2. Dermed er dₘᵢₙ=2. Se side {page:kodeavstand} for avstandsregelen.'),
    ], source='Canvas · exercise11, Problem 11.2 · Delprøve 4'),
    page('gruppekode', 'Kodeteori', 'Fra koderegel til G, H og avstand',
         'Given E · generator matrix · parity check · group code · list codewords · error detection', '', [
        box('For en lineær koding med radvektorer er **rad i i G = E(meldingen med bare bit i lik 1)**. '
            'En (n,k)-kode har k meldingsbit og n kodebit. G har k rader og n kolonner.'),
        h('Eksempel E(w₁w₂)=w₁w₂(w₁+w₂)'),
        p('Regn med 1+1=0. E(10)=101 gir første rad. E(01)=011 gir andre rad. '
          'G har identiteten til venstre, så H=[Pᵀ|I] fås ved å legge siste kolonne i G som rad og føye til 1.'),
        code('G = 1 0 | 1        H = 1 1 | 1\n'
             '    0 1 | 1'),
        p('Med r=111 skal siste bit være 1+1=0, men du fikk 1. Syndromet er **1**. '
          'Alle tre H-kolonnene er 1, så en feil i hvilken som helst enkeltbit gir dette syndromet.'),
        h('Bevis at kodeordene danner en gruppe'),
        p('Med **G eller lineære kontrollregler** er E(0)=0 og E(u⊕v)=E(u)⊕E(v), siden du regner '
          'hver utbit som summer av innbit modulo 2. Derfor er summen av to kodeord et kodeord. '
          'Hvert kodeord er sin egen invers, siden c⊕c=0.'),
        p('For en **liste C** sjekker du at nullordet står der, og at XOR av hvert par fra C fortsatt ligger i C. '
          'Ett par som gir noe utenfor listen, er nok som moteksempel.'),
        h('Finn den minste avstanden du faktisk trenger'),
        p('**For en lineær kode**, ta minste vekt blant kodeordene utenom nullordet. '
          'Eksemplet har {000,011,101,110}, så dₘᵢₙ=2. For en generell kodeliste sammenligner du par av ulike ord. '
          'Ser du **000000 og 000100** i samme liste, er dₘᵢₙ=1 med én gang.'),
        p('Du kan alltid **oppdage** opptil dₘᵢₙ−1 feil og **rette** opptil heltallsdelen '
          'av (dₘᵢₙ−1)/2. For dₘᵢₙ=2 betyr det oppdage 1 og rette 0. '
          'For dₘᵢₙ=3 betyr det oppdage 2 og rette 1.'),
        p('Ved **matriseprodukt mod 2** ganger du rad med kolonne, legger sammen produktene og tar rest mod 2. '
          'For eksempel gir [1 1]·[1 1]ᵀ summen 1+1=0 mod 2.'),
        p('I **Canvas 12.1(a)** gir oppgavetekstens formel ti kodebit. Med bare w₆=1 får du vekt 1, '
          'så dₘᵢₙ=1 for den formelen. I fasitens sjubiters paritetskode gir dₘᵢₙ=2. '
          'Tell bitene i E slik oppgaven oppgir dem.'),
    ], source='Canvas · exercise11, Problem 11.1–2 · exercise12, Problem 12.1–2'),
]
