#!/usr/bin/env python3
"""Rebuild the searchable PDF and Markdown solely from committed source files."""
from __future__ import annotations

import copy
import html
import json
from pathlib import Path
import re

import fitz
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'source'
VERSION = 6
STEM = f'TEST3DOCSV{VERSION}'
DATE = '5. november 2026'
WIDTH = A4[0] - 88
HEIGHT = A4[1] - 48 - 55 - 12
NAVY = colors.HexColor('#17324e')
BLUE = colors.HexColor('#215c85')
TEAL = colors.HexColor('#087f75')
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')


def load(name):
    return json.loads((SOURCE / name).read_text(encoding='utf-8'))


def make_page(key, title, search='', blocks=None):
    return dict(key=key, title=title, search=search, blocks=blocks or [])


TYPE_KEYS = {
    'initial_distinct': 'rec-roots', 'initial_repeated': 'rec-repeated',
    'particular': 'rec-particular', 'words': 'rec-words',
    'recurrence_mc': 'rec-mc-rules', 'permutation': 'permutation-product',
    'D3': 'D3-table', 'subgroup': 'subgroup-zn', 'group_mc': 'group-read',
    'mod_products': 'mod-product', 'mod_table': 'mod-tables57', 'index': 'index-product',
}
TYPE_NAMES = {
    'initial_distinct': 'Ulike røtter', 'initial_repeated': 'Dobbel rot',
    'particular': 'Gitt p[n]', 'words': 'Antall ord',
    'recurrence_mc': 'Rekurrensflervalg', 'permutation': 'Permutasjoner',
    'D3': 'D3-tabell', 'subgroup': 'Undergrupper', 'group_mc': 'Gruppeflervalg',
    'mod_products': 'Produkt / invers', 'mod_table': 'P_m-tabell', 'index': 'Indeks',
}


def coverage_keys(source, typ):
    ident = source.get('duplicate_of') or source['id']
    if typ == 'recurrence_mc':
        suffix = {'B03': 'a', 'B05': 'a', 'B15': 'b', 'B16': 'b',
                  'B27': 'c', 'B33': 'c', 'B35': 'd', 'B36': 'd', 'N04': 'e'}[ident]
        return ['rec-cases-' + suffix]
    if typ == 'group_mc':
        suffix = {'B05': '1', 'B22': '1', 'B07': '2', 'B34': '2',
                  'B18': '3', 'B08': '3', 'B35': '4'}[ident]
        return ['group-source-cards-' + suffix]
    return {
        'initial_distinct': ['rec-roots', 'rec-repeated'],
        'initial_repeated': ['rec-repeated'],
        'particular': ['rec-particular', 'rec-particular-lookup'],
        'words': ['rec-words', 'rec-words-general'],
        'permutation': ['permutation-product', 'permutation-inverse'],
        'D3': ['D3-table'],
        'subgroup': ['subgroup-zn', 'subgroup-pairs', 'subgroup-pairs-answers'],
        'mod_products': ['mod-product', 'mod-known45-49', 'mod-known50'],
        'mod_table': ['mod-tables57', 'mod-tables89'],
        'index': ['index-product', 'index-d4'],
    }[typ]


