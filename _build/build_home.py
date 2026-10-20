import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
import shared as S
os.chdir(sys.argv[1])
src=open('T91_presentazione_nuovo_sito.html').read()
head=src[:src.index('</head>')].replace('<title>Il nuovo T91</title>','<title>T91 · Homepage</title>')
svg=src[src.index('<svg width="0"'):src.index('</svg>',src.index('<svg width="0"'))+6]
n1=re.search(r'src="(data:image/jpeg;base64,[^"]+)"',src).group(1)
C=S.CDN; PDP='T91_mockup_pagina_prodotto.html'
def card(name,img,price,badge='',link='#',old='',sub=''):
    b=f'<span class="bdg{" k" if badge in ("Signature","Bestseller") else ""}">{badge}</span>' if badge else ''
    o=f'<s>{old}</s> ' if old else ''
    return f'<a class="p-card" href="{link}"><div class="im">{b}<img src="{C}{img}&width=500" alt=""></div><b>{name}</b><span class="pr">{o}{price}<small>{sub}</small></span></a>'
best=''.join([
 card('Boss One K12 Pro Master 6.0','BossOneK12Master6.01.webp?v=1791205585','€328,90','Novità',PDP,sub='o 3 × €109,63 con Klarna'),
 card('Mystery Box · racchetta garantita','Mistery_Livello_3.2.webp?v=1773227101','da €300,00','Bestseller',old='€740,00',sub='Il più venduto'),
 card('Huracán 2.0','Huracan_2.0_Nera_d0923663-c471-4cd0-b0a6-536e9564d7a8.webp?v=1766168628','€328,90',sub='o 3 × €109,63 con Klarna'),
 card('Huracán Full Black x Iriart 3.0','HURACANFULLBLACKXEMILIANOIRIART.webp?v=1791215495','€328,90','Signature',sub='o 3 × €109,63 con Klarna'),
 card('Finder Pro Master K3','FinderProMasterK31.webp?v=1791205236','€328,90','Novità',sub='o 3 × €109,63 con Klarna'),
 card('Boss One K3 Pro Master','BossOneK3Master6.01.webp?v=1791205374','€328,90','Novità',sub='o 3 × €109,63 con Klarna'),
])
lv=[('Principianti','Huracan_2.0_Nera_d0923663-c471-4cd0-b0a6-536e9564d7a8.webp?v=1766168628','Leggere e facili da gestire'),
    ('Intermedi','FinderProMasterK31.webp?v=1791205236','Per crescere, con più controllo'),
    ('Avanzati','BossOneK12Master6.01.webp?v=1791205585','Potenza e risposta secca'),
    ('Pro','HURACANFULLBLACKXEMILIANOIRIART.webp?v=1791215495','Le racchette del Team')]
levels=''.join(f'<a class="h-lv" href="#"><div class="im"><img src="{C}{i}&width=500" alt=""></div><b>{n}</b><span>{d}</span><em>→</em></a>' for n,i,d in lv)
REV=[("FP","Francesco P.","Feeling dal primo momento","Pala solida e ben fatta, il contatto con la pallina dà tanto controllo, e quando serve potenza risponde subito presente.","Huracán 2.0"),
   ("DP","Davide P.","Leggera e super maneggevole","Bilanciamento ottimo, grafica stupenda. La consiglio a chi vuole il massimo del controllo.","Huracán 2.0"),
   ("SC","Stefano C.","Arrivata in un paio di giorni","Mi trovo bene, devo ancora imparare a domarla. Ottima in difesa sui blocchi e sui pallonetti.","Huracán 2.0"),
   ("CK","Christer K.","Fantastic racket","Big sweet spot, great output.","Huracán 2.0"),
   ("AP","Alessandro P.","Servizio clienti ai massimi","Pala e servizio clienti ai massimi livelli.","Huracán 2.0")]
