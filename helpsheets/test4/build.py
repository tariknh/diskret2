#!/usr/bin/env python3
"""Rebuild the searchable PDF and Markdown solely from committed source files."""
from __future__ import annotations

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
VERSION = 2
STEM = f'TEST4DOCSV{VERSION}'
DATE = '18. november 2026'
WIDTH = A4[0] - 88
HEIGHT = A4[1] - 48 - 55 - 12
NAVY = colors.HexColor('#17324e')
BLUE = colors.HexColor('#215c85')
TEAL = colors.HexColor('#087f75')
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')


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
    canvas.drawString(44, 27, f'MA-224 • Delprøve 4 • Versjon {VERSION} • {DATE}')
    canvas.drawRightString(A4[0]-44, 27, f'{doc.page} / {total}')
    canvas.restoreState()


def markdown(pages, numbers):
    lines = [f'# MA-224 – Delprøve 4 – Hjelpeark versjon {VERSION}', '', f'Gjenoppbygd {DATE}. Søk med Cmd+F / Ctrl+F. Sidetall viser til PDF-en.', '']
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


def all_pages():
    pages=json.loads((SOURCE / 'guide.json').read_text(encoding='utf-8'))
    numbers={p['key']: i+1 for i,p in enumerate(pages)}
    assert len(numbers)==len(pages)
    def resolve(v):
        if isinstance(v,str): return re.sub(r'\{page:([\w-]+)\}', lambda m:str(numbers[m[1]]),v)
        if isinstance(v,list): return [resolve(x) for x in v]
        if isinstance(v,dict): return {k:resolve(x) for k,x in v.items()}
        return v
    return resolve(pages),numbers

def build():
    init_fonts()
    pages,numbers=all_pages()
    story,layout=[],[]
    for n,page in enumerate(pages):
        if n: story.append(PageBreak())
        content,metric=fit_page(page,numbers)
        story.extend(content); layout.append(metric)
    pdf=ROOT / f'{STEM}.pdf'
    doc=SimpleDocTemplate(str(pdf),pagesize=A4,rightMargin=44,leftMargin=44,topMargin=48,bottomMargin=55,
        title=f'MA-224: Delprøve 4 – søkbart hjelpeark V{VERSION}',author='MA-224 hjelpeark',
        subject='RSA, Hamming, bitfeil, generator- og kontrollmatriser, syndrom og dekoding')
    paint=lambda c,d:footer(c,d,len(pages))
    doc.build(story,onFirstPage=paint,onLaterPages=paint)
    document=fitz.open(pdf)
    assert len(document)==len(pages),(len(document),len(pages))
    for i,page in enumerate(pages):
        assert ' '.join(page['title'].split()) in ' '.join(document[i].get_text().split()),page['key']
    document.set_toc([[1,p['title'],i+1] for i,p in enumerate(pages)])
    temporary=pdf.with_suffix('.tmp.pdf');document.save(temporary,garbage=4,deflate=True);document.close();temporary.replace(pdf)
    (ROOT / f'{STEM}.md').write_text(markdown(pages,numbers),encoding='utf-8')
    (ROOT / 'build-manifest.json').write_text(json.dumps(dict(version=VERSION,date=DATE,pages=len(pages),page_numbers=numbers,layout=layout),ensure_ascii=False,indent=2)+'\n')
    print(f'Built {pdf}: {len(pages)} searchable pages.')

if __name__=='__main__': build()
