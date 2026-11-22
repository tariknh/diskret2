"""Editable content for the MA-224 printed exam guide.

Question references use the numbering in the uploaded 2021–2025 exams.
Each entry in PAGES is one A4 page. The front page is generated from INDEX.
"""


def page(key, label, title, prompt, exams, blocks):
    return dict(key=key, label=label, title=title, prompt=prompt, exams=exams, blocks=blocks)


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
    ('Logikk og bevisfeil', 'Truth table / logical inferences / find the flaws', 'logikk'),
    ('Induksjon og Peano', 'Prove by induction / using the definitions', 'induksjon'),
    ('Grammatikk og syntakstrær', 'Find a derivation / syntax tree / ambiguous / 4-tuple', 'grammatikk'),
    ('NFA → DFA og minimering', 'Translate NFA to DFA / minimize', 'dfa'),
    ('Regulære uttrykk', 'NFA to regular expression / right-regular grammar', 'regex'),
    ('Programkorrekthet og JML', 'Correct implementation / refinement / extend JML', 'program'),
    ('Relasjoner', 'Reflexive / antisymmetric / equivalence / order', 'relasjoner'),
    ('Rekurrens', 'Initial values / find a recurrence / particular / periodic', 'rekurrens'),
    ('Grupper og Lagrange', 'Multiplication table / order / cyclic / subgroup / index', 'grupper'),
    ('Modulo og Euklid', 'Euler totient / Pₙ / modular inverse / integer solutions', 'modulo'),
    ('Kodeavstand og G', 'Detect / correct / choose a generator / minimum weight', 'kodeavstand'),
    ('Syndrom og feilretting', 'Parity check / syndrome / codeword / coset leaders', 'syndrom'),
    ('Turing-maskin og løkker', 'Last 1 on the tape / watchdog / infinite loop', 'maskin'),
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
        p('Når oppgaven gir s(x)+a=s(x+a), åpner du første argument i +. '
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
        p('En ε-lukning inneholder tilstanden du startet i. Følg også kjeder av ε-piler. '
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
        table(['Egenskap', 'Skriv dette for å bevise den', 'Moteksempel'], [
            ['Refleksiv', 'For vilkårlig a, vis aRa.', 'Én a uten aRa.'],
            ['Symmetrisk', 'Anta aRb. Vis bRa.', 'aRb, men ikke bRa.'],
            ['Antisymmetrisk', 'Anta aRb og bRa. Vis a=b.', 'Ulike a,b med begge piler.'],
            ['Transitiv', 'Anta aRb og bRc. Vis aRc.', 'To piler i kjede uten snarvei.'],
            ['Total / sammenlignbar', 'For alle a,b, vis aRb eller bRa.', 'Ingen av pilene finnes.'],
        ], [1.25, 1.9, 1.8]),
        box('**Ekvivalens** = refleksiv + symmetrisk + transitiv. '
            '**Delvis ordning** = refleksiv + antisymmetrisk + transitiv. '
            '**Total ordning** = delvis ordning + alle par kan sammenlignes.'),
        h('Samme paritet, fra 2025'),
        p('aRb betyr at a+b er partall. a+a=2a gir refleksivitet. a+b=b+a gir symmetri. '
          'Hvis a+b og b+c er partall, er a+c=(a+b)+(b+c)−2b partall, så R er transitiv. '
          '1 og 3 har begge piler, så R er ikke antisymmetrisk. Konklusjon: ekvivalens.'),
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
        p('**Antisymmetri med «a≠b»:** Vis begge retninger. Anta a≠b og aRb. '
          'Hvis bRa også, tvinger antisymmetri a=b. Omvendt kan begge piler bare finnes '
          'når a=b. For ordning på par kan du bruke hver egenskap separat på hver koordinat.'),
    ]),
    page('rekurrens', 'Rekurrens', 'Fra rekurrens til formel, og tilbake',
         'Initial value problem · find a recurrence · particular solution · periodic',
         '2021 Q13 · 2022 Q7 · 2023 Q7 · 2024 Q7 · 2025 Q7', [
        box('Skriv hele likningen **a[n]−S·a[n−1]+P·a[n−2]=0**. '
            'Det karakteristiske polynomet er **r²−S·r+P**. Har du røttene, bruk **S=r₁+r₂** og **P=r₁r₂**.'),
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
            ['Maksimal indeks', 'Velg en tillatt undergruppe H med minst mulig |H|. Indeks [G:H]=|G|/|H|.'],
        ], [1.45, 3.4]),
        h('Regn med orden'),
        p('I Z/m er ord(a)=m/gcd(m,a). I et direkte produkt tar du minste felles multiplum (lcm) '
          'av koordinatordenene. I Z/2×Z/3 har (1,1) orden lcm(2,3)=6, så den genererer hele gruppen.'),
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
        p('**Pₙ** inneholder tallene 1≤a<n med gcd(a,n)=1. Gruppens orden er φ(n). '
          'Når n er primtall får du n−1. For en primpotens pᵏ er φ=pᵏ−pᵏ⁻¹. '
          'Generelt: faktoriser n og gang n med (p−1)/p for hvert **ulikt** primtall p.'),
        p('**2024:** φ(1024)=512 fordi n er en 2-potens og bare oddetallene telles. '
          '**2025:** for n=pq og uniformt valg fra 1 til n er sannsynligheten for Pₙ lik '
          'φ(n)/n=(1−1/p)(1−1/q), nær 1 når begge er store.'),
        p('**Syklisk?** Regn potenser med rest etter hvert steg. I P₅ gir 2,4,3,1 orden 4, '
          'så 2 er generator. I P₈ er gruppen {1,3,5,7}, og alle kvadrater er 1. Da finnes ingen generator.'),
        h('Invers a⁻¹ mod m, med to kolonner'),
        p('Start med (r,t)=(m,0) og (a,1). Del forrige r på siste r og ta heltallsdelen q. '
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
        p('**Regn modulo:** 2257³ mod 5 = 2³ mod 5 = 3. Reduser basen først. '
          '**Fermat:** En rest ulik 1 i aⁿ⁻¹ mod n for 1≤a<n viser at n er sammensatt. '
          'Å få 1 for noen baser gir ingen sikker konklusjon.'),
    ]),
    page('kodeavstand', 'Kodeteori', 'Bygg G og sjekk hva koden tåler',
         'Minimum distance · find a generator · detect or correct errors',
         '2021 Q21–22 · 2022 Q11–12 · 2023 Q11 · 2024 Q11 · 2025 Q11', [
        box('For en lineær kode er **dₘᵢₙ = minste antall 1-ere i et kodeord ulik null**. '
            'Alle feil med opptil t bit oppdages hvis dₘᵢₙ≥t+1. '
            'Alle feil med opptil t bit kan rettes hvis dₘᵢₙ≥2t+1.'),
        p('For å lage et kodeord wG, legg sammen de radene der w har 1, bit for bit. '
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
        p('For G=[I|P] finner du **H=[Pᵀ|I]**. Les hver kontrollkolonne i G ovenfra og ned og '
          'legg den som en rad i H. Sett identitetsmatrisen til høyre. Én rad i H gir én kontrollbit.'),
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
]