def catalog_pages(catalog):
    attempts = [x for x in catalog if x['kind'] == 'attempt']
    pages = []
    for chunk_start in range(0, len(attempts), 14):
        chunk = attempts[chunk_start:chunk_start + 14]
        rows = []
        for src in chunk:
            types = src.get('question_types', [])
            if isinstance(types, dict):
                types = [types.get(str(n), types.get(f'Q{n}', '')) for n in [1, 2, 3]]
            links = [TYPE_NAMES.get(t, t) + '\n' + ', '.join('{page:' + key + '}' for key in coverage_keys(src, t)) for t in types]
            label = src['id'] + (f" (kopi av {src['duplicate_of']})" if src.get('duplicate_of') else '')
            rows.append([label + '\n' + src['source_file']] + links)
        pages.append(make_page(
            f'sources-{len(pages)+1}', f'Kildesjekk: prøvefilene {len(pages)+1}',
            'Originalprøver • kildeoversikt • coverage • B01–B50 • N01–N04',
            [['p', 'Hver regneoppgave er koblet til et oppslag. Sidetallet under oppgavetypen viser hvor du begynner. Kopier er merket.'],
             ['table', dict(headers=['Kilde / fil', 'Oppgave 1', 'Oppgave 2', 'Oppgave 3'], rows=rows, widths=[225, 94, 94, 94])]]))
    notes = [x for x in catalog if x['kind'] != 'attempt']
    rows = [[x['id'] + '\n' + x['source_file'], '\n'.join(x.get('notes', [])) or 'Støttedokument; metoden er kontrollert mot prøveoppgavene.'] for x in notes]
    pages.append(make_page('source-notes', 'Kildegrunnlag og rettelser til gamle notater',
        'Rekursjon_Leselig • regler • source • fortegn • gamle notater',
        [['p', '**Grunnlag:** 50 PDF-er i Delprove_3 på GitHub, fire nyere opplastede prøver og de to flervalgsspørsmålene fra ditt eget skjermbilde. Etter fjerning av identiske kopier: **43 ulike PDF-prøver med 129 regneoppgaver**. Signeringskode er ikke en regneoppgave.'],
         ['table', dict(headers=['Støttedokument', 'Bruk / merknad'], rows=rows, widths=[230, 277])],
         ['box', '**Gamle tekstnotater har feil.** Én lik verdi bestemmer ikke en andreordens følge. Z/7 × Z/10 er endelig og har 70 elementer. For a[n]=2*a[n-1]−2*a[n-2], a0=0,a1=−128 blir a2=−256, ikke −253. «None of the above» avhenger alltid av de andre alternativene.'],
         ['p', 'De to tekstnotatene og fire håndskrevne bildene i originalmappen er støttemateriale. Avkryssinger og prosenttall i tidligere forsøk er ikke alene brukt som fasit. Hver metode og svartabell er kontrollert matematisk.']]))
    return pages


def all_pages():
    front = load('front.json')
    checklist = load('recurrence-checklist.json')
    body = load('recurrence.json') + load('groups.json') + load('modular.json')
    catalog = load('catalog.json')
    tail = catalog_pages(catalog)
    destinations = [(p['title'], p['key']) for p in checklist + body + tail]
    toc = []
    for n, start in enumerate(range(0, len(destinations), 19), 1):
        toc.append(make_page(f'contents-{n}', f'Innhold {n}: klikk på oppgaven',
            'Cmd+F • Ctrl+F • søkbar • innhold',
            [['p', 'Ferdige avkryssinger til dine to spørsmål står på **side 1**. Klikk på en rad for å gå direkte til oppslaget. Du kan også søke på engelske ord fra oppgaveteksten.'],
             ['toc', destinations[start:start+19]]]))
    pages = front + checklist + toc + body + tail
    keys = [p['key'] for p in pages]
    if len(keys) != len(set(keys)):
        raise ValueError('Repeated page keys: ' + str([k for k in keys if keys.count(k) > 1]))
    numbers = {p['key']: i+1 for i, p in enumerate(pages)}
    missing = sorted(set(TYPE_KEYS.values()) - set(numbers))
    if missing:
        raise ValueError('Source coverage targets missing: ' + str(missing))

    def resolve(value):
        if isinstance(value, str):
            return re.sub(r'\{page:([\w-]+)\}', lambda m: str(numbers[m[1]]), value)
        if isinstance(value, list):
            return [resolve(v) for v in value]
        if isinstance(value, dict):
            return {k: resolve(v) for k, v in value.items()}
        return value
    return resolve(pages), numbers


