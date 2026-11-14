#!/usr/bin/env python3
"""Recalculate the source answers independently and check the published PDF."""
import itertools,json,math,re
from pathlib import Path
import fitz
import build
R=Path(__file__).resolve().parent
A=json.loads((R/'source/cases.json').read_text());C=json.loads((R/'source/catalog.json').read_text());O=json.loads((R/'source/rsa-options.json').read_text())
checks=0
def check(v,label):
 global checks
 assert v,label
 checks+=1
def words(G):
 return sorted({''.join(str(sum(G[i][j]*u[i] for i in range(len(G)))%2) for j in range(len(G[0]))) for u in itertools.product([0,1],repeat=len(G))})
def dist(a,b):return sum(x!=y for x,y in zip(a,b))
def isprime(v):return v>=2 and all(v%d for d in range(2,math.isqrt(v)+1))
def syn(r,H):return ''.join(str(sum(int(b)*h for b,h in zip(r,row))%2) for row in H)
check(len(C)==44 and len(A)==36,'file inventory')
check(sum(not c['duplicate_of'] for c in C if c['kind']=='attempt')==32,'32 distinct attempts')
check(len(O)==30 and sum(o['valid'] for o in O)==10,'30 RSA options,10 valid')
for o in O:
 good=isprime(o['p']) and isprime(o['q']) and o['p']!=o['q'] and o['n']==o['p']*o['q'] and (o['x']*o['y'])%((o['p']-1)*(o['q']-1))==1
 check(o['valid']==good,f"RSA option {o['x']}")
