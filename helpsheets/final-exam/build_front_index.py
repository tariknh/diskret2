#!/usr/bin/env python3
"""Build the duplex paper index. References use PDF pages counted from 1."""
from dataclasses import dataclass
from pathlib import Path

import fitz
from reportlab.platypus import PageBreak, SimpleDocTemplate, TableStyle

from build import (BOTTOM_MARGIN, DARK, FRAME_PAD, HEIGHT, INK, MARGIN, MUTED,
                   PAGE_H, PAGE_W, RULE, TOP_MARGIN, grid, height, paragraph,
                   register_fonts)


OUTPUT = Path(__file__).with_name('MA224_FORSIDE_OPPSLAG.pdf')


@dataclass(frozen=True)
class Solution:
    year: int
    task: str
    pages: str
    caveat: bool = False
    hint: str = ''

    def label(self):
        flag = '†' if self.caveat else ''
        prefix = f'{self.hint} ' if self.hint else ''
        return f'{prefix}{self.year} Q{self.task} · s. {self.pages}{flag}'


@dataclass(frozen=True)
class Lookup:
    prompt: str
    guide: str
    solutions: tuple[Solution, ...]
    handins: tuple[str, ...] = ()

    def row(self):
        return [f'**{self.prompt}**', f'**{self.guide}**',
                '\n'.join(x.label() for x in self.solutions) or '–',
                '\n'.join(self.handins) or '–']


S = Solution
L = Lookup
FRONT = [
    L('Truth tables + logical inferences', '2',
      (S(2025, '1', '1–2'), S(2022, '1', '1–2')),
      ('H01 Task 2–3 · s. 2–3',)),
    L('Find the flaws / fix the proof', '2', (S(2024, '1', '1'),),
      ('H01 Task 6 · s. 4',)),
    L('Peano definitions / induction', '3',
      (S(2024, '2', '2'), S(2023, '1–2', '1–2', True)),
      ('H01 Task 5 · s. 3', 'H02 Task 5 · s. 7')),
    L('Induction on strings or sequences', '3',
      (S(2025, '2', '3', hint='Streng'), S(2022, '2', '2', hint='Følge'), S(2021, '1–2', '1')),
      ('H02 Task 6 · s. 7–8', 'H07 7.2 · s. 20')),
    L('Derivation / syntax tree / EBNF', '4',
      (S(2023, '3', '3–4'), S(2021, '3–4', '2–3')),
      ('H03 Task 1, 4 · s. 9–10',)),
    L('Ambiguous grammar / two trees', '4',
      (S(2025, '3', '4–5'), S(2024, '3', '3'), S(2022, '3', '3–4')),
      ('H03 Task 3 · s. 9', 'H03 Task 5 · s. 11')),
    L('NFA → DFA / minimize', '5',
      (S(2023, '4', '5–7'), S(2021, '5', '3–5')),
      ('H04 Task 1, 3 · s. 13–14',)),
    L('NFA → regular expression', '6',
      (S(2025, '4', '5–6'), S(2022, '4', '4–5'), S(2021, '6', '6–7'))),
    L('Regex → right-regular grammar', '6',
      (S(2024, '4', '3–4'),), ('H04 Task 6 · s. 14–15',)),
    L('Correct implementation / refinement', '7',
      (S(2023, '5', '8'), S(2022, '5', '6–7'), S(2025, '5', '7–8', True), S(2021, '10', '9')),
      ('H05 Task 6 · s. 17–18',)),
    L('Extend the JML definition', '7',
      (S(2024, '5', '5'), S(2021, '9', '9')), ('H05 Task 5 · s. 16–17',)),
    L('Reflexive / symmetric / transitive / order', '8',
      (S(2025, '6', '8'), S(2024, '6', '6–7'), S(2021, '11', '9–10')),
      ('H06 6.1, 6.3–4 · s. 19*',)),
    L('Antisymmetry proof / equivalence classes', '8',
      (S(2023, '6', '8–9', hint='Anti.'), S(2022, '6', '7', hint='Klasser'), S(2021, '12', '10–11')),
      ('H06 6.5–6 · s. 19*',)),
]
BACK = [
    L('Initial values / double root', '9', (S(2024, '7', '7'),),
      ('H07 7.1 · s. 20', 'Første orden')),
    L('Particular solution / find a recurrence', '9',
      (S(2021, '13', '11', hint='Part.'), S(2025, '7', '9', hint='Regel')),
      ('H07 7.5–6 · s. 21', 'Lag regel fra tekst')),
    L('Period / prove a sequence increases', '9, 3',
      (S(2022, '7', '8', True, 'Periode'), S(2023, '7', '10–11', True, 'Vekst')),
      ('H07 7.2 · s. 20 (økende)',)),
    L('Group table / identity / element order', '10',
      (S(2025, '8', '10'), S(2021, '15', '12–13')), ('H08 8.2 · s. 22',)),
    L('Cyclic group / subgroups / group inverse', '10',
      (S(2022, '8–9', '9–10'), S(2021, '14', '12'), S(2024, '8', '8', hint='Invers'), S(2023, '8', '11')),
      ('H08 8.4–6 · s. 23',)),
    L('Index / Lagrange / possible orders', '10',
      (S(2022, '10', '10'), S(2023, '10', '12–13'), S(2025, '10', '11', True),
       S(2024, '10', '8'), S(2021, '19', '14')),
      ('H09 9.4–6 · s. 25',)),
    L('Euler totient / order of Pₙ', '11',
      (S(2025, '9', '11'), S(2024, '9', '8')), ('H09 9.2 · s. 24', 'H10 10.4–5 · s. 29–30')),
    L('Extended Euclid / inverse / integer solutions', '11',
      (S(2021, '16–17', '13'), S(2023, '9', '12', hint='Heltall')), ('H10 10.1 · s. 26',)),
    L('Modulo powers / Fermat / RSA', '11',
      (S(2021, '18, 20', '14–15'),), ('H10 10.2–3 · s. 26–29',)),
    L('Min distance / detect errors', '12',
      (S(2025, '11', '12'), S(2023, '11', '13–14'), S(2021, '21', '15–16')),
      ('H11 11.3–4 · s. 31–32',)),
    L('Build G to correct or detect', '12',
      (S(2024, '11', '9–10'), S(2022, '12', '12–13'), S(2021, '22', '16–17'))),
    L('H / syndrome / is r a codeword?', '13',
      (S(2025, '12', '13'), S(2022, '11', '11')), ('H12 12.1 · s. 33*',)),
    L('Coset leaders / can we correct a bit?', '13',
      (S(2023, '12', '15–16'), S(2024, '12', '10')), ('H12 12.1 · s. 33*', 'Rette en bitfeil')),
    L('Turing machine / watchdog', '14', (S(2021, '7–8', '7–8'),)),
]


