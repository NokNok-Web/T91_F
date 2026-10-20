import sys,os,json
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import shared as S
os.chdir(sys.argv[1])
src=open('T91_presentazione_nuovo_sito.html').read()
head=src[:src.index('</head>')].replace('<title>Il nuovo T91</title>','<title>T91 · Racchette</title>')
svg=src[src.index('<svg width="0"'):src.index('</svg>',src.index('<svg width="0"'))+6]
C=S.CDN
# livello e stile: ESEMPIO, da sostituire con i dati di T91
P=[
 dict(n='Boss One K12 Pro Master 6.0',i='BossOneK12Master6.01.webp?v=1791205585',p=328.90,lv='Avanzati',st='Potenza',co='Holo',b='Novità',link='pdp',k='12K',w='356–365 g'),
 dict(n='Boss One K3 Pro Master',i='BossOneK3Master6.01.webp?v=1791205374',p=328.90,lv='Intermedi',st='Potenza',co='Holo',b='Novità',k='3K',w='356–365 g'),
 dict(n='Finder Pro Master K3',i='FinderProMasterK31.webp?v=1791205236',p=328.90,lv='Intermedi',st='Controllo',co='Holo',b='Novità',k='3K',w='348–355 g'),
 dict(n='Huracán Full Black x Iriart 3.0',i='HURACANFULLBLACKXEMILIANOIRIART.webp?v=1791215495',p=328.90,lv='Pro',st='Polivalenti',co='Signature Pro',b='Signature',k='Carbonio',w='—'),
 dict(n='Huracán 2.0 12K x Bubu Salandro',i='LimitedEdition12KBubu.webp?v=1785322689',p=328.90,lv='Pro',st='Potenza',co='Signature Pro',b='Signature',k='12K',w='346–360 g'),
 dict(n='Huracán 2.0 3K x Bubu Salandro',i='LimitedEdition12KBubu2.webp?v=1785322689',p=328.90,lv='Avanzati',st='Polivalenti',co='Signature Pro',b='Signature',k='3K',w='346–360 g'),
 dict(n='Huracán 2.0',i='Huracan_2.0_Nera_d0923663-c471-4cd0-b0a6-536e9564d7a8.webp?v=1766168628',p=328.90,lv='Principianti',st='Controllo',co='',b='Bestseller',k='Carbonio',w='—'),
 dict(n='Boss One 18K 3.0 PWR',i='BossOnePWR1.webp?v=1763487605',p=328.90,lv='Avanzati',st='Potenza',co='',b='',k='18K',w='—'),
 dict(n='Finder Pro K12 3.0 PWR',i='Finder_Pro_Remedi_3.0_PWR_1.webp?v=1780990777',p=328.90,lv='Intermedi',st='Polivalenti',co='Signature Pro',b='',k='12K',w='—'),
]
for x in P:
    x['img']=C+x['i']+'&width=600'; x['href']=S.LINKS['pdp'] if x.get('link')=='pdp' else '#'