for a in A:
 for q in a['tasks']:
  label=a['id']+' '+q['type']
  if q['type']=='rsa_break':
   check(isprime(q['p']) and isprime(q['q']) and q['n']==q['p']*q['q'],label+' factors')
   phi=(q['p']-1)*(q['q']-1)
   check(q['y']==pow(q['x'],-1,phi),label+' inverse')
   check(q['plain']==pow(q['cipher'],q['y'],q['n']),label+' plaintext')
   check(pow(q['plain'],q['x'],q['n'])==q['cipher'],label+' encrypt back')
  elif q['type']=='hamming':
   ds=[dist(u,v) for u,v in itertools.combinations(q['words'],2)]
   check(ds==q['distances'] and min(ds)==q['minimum'] and max(ds)==q['maximum'],label)
  elif q['type']=='channel':
   # Enumerate all 128 received strings instead of using binomial formulas.
   p=q['p'];probs={v:p**dist(q['w'],v)*(1-p)**(len(v)-dist(q['w'],v)) for b in itertools.product('01',repeat=len(q['w'])) for v in [''.join(b)]}
   vals=[probs[q['w']],sum(pr for v,pr in probs.items() if dist(q['w'],v)<=q['upto']),probs[q['r']]]
   check([round(v,3) for v in vals]==q['answers'],label)
   check(abs(sum(probs.values())-1)<1e-10,label+' total probability')
  elif 'G' in q:
   G,H=q['G'],q['H'];cw=words(G);n=len(G[0])
   check(cw==sorted(q['codewords']) and len(cw)==2**len(G),label+' codewords')
   nullspace=[''.join(b) for b in itertools.product('01',repeat=n) if syn(''.join(b),H)=='0'*len(H)]
   check(cw==nullspace,label+' H nullspace')
   dm=min(dist(u,v) for u,v in itertools.combinations(cw,2))
   check(dm==q['dmin'],label+' pairwise distance')
   check(q['detect']==dm-1 and q['correct']==(dm-1)//2,label+' detection/correction')
   check(q['example_code'] in cw and '1' in q['example_code'],label+' nonzero codeword')
   check(q['example_noncode'] not in cw,label+' noncodeword')
   if 'r' in q:check(q['syndrome']==syn(q['r'],H),label+' syndrome')
   if q['type']=='syndrome_decode':
    best=min(dist(q['r'],w) for w in cw);nearest=[w for w in cw if dist(q['r'],w)==best]
    check(nearest==[q['decoded']] and best==q['error_weight']==1,label+' unique nearest')
    check(''.join(str(int(a)^int(b)) for a,b in zip(q['decoded'],q['error']))==q['r'],label+' error pattern')
pages,numbers=build.all_pages()
by_key={p['key']:p for p in pages}
def rows(key):return [row for kind,table in by_key[key]['blocks'] if kind=='table' for row in table['rows']]
def matrix_text(M):return '\n'.join(' '.join(map(str,row)) for row in M)
def unique(typ,fields):
    out={}
    for a in A:
        for q in a['tasks']:
            if q['type']==typ:out.setdefault(json.dumps([q[k] for k in fields]),q)
    return list(out.values())
for o in O:
    row=next(row for i in range(1,4) for row in rows('rsa-options-'+str(i)) if row[0].splitlines()[0]=='x='+str(o['x']))
    check(row[0]=='x='+str(o['x'])+'\ny='+str(o['y']) and row[1]==f"p={o['p']}, q={o['q']}\nn={o['n']}",'RSA lookup exact tuple')
    check((row[2]=='KRYSS AV')==o['valid'],'RSA lookup choice')
expected=[[f"{q['n']} ; {q['x']}",f"{q['p']} ; {q['q']} ; {q['phi']}",f"{q['cipher']} → {q['plain']}",str(q['y'])] for q in unique('rsa_break',['n','x','cipher'])]
check(rows('rsa-known')==expected,'RSA lookup all answers')
expected=[['\n'.join(q['words']),' '.join(map(str,q['distances'])),f"{q['minimum']} ; {q['maximum']}"] for q in unique('hamming',['words'])]
check(rows('hamming-known-1')+rows('hamming-known-2')==expected,'Hamming lookup all answers')
expected=[[f"{q['p']:.3f} ; {q['upto']}",q['w']+' →\n'+q['r'],str(q['d']),' ; '.join(f'{v:.3f}' for v in q['answers'])] for q in unique('channel',['p','w','r','upto'])]
check(rows('channel-known')==expected,'BSC lookup all answers')
expected=[[matrix_text(q['G']),matrix_text(q['H']),q['r']+' → '+q['syndrome']] for q in unique('coding_matrices',['G','r'])]
check([row for i in range(1,5) for row in rows('matrices-known-'+str(i))]==expected,'G H syndrome lookup all answers')
codes={}
for a in A:
    q=a['tasks'][2]
    if q['type'] in ['code_dmin','code_detect']:codes.setdefault(json.dumps(q['G']),q)
expected=[['\n'.join(''.join(map(str,row)) for row in q['G']),f"{q['dmin']} ; {q['detect']}",q['example_code'],q['example_noncode']] for q in codes.values()]
check([row for i in range(1,4) for row in rows('distance-known-'+str(i))]==expected,'code distance lookup all answers')
dec=unique('syndrome_decode',['G','r']);gids={}
for q in dec:gids.setdefault(json.dumps(q['G']),'D'+str(len(gids)+1))
expected=[[gids[json.dumps(q['G'])],q['r'],q['syndrome'],q['error'],q['decoded']] for q in dec]
check(rows('decode-known')==expected,'decode lookup all answers')
expected_matrices=[]
for key in gids:
    q=next(q for q in dec if json.dumps(q['G'])==key)
    expected_matrices.append([matrix_text(q['G']),matrix_text(q['H'])])
check([row for i in range(1,4) for row in rows('decode-matrices-'+str(i))]==expected_matrices,'decode G H registry')
check(words([[1,0,0,0,1],[0,0,0,1,1],[0,1,1,1,0]])==sorted(['00000','01110','00011','01101','10001','11111','10010','11100']),'T42 nonsystematic code')
pdf=fitz.open(R/'TEST4DOCSV1.pdf')
check(len(pdf)==len(pages)==40,'40 logical and rendered pages')
for i,page in enumerate(pages):
 txt=pdf[i].get_text();flat=lambda s:' '.join(str(s).replace('**','').split())
 check(flat(page['title']) in flat(txt),page['key']+' searchable title')
 check('{page:' not in txt,page['key']+' resolved references')
 for block in pdf[i].get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for span in line['spans']:
    x0,y0,x1,y1=span['bbox'];check(x0>=38 and y0>=20 and x1<=pdf[i].rect.width-38 and y1<=pdf[i].rect.height-15,page['key']+' text within page')
 # Every table cell must survive text extraction, including leading-zero strings.
 for kind,val in page['blocks']:
  if kind=='table':
   for row in [val['headers']]+val['rows']:
    for cell in row:check(flat(cell) in flat(txt),page['key']+' table text '+str(cell)[:25])
check(len(pdf.get_toc())==40,'PDF bookmarks')
whole='\n'.join(p.get_text() for p in pdf)
for phrase in ['at most 3','valid key pair','private key','Hamming','error pattern','11010110','1001','00000010']:
 check(phrase in whole,'search keyword '+phrase)
print(json.dumps({'passed':checks,'pdf_pages':len(pdf),'source_attempts':32,'source_math_questions':96,'rsa_options':30}))