def lookup_table(rows):
    rendered = grid(['Se etter i oppgaven', 'Ark', 'Løsning i gammel eksamen', 'Handin-vedlegg'],
                    [lookup.row() for lookup in rows], [1.75, .40, 1.62, 1.46])
    rendered.setStyle(TableStyle([
        ('TOPPADDING', (0, 1), (-1, -1), 2.8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 2.8),
    ]))
    return rendered


def paint(canvas, doc):
    left = MARGIN + FRAME_PAD
    right = PAGE_W - left
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.setFont('Bold', 10)
    canvas.drawString(left, PAGE_H - 30, 'MA-224  /  OPPSLAG PÅ PAPIR')
    canvas.drawRightString(right, PAGE_H - 30, f'{doc.page} / 2')
    canvas.setStrokeColor(DARK)
    canvas.setLineWidth(.65)
    canvas.line(left, PAGE_H - 42, right, PAGE_H - 42)
    canvas.setStrokeColor(RULE)
    canvas.line(left, 43, right, 43)
    canvas.setFillColor(MUTED)
    canvas.setFont('Main', 8.6)
    canvas.drawString(left, 28, 'Eksamener 2021–2025 · Eksamensarket på 15 sider · Handin-vedlegget på 34 sider')
    canvas.restoreState()


def build():
    register_fonts()
    common_note = paragraph('† Se rettelsen eller forutsetningen i eksamensarket. '
                            '* H06 og H12 inneholder oppgavetekst.', 'table_cell')
    sections = [
        [paragraph('Finn en løst oppgave', 'title'),
         paragraph('Logikk, induksjon, grammatikk, automater, programmer og relasjoner', 'prompt'),
         paragraph('**Ark** = eksamensarket. **2025 Q1 · s. 1–2** = Problem 1, PDF-side 1–2 i 2025-eksamenen. '
                   '**Handin** = sidetall i vedlegget. Bruk første løsning som passer formuleringen.', 'p'),
         lookup_table(FRONT), common_note],
        [paragraph('Rekurrens, grupper og koder', 'title'),
         lookup_table(BACK),
         paragraph('**Tidslogikk og semantikk:** Ark s. 15. **RSA:** Delprøve 4 V3, s. 8–12. '
                   '**Bitfeil:** Delprøve 4 V3, s. 16–18 og H11 11.2, s. 31.', 'table_cell'),
         common_note],
    ]
    story = []
    for number, section in enumerate(sections, 1):
        needed = height(section)
        if needed > HEIGHT:
            raise ValueError(f'Index side {number} needs {needed:.1f} pt; available {HEIGHT:.1f}.')
        if story:
            story.append(PageBreak())
        story.extend(section)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=(PAGE_W, PAGE_H),
                            title='MA-224 · Finn en løst oppgave', author='MA-224 hjelpemateriell',
                            leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
    doc.build(story, onFirstPage=paint, onLaterPages=paint)
    with fitz.open(OUTPUT) as pdf:
        assert len(pdf) == len(sections)
        pdf.set_toc([[1, 'Logikk til relasjoner', 1], [1, 'Rekurrens til kodeteori', 2]])
        temporary = OUTPUT.with_suffix('.tmp.pdf')
        pdf.save(temporary, garbage=4, deflate=True)
    temporary.replace(OUTPUT)
    print(f'{OUTPUT}: {len(FRONT) + len(BACK)} lookups on one duplex A4 sheet')


if __name__ == '__main__':
    build()