def init_fonts():
    for name, file in [('DV', 'DejaVuSans.ttf'), ('DV-Bold', 'DejaVuSans-Bold.ttf'), ('DVM', 'DejaVuSansMono.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
    pdfmetrics.registerFontFamily('DV', normal='DV', bold='DV-Bold', italic='DV', boldItalic='DV-Bold')


def styles(scale):
    specs = {
        'title': dict(fontName='DV-Bold', fontSize=19, leading=24, textColor=NAVY, spaceAfter=9),
        'search': dict(fontName='DV', fontSize=8.3, leading=11, textColor=BLUE, spaceAfter=10),
        'p': dict(fontName='DV', fontSize=10, leading=14.3, textColor=NAVY, spaceAfter=9),
        'h': dict(fontName='DV-Bold', fontSize=12, leading=16, textColor=BLUE, spaceBefore=3, spaceAfter=6),
        'code': dict(fontName='DVM', fontSize=9.7, leading=14, textColor=NAVY, spaceAfter=8),
        'cell': dict(fontName='DV', fontSize=8.8, leading=12, textColor=NAVY),
        'white': dict(fontName='DV-Bold', fontSize=8.8, leading=12, textColor=colors.white),
    }
    for name, values in specs.items():
        for attr in ['fontSize', 'leading', 'spaceAfter', 'spaceBefore']:
            if attr in values:
                values[attr] *= scale
    return {k: ParagraphStyle(k, **v) for k, v in specs.items()}


def markup(value):
    s = html.escape(str(value), quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s, flags=re.S)
    return s.replace('\n', '<br/>')


def blocks(page, scale, numbers):
    ss = styles(scale)
    par = lambda text, kind='p': Paragraph(markup(text), ss[kind])
    result = [Paragraph(f'<a name="{page["key"]}"/>' + markup(page['title']), ss['title']), par('Søk: ' + page.get('search', ''), 'search')]
    for kind, value in page['blocks']:
        if kind in ['p', 'h', 'code']:
            result.append(par(value, kind))
        elif kind == 'box':
            t = Table([[par(value)]], colWidths=[WIDTH])
            t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.HexColor('#e7f3ee')),
                ('BOX', (0, 0), (-1, -1), .4, colors.HexColor('#c9e2d7')),
                ('LEFTPADDING', (0, 0), (-1, -1), 10), ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                ('TOPPADDING', (0, 0), (-1, -1), 8*scale), ('BOTTOMPADDING', (0, 0), (-1, -1), 1)]))
            t.spaceAfter = 10*scale
            result.append(t)
        elif kind in ['table', 'toc']:
            if kind == 'table':
                headers, rows = value['headers'], value['rows']
                widths = value.get('widths') or [1]*len(headers)
                cells = [[par(h, 'white') for h in headers]] + [[par(c, 'cell') for c in row] for row in rows]
                for row in rows:
                    if len(row) != len(headers):
                        raise ValueError(f'{page["key"]}: invalid table row {row}')
            else:
                widths = [WIDTH-45, 45]
                cells = [[Paragraph(f'<link href="#{key}" color="#215c85">' + markup(title) + '</link>', ss['cell']), par(numbers[key], 'cell')] for title, key in value]
            t = Table(cells, colWidths=[WIDTH*w/sum(widths) for w in widths], hAlign='LEFT', repeatRows=1 if kind == 'table' else 0)
            ts = [('VALIGN', (0, 0), (-1, -1), 'TOP'), ('ROWBACKGROUNDS', (0, 1 if kind == 'table' else 0), (-1, -1), [colors.HexColor('#edf4f9'), colors.white]),
                  ('LEFTPADDING', (0, 0), (-1, -1), 5), ('RIGHTPADDING', (0, 0), (-1, -1), 5),
                  ('TOPPADDING', (0, 0), (-1, -1), 4.6*scale), ('BOTTOMPADDING', (0, 0), (-1, -1), 4.6*scale)]
            if kind == 'table':
                ts.append(('BACKGROUND', (0, 0), (-1, 0), BLUE))
            t.setStyle(TableStyle(ts))
            t.spaceAfter = 10*scale
            result.append(t)
        else:
            raise ValueError(f'{page["key"]}: unknown block {kind}')
    return result


def fit_page(page, numbers):
    for scale in ([.94, .91, .88, .85] if page['key'] == 'answer-start' else [1, .97, .94, .91, .88, .85]):
        rendered = blocks(page, scale, numbers)
        height = sum(flow.wrap(WIDTH, HEIGHT)[1] + flow.getSpaceBefore() + flow.getSpaceAfter() for flow in rendered)
        if height <= HEIGHT-2:
            return rendered, dict(key=page['key'], scale=scale, content_height=round(height, 2))
    raise ValueError(f'Page too crowded, split it: {page["key"]}, height={height:.1f}, maximum={HEIGHT:.1f}')


