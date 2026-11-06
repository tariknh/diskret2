#!/usr/bin/env python3
"""Check the rendered document and independently recalculate answer tables."""
from collections import Counter
import csv
from fractions import Fraction
from itertools import permutations, product
import json
from math import gcd, lcm
from pathlib import Path
import re

import fitz

import build

ROOT = Path(__file__).resolve().parent
CHECKS = []


def check(label, condition):
    if not condition:
        raise AssertionError(label)
    CHECKS.append(label)


def flat(text):
    return ' '.join(str(text).replace('**', '').split())


def tables(page):
    return [value for kind, value in page['blocks'] if kind == 'table']


def order_perm(p):
    seen = set()
    lengths = []
    for start in range(len(p)):
        if start in seen:
            continue
        cur, count = start, 0
        while cur not in seen:
            seen.add(cur)
            cur = p[cur]
            count += 1
        lengths.append(count)
    return lcm(*lengths)


def group_checks(pages):
    # Enumerate element orders independently; a full generator must have order |G|.
    orders = [[3//gcd(3, k) for k in range(3)], [6//gcd(6, k) for k in range(6)]]
    units = [x for x in range(1, 5) if gcd(x, 5) == 1]
    orders.append([next(k for k in range(1, 5) if pow(x, k, 5) == 1) for x in units])
    for m, n in [(7, 10), (3, 10)]:
        orders.append([lcm(m//gcd(m, a), n//gcd(n, b)) for a in range(m) for b in range(n)])
    for n in [3, 6]:
        orders.append([order_perm(p) for p in permutations(range(n))])
    orders.append([1, 2])  # S2, added by the six November uploads.
    sizes = [len(x) for x in orders]
    check('Group sizes derived from elements', sizes == [3, 6, 4, 70, 30, 6, 720, 2])
    cyclic = [N in values for N, values in zip(sizes, orders)]
    # The first five are cyclic. In each S_n the transpositions (12),(23) do not commute.
    abelian = []
    for n in [3, 6]:
        a = list(range(n)); a[0], a[1] = a[1], a[0]
        b = list(range(n)); b[1], b[2] = b[2], b[1]
        abelian.append(all(b[a[i]] == a[b[i]] for i in range(n)))
    abelian = [True]*5 + abelian + [True]
    proper = [any(1 < o < N for o in values) for N, values in zip(sizes, orders)]
    lookup = {
        'The group G is finite.': [True]*8,
        'The group G is infinite.': [False]*8,
        'The group G is abelian.': abelian,
        'For all elements a,b ∈ G, the following is true: ab = ba.': abelian,
        'The group G is not abelian.': [not x for x in abelian],
        'There exist elements g,h ∈ G such that gh ≠ hg.': [not x for x in abelian],
        'The group G is cyclic.': cyclic,
        'The group G is not cyclic.': [not x for x in cyclic],
        'There exists an element g ∈ G such that ⟨g⟩=G.': cyclic,
        'There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G.': cyclic,
        'For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G.': [not x for x in cyclic],
        'For each element g ∈ G, ⟨g⟩=G.': [False]*8,
        'There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G.': [True]*8,
        'The group G has a non-trivial and proper subgroup.': proper,
        'The only subgroups of G are the trivial subgroup {e}, and G itself.': [not x for x in proper],
        'The order of G is divisible by 3.': [N % 3 == 0 for N in sizes],
    }
    profile_columns = {key: i for i, key in enumerate(['gp-c3', 'gp-c6', 'gp-p5', 'gp-z7z10', 'gp-z3z10', 'gp-s3', 'gp-s6', 'gp-s2'])}
    for page in pages:
        if page['key'] in profile_columns:
            col = profile_columns[page['key']]
            for row in tables(page)[0]['rows']:
                match = re.fullmatch(r'The order of G is (\d+)\.', row[0])
                expected = sizes[col] == int(match[1]) if match else lookup[row[0]][col]
                check(page['key'] + ': ' + row[0], (flat(row[1]) == 'KRYSS AV') == expected)
        if not page['key'].startswith('group-matrix-'):
            continue
        for row in tables(page)[0]['rows']:
            statement = row[0]
            if statement.startswith('Riktig antall'):
                check('Group order lookup values', list(map(int, row[1:])) == sizes[:7])
                continue
            match = re.fullmatch(r'The order of G is (\d+)\.', statement)
            expected = [N == int(match[1]) for N in sizes] if match else lookup[statement]
            actual = [flat(v) == 'JA' for v in row[1:]]
            check(statement + ' (all seven original matrix columns)', actual == expected[:7])


def modular_checks(pages):
    for page in pages:
        if page['key'] not in ['mod-tables57', 'mod-tables89']:
            continue
        modulus = None
        for table in tables(page):
            if table['headers'][0].startswith('∙'):
                modulus = int(table['headers'][0][1:])
                for row in table['rows']:
                    a = int(row[0])
                    for b, actual in zip(map(int, table['headers'][1:]), row[1:]):
                        check(f'P{modulus}: {a}*{b}', int(actual) == a*b % modulus)
            else:
                for a, actual in zip(map(int, table['headers'][1:]), table['rows'][0][1:]):
                    check(f'P{modulus}: inverse {a}', a*int(actual) % modulus == 1)
    for page in pages:
        if page['key'] not in ['mod-known45-49', 'mod-known50']:
            continue
        for row in tables(page)[0]['rows']:
            modulus = int(row[0]) if page['key'] == 'mod-known45-49' else 50
            for cell in row[1:]:
                value = flat(cell)
                product = re.fullmatch(r'(\d+)\*(\d+) → (\d+)', value)
                inverse = re.fullmatch(r'(\d+)⁻¹ → (\d+)', value)
                if product:
                    a, b, actual = map(int, product.groups())
                    check(f'Known product {a}*{b} mod {modulus}', actual == a*b % modulus)
                else:
                    check('Recognized inverse table syntax', inverse is not None)
                    a, actual = map(int, inverse.groups())
                    check(f'Known inverse {a} mod {modulus}', a*actual % modulus == 1)
        if page['key'] == 'mod-known50':
            for row in tables(page)[1]['rows']:
                for a, actual in [(row[0], row[1]), (row[2], row[3])]:
                    check(f'Complete P50 inverse {a}', int(a)*int(flat(actual)) % 50 == 1)
    # D3 products use the course's convention: apply the left permutation first.
    pmap = dict(id=(0, 1, 2), r1=(1, 2, 0), r2=(2, 0, 1), t1=(0, 2, 1), t2=(2, 1, 0), t3=(1, 0, 2))
    table = tables(next(p for p in pages if p['key'] == 'D3-table'))[0]
    for row in table['rows']:
        left = flat(row[0]).replace(' ', '')
        for right, actual in zip(table['headers'][1:], row[1:]):
            right = flat(right).replace(' ', '')
            actual = flat(actual).replace(' ', '')
            check(f'D3 {left} then {right}', pmap[actual] == tuple(pmap[right][pmap[left][i]] for i in range(3)))


def november_checks(pages):
    data = build.load('new-2026-11-checks.json')
    new_mc = next(p for p in pages if p['key'] == 'new-nov6-mc')
    for case, table in zip(data['recurrence_mc'], tables(new_mc)):
        P, Q = -Fraction(case['B'],case['A']), -Fraction(case['C'],case['A'])
        expected = [2,5,6] if case['id']=='N05' else [1,3]
        check(case['id']+' exact checkbox card', [int(row[0].split('.')[0]) for row in table['rows'] if flat(row[1])=='KRYSS AV'] == expected == case['true_choices'])
        check(case['id']+' integer recurrence coefficients', P.denominator == Q.denominator == 1)
        x, y = [Fraction(4),Fraction(3)], [Fraction(5),Fraction(-2)]
        for _ in range(6):
            x.append(P*x[-1]+Q*x[-2]); y.append(P*y[-1]+Q*y[-2])
        d = [a+13*b for a,b in zip(x,y)]
        check(case['id']+' linear combinations solve recurrence', all(d[n]==P*d[n-1]+Q*d[n-2] for n in range(2,len(d))))
        if case['id']=='N07':
            check('N07 wrong third initial value', P*162+Q*(-18)==-360 and -360!=-357)
            check('N07 one matching term insufficient', x[4]==0 and x[5]!=0)
        else:
            check('N05 one matching term insufficient', 3**2-9==0 and 3**3-9!=0)
    for row in data['words']:
        p,q=row['p'],row['q']
        count=sum(1 for w in product(range(p+q),repeat=3) if w[0]<p and w[-1]<p and all(w[i]<p or w[i+1]<p for i in range(2)))
        check(row['id']+' direct enumeration of all valid length-3 words', count==row['a3']==p**3+p*p*q and row['a1']==p)
        a,b,D=row['root_real'],row['root_sqrt_coefficient'],row['root_sqrt']
        check(row['id']+' both exact radical roots', a*a+b*b*D-p*a-p*q==0 and 2*a*b-p*b==0)
    check('N06 proposed root 4 fails', 4**2-4*4-16!=0)
    for row in data['particular']:
        A,B,t,H,a0,r,a1=[Fraction(row[k]) for k in ['A','B','rhs_base','particular_amplitude','a0','homogeneous_root','a1']]
        check(row['id']+' given particular solution identity', H*(A*t+B)==t)
        check(row['id']+' homogeneous root sign', A*r+B==0)
        check(row['id']+' initial a1 exact value', A*a1+B*a0==t)
        for n in range(1,7):
            check(row['id']+f' another solution at n={n}', A*(H*t**n+r**n)+B*(H*t**(n-1)+r**(n-1))==t**n)
    for row in data['permutations']:
        check(row['id']+' left-first product '+str(row['p']), [row['q'][a-1] for a in row['p']]==row['product'])
    for row in data['inverses']:
        check(row['id']+' inverse '+str(row['p']), all(row['inverse'][a-1]==i+1 for i,a in enumerate(row['p'])))
    for row in data['index']:
        H={tuple(v) for v in row['H']}
        check(row['id']+' H closed under mod-2 addition', all(tuple((a+b)%2 for a,b in zip(u,v)) in H for u in H for v in H))
        check(row['id']+' product group index', len(H)*row['index']==2**5)
        check(row['id']+' D4 index', row['D4_generator_order']*row['D4_index']==8)
    pm=dict(id=(0,1,2),r1=(1,2,0),r2=(2,0,1),t1=(0,2,1),t2=(2,1,0),t3=(1,0,2))
    for a,b,c in data['D3_N07']:
        check(f'N07 D3 {a} then {b}', tuple(pm[b][pm[a][i]] for i in range(3))==pm[c])
    for a,b,c in data['P5_N09']:
        check(f'N09 P5 {a}*{b}', a*b%5==c)


def verify():
    pages, numbers = build.all_pages()
    pdf = fitz.open(ROOT / f'{build.STEM}.pdf')
    check('One PDF page per planned page', len(pdf) == len(pages))
    check('One correct bookmark per page', pdf.get_toc() == [[1, p['title'], n+1] for n, p in enumerate(pages)])
    for n, (page, actual) in enumerate(zip(pages, pdf), 1):
        text = flat(actual.get_text())
        check(f'Page {n} searchable title', flat(page['title']) in text)
        check(f'Page {n} resolved references', '{page:' not in text)
        check(f'Page {n} valid characters', '\ufffd' not in text)
        check(f'Page {n} text within margins', all(b[0] >= 39 and b[1] >= 20 and b[2] <= actual.rect.width-39 and b[3] <= actual.rect.height-20 for b in actual.get_text('blocks')))
        if 'cases-' in page['key'] or 'source-cards-' in page['key'] or page['key'] in ['answer-start', 'my-group', 'my-recurrence', 'new-nov6-mc']:
            for table in tables(page):
                for row in table['rows']:
                    # Exact statements should remain searchable after line wrapping.
                    statement = row[1] if page['key'] == 'answer-start' else row[0]
                    check(f'Page {n} statement searchable: {statement[:36]}', flat(statement) in text)
        for link in actual.get_links():
            check(f'Page {n} link target', link['kind'] == fitz.LINK_GOTO and 0 <= link['page'] < len(pdf))
    front = tables(pages[0])
    for name, table, expected in [('group', front[0], [1, 2, 3, 5]), ('recurrence', front[1], [1, 3, 5])]:
        actual = [int(row[0]) for row in table['rows'] if flat(row[-1]) == 'KRYSS AV']
        check(f'Front {name} exact checkbox set', actual == expected)
    sequence = [11, 12]
    for _ in range(5):
        sequence.append(2*sequence[-1]-3*sequence[-2])
    check('Counterexample: same term at 5, different at 6', sequence == [11, 12, -9, -54, -81, 0, 243])
    check('Correct normalization of user recurrence', Fraction(-8, -4) == 2 and Fraction(12, -4) == -3)
    short_pages = [p for p in pages if p['key'].startswith('rec-checklist-')]
    short = fitz.open(ROOT / 'REKURRENS_SJEKKLISTE.pdf')
    check('Printable checklist has three pages', len(short_pages) == len(short) == 3)
    for i, (page, actual) in enumerate(zip(short_pages, short), 1):
        check(f'Checklist {i} searchable title', flat(page['title']) in flat(actual.get_text()))
        check(f'Checklist {i} text within margins', all(b[0] >= 39 and b[1] >= 20 and b[2] <= actual.rect.width-39 and b[3] <= actual.rect.height-20 for b in actual.get_text('blocks')))
    latest = tables(short_pages[-1])[-1]
    check('Checklist worked example has correct choices', [int(row[0].split('.')[0]) for row in latest['rows'] if flat(row[-1]) == 'KRYSS AV'] == [2, 4, 5, 6])
    check('Worked example three initial values agree', 4*(-2)-3*2 == -14)
    def integer_rule(P, Q, a0, a1):
        if P.denominator == Q.denominator == 1:
            return True
        if a0 == a1 == 0:
            return True
        if a0 == 0:
            return False
        r = Fraction(a1, a0)
        return r.denominator == 1 and r*r == P*r+Q
    for P, Q, a0, a1, expected in [
        (4, -3, 4, 1, True), (Fraction(5, 2), -1, 1, 2, True),
        (Fraction(1, 2), Fraction(1, 2), 0, 0, True),
        (Fraction(1, 2), Fraction(1, 2), 0, 2, False),
        (Fraction(1, 2), Fraction(1, 2), 1, 2, False),
        (Fraction(1, 2), Fraction(1, 2), 2, 1, False),
    ]:
        P, Q = Fraction(P), Fraction(Q)
        check(f'Checklist integer decision {P,Q,a0,a1}', integer_rule(P, Q, a0, a1) == expected)
        seq = [Fraction(a0), Fraction(a1)]
        for _ in range(18):
            seq.append(P*seq[-1]+Q*seq[-2])
        check(f'Integer decision matches exact terms {P,Q,a0,a1}', all(v.denominator == 1 for v in seq) == expected)
    for P, Q, gap, expected in [(4,-3,1,True), (4,-3,2,True), (0,1,2,False), (1,-1,3,False)]:
        H = [0, 1]
        for _ in range(max(0, gap-1)):
            H.append(P*H[-1]+Q*H[-2])
        check(f'Checklist index-gap decision {P,Q,gap}', (H[gap] != 0) == expected)
    group_checks(pages)
    group_pages = [p for p in pages if p['key'].startswith('gp-')]
    group_pdf = fitz.open(ROOT / 'GRUPPER_SVARPROFILER.pdf')
    check('Group lookup includes route, eight profiles and two rule pages', len(group_pages) == len(group_pdf) == 11)
    for i, (page, actual) in enumerate(zip(group_pages, group_pdf), 1):
        text = flat(actual.get_text())
        check(f'Group lookup {i} title searchable', flat(page['title']) in text)
        check(f'Group lookup {i} text within margins', all(b[0] >= 39 and b[1] >= 20 and b[2] <= actual.rect.width-39 and b[3] <= actual.rect.height-20 for b in actual.get_text('blocks')))
        if page['key'] in ['gp-c3','gp-c6','gp-p5','gp-z7z10','gp-z3z10','gp-s3','gp-s6','gp-s2']:
            for row in tables(page)[0]['rows']:
                check(f'Group lookup {i} exact English statement {row[0]}', flat(row[0]) in text)
    check('Group lookup has eleven bookmarks', len(group_pdf.get_toc()) == 11)
    # Exercise the changed-number rules, including the explicitly separated trivial case.
    finite_examples = [(f'C{N}', [N//gcd(N,k) for k in range(N)]) for N in range(1,17)]
    for m,n in [(1,1),(4,2),(2,2),(3,5)]:
        finite_examples.append((f'Z{m}xZ{n}',[lcm(m//gcd(m,a),n//gcd(n,b)) for a in range(m) for b in range(n)]))
    for m in range(2,21):
        units = [a for a in range(1,m) if gcd(a,m)==1]
        finite_examples.append((f'P{m}',[next(k for k in range(1,len(units)+1) if pow(a,k,m)==1) for a in units]))
    for label, element_orders in finite_examples:
        N=len(element_orders)
        is_cyclic=N in element_orders
        check(label+': every generated subgroup proper iff not cyclic', all(o<N for o in element_orders)==(not is_cyclic))
        check(label+': every element generates whole group iff trivial', all(o==N for o in element_orders)==(N==1))
        check(label+': some generated subgroup proper iff nontrivial', any(o<N for o in element_orders)==(N>1))
        if N>1:
            composite=any(N%d==0 for d in range(2,N))
            check(label+': nontrivial proper subgroup for composite order', any(1<o<N for o in element_orders)==composite)
    modular_checks(pages)
    november_checks(pages)
    catalog = build.load('catalog.json')
    attempts = [x for x in catalog if x['kind'] == 'attempt']
    unique = [x for x in attempts if not x.get('duplicate_of')]
    check('60 PDF source catalog entries', len(catalog) == 60)
    check('49 distinct attempts / 147 math questions', len(unique) == 49 and sum(len(x['question_types']) for x in unique) == 147)
    check('Every math question has a method', all(t in build.TYPE_KEYS for x in attempts for t in x['question_types'].values()))
    coverage = []
    for x in attempts:
        for number, typ in x['question_types'].items():
            coverage.append(dict(source_id=x['id'], source_file=x['source_file'], duplicate_of=x.get('duplicate_of') or '', question=number, type=typ, helpsheet_pages=', '.join(str(numbers[key]) for key in build.coverage_keys(x, typ))))
    with (ROOT / 'source' / 'coverage.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(coverage[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(coverage)
    report = dict(passed=len(CHECKS), pdf_pages=len(pdf), distinct_attempts=len(unique), math_questions=sum(len(x['question_types']) for x in unique), checks=CHECKS)
    (ROOT / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(CHECKS)} checks passed: {len(pdf)} searchable pages, {report["math_questions"]} unique source questions covered.')


if __name__ == '__main__':
    verify()
