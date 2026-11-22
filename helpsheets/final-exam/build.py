#!/usr/bin/env python3
"""Build the A4 print guide from guide.py with live PDF text and bookmarks."""
from __future__ import annotations

import html
import re
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Table, TableStyle

from guide import INDEX, PAGES


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'MA224_EKSAMEN_PAPIR.pdf'
FONT_DIR = Path('/usr/share/fonts/truetype/dejavu')
PAGE_W, PAGE_H = A4
MARGIN = 44
TOP_MARGIN = 55
BOTTOM_MARGIN = 58
FRAME_PAD = 6
WIDTH = PAGE_W - 2 * (MARGIN + FRAME_PAD)
HEIGHT = PAGE_H - TOP_MARGIN - BOTTOM_MARGIN - 2 * FRAME_PAD
INK = colors.HexColor('#16191c')
MUTED = colors.HexColor('#40454a')
RULE = colors.HexColor('#c2c4c6')
SHADE = colors.HexColor('#f1f2f3')
DARK = colors.HexColor('#2a3036')


def register_fonts():
    for name, file in [('Main', 'DejaVuSans.ttf'), ('Bold', 'DejaVuSans-Bold.ttf'),
                       ('Mono', 'DejaVuSansMono.ttf')]:
        pdfmetrics.registerFont(TTFont(name, str(FONT_DIR / file)))
    pdfmetrics.registerFontFamily('Main', normal='Main', bold='Bold')


def style(font, size, leading, after=0, before=0, color=INK, center=False):
    s = ParagraphStyle(font, fontName=font, fontSize=size, leading=leading,
                       spaceAfter=after, spaceBefore=before, textColor=color)
    if center:
        s.alignment = TA_CENTER
    return s


STYLES = {
    'title': style('Bold', 23, 27, after=6),
    'cover_title': style('Bold', 29, 34, after=10),
    'prompt': style('Main', 10.4, 14.4, after=13, color=MUTED),
    'p': style('Main', 11, 15.4, after=8),
    'h': style('Bold', 12.7, 16.1, after=5, before=5),
    'code': style('Mono', 10.4, 14.2, after=9),
    'table_cell': style('Main', 10.4, 14),
    'table_head': style('Bold', 10, 13.5, color=colors.white),
    'page_number': style('Bold', 14, 17, center=True),
}


def paragraph(text, kind):
    escaped = html.escape(text, quote=False)
    if kind == 'code':
        # Preserve alignment of mathematical columns in ReportLab paragraphs.
        escaped = escaped.replace(' ', '&nbsp;')
    else:
        escaped = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', escaped)
        escaped = re.sub(r'`([^`]+)`', r'<font name="Mono">\1</font>', escaped)
    return Paragraph(escaped.replace('\n', '<br/>'), STYLES[kind])


def grid(headings, rows, weights, cover=False):
    if any(len(row) != len(headings) for row in rows):
        raise ValueError('Invalid table row')
    header = [paragraph(text, 'table_head') for text in headings]
    body = [[paragraph(text, 'page_number' if cover and i == 2 else 'table_cell')
             for i, text in enumerate(row)] for row in rows]
    result = Table([header, *body], colWidths=[WIDTH * w / sum(weights) for w in weights],
                   hAlign='LEFT')
    pad = 7 if cover else 4.2
    result.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), pad),
        ('BOTTOMPADDING', (0, 0), (-1, -1), pad),
        ('LINEBELOW', (0, 1), (-1, -1), 0.45, RULE),
    ]))
    result.spaceAfter = 10
    return result


def callout(text):
    result = Table([[paragraph(text, 'p')]], colWidths=[WIDTH], hAlign='LEFT')
    result.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), SHADE),
        ('LINEBEFORE', (0, 0), (0, 0), 2.0, DARK),
        ('LEFTPADDING', (0, 0), (0, 0), 11),
        ('RIGHTPADDING', (0, 0), (0, 0), 10),
        ('TOPPADDING', (0, 0), (0, 0), 7),
        ('BOTTOMPADDING', (0, 0), (0, 0), 7),
    ]))
    result.spaceAfter = 10
    return result