revs=''.join(f'<article class="p-rc"><div class="top"><span class="who"><i>{i}</i>{n}</span><span class="vf">✓ Acquisto verificato</span></div><span>★★★★★</span><h4>{t}</h4><p>{b}</p><div class="meta"><span>Acquistato: <b>{pr}</b></span></div></article>' for i,n,t,b,pr in REV)
NAV=lambda a,b:f'<div class="h-nav"><button class="js-prev" aria-label="Indietro"><svg class="i"><use href="#i-l"/></svg></button><button class="js-next" aria-label="Avanti"><svg class="i"><use href="#i-r"/></svg></button></div>'
body=f'''<div class="p home">
{S.TOPBAR}  <div class="p-bar"><div class="p-marq"><span>⚡ SPEDIZIONE GRATUITA 24/48H</span><span>· RESO GRATUITO 30 GIORNI</span><span>· PAGA IN 3 RATE CON KLARNA</span><span>· T91 CLUB: -30% SEMPRE</span><span>⚡ SPEDIZIONE GRATUITA 24/48H</span><span>· RESO GRATUITO 30 GIORNI</span><span>· PAGA IN 3 RATE CON KLARNA</span><span>· T91 CLUB: -30% SEMPRE</span></div></div>
{S.HEAD('')}
  <section class="h-hero">
    <div class="tx">
      <span class="ey">Novità · Holo Collection</span>
      <h1>Nata per chiudere<br>il punto.</h1>
      <p>La nuova linea Master 6.0: carbonio, potenza e i colori Holo.</p>
      <div class="ctas"><a class="h-btn v" href="{PDP}">Scopri la Boss One K12</a><a class="h-btn o" href="#">Tutte le racchette</a></div>
    </div>
    <a class="im" href="{PDP}"><picture><source media="(min-width:900px)" srcset="https://t91padel.com/cdn/shop/files/Racchetta_HOLO_arancione_in_carbonio_pc.webp?v=1791307698&width=1600"><img src="https://t91padel.com/cdn/shop/files/Racchetta_HOLO_arancione_in_carbonio_cell.webp?v=1791307714&width=900" alt="Racchetta T91 Holo arancione"></picture></a>
  </section>

  <section class="h-sec">
    <div class="p-sh"><h2>Una racchetta<br>per ogni livello.</h2><a href="#">Vedi tutte le racchette</a></div>
    <div class="h-lvs">{levels}</div>
  </section>

  <section class="h-quiz">
    <div><span class="ey">Non sai quale scegliere?</span><h2>Trova la tua racchetta<br>in 4 domande.</h2><p>Livello, stile di gioco, peso e budget. Il risultato arriva anche su WhatsApp.</p></div>
    <div class="steps"><span>1 · Livello</span><span>2 · Stile</span><span>3 · Peso</span><span>4 · Budget</span><a class="h-btn k" href="#">Inizia il test</a></div>
  </section>

  <section class="h-sec">
    <div class="p-sh"><h2>Le più vendute.</h2>{NAV(0,0)}</div>
    <div class="h-car"><div class="h-track">{best}</div></div>
  </section>

  <section class="h-sec h-wear">
    <div class="p-sh"><h2>Vesti come giochi.</h2><a href="#">Tutto l'abbigliamento</a></div>
    <div class="h-wg">
      <a class="h-wt" href="#"><img src="https://t91padel.com/cdn/shop/files/HALO_COLLECTION_COVER_PC.webp?v=1779720697&width=1200" alt=""><span><small>Halo Collection</small>Uomo</span></a>
      <a class="h-wt" href="#"><img src="https://t91padel.com/cdn/shop/files/Abbigliamento_Donna_Computer.webp?v=1791538718&width=1200" alt=""><span><small>Nuova stagione</small>Donna</span></a>
    </div>
    <a class="h-pers" href="#"><span><b>Personalizzabili</b>Il tuo nome sulla maglia, anche per un pezzo solo.</span><em>→</em></a>
  </section>

  <section class="h-team">
    <div class="p-sh"><h2>Il Team T91.</h2><a href="#">Scopri tutto il team</a></div>
    <div class="h-tg">
      <a class="h-feat" href="{PDP}"><img src="{n1}" alt="Atleta T91 in smash"><span class="tx"><span class="big">N.1</span><b>Nome Cognome</b><span>N.1 del ranking italiano · gioca la Boss One K12 Pro Master 6.0</span><u>Vedi la sua racchetta →</u></span></a>
      <div class="h-ath">
        <a href="#"><img src="{C}HURACANFULLBLACKXEMILIANOIRIART.webp?v=1791215495&width=300" alt=""><span><b>Emiliano Iriart</b>Huracán Iriart 3.0</span><em>→</em></a>
        <a href="#"><img src="{C}LimitedEdition12KBubu.webp?v=1785322689&width=300" alt=""><span><b>Bubu Salandro</b>Huracán 2.0 12K</span><em>→</em></a>
        <a href="#"><img src="{C}Finder_Pro_Remedi_3.0_PWR_1.webp?v=1780990777&width=300" alt=""><span><b>Nick Remedi</b>Finder Pro K12 3.0</span><em>→</em></a>
        <a href="#" class="more"><span><b>Ambassador e Team Under</b>I giovani e chi rappresenta T91</span><em>→</em></a>
      </div>
    </div>
  </section>

  <section class="h-sec">
    <div class="p-sh"><h2>Non solo racchette.</h2></div>
    <div class="p-sg">
      <div><small>Ritiro usato</small><b>T91 Care</b><span>La tua vecchia racchetta, anche non T91, diventa uno sconto.</span><a href="#">Valutala</a></div>
      <div><small>Riparazioni</small><b>T91 Repair</b><span>Ripariamo racchette di qualsiasi marca.</span><a href="#">Preventivo</a></div>
      <div><small>Protezione</small><b>Garanzia estesa</b><span>Si rompe? Te la sostituiamo.</span><a href="#">Come funziona</a></div>
      <div><small>Anche 1 pezzo</small><b>Personalizza</b><span>Il tuo nome sul completo.</span><a href="#">Inizia</a></div>
    </div>
  </section>

  <section class="h-club">
    <div><span class="ey">T91 Club</span><h2>-30%. Sempre.</h2><p>Una quota all'anno e lo sconto su tutto, più il regalo di compleanno e le novità in anteprima.</p></div>
    <div class="r"><div class="pr">€79,90<small>/ anno</small></div><a class="h-btn v" href="#">Scopri il Club</a></div>
  </section>

  <section class="h-sec p-rev">
    <div class="p-sh"><h2>Cosa dicono<br>i giocatori.</h2>{NAV(0,0)}</div>
    <div class="p-score" style="margin-bottom:8px"><span class="n">4,9</span><span><span class="s">★★★★★</span><br><span class="c">770 recensioni verificate</span></span></div>
    <div class="h-car"><div class="h-track">{revs}</div></div>
  </section>

  <section class="h-sec p-blog">
    <div class="p-sh"><h2>Dal blog.</h2><a href="#">Tutti gli articoli</a></div>
    <div class="p-rail">
      <a class="p-post" href="#"><div class="im"><span>Guide</span><img src="{C}Boss_One_K12_Master_6.0_6.webp?v=1791207039&width=700" alt=""></div><small>6 min · Guide</small><b>Come scegliere la racchetta per il tuo livello</b></a>
      <a class="p-post" href="{PDP}"><div class="im"><span>Novità</span><img src="https://t91padel.com/cdn/shop/files/Racchetta_HOLO_arancione_in_carbonio_pc.webp?v=1791307698&width=700" alt=""></div><small>4 min · Novità</small><b>Holo Collection: la nuova linea Master 6.0</b></a>
      <a class="p-post" href="#"><div class="im"><span>Tornei</span><img src="https://t91padel.com/cdn/shop/files/IRIART_3_COVER_PC_a5cd421b-ba5d-4364-9af6-ef683e77ac0d.webp?v=1791215341&width=700" alt=""></div><small>3 min · I nostri pro</small><b>Il Team T91 nel weekend: i risultati</b></a>
    </div>
  </section>

  <section class="h-sec h-near">
    <a href="#" class="a"><span class="ey">70 centri partner</span><b>Trova T91 vicino a te.</b><span>Prova le racchette e compra nei centri in Italia ed Europa.</span><u>Apri la mappa →</u></a>
    <a href="#" class="b"><span class="ey">Per i professionisti</span><b>Sei un centro o un maestro?</b><span>Il programma T91 per centri, maestri e academy.</span><u>Scopri il programma →</u></a>
  </section>

{S.FOOTER}</div>
'''
css='''<style>
.home .p-sh h2 br{display:none}
.h-btn{display:inline-flex;align-items:center;border-radius:980px;padding:13px 22px;font-size:15px;white-space:nowrap}
.h-btn.v{background:var(--volt);color:#000}
.h-btn.o{border:1px solid rgba(255,255,255,.4);color:#fff}
.h-btn.k{background:#000;color:#fff}
.ey{display:block;font-size:13px;color:var(--mute);margin-bottom:8px}
.h-hero{background:#000;color:#fff;display:flex;flex-direction:column-reverse}
.h-hero .im{display:block;aspect-ratio:5/6;overflow:hidden}
.h-hero .im img{width:100%;height:100%;object-fit:cover}
.h-hero .tx{padding:28px 20px 36px}
.h-hero .ey{color:var(--volt)}
.h-hero h1{font-weight:400;font-size:42px;line-height:1;letter-spacing:-.04em}
.h-hero p{font-size:16px;color:#C7C7CC;margin:14px 0 22px;max-width:420px}
.h-hero .ctas{display:flex;gap:10px;flex-wrap:wrap}
.h-sec{padding:48px 20px}
.h-lvs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.h-lv{background:var(--fog);border-radius:20px;padding:14px;display:flex;flex-direction:column;gap:2px;position:relative}
.h-lv .im{aspect-ratio:1/1;display:grid;place-items:center;margin-bottom:8px}
.h-lv .im img{width:78%;height:78%;object-fit:contain;transition:transform .3s}
.h-lv:hover .im img{transform:scale(1.05) rotate(-3deg)}
.h-lv b{font-size:19px;letter-spacing:-.015em}
.h-lv span{font-size:13px;color:var(--mute)}
.h-lv em{position:absolute;right:14px;bottom:14px;font-style:normal;color:var(--mute)}
.h-quiz{background:var(--volt);padding:40px 20px;display:flex;flex-direction:column;gap:20px}
.h-quiz .ey{color:#333}
.h-quiz h2{font-weight:400;font-size:32px;line-height:1.05;letter-spacing:-.03em}
.h-quiz p{font-size:15.5px;margin-top:10px;color:#222}
.h-quiz .steps{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.h-quiz .steps span{background:rgba(0,0,0,.08);border-radius:980px;padding:8px 14px;font-size:14px}
.h-quiz .steps .h-btn{margin-top:6px}
.h-nav{display:flex;gap:8px}
.h-nav button{width:42px;height:42px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;background:#fff}
.h-nav button:disabled{opacity:.35;cursor:default}
.h-nav svg{width:18px;height:18px}
.h-car{overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin:0 -20px;padding:0 20px;scroll-padding:0 20px}
.h-car::-webkit-scrollbar{display:none}
.h-track{display:flex;gap:12px;width:max-content}
.h-track::after{content:"";width:8px;flex:none}
.h-track>*{scroll-snap-align:start;flex:none}
.h-track .p-card{width:220px}
.h-track .p-rc{width:280px}
.p-card s{color:var(--mute);font-size:12px;margin-right:2px}
.h-wg{display:grid;gap:10px}
.h-wt{position:relative;border-radius:22px;overflow:hidden;aspect-ratio:4/3;background:#111;display:block}
.h-wt img{width:100%;height:100%;object-fit:cover;transition:transform .4s}
.h-wt:hover img{transform:scale(1.04)}
.h-wt span{position:absolute;left:18px;bottom:16px;color:#fff;font-size:30px;letter-spacing:-.03em;line-height:1;text-shadow:0 2px 20px rgba(0,0,0,.4)}
.h-wt small{display:block;font-size:13px;letter-spacing:0;margin-bottom:6px;opacity:.85}
.h-pers{display:flex;justify-content:space-between;align-items:center;gap:12px;background:var(--fog);border-radius:18px;padding:16px 18px;margin-top:10px;font-size:14px;color:var(--mute)}
.h-pers b{display:block;font-size:17px;color:var(--ink)}
.h-pers em{font-style:normal;width:36px;height:36px;border-radius:50%;background:#000;color:var(--volt);display:grid;place-items:center;flex:none}
.h-team{background:#000;color:#fff;padding:48px 20px}
.h-team .p-sh a{color:#fff}
.h-tg{display:grid;gap:10px}
.h-feat{position:relative;display:block;border-radius:22px;overflow:hidden;aspect-ratio:4/5;background:#111}
.h-feat img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:76% 30%}
.h-feat::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.85))}
.h-feat .tx{position:absolute;left:20px;right:20px;bottom:20px;z-index:1;display:flex;flex-direction:column;gap:4px}
.h-feat .big{font-size:64px;line-height:.85;letter-spacing:-.06em;color:var(--volt)}
.h-feat b{font-size:24px;letter-spacing:-.02em}
.h-feat .tx>span:not(.big){font-size:14px;color:#C7C7CC}
.h-feat u{font-size:14px;color:var(--volt);text-decoration:none;margin-top:6px}
.h-ath{display:flex;flex-direction:column;gap:8px}
.h-ath a{display:flex;align-items:center;gap:14px;background:#1D1D1F;border-radius:18px;padding:12px 16px 12px 12px}
.h-ath img{width:64px;height:64px;border-radius:14px;background:#F5F5F7;object-fit:contain;padding:4px;flex:none}
.h-ath span{flex:1;font-size:13px;color:#A1A1A6}
.h-ath b{display:block;font-size:17px;color:#fff}
.h-ath em{font-style:normal;color:var(--volt)}
.h-ath .more{background:transparent;border:1px solid #3A3A3C;padding:16px}
.h-club{margin:0 20px;background:#000;color:#fff;border-radius:24px;padding:28px 22px;display:flex;flex-direction:column;gap:18px}
.h-club .ey{color:var(--volt)}
.h-club h2{font-weight:400;font-size:40px;letter-spacing:-.04em;line-height:1}
.h-club p{font-size:15px;color:#C7C7CC;margin-top:10px;max-width:460px}
.h-club .r{display:flex;align-items:center;justify-content:space-between;gap:12px}
.h-club .pr{font-size:30px;letter-spacing:-.03em}
.h-club .pr small{font-size:14px;color:#A1A1A6;margin-left:4px}
.h-near{display:grid;gap:10px}
.h-near a{border-radius:22px;padding:24px;display:flex;flex-direction:column;gap:6px;min-height:200px}
.h-near .a{background:var(--fog)}
.h-near .b{background:#000;color:#fff}
.h-near .b .ey{color:#A1A1A6}
.h-near b{font-size:26px;letter-spacing:-.025em;line-height:1.1}
.h-near span:not(.ey){font-size:14.5px;color:var(--mute)}
.h-near .b span:not(.ey){color:#C7C7CC}
.h-near u{margin-top:auto;text-decoration:none;font-size:14.5px}
.h-near .b u{color:var(--volt)}
.home .p-sg div{min-height:170px}
@container dev (min-width: 900px){
  .home .p-sh h2 br{display:inline}
  .h-hero{flex-direction:row;align-items:stretch;min-height:640px}
  .h-hero .tx{flex:1;display:flex;flex-direction:column;justify-content:center;padding:64px 40px 64px 80px}
  .h-hero .im{flex:1.25;aspect-ratio:auto}
  .h-hero h1{font-size:76px}
  .h-hero p{font-size:19px}
  .h-sec{padding:88px 80px}
  .home .p-sh h2{font-size:52px}
  .h-lvs{grid-template-columns:repeat(4,1fr);gap:16px}
  .h-lv{padding:20px;border-radius:24px}
  .h-lv b{font-size:24px}
  .h-quiz{flex-direction:row;align-items:center;justify-content:space-between;padding:64px 80px;gap:40px}
  .h-quiz h2{font-size:52px}
  .h-quiz .steps{max-width:420px;justify-content:flex-end}
  .h-car{margin:0 -80px;padding:0 80px;scroll-padding:0 80px}
  .h-track{gap:16px}
  .h-track .p-card{width:270px}
  .h-track .p-rc{width:340px}
  .h-track::after{width:64px}
  .h-wg{grid-template-columns:1fr 1fr;gap:16px}
  .h-wt{aspect-ratio:5/4}
  .h-wt span{font-size:44px;left:28px;bottom:24px}
  .h-team{padding:88px 80px}
  .h-tg{grid-template-columns:1.4fr 1fr;gap:16px}
  .h-feat{aspect-ratio:auto;min-height:560px}
  .h-feat::after{background:linear-gradient(90deg,rgba(0,0,0,.7),rgba(0,0,0,0) 60%)}
  .h-feat img{object-position:70% 40%}
  .h-feat .tx{top:0;bottom:0;right:auto;width:52%;justify-content:center;padding:0 0 0 20px}
  .h-feat .big{font-size:140px}
  .h-feat b{font-size:34px}
  .h-ath{justify-content:space-between}
  .h-ath a{flex:1}
  .h-club{margin:0 80px;flex-direction:row;align-items:center;justify-content:space-between;padding:48px 56px;border-radius:32px}
  .h-club h2{font-size:64px}
  .h-club .r{flex-direction:column;align-items:flex-end}
  .h-club .pr{font-size:44px}
  .h-near{grid-template-columns:1fr 1fr;gap:16px}
  .h-near a{min-height:260px;padding:36px;border-radius:28px}
  .h-near b{font-size:34px}
}
html,body{height:100%;overflow:hidden}
.screen{position:fixed!important;inset:0;width:100%;height:100%}
</style>
'''
js='''<script>
(function(){
'''+S.JS_MENU+'''
const screen=document.querySelector('.screen');
screen.appendChild(document.getElementById('tpl-menu').content.cloneNode(true));
t91Menu(screen);t91Toast(screen);
screen.querySelectorAll('.h-sec').forEach(sec=>{
  const car=sec.querySelector('.h-car'),pv=sec.querySelector('.js-prev'),nx=sec.querySelector('.js-next');
  if(!car||!pv)return;
  const step=()=>{const c=car.querySelector('.h-track>*');return c?c.getBoundingClientRect().width+16:280;};
  const upd=()=>{pv.disabled=car.scrollLeft<4;nx.disabled=car.scrollLeft+car.clientWidth>=car.scrollWidth-4;};
  pv.onclick=()=>car.scrollBy({left:-step(),behavior:'smooth'});nx.onclick=()=>car.scrollBy({left:step(),behavior:'smooth'});
  car.addEventListener('scroll',upd,{passive:true});setTimeout(upd,300);
});
})();
</script>
'''
out=head+css+'</head>\n<body>\n'+svg+'\n<div class="screen"><div class="scroller">\n'+body+'</div></div>\n<template id="tpl-menu">\n'+S.MENU+'</template>\n'+js+'</body>\n</html>\n'
out=out.replace('href="#" data-link="home"','href="T91_mockup_homepage.html" data-link="home"')
open('T91_mockup_homepage.html','w').write(out); print('home built',len(out))
