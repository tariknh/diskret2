const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '../../test3-med-preview.html'), 'utf8');
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)];
assert.equal(scripts.length, 1);
const context = {module: {exports: {}}};
vm.runInNewContext(scripts[0][1], context);
const T = context.module.exports;
let count = 0;
function check(ok, label) { assert.ok(ok, label); count++; }
function near(a,b) { return Math.abs(a-b) <= 1e-8*Math.max(1,Math.abs(a),Math.abs(b)); }
const gcd = (a,b) => b ? gcd(b,a%b) : a;
function rat(n,d=1n) { if(d<0n){n=-n;d=-d;}const g=gcd(n<0n?-n:n,d);return [n/g,d/g]; }
function integerTerms(A,B,C,u,v) {
  let x=rat(BigInt(u)),y=rat(BigInt(v));
  for(let n=2;n<26;n++){
    const z=rat(-BigInt(B)*y[0]*x[1]-BigInt(C)*x[0]*y[1],BigInt(A)*y[1]*x[1]);
    if(z[1]!==1n)return false;
    [x,y]=[y,z];
  }
  return true;
}
const words=new Set(),coefficients=new Set(),groups=new Set(),presets=new Set();
let mixedSubspace=false;
for(let seed=0;seed<500;seed++){
  for(const q of T.generate(seed,'all')){
    const m=q.meta;
    check(q.grade(q.solution).score===1, `${seed} ${q.type}: answer key accepted`);
    check(q.pages===T.HELP.pages[q.type],`${q.type}: current helpsheet reference`);
    check(q.grade({}).score===0,`${q.type}: blank attempt gets no credit`);
    if(q.type==='initial'){
      const ast=T.parse(q.solution.x), f=n=>T.evaluate(ast,{n});
      check(near(f(0),m.a0)&&near(f(1),m.a1),'Initial values');
      for(let n=2;n<7;n++)check(near(f(n)+m.B*f(n-1)+m.C*f(n-2),0),'Initial recurrence');
    } else if(q.type==='particular'){
      if(m.preset)presets.add(m.preset);
      const ast=T.parse(q.solution.x), f=n=>T.evaluate(ast,{n});
      for(let n=1;n<6;n++)check(near(m.A*f(n)+m.B*f(n-1),m.c*m.t**n),'Particular recurrence');
      check(near(m.A*T.evaluate(T.parse(q.solution.a1))+m.B*m.a0,m.c*m.t),'Particular initial value');
    } else if(q.type==='words'){
      words.add(`${m.p},${m.q}`);
      let expected=0;
      for(let a=0;a<m.p+m.q;a++)for(let b=0;b<m.p+m.q;b++)for(let c=0;c<m.p+m.q;c++)if(a<m.p&&c<m.p)expected++;
      check(Number(q.solution.a3)===expected,'Independent word enumeration');
      check(Number(q.solution.a1)===m.p,'First word count');
      for(const r of m.roots)check(near(r*r-m.p*r-m.p*m.q,0),'Word characteristic root');
      check(!q.grade({...q.solution,general:'A*4^n+B*(-4)^n'}).results.find(x=>x.key==='general').ok,'Reject incorrect word roots');
    } else if(q.type==='recurrence_mc'){
      coefficients.add([m.A,m.B,m.C].join(','));
      const ints=integerTerms(m.A,m.B,m.C,m.u,m.v);
      for(const claim of q.claims){
        const s=claim.text;let truth;
        if(s==='None of the above')truth=!q.claims.slice(0,-1).some(x=>x.truth);
        else if(s.includes('not an integer'))truth=!ints;
        else if(s.includes('every later term is an integer'))truth=ints;
        else if(s.includes('zero sequence'))truth=false;
        else if(s.includes('cannot be a solution'))truth=false;
        else if(s.includes('could be a solution')){
          const w=Number(s.match(/a\[2\]=([^,]+)/)[1].split('/').reduce((a,b)=>a/Number(b)));
          truth=near(m.A*w+m.B*(-2)+m.C*2,0);
        }else if(s.includes('two solutions are equal'))truth=(s.match(/=b\[/g)||[]).length===2;
        else truth=true;
        check(claim.truth===truth,`${s}: independent recurrence claim`);
      }
    } else if(q.type==='group_mc'){
      const g=m.group;groups.add(g.name);let N,cyclic,abelian;
      if(g.name.startsWith('S')){
        const n=Number(g.name.match(/^S(\d+)/)[1]);N=1;for(let k=2;k<=n;k++)N*=k;cyclic=abelian=n<=2;
      }else if(g.name.includes('⟨x⟩')){N=Number(g.name.match(/order (\d+)/)[1]);cyclic=abelian=true;}
      else if(g.name.includes('Z/')){const ns=[...g.name.matchAll(/Z\/(\d+)/g)].map(x=>Number(x[1]));N=ns[0]*ns[1];cyclic=T.gcd(...ns)===1;abelian=true;}
      else {N=4;cyclic=abelian=true;}
      const proper=Array.from({length:N-2},(_,i)=>i+2).some(x=>N%x===0);
      check(g.order===N&&g.cyclic===cyclic&&g.abelian===abelian&&g.proper===proper,'Group properties');
      for(const claim of q.claims){
        const s=claim.text;let truth;
        if(s==='None of the above')truth=!q.claims.slice(0,-1).some(x=>x.truth);
        else if(s.includes('infinite'))truth=false;
        else if(s.includes('finite'))truth=true;
        else if(s.includes('not abelian')||s.includes('gh≠hg'))truth=!abelian;
        else if(s.includes('abelian')||s.includes('ab=ba'))truth=abelian;
        else if(s.includes('not cyclic'))truth=!cyclic;
        else if(s.includes('cyclic'))truth=cyclic;
        else if(s.includes('non-trivial and proper'))truth=proper;
        else if(s.includes('only subgroups'))truth=!proper;
        else if(s.includes('For each')&&s.includes('proper'))truth=!cyclic;
        else if(s.includes('For each'))truth=N===1;
        else if(s.includes('There exists')&&s.includes('proper'))truth=N>1;
        else if(s.includes('There exists'))truth=cyclic;
        else if(s.includes('divisible'))truth=N%3===0;
        else truth=N===Number(s.match(/is (\d+)\./)[1]);
        check(claim.truth===truth,s+': independent group claim');
      }
    } else if(q.type==='index'){
      const H=new Set(m.H.map(v=>v.join('')));
      check(H.size===2**m.dimension,'Binary subspace dimension');
      for(const a of m.H)for(const b of m.H)check(H.has(a.map((v,i)=>v^b[i]).join('')),'Binary subgroup closure');
      if(m.H.filter(v=>v.reduce((a,b)=>a+b,0)===1).length<m.dimension)mixedSubspace=true;
      check(Number(q.solution.g)*H.size===2**m.k,'Product-group index');
      check(Number(q.solution.d)===8/(m.symmetry.order/T.gcd(m.symmetry.order,m.exponent)),'D4 index of a power');
    } else if(q.type==='mod_products'){
      m.products.forEach(([a,b],i)=>check(Number(q.solution[`p${i}`])===a*b%m.m,'Modular product'));
      check(m.a*Number(q.solution.inv)%m.m===1,'Modular inverse');
    }
  }
}
check(words.size===8,'All eight word variants can be generated');
check(groups.size===8,'All eight group variants can be generated');
check(coefficients.size===12,'All twelve coefficient triples can be generated');
check(presets.size===3,'All fractional/signed particular presets can be generated');
check(mixedSubspace,'Mixed binary-coordinate subgroups are reachable');
const latest=T.generate(42,'latest');
check(latest.length===7,'Seven targeted new variants');
check(latest[1].claims.filter(x=>x.truth).map(x=>x.text).join('')==='The group G is cyclic.','N05 S2 exact choices');
for(const q of latest)check(q.grade(q.solution).score===1,'Latest variant answer key');
for(const q of latest.filter(q=>q.type==='words')){
  const d=q.meta.q===4?5:7;
  check(q.grade({...q.solution,general:`U*(2+2*sqrt(${d}))^n+V*(2-2*sqrt(${d}))^n`}).score===1,'Accept simplified radical roots from PDF');
}
const n10=latest[6];
check(!n10.grade({...n10.solution,x:'1/(30*3^n)+(4/-2)^n'}).results[0].ok,'Reject N10 submitted wrong solution');
check(!n10.grade({...n10.solution,x:'1/(10*3^n)+(-2)^n'}).results[0].ok,'Reject N10 sign trap');
check(!n10.grade({...n10.solution,x:'1/(10*3^n)'}).results[0].ok,'Reject unchanged particular solution');
check(n10.grade({...n10.solution,x:'1/(10*3^n)-3*2^n'}).score===1,'Accept another nonzero homogeneous multiple');
check(T.preview('U*(2+2*sqrt(5))^n+V*(2-2*sqrt(5))^n').mathML.includes('<msqrt>'),'Native radical preview');
check(T.preview('<img src=x onerror=alert(1)>').error,'Reject markup in math input');
check(T.evaluate(T.parse('-2^2'))===-4&&T.evaluate(T.parse('(-2)^2'))===4,'Power precedence');
const parentheses=T.genInitial(T.random(1),{repeated:true,x:2,u:-2,v:4});
for(const x of ['(-2+4*n)*2^n','(-2+4*n)*(2)^n','-2*2^n+4*n*2^n'])check(parentheses.grade({x}).score===1,'Accept correct parentheses example: '+x);
for(const x of ['-2+4*n*2^n','(-2+4*n)*(-2)^n','(-2+4*n)^n'])check(parentheses.grade({x}).score===0,'Reject changed grouping/base: '+x);
console.log(JSON.stringify({passed:count,seeds:500,generatedQuestions:5500,latest:7,wordVariants:words.size,groupVariants:groups.size}));