def footer(canvas, doc, total):
    canvas.saveState()
    canvas.setFillColor(TEAL)
    canvas.rect(44, A4[1]-27, 32, 3, fill=1, stroke=0)
    canvas.setStrokeColor(colors.HexColor('#cfdae4'))
    canvas.line(44, 42, A4[0]-44, 42)
    canvas.setFillColor(NAVY)
    canvas.setFont('DV', 8)
    canvas.drawString(44, 27, f'MA-224 • Delprøve 3 • Versjon {VERSION} • {DATE}')
    canvas.drawRightString(A4[0]-44, 27, f'{doc.page} / {total}')
    canvas.restoreState()


def markdown(pages, numbers):
    lines = [f'# MA-224 – Delprøve 3 – Hjelpeark versjon {VERSION}', '', f'Gjenoppbygd {DATE}. Søk med Cmd+F / Ctrl+F. Sidetall viser til PDF-en.', '']
    for n, page in enumerate(pages, 1):
        lines += [f'## Side {n}: {page["title"]}', '', 'Søk: ' + page.get('search', ''), '']
        for kind, value in page['blocks']:
            if kind in ['p', 'box']:
                lines += [value, '']
            elif kind == 'h':
                lines += ['### ' + value, '']
            elif kind == 'code':
                lines += ['```text', value, '```', '']
            elif kind == 'table':
                clean = lambda x: str(x).replace('|', '\\|').replace('\n', '<br>')
                lines += ['| ' + ' | '.join(map(clean, value['headers'])) + ' |', '| ' + ' | '.join(['---']*len(value['headers'])) + ' |']
                lines += ['| ' + ' | '.join(map(clean, row)) + ' |' for row in value['rows']] + ['']
            elif kind == 'toc':
                lines += [f'- {title}: side {numbers[key]}' for title, key in value] + ['']
    return '\n'.join(lines)


def build():
    init_fonts()
    pages, numbers = all_pages()
    story, layout = [], []
    for n, page in enumerate(pages):
        if n:
            story.append(PageBreak())
        content, metric = fit_page(page, numbers)
        story += content
        layout.append(metric)
    pdf = ROOT / f'{STEM}.pdf'
    doc = SimpleDocTemplate(str(pdf), pagesize=A4, rightMargin=44, leftMargin=44, topMargin=48, bottomMargin=55,
        title=f'MA-224: Delprøve 3 – søkbart hjelpeark, versjon {VERSION}', author='Hjelpeark fra prøvemappen og opplastede forsøk',
        subject='Konkrete flervalgssvar, rekurrens, permutasjoner, grupper, modulo og indeks')
    paint = lambda c, d: footer(c, d, len(pages))
    doc.build(story, onFirstPage=paint, onLaterPages=paint)
    document = fitz.open(pdf)
    assert len(document) == len(pages), (len(document), len(pages))
    for n, page in enumerate(pages):
        assert ' '.join(page['title'].split()) in ' '.join(document[n].get_text().split()), (n+1, page['key'])
    document.set_toc([[1, p['title'], n+1] for n, p in enumerate(pages)])
    temporary = pdf.with_suffix('.tmp.pdf')
    document.save(temporary, garbage=4, deflate=True)
    document.close()
    temporary.replace(pdf)
    (ROOT / f'{STEM}.md').write_text(markdown(pages, numbers), encoding='utf-8')
    # A short printable checklist, rebuilt from the same source as the full PDF.
    selected = [p for p in pages if p['key'].startswith('rec-checklist-')]
    short_numbers = {p['key']: i+1 for i, p in enumerate(selected)}
    short_story = []
    for i, page in enumerate(selected):
        if i:
            short_story.append(PageBreak())
        content, _ = fit_page(page, short_numbers)
        short_story.extend(content)
    short = ROOT / 'REKURRENS_SJEKKLISTE.pdf'
    short_doc = SimpleDocTemplate(str(short), pagesize=A4, rightMargin=44, leftMargin=44, topMargin=48, bottomMargin=55,
        title='Rekurrensflervalg – sjekkliste', author='MA-224 hjelpeark', subject='Faste svar, indekser og heltall')
    short_paint = lambda c, d: footer(c, d, len(selected))
    short_doc.build(short_story, onFirstPage=short_paint, onLaterPages=short_paint)
    (ROOT / 'build-manifest.json').write_text(json.dumps(dict(version=VERSION, date=DATE, pages=len(pages), page_numbers=numbers, layout=layout), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'Built {pdf}: {len(pages)} searchable pages.')


if __name__ == '__main__':
    build()
