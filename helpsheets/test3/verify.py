#!/usr/bin/env python3
"""Check the rendered document and independently recalculate answer tables."""
from collections import Counter
import csv
from fractions import Fraction
from itertools import permutations
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
    sizes = [len(x) for x in orders]
    check('Group sizes derived from elements', sizes == [3, 6, 4, 70, 30, 6, 720])
    cyclic = [N in values for N, values in zip(sizes, orders)]
    # The first five are cyclic. In each S_n the transpositions (12),(23) do not commute.
    abelian = []
    for n in [3, 6]:
        a = list(range(n)); a[0], a[1] = a[1], a[0]
        b = list(range(n)); b[1], b[2] = b[2], b[1]
        abelian.append(all(b[a[i]] == a[b[i]] for i in range(n)))
    abelian = [True]*5 + abelian
    proper = [any(1 < o < N for o in values) for N, values in zip(sizes, orders)]
    lookup = {
        'The group G is finite.': [True]*7,
        'The group G is infinite.': [False]*7,
        'The group G is abelian.': abelian,
        'For all elements a,b ∈ G, the following is true: ab = ba.': abelian,
        'The group G is not abelian.': [not x for x in abelian],
        'There exist elements g,h ∈ G such that gh ≠ hg.': [not x for x in abelian],
        'The group G is cyclic.': cyclic,
        'The group G is not cyclic.': [not x for x in cyclic],
        'There exists an element g ∈ G such that ⟨g⟩=G.': cyclic,
        'There exists an element g ∈ G such that the order of the subgroup ⟨g⟩ equals the order of G.': cyclic,
        'For each element g ∈ G, the subgroup ⟨g⟩ ⊊ G is a proper subgroup of G.': [not x for x in cyclic],
        'For each element g ∈ G, ⟨g⟩=G.': [False]*7,
        'There exists an element g ∈ G such that ⟨g⟩ is a proper subgroup of G.': [True]*7,
        'The group G has a non-trivial and proper subgroup.': proper,
        'The only subgroups of G are the trivial subgroup {e}, and G itself.': [not x for x in proper],
        'The order of G is divisible by 3.': [N % 3 == 0 for N in sizes],
    }
    for page in pages:
        if not page['key'].startswith('group-matrix-'):
            continue
        for row in tables(page)[0]['rows']:
            statement = row[0]
            if statement.startswith('Riktig antall'):
                check('Group order lookup values', list(map(int, row[1:])) == sizes)
                continue
            match = re.fullmatch(r'The order of G is (\d+)\.', statement)
            expected = [N == int(match[1]) for N in sizes] if match else lookup[statement]
            actual = [flat(v) == 'JA' for v in row[1:]]
            check(statement + ' (all seven columns)', actual == expected)


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
        if 'cases-' in page['key'] or 'source-cards-' in page['key'] or page['key'] in ['answer-start', 'my-group', 'my-recurrence']:
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
    group_checks(pages)
    modular_checks(pages)
    catalog = build.load('catalog.json')
    attempts = [x for x in catalog if x['kind'] == 'attempt']
    unique = [x for x in attempts if not x.get('duplicate_of')]
    check('54 PDF source catalog entries', len(catalog) == 54)
    check('43 distinct attempts / 129 math questions', len(unique) == 43 and sum(len(x['question_types']) for x in unique) == 129)
    check('Every math question has a method', all(t in build.TYPE_KEYS for x in attempts for t in x['question_types'].values()))
    coverage = []
    for x in attempts:
        for number, typ in x['question_types'].items():
            coverage.append(dict(source_id=x['id'], source_file=x['source_file'], duplicate_of=x.get('duplicate_of') or '', question=number, type=typ, helpsheet_pages=', '.join(str(numbers[key]) for key in build.coverage_keys(x, typ))))
    with (ROOT / 'source' / 'coverage.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(coverage[0]), lineterminator='\n')
        writer.writeheader(); writer.writerows(coverage)
    report = dict(passed=len(CHECKS), pdf_pages=len(pdf), distinct_attempts=43, math_questions=129, checks=CHECKS)
    (ROOT / 'verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{len(CHECKS)} checks passed: {len(pdf)} searchable pages, 129 unique source questions covered.')


if __name__ == '__main__':
    verify()