DATA=json.dumps(P,ensure_ascii=False)
body=f'''<div class="p rk">
{S.TOPBAR}  <div class="p-bar"><div class="p-marq"><span>⚡ SPEDIZIONE GRATUITA 24/48H</span><span>· RESO GRATUITO 30 GIORNI</span><span>· PAGA IN 3 RATE CON KLARNA</span><span>· T91 CLUB: -30% SEMPRE</span><span>⚡ SPEDIZIONE GRATUITA 24/48H</span><span>· RESO GRATUITO 30 GIORNI</span><span>· PAGA IN 3 RATE CON KLARNA</span><span>· T91 CLUB: -30% SEMPRE</span></div></div>
{S.HEAD('Racchette')}
  <div class="p-crumbs"><a href="#" data-link="home">Home</a><i>/</i><b id="rkCrumb">Racchette</b></div>
  <section class="r-hero">
    <div class="tx"><h1 id="rkTitle">Racchette da padel.</h1><p id="rkDesc">Tutte le racchette T91, dal primo match al torneo. Filtra per livello e stile di gioco, o fatti consigliare dal test.</p><span class="url" id="rkUrl">t91padel.com/racchette</span></div>
    <div class="sc" id="rkShort"></div>
  </section>
  <section class="r-body">
    <aside class="r-side" id="rkSide"></aside>
    <div class="r-main">
      <div class="r-bar"><button class="r-fbtn js-fopen"><svg class="i"><use href="#i-burger"/></svg>Filtri e ordina<em id="rkFc"></em></button><span class="r-count" id="rkCount"></span><label class="r-sort">Ordina <select id="rkSort"><option value="ev">In evidenza</option><option value="new">Novità</option><option value="pa">Prezzo crescente</option><option value="pd">Prezzo decrescente</option></select></label></div>
      <div class="r-active" id="rkActive"></div>
      <div class="r-grid" id="rkGrid"></div>
      <p class="r-note">Livello e stile di gioco di ogni racchetta sono di esempio: quelli veri li indicherà T91.</p>
    </div>
  </section>
  <section class="r-guide">
    <a class="g1" href="#"><img src="{C}Boss_One_K12_Master_6.0_6.webp?v=1791207039&width=900" alt=""><span><small>Guida · 6 minuti</small><b>Come scegliere la racchetta per il tuo livello</b><u>Leggi la guida →</u></span></a>
    <a class="g2" href="#"><span><small>Ancora indeciso?</small><b>Confronta fino a 4 racchette, fianco a fianco.</b><u>Apri il confronto →</u></span></a>
  </section>
  <section class="r-seo">
    <div class="t"><h2 id="rkSeoT">Come scegliere una racchetta da padel</h2><p>Per chi inizia conta la maneggevolezza: peso contenuto, bilanciamento basso e una gomma morbida che perdona. Con l'esperienza si cerca più potenza, con carbonio più rigido e bilanciamento alto. Le racchette T91 sono progettate in Italia e provate dal nostro Team prima di arrivare a te.</p></div>
    <div class="faq">
      <details><summary>Che differenza c'è tra carbonio 3K, 12K e 18K?</summary><p>Più è alto il numero, più il telaio è rigido: la palla esce più veloce ma serve più tecnica. Il 3K è più morbido e confortevole.</p></details>
      <details><summary>Che peso devo scegliere?</summary><p>Tra 345 e 360 g va bene per la maggior parte dei giocatori. Su molte racchette puoi scegliere il grammo esatto a +€10.</p></details>
      <details><summary>Posso provarla prima di comprarla?</summary><p>Sì, nei centri partner T91 e a Osio Sotto. E hai comunque 30 giorni per il reso gratuito.</p></details>
      <details><summary>Posso pagare a rate?</summary><p>Sì, con Klarna in 3 rate senza interessi.</p></details>
    </div>
  </section>
{S.FOOTER}  <div class="r-cmp" id="rkCmp"><div class="th" id="rkCmpTh"></div><span id="rkCmpTx"></span><a class="go" href="#">Confronta</a><button class="x js-cclear" aria-label="Svuota">×</button></div>
</div>
'''
sheet='''<div class="r-ov js-fclose"></div><div class="r-sheet"><div class="hd"><b>Filtri e ordina</b><button class="js-fclose" aria-label="Chiudi"><svg class="i"><use href="#i-x"/></svg></button></div><div class="bd" id="rkSheet"></div><div class="ft"><button class="clr js-clear">Rimuovi filtri</button><button class="ok js-fclose" id="rkSheetOk">Mostra risultati</button></div></div>'''
css='''<style>
.r-hero{padding:8px 20px 20px}
.r-hero h1{font-weight:400;font-size:40px;line-height:.98;letter-spacing:-.045em}
.r-hero p{font-size:15.5px;color:#3A3A3C;margin-top:10px;max-width:620px}
.r-hero .url{display:inline-block;margin-top:12px;font-family:ui-monospace,Menlo,monospace;font-size:12px;color:var(--mute);background:var(--fog);border-radius:8px;padding:4px 8px}
.r-hero .url b{font-weight:400;color:#000;background:var(--volt);border-radius:4px;padding:0 3px}
.r-hero .sc{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;margin:18px -20px 0;padding:0 20px}
.r-hero .sc::-webkit-scrollbar{display:none}
.r-hero .sc button{flex:none;font:inherit;font-size:14px;border:1px solid var(--line);border-radius:980px;padding:9px 16px;background:#fff;cursor:pointer}
.r-hero .sc button.on{background:#000;color:#fff;border-color:#000}
.r-hero .sc .sep{flex:none;width:1px;background:var(--line);margin:4px 2px}
.r-body{padding:0 20px 40px}
.r-side{display:none}
.r-bar{display:flex;align-items:center;gap:10px;justify-content:space-between;padding:12px 0;border-top:1px solid var(--line);border-bottom:1px solid var(--line);position:sticky;top:54px;background:rgba(255,255,255,.95);backdrop-filter:blur(10px);z-index:5}
.r-fbtn{display:inline-flex;align-items:center;gap:8px;font:inherit;font-size:14px;border:1px solid #000;border-radius:980px;padding:8px 14px;background:#fff;cursor:pointer}
.r-fbtn svg{width:16px;height:16px}
.r-fbtn em{font-style:normal;background:var(--volt);border-radius:980px;padding:0 7px;font-size:12px}
.r-fbtn em:empty{display:none}
.r-count{font-size:13px;color:var(--mute)}
.r-sort{display:none;font-size:13px;color:var(--mute);align-items:center;gap:8px}
.r-sort select{font:inherit;font-size:14px;border:1px solid var(--line);border-radius:980px;padding:7px 12px;background:#fff;color:#000}
.r-active{display:flex;flex-wrap:wrap;gap:6px;margin:12px 0 0}
.r-active button{font:inherit;font-size:13px;background:var(--fog);border:0;border-radius:980px;padding:6px 12px;cursor:pointer}
.r-active button::after{content:" ×";color:var(--mute)}
.r-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px 10px;margin-top:16px}
.r-card{display:flex;flex-direction:column;gap:5px;position:relative;animation:rin .3s ease both}
@keyframes rin{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.r-card .im{aspect-ratio:4/5;background:var(--fog);border-radius:20px;position:relative;overflow:hidden;display:grid;place-items:center}
.r-card .im img{width:84%;height:84%;object-fit:contain;transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.r-card:hover .im img{transform:scale(1.06) rotate(-3deg)}
.r-card .bdg{position:absolute;top:10px;left:10px;font-size:11px;background:var(--volt);padding:3px 9px;border-radius:980px}
.r-card .bdg.k{background:#000;color:#fff}
.r-card .bdg.o{background:#FF3B30;color:#fff}
.r-card .cmp{position:absolute;right:10px;top:10px;display:flex;align-items:center;gap:6px;font-size:11.5px;background:rgba(255,255,255,.92);border-radius:980px;padding:4px 9px 4px 5px;cursor:pointer;border:0;font-family:inherit}
.r-card .cmp i{width:16px;height:16px;border-radius:5px;border:1.5px solid #000;display:grid;place-items:center;font-style:normal;font-size:11px}
.r-card .cmp.on{background:#000;color:#fff}
.r-card .cmp.on i{background:var(--volt);border-color:var(--volt);color:#000}
.r-card .cmp.on i::after{content:"✓"}
.r-card .tg{display:flex;gap:4px;flex-wrap:wrap}
.r-card .tg span{font-size:11px;color:var(--mute);background:var(--fog);border-radius:980px;padding:2px 8px}
.r-card b{font-size:15px;line-height:1.2;letter-spacing:-.01em}
.r-card .pr{font-size:15px}
.r-card .pr s{color:var(--mute);font-size:12.5px;margin-left:4px}
.r-card .pr small{display:block;font-size:12px;color:var(--mute)}
.r-quiz{grid-column:1/-1;background:var(--volt);border-radius:24px;padding:26px 22px;display:flex;flex-direction:column;gap:12px}
.r-quiz small{font-size:13px;color:#333}
.r-quiz b{font-size:30px;letter-spacing:-.04em;line-height:1}
.r-quiz p{font-size:15px;color:#222}
.r-quiz .h{align-self:flex-start;background:#000;color:#fff;border-radius:980px;padding:12px 20px;font-size:15px}
.r-empty{grid-column:1/-1;background:var(--fog);border-radius:20px;padding:28px;text-align:center;color:var(--mute)}
.r-empty button{font:inherit;margin-top:10px;border:1px solid #000;background:#fff;border-radius:980px;padding:8px 14px;cursor:pointer}
.r-note{font-size:12.5px;color:var(--mute);margin-top:22px;text-align:center}
.r-guide{display:grid;gap:10px;padding:0 20px 40px}
.r-guide a{position:relative;border-radius:24px;overflow:hidden;min-height:240px;display:flex;align-items:flex-end}
.r-guide .g1{background:#111;color:#fff}
.r-guide .g1 img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.75}
.r-guide .g1::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.8))}
.r-guide .g2{background:#000;color:#fff}
.r-guide span{position:relative;z-index:1;padding:24px;display:flex;flex-direction:column;gap:6px}
.r-guide small{font-size:13px;color:#C7C7CC}
.r-guide b{font-size:28px;letter-spacing:-.035em;line-height:1.05;max-width:440px}
.r-guide u{text-decoration:none;color:var(--volt);font-size:14.5px;margin-top:6px}
.r-seo{display:grid;gap:24px;padding:40px 20px 56px;border-top:1px solid var(--line)}
.r-seo h2{font-weight:400;font-size:28px;letter-spacing:-.03em;line-height:1.1}
.r-seo p{font-size:15.5px;color:#3A3A3C;margin-top:10px}
.r-seo details{border-bottom:1px solid var(--line)}
.r-seo summary{list-style:none;cursor:pointer;padding:16px 0;font-size:16px;display:flex;justify-content:space-between;gap:12px}
.r-seo summary::after{content:"+";color:var(--mute);font-size:20px;line-height:1}
.r-seo details[open] summary::after{content:"–"}
.r-seo summary::-webkit-details-marker{display:none}
.r-seo details p{margin:0 0 16px;font-size:14.5px;color:var(--mute)}
.r-cmp{position:sticky;bottom:12px;margin:0 12px;z-index:20;background:#000;color:#fff;border-radius:980px;padding:8px 8px 8px 10px;display:flex;align-items:center;gap:10px;transform:translateY(140%);transition:transform .3s cubic-bezier(.2,.8,.2,1);margin-top:-64px;width:max-content;max-width:calc(100% - 24px);margin-left:auto;margin-right:auto}
.r-cmp.show{transform:none}
.r-cmp .th{display:flex}
.r-cmp .th img{width:36px;height:36px;border-radius:50%;background:#fff;object-fit:contain;padding:3px;margin-left:-8px;border:2px solid #000}
.r-cmp .th img:first-child{margin-left:0}
.r-cmp span{font-size:13.5px;white-space:nowrap}
.r-cmp .go{background:var(--volt);color:#000;border-radius:980px;padding:9px 16px;font-size:14px}
.r-cmp .x{width:30px;height:30px;border-radius:50%;background:#1D1D1F;color:#fff;border:0;font-size:16px;cursor:pointer}
/* pannello filtri */
.r-ov{position:absolute;inset:0;background:rgba(0,0,0,.4);opacity:0;pointer-events:none;transition:opacity .25s;z-index:45}
.r-ov.open{opacity:1;pointer-events:auto}
.r-sheet{position:absolute;left:0;right:0;bottom:0;max-height:86%;background:#fff;border-radius:24px 24px 0 0;z-index:46;transform:translateY(102%);transition:transform .32s cubic-bezier(.2,.8,.2,1);display:flex;flex-direction:column;font-family:'Questrial',sans-serif;color:var(--ink)}
.r-sheet.open{transform:none}
.r-sheet .hd{display:flex;justify-content:space-between;align-items:center;padding:18px 20px;border-bottom:1px solid var(--line)}
.r-sheet .hd b{font-size:20px;letter-spacing:-.02em}
.r-sheet .hd button{width:36px;height:36px;border-radius:50%;background:var(--fog);border:0;display:grid;place-items:center;cursor:pointer}
.r-sheet .hd svg{width:16px;height:16px}
.r-sheet .bd{overflow-y:auto;padding:8px 20px 20px}
.r-sheet .ft{display:flex;gap:10px;padding:14px 20px 20px;border-top:1px solid var(--line)}
.r-sheet .ft button{flex:1;font:inherit;font-size:15px;border-radius:980px;padding:13px;cursor:pointer}
.r-sheet .clr{background:#fff;border:1px solid var(--line)}
.r-sheet .ok{background:#000;color:#fff;border:0}
.fgrp{padding:14px 0;border-bottom:1px solid var(--line)}
.fgrp h6{font-weight:400;font-size:13px;color:var(--mute);margin:0 0 10px}
.fgrp .opts{display:flex;flex-wrap:wrap;gap:6px}
.fgrp button{font:inherit;font-size:14px;border:1px solid var(--line);border-radius:980px;padding:8px 14px;background:#fff;cursor:pointer;display:inline-flex;gap:6px;align-items:center}
.fgrp button small{color:var(--mute);font-size:12px}
.fgrp button.on{background:#000;color:#fff;border-color:#000}
.fgrp button.on small{color:#A1A1A6}
.fgrp button:disabled{opacity:.35;cursor:default}
@container dev (min-width: 900px){
  .r-hero{padding:8px 40px 28px;display:grid;grid-template-columns:1fr auto;align-items:end;gap:24px}
  .r-hero h1{font-size:72px}
  .r-hero p{font-size:18px}
  .r-hero .sc{grid-column:1/-1;margin:8px 0 0;padding:0;flex-wrap:wrap}
  .r-body{display:grid;grid-template-columns:240px 1fr;gap:40px;padding:0 40px 64px}
  .r-side{display:block;position:sticky;top:96px;align-self:start}
  .r-fbtn{display:none}
  .r-sort{display:inline-flex}
  .r-bar{top:70px;border-top:0}
  .r-grid{grid-template-columns:repeat(3,1fr);gap:28px 16px;margin-top:20px}
  .r-card b{font-size:16.5px}
  .r-quiz{flex-direction:row;align-items:center;justify-content:space-between;padding:36px 40px;border-radius:28px}
  .r-quiz b{font-size:44px}
  .r-guide{grid-template-columns:1.5fr 1fr;gap:16px;padding:0 40px 64px}
  .r-guide a{min-height:360px;border-radius:32px}
  .r-guide span{padding:36px}
  .r-guide b{font-size:42px}
  .r-seo{grid-template-columns:1fr 1fr;gap:64px;padding:72px 40px 88px}
  .r-seo h2{font-size:40px}
  .r-sheet{display:none}
}
html,body{height:100%;overflow:hidden}
.screen{position:fixed!important;inset:0;width:100%;height:100%}
</style>
'''
js='''<script>
(function(){
'''+S.JS_MENU+'''
const P='''+DATA+''';
const screen=document.querySelector('.screen');
screen.appendChild(document.getElementById('tpl-menu').content.cloneNode(true));
t91Menu(screen);t91Mega(screen);t91Toast(screen);
const G=[['lv','Livello',['Principianti','Intermedi','Avanzati','Pro']],['st','Stile di gioco',['Potenza','Controllo','Polivalenti']],['co','Collezione',['Holo','Signature Pro']],['pz','Prezzo',['Sotto €200','€200 – €330']]];
const SLUG={Principianti:'principianti',Intermedi:'intermedi',Avanzati:'avanzati',Pro:'pro',Potenza:'potenza',Controllo:'controllo',Polivalenti:'polivalenti',Holo:'holo','Signature Pro':'signature',Outlet:'outlet','Sotto €200':'sotto-200','€200 – €330':'200-330'};
const UNSLUG=Object.fromEntries(Object.entries(SLUG).map(([k,v])=>[v,k]));
const KEY={Principianti:'lv',Intermedi:'lv',Avanzati:'lv',Pro:'lv',Potenza:'st',Controllo:'st',Polivalenti:'st',Holo:'co','Signature Pro':'co',Outlet:'co','Sotto €200':'pz','€200 – €330':'pz'};
let sel={},cmp=[];
const $=id=>document.getElementById(id);
const eur=n=>'€'+n.toFixed(2).replace('.',',');
const match=(x,s)=>Object.entries(s).every(([k,v])=>k==='pz'?(v==='Sotto €200'?x.p<200:x.p>=200):x[k]===v);
function list(){let r=P.filter(x=>match(x,sel));const o=$('rkSort').value;if(o==='pa')r=[...r].sort((a,b)=>a.p-b.p);if(o==='pd')r=[...r].sort((a,b)=>b.p-a.p);if(o==='new')r=[...r].sort((a,b)=>(b.b==='Novità')-(a.b==='Novità'));return r;}
function count(k,v){const s={...sel,[k]:v};return P.filter(x=>match(x,s)).length;}
function groups(){return G.map(([k,l,opts])=>`<div class="fgrp"><h6>${l}</h6><div class="opts">${opts.map(o=>{const n=count(k,o);return `<button data-k="${k}" data-v="${o}" class="${sel[k]===o?'on':''}" ${n||sel[k]===o?'':'disabled'}>${o}<small>${n}</small></button>`}).join('')}</div></div>`).join('');}
function title(){const lv=sel.lv,st=sel.st,co=sel.co;
  if(co==='Holo')return['Holo Collection.','La nuova linea Master 6.0: carbonio, potenza e i colori Holo.'];
  if(co==='Signature Pro')return['Signature Pro.','Le racchette progettate insieme ai nostri atleti.'];
  const L={Principianti:'per principianti',Intermedi:'per intermedi',Avanzati:'per giocatori avanzati',Pro:'per professionisti'}[lv]||'';
  const T={Potenza:'da potenza',Controllo:'da controllo',Polivalenti:'polivalenti'}[st]||'';
  if(!L&&!T)return['Racchette da padel.','Tutte le racchette T91, dal primo match al torneo. Filtra per livello e stile di gioco, o fatti consigliare dal test.'];
  const D={Principianti:'Leggere, maneggevoli e facili da gestire: per imparare e divertirsi dal primo giorno.',Intermedi:'Per chi gioca con continuità e vuole crescere: più controllo e più precisione.',Avanzati:'Potenza e risposta secca per chi chiude il punto.',Pro:'Le racchette che gioca il nostro Team in torneo.'}[lv]||{Potenza:'Carbonio rigido e bilanciamento alto per smash e víbora.',Controllo:'Bilanciamento basso e gomma morbida per piazzare la palla dove vuoi.',Polivalenti:'Un equilibrio tra potenza e controllo, per ogni fase del gioco.'}[st];
  return['Racchette '+[T,L].filter(Boolean).join(' ')+'.',D];}
function render(){
  const r=list();const [t,d]=title();$('rkTitle').textContent=t;$('rkDesc').textContent=d;
  const segs=['lv','st','co'].filter(k=>sel[k]).map(k=>'<b>'+SLUG[sel[k]]+'</b>');
  $('rkUrl').innerHTML='t91padel.com/racchette'+(segs.length?'/'+segs.join('/'):'')+(sel.pz?'?prezzo=<b>'+SLUG[sel.pz]+'</b>':'');
  $('rkCrumb').textContent=segs.length||sel.pz?t.replace('.',''):'Racchette';
  $('rkShort').innerHTML=['Principianti','Intermedi','Avanzati','Pro'].map(v=>`<button data-k="lv" data-v="${v}" class="${sel.lv===v?'on':''}">${v}</button>`).join('')+'<span class="sep"></span>'+['Potenza','Controllo','Polivalenti'].map(v=>`<button data-k="st" data-v="${v}" class="${sel.st===v?'on':''}">${v}</button>`).join('');
  const g=groups();$('rkSide').innerHTML=g+(Object.keys(sel).length?'<button class="r-fbtn js-clear" style="display:inline-flex;margin-top:14px">Rimuovi filtri</button>':'');$('rkSheet').innerHTML=g;
  const n=Object.keys(sel).length;$('rkFc').textContent=n||'';
  $('rkCount').textContent=r.length+(r.length===1?' racchetta':' racchette');$('rkSheetOk').textContent='Mostra '+r.length+(r.length===1?' risultato':' risultati');
  $('rkActive').innerHTML=Object.entries(sel).map(([k,v])=>`<button data-rm="${k}">${v}</button>`).join('');
  const cards=r.map((x,i)=>`<a class="r-card" href="${x.href}" style="animation-delay:${Math.min(i,8)*30}ms"><div class="im">${x.b?`<span class="bdg ${x.b==='Signature'?'k':x.b.startsWith('-')?'o':''}">${x.b}</span>`:''}<button class="cmp ${cmp.includes(x.n)?'on':''}" data-c="${x.n}"><i></i>Confronta</button><img src="${x.img}" alt="" loading="lazy"></div><div class="tg"><span>${x.lv}</span><span>${x.st}</span></div><b>${x.n}</b><span class="pr">${eur(x.p)}${x.o?`<s>${eur(x.o)}</s>`:''}<small>o 3 rate da ${eur(x.p/3)} con Klarna</small></span></a>`);
  const q='<div class="r-quiz"><div><small>Non sai quale scegliere?</small><b>Trova la tua racchetta.</b><p>4 domande, il risultato anche su WhatsApp.</p></div><a class="h" href="#">Inizia il test →</a></div>';
  if(!cards.length){$('rkGrid').innerHTML='<div class="r-empty">Nessuna racchetta con questi filtri.<br><button class="js-clear">Rimuovi filtri</button></div>'+q;}
  else{cards.splice(Math.min(6,cards.length),0,q);$('rkGrid').innerHTML=cards.join('');}
  const h=['lv','st','co'].filter(k=>sel[k]).map(k=>SLUG[sel[k]]).join('/');try{if(location.hash.slice(1)!==h)history.replaceState(null,'',h?'#'+h:location.pathname+location.search);}catch(e){}
  renderCmp();
}
function renderCmp(){const bar=$('rkCmp');bar.classList.toggle('show',cmp.length>0);$('rkCmpTh').innerHTML=cmp.map(n=>`<img src="${P.find(x=>x.n===n).img}" alt="">`).join('');$('rkCmpTx').textContent=cmp.length+(cmp.length===1?' racchetta':' racchette')+' · max 4';}
screen.addEventListener('click',e=>{
  const c=e.target.closest('.cmp');if(c){e.preventDefault();e.stopPropagation();const n=c.dataset.c;cmp=cmp.includes(n)?cmp.filter(x=>x!==n):(cmp.length<4?[...cmp,n]:cmp);c.classList.toggle('on',cmp.includes(n));renderCmp();return;}
  const b=e.target.closest('button[data-k]');if(b&&!b.disabled){const k=b.dataset.k,v=b.dataset.v;if(sel[k]===v)delete sel[k];else sel[k]=v;render();return;}
  const rm=e.target.closest('[data-rm]');if(rm){delete sel[rm.dataset.rm];render();return;}
  if(e.target.closest('.js-clear')){sel={};render();return;}
  if(e.target.closest('.js-cclear')){cmp=[];render();return;}
  if(e.target.closest('.js-fopen')){$('rkOv').classList.add('open');$('rkSh').classList.add('open');return;}
  if(e.target.closest('.js-fclose')){$('rkOv').classList.remove('open');$('rkSh').classList.remove('open');return;}
},true);
$('rkSort').onchange=render;
function fromHash(){sel={};location.hash.slice(1).split('/').filter(Boolean).forEach(s=>{const v=UNSLUG[s];if(v)sel[KEY[v]]=v;});}
fromHash();render();
addEventListener('hashchange',()=>{fromHash();render();});
})();
</script>
'''
out=head+css+'</head>\n<body>\n'+svg+'\n<div class="screen"><div class="scroller">\n'+body+'</div>'+sheet.replace('<div class="r-ov js-fclose">','<div class="r-ov js-fclose" id="rkOv">').replace('<div class="r-sheet">','<div class="r-sheet" id="rkSh">')+'</div>\n<template id="tpl-menu">\n'+S.MENU+'</template>\n'+js+'</body>\n</html>\n'
out=S.link_fix(out)
open('T91_mockup_racchette.html','w').write(out); print('racchette built',len(out))
