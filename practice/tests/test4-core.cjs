const fs=require('node:fs'),path=require('node:path'),vm=require('node:vm'),assert=require('node:assert/strict');
const root=path.join(__dirname,'../..'),html=fs.readFileSync(path.join(root,'test4-med-preview.html'),'utf8'),sandbox={module:{exports:{}}};
vm.runInNewContext(html.split('<script>')[1].split('</script>')[0],sandbox);const T=sandbox.module.exports;
let checks=0;function check(v,label){assert.ok(v,label);checks++;}
const plain=x=>JSON.parse(JSON.stringify(x));
const cases=JSON.parse(fs.readFileSync(path.join(root,'helpsheets/test4/source/cases.json')));
const hamming=(a,b)=>Array.from(a).filter((v,i)=>v!==b[i]).length;
function expectedWords(G){let out=[];for(let v=0;v<2**G.length;v++){const w=v.toString(2).padStart(G.length,'0');let row='';for(let j=0;j<G[0].length;j++){let bit=0;for(let i=0;i<G.length;i++)bit^=Number(w[i])*G[i][j];row+=bit;}out.push(row);}return out;}
for(const s of T.sources){const q=T.generate(7,'source:'+s.id),data=cases.find(c=>c.id===s.id);check(q.length===3,'three source questions');q.forEach((x,i)=>{const d=data.tasks[i];check(x.type===d.type,'source type');check(x.grade(x.solution).score===1,'source full score');if(d.type==='rsa_valid')check(x.claims.slice(0,-1).every((c,i)=>c.truth===d.options[i].valid),'source RSA');if(d.type==='rsa_break')check(Number(x.solution.y)===d.y&&Number(x.solution.m)===d.plain,'source RSA answers');if(d.type==='hamming')check(Number(x.solution.min)===d.minimum&&Number(x.solution.max)===d.maximum,'source distance answers');if(d.type==='channel')check('abc'.split('').every((k,i)=>Number(x.solution[k])===d.answers[i]),'source probabilities');if(d.type==='syndrome_decode')check(x.solution.s===d.syndrome&&x.solution.e===d.error&&x.solution.c===d.decoded,'source decoding answers');});}
check(T.sources.length===32,'32 distinct source files');
for(let seed=0;seed<250;seed++){
 const all=T.generate(seed,'all');check(all.length===8,'all types');check(T.generate(seed,'test').length===3,'full test');
 for(const q of all){
  check(q.grade(q.solution).score===1,q.type+' full score '+seed);
  check(q.grade({}).score===0,q.type+' blank');
  check(q.grade(Object.fromEntries(Object.keys(q.solution).map(k=>[k,'<script>bad</script>']))).score===0||q.type==='rsa_valid',q.type+' malformed');
  if(q.meta.G){const cw=expectedWords(q.meta.G);check(new Set(cw).size===2**q.meta.G.length,'independent codebook');check(cw.every(w=>T.syndrome(w,T.parity(q.meta.G))==='0'.repeat(q.meta.G[0].length-q.meta.G.length)),'H annihilates all codewords');
   if(q.type==='code_dmin'||q.type==='code_detect'){
    const dm=Math.min(...cw.flatMap((a,i)=>cw.slice(i+1).map(b=>hamming(a,b))));check(Number(q.solution.a)===(q.type==='code_detect'?dm-1:dm),'distance via all pairs');
    for(const word of cw)check(q.grade({...q.solution,b:word}).results[1].ok===word.includes('1'),'accept all and only nonzero codewords');
    for(let v=0;v<32;v++){const word=v.toString(2).padStart(5,'0');check(q.grade({...q.solution,c:word}).results[2].ok===!cw.includes(word),'noncodeword membership');}
   }
   if(q.type==='coding_matrices'){
    const H=q.meta.H;
    const transforms=[[[1,0],[0,1]],[[0,1],[1,0]],[[1,1],[0,1]],[[1,0],[1,1]],[[0,1],[1,1]],[[1,1],[1,0]]];
    for(const tr of transforms){const alt=tr.map(row=>H[0].map((_,j)=>(row[0]*H[0][j]+row[1]*H[1][j])%2)),s=T.syndrome(q.meta.r,alt);check(q.grade({...q.solution,H:T.matrixText(alt),s}).score===1,'valid alternate H and syndrome');}
    check(q.grade({...q.solution,H:'0 0 0 0 0\n0 0 0 0 0'}).results[1].ok===false,'reject rank zero H');
   }
   if(q.type==='syndrome_decode'){
    const ds=cw.map(c=>hamming(c,q.meta.r)),best=Math.min(...ds);check(best===1&&ds.filter(d=>d===best).length===1,'one unique nearest');check(q.solution.c===cw[ds.indexOf(best)],'nearest codeword');check(T.xor(q.solution.c,q.solution.e)===q.meta.r,'error vector relation');
   }
  }
  if(q.type==='channel'){
   const {p,w,r,upto}=q.meta;let p0=0,pk=0,pr=0,total=0;
   for(let i=0;i<128;i++){const v=i.toString(2).padStart(7,'0'),d=hamming(v,w),prob=p**d*(1-p)**(7-d);total+=prob;if(v===w)p0=prob;if(d<=upto)pk+=prob;if(v===r)pr=prob;}
   check(Math.abs(total-1)<1e-10,'channel sums to 1');[p0,pk,pr].forEach((v,i)=>check(Number(q.solution['abc'[i]])===Number(v.toFixed(3)),'independent BSC enumeration'));
   check(q.grade({...q.solution,a:q.solution.a.replace('.',',')}).results[0].ok,'decimal comma');
  }
  if(q.type==='rsa_break')check(Number(T.powMod(BigInt(q.solution.m),BigInt(q.meta.x),BigInt(q.meta.n)))===q.meta.cipher,'RSA encrypt back');
  if(q.type==='rsa_valid'){
   const none=q.claims.at(-1);check(none.truth===!q.claims.slice(0,-1).some(c=>c.truth),'None truth');const allSelected=Object.fromEntries(q.claims.map((c,i)=>['o'+i,true]));check(q.grade(allSelected).score<1,'selecting every option penalized');
  }
 }
}
check(T.calculator('mul','20271383','22663367','27523440')==='1','exact RSA product');
check(T.calculator('pow','1209','263','1349')==='1148','exact RSA power');
check(T.calculator('pow','7','0','33')==='1','zero exponent');
check(T.calculator('mul','-3','2','5')==='4','negative modulo normalized');
for(const args of [['pow','2','-1','5'],['mul','1','2','0'],['mul','1.2','2','5'],['pow','a','3','5']])assert.throws(()=>T.calculator(...args));
check(T.preview('0010','bits:4').mathML.includes('0010'),'leading-zero preview');
check(T.preview('10','bits:4').error,'reject dropped leading zeros');
check(T.preview('1 0\n0 1','matrix:2:2').mathML.includes('<mtable'),'matrix preview');
check(T.preview('1/(2+3)','numeric').mathML.includes('<mfrac>'),'fraction preview');
check(T.preview('<img src=x>','numeric').error,'HTML rejected');
check(T.preview('0,125','numeric').mathML.includes('0.125'),'comma preview');
const pages=JSON.parse(fs.readFileSync(path.join(root,'helpsheets/test4/build-manifest.json'))).page_numbers;
check(T.HELP.pages.channel===pages.channel+'–'+pages['channel-known'],'help references current PDF pages');
check(!/<script[^>]+src|https?:\/\/[^'"\s]*\.js/i.test(html),'no external scripts');
console.log(JSON.stringify({passed:checks,seeds:250,question_types:T.types.length,source_attempts:T.sources.length}));