def cover(numbers):
    return [
        paragraph('Eksamensark på papir', 'cover_title'),
        paragraph('Diskret matematikk 2 · MA-224', 'prompt'),
        paragraph('Les oppgaven, finn formuleringen i midtkolonnen, og bla til tallet i høyre '
                  'kolonne. Der finner du framgangsmåten og et regnet eksempel.', 'p'),
        grid(['Tema', 'Se etter disse ordene i oppgaven', 'Side'],
             [[f'**{topic}**', clue, str(numbers[key])] for topic, clue, key in INDEX],
             [1.55, 2.95, .49], cover=True),
        callout('Når oppgaven sier **«prove»**, vis steget som gjør argumentet gyldig. '
                'Når den sier **«give a counterexample»**, skriv verdiene, regn ut hva som skjer, '
                'og si hvilket krav som feiler.'),
        paragraph('Bygger på 70 nummererte oppgaver fra de fem MA-224-eksamenene 2021–2025. '
                  'Eksemplene følger oppgavetypene som faktisk ble brukt.', 'p'),
    ]


def page_references(text, numbers):
    return re.sub(r'\{page:([a-z-]+)\}', lambda match: str(numbers[match[1]]), text)


def lesson(page, numbers):
    result = [paragraph(page['title'], 'title'), paragraph(page['prompt'], 'prompt')]
    for kind, value in page['blocks']:
        if kind == 'table':
            headings, rows, weights = value
            rows = [[page_references(cell, numbers) for cell in row] for row in rows]
            result.append(grid(headings, rows, weights))
            continue
        value = page_references(value, numbers)
        result.append(callout(value) if kind == 'box' else paragraph(value, kind))
    return result


def height(flowables):
    return sum(flow.wrap(WIDTH, HEIGHT)[1] + flow.getSpaceBefore() + flow.getSpaceAfter()
               for flow in flowables)


def paint(canvas, doc):
    current = doc.page
    page = PAGES[current - 2] if 1 < current <= len(PAGES) + 1 else None
    canvas.saveState()
    canvas.setFillColor(INK)
    canvas.setFont('Bold', 10)
    label = page['label'].upper() if page else 'SIDEOVERSIKT'
    canvas.drawString(MARGIN + FRAME_PAD, PAGE_H - 30, f'MA-224  /  {label}')
    canvas.setFont('Bold', 23)
    canvas.drawRightString(PAGE_W - MARGIN - FRAME_PAD, PAGE_H - 33, str(current))
    canvas.setStrokeColor(DARK)
    canvas.setLineWidth(.65)
    canvas.line(MARGIN + FRAME_PAD, PAGE_H - 42, PAGE_W - MARGIN - FRAME_PAD, PAGE_H - 42)
    canvas.setStrokeColor(RULE)
    canvas.line(MARGIN + FRAME_PAD, 43, PAGE_W - MARGIN - FRAME_PAD, 43)
    canvas.setFont('Main', 8.6)
    canvas.setFillColor(MUTED)
    citation = f"Sett i {page['exams']}" if page else 'MA-224 · Eksamener 2021–2025 · A4'
    canvas.drawString(MARGIN + FRAME_PAD, 28, citation)
    canvas.drawRightString(PAGE_W - MARGIN - FRAME_PAD, 28, f'{current} / {len(PAGES)+1}')
    canvas.restoreState()


def build():
    register_fonts()
    numbers = {page['key']: i for i, page in enumerate(PAGES, start=2)}
    if set(numbers) != {key for _, _, key in INDEX} or len(numbers) != len(PAGES):
        raise ValueError('The cover must link to every topic once.')
    sections = [cover(numbers), *(lesson(page, numbers) for page in PAGES)]
    story = []
    for n, blocks in enumerate(sections, 1):
        needed = height(blocks)
        if needed > HEIGHT:
            raise ValueError(f'Page {n} needs {needed:.1f} pt, available {HEIGHT:.1f} pt.')
        if n > 1:
            story.append(PageBreak())
        story.extend(blocks)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=A4, title='MA-224 Eksamensark på papir',
                            author='MA-224 hjelpemateriell', leftMargin=MARGIN, rightMargin=MARGIN,
                            topMargin=TOP_MARGIN, bottomMargin=BOTTOM_MARGIN)
    doc.build(story, onFirstPage=paint, onLaterPages=paint)
    with fitz.open(OUTPUT) as pdf:
        if len(pdf) != len(sections):
            raise ValueError('Printed and planned page counts do not match.')
        titles = ['Sideoversikt', *(page['title'] for page in PAGES)]
        pdf.set_toc([[1, title, n] for n, title in enumerate(titles, 1)])
        temp = OUTPUT.with_suffix('.tmp.pdf')
        pdf.save(temp, garbage=4, deflate=True)
    temp.replace(OUTPUT)
    print(f'{OUTPUT}: {len(sections)} A4 pages')


if __name__ == '__main__':
    build()
