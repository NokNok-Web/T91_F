import sys,os,re
sys.path.insert(0,os.path.dirname(__file__))
import shared as S
os.chdir(sys.argv[1])
src=open('T91_presentazione_nuovo_sito.html').read()
head=src[:src.index('</head>')].replace('<title>Il nuovo T91</title>','<title>T91 · Homepage</title>')
svg=src[src.index('<svg width="0"'):src.index('</svg>',src.index('<svg width="0"'))+6]
import base64
b64=lambda f:'data:image/jpeg;base64,'+base64.b64encode(open(f,'rb').read()).decode()
HD=b64('img/hero-desktop.jpg')
n1=re.search(r'src="(data:image/jpeg;base64,[^"]+)"',src).group(1)
C=S.CDN; PDP='T91_mockup_pagina_prodotto.html'
def card(name,img,price,badge='',link='#',old='',sub='',cat=''):
    b=f'<span class="bdg{" k" if badge in ("Signature","Il più venduto") else ""}">{badge}</span>' if badge else ''
    o=f'<s>{old}</s> ' if old else ''
    c=f'<small class="cat">{cat}</small>' if cat else ''
    return f'<a class="p-card" href="{link}"><div class="im">{b}<img src="{C}{img}&width=500" alt=""></div>{c}<b>{name}</b><span class="pr">{o}{price}<small>{sub}</small></span></a>'
best=''.join([
 card('Mystery Box · racchetta garantita','Mistery_Livello_3.2.webp?v=1773227101','da €300,00','Il più venduto',old='€740,00',cat='Mystery Box'),
 card('Huracán 2.0','Huracan_2.0_Nera_d0923663-c471-4cd0-b0a6-536e9564d7a8.webp?v=1766168628','€328,90',sub='o 3 × €109,63 con Klarna',cat='Racchetta'),
 card('Borsa isotermica XL 2.0','BorsoneXLArancione1.webp?v=1788959393','€129,90','Preordine',cat='Borsa'),
 card('Boss One K12 Pro Master 6.0','BossOneK12Master6.01.webp?v=1791205585','€328,90','Novità',PDP,sub='o 3 × €109,63 con Klarna',cat='Racchetta'),
 card('T-shirt Premium Performance','T-shirt_rosa_1_5f220f5e-2edd-484a-923a-0c4b7c06e8b6.webp?v=1713189215','€56,90',cat='Abbigliamento donna'),
 card('Halo T-shirt con il tuo nome','T-shirt_rosa_grigio_2_pers.webp?v=1779469145','€59,90','Personalizzabile',cat='Abbigliamento uomo'),
 card('Gonna Premium Performance','Gonna_Indaco_1.webp?v=1788874382','€42,90',cat='Abbigliamento donna'),
 card('Ultra Performance Cap 2.0','T91ULTRACAPNERO.webp?v=1775209993','€28,90',cat='Accessori'),
])
lv=[('Principianti','Huracan_2.0_Nera_d0923663-c471-4cd0-b0a6-536e9564d7a8.webp?v=1766168628','Leggere e facili da gestire'),
    ('Intermedi','FinderProMasterK31.webp?v=1791205236','Per crescere, con più controllo'),
    ('Avanzati','BossOneK12Master6.01.webp?v=1791205585','Potenza e risposta secca'),
    ('Pro','HURACANFULLBLACKXEMILIANOIRIART.webp?v=1791215495','Le racchette del Team')]
levels=''.join(f'<a class="h-lv" href="#" data-link="racchette#{n.lower()}"><div class="im"><img src="{C}{i}&width=500" alt=""></div><b>{n}</b><span>{d}</span><em>→</em></a>' for n,i,d in lv)
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
    <img class="bg d" src="{HD}" alt="Giocatore T91 al servizio in torneo">
    <div class="tx">
      <span class="ey">Novità · Holo Collection</span>
      <h1>Nata per<br>chiudere<br>il punto.</h1>
      <p>La nuova linea Master 6.0: carbonio, potenza e i colori Holo.</p>
      <div class="ctas"><a class="h-btn v" href="{PDP}">Scopri la Boss One K12</a><a class="h-btn o" href="#" data-link="racchette">Tutte le racchette</a></div>
    </div>
  </section>

  <div class="h-band"><div class="tr"><span>From players to players</span><i>★</i><span>4,9 su 770 recensioni</span><i>★</i><span>Spedita in 24/48h</span><i>★</i><span>120 pro giocano T91</span><i>★</i><span>From players to players</span><i>★</i><span>4,9 su 770 recensioni</span><i>★</i><span>Spedita in 24/48h</span><i>★</i><span>120 pro giocano T91</span><i>★</i></div></div>

  <section class="h-sec">
    <div class="h-tt"><h2>Una racchetta<br>per ogni livello.</h2><a href="#" data-link="racchette">Vedi tutte le racchette →</a></div>
    <div class="h-lvs">{levels}</div>
  </section>

  <section class="h-quiz">
    <div><span class="ey">Non sai quale scegliere?</span><h2>Trova la tua<br>racchetta.</h2><p>Quattro domande su livello, stile di gioco, peso e budget. Il risultato arriva anche su WhatsApp.</p></div>
    <div class="r"><div class="steps"><span>1 · Livello</span><span>2 · Stile</span><span>3 · Peso</span><span>4 · Budget</span></div><a class="h-btn k big" href="#">Inizia il test →</a></div>
  </section>

  <section class="h-sec">
    <div class="h-tt"><h2>I più venduti.</h2>{NAV(0,0)}</div>
    <div class="h-car"><div class="h-track">{best}</div></div>
  </section>

  <section class="h-sec h-wear">
    <div class="h-tt"><h2>Vesti come giochi.</h2><a href="#">Tutto l'abbigliamento →</a></div>
    <div class="h-wg">
      <a class="h-wt" href="#"><img src="https://t91padel.com/cdn/shop/files/HALO_COLLECTION_COVER_PC.webp?v=1779720697&width=1400" alt=""><span><small>Halo Collection</small>Uomo</span></a>
      <a class="h-wt" href="#"><img src="https://t91padel.com/cdn/shop/files/Abbigliamento_Donna_Computer.webp?v=1791538718&width=1400" alt=""><span><small>Nuova stagione</small>Donna</span></a>
    </div>
    <a class="h-pers" href="#">
      <div class="tx"><span class="ey">Personalizzabili · anche un pezzo solo</span><h3>Il tuo nome.<br>Sulla tua maglia.</h3><p>Scegli il capo, scrivi il nome o il numero e vedi l'anteprima. Nessun minimo d'ordine.</p><span class="h-btn k">Personalizza ora →</span></div>
      <div class="vis"><img src="{C}T-shirt_rosa_grigio_2_pers.webp?v=1779469145&width=900" alt="T-shirt Halo personalizzata con il nome"><span class="tag">Anteprima dal vivo</span></div>
    </a>
  </section>

  <section class="h-team">
    <div class="h-tt"><h2>Il Team T91.</h2><a href="#">Scopri tutto il team →</a></div>
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

  <section class="h-serv">
    <div class="h-tt"><div><span class="ey">I servizi T91</span><h2>Non solo<br>racchette.</h2></div><p class="lead">Quello che facciamo oltre a vendere: per far durare la tua racchetta, darle una seconda vita e renderla tua.</p></div>
    <div class="h-sg">
      <a class="s1" href="#"><img src="{C}Boss_One_K12_Master_6.0_7.webp?v=1791207039&width=1200" alt=""><span class="tx"><small>01 · Ritiro usato</small><b>T91 Care</b><span>La tua vecchia racchetta, anche non T91, diventa uno sconto sulla nuova.</span><u>Valuta la tua racchetta →</u></span></a>
      <a class="s2" href="#"><span class="tx"><small>02 · Riparazioni</small><b>T91 Repair</b><span>Ripariamo racchette di qualsiasi marca. Preventivo da foto su WhatsApp.</span><u>Chiedi un preventivo →</u></span></a>
      <a class="s3" href="#"><span class="tx"><small>03 · Protezione</small><b>Garanzia estesa</b><span>Si rompe? Te la sostituiamo. Da €39,90.</span><u>Come funziona →</u></span></a>
      <a class="s4" href="#"><span class="tx"><small>04 · Ritiro in negozio</small><b>Click &amp; Collect</b><span>Ordini online, ritiri a Osio Sotto.</span><u>Punti di ritiro →</u></span></a>
    </div>
  </section>

  <section class="h-club">
    <div><span class="ey">T91 Club</span><h2>-30%.<br>Sempre.</h2><p>Una quota all'anno e lo sconto su tutto, più il regalo di compleanno e le novità in anteprima.</p></div>
    <div class="r"><div class="pr">€79,90<small>/ anno</small></div><a class="h-btn v big" href="#">Scopri il Club →</a></div>
  </section>

  <section class="h-sec p-rev">
    <div class="h-tt"><h2>Cosa dicono<br>i giocatori.</h2>{NAV(0,0)}</div>
    <div class="p-score" style="margin-bottom:8px"><span class="n">4,9</span><span><span class="s">★★★★★</span><br><span class="c">770 recensioni verificate</span></span></div>
    <div class="h-car"><div class="h-track">{revs}</div></div>
  </section>

  <section class="h-sec p-blog">
    <div class="h-tt"><h2>Dal blog.</h2><a href="#">Tutti gli articoli →</a></div>
    <div class="p-rail">
      <a class="p-post" href="#"><div class="im"><span>Guide</span><img src="{C}Boss_One_K12_Master_6.0_6.webp?v=1791207039&width=700" alt=""></div><small>6 min · Guide</small><b>Come scegliere la racchetta per il tuo livello</b></a>
      <a class="p-post" href="{PDP}"><div class="im"><span>Novità</span><img src="https://t91padel.com/cdn/shop/files/Racchetta_HOLO_arancione_in_carbonio_pc.webp?v=1791307698&width=700" alt=""></div><small>4 min · Novità</small><b>Holo Collection: la nuova linea Master 6.0</b></a>
      <a class="p-post" href="#"><div class="im"><span>Tornei</span><img src="https://t91padel.com/cdn/shop/files/IRIART_3_COVER_PC_a5cd421b-ba5d-4364-9af6-ef683e77ac0d.webp?v=1791215341&width=700" alt=""></div><small>3 min · I nostri pro</small><b>Il Team T91 nel weekend: i risultati</b></a>
    </div>
  </section>

  <section class="h-sec h-near">
    <a href="#" class="a"><span class="ey">70 centri partner</span><b>Trova T91<br>vicino a te.</b><span>Prova le racchette e compra nei centri in Italia ed Europa.</span><u>Apri la mappa →</u></a>
    <a href="#" class="b"><span class="ey">Per i professionisti</span><b>Sei un centro<br>o un maestro?</b><span>Il programma T91 per centri, maestri e academy.</span><u>Scopri il programma →</u></a>
  </section>

{S.FOOTER}</div>
'''
css='''<style>
.h-btn{display:inline-flex;align-items:center;justify-content:center;border-radius:980px;padding:14px 24px;font-size:15px;white-space:nowrap;transition:transform .15s}
.h-btn:hover{transform:translateY(-2px)}
.h-btn.big{padding:18px 30px;font-size:17px}
.h-btn.v{background:var(--volt);color:#000}
.h-btn.o{border:1px solid rgba(255,255,255,.5);color:#fff}
.h-btn.k{background:#000;color:#fff}
.ey{display:block;font-size:13px;color:var(--mute);margin-bottom:10px;letter-spacing:.02em}
.h-tt{display:flex;align-items:flex-end;justify-content:space-between;gap:16px;margin-bottom:24px}
.h-tt h2{font-weight:400;font-size:40px;line-height:.98;letter-spacing:-.045em}
.h-tt>a{font-size:14px;white-space:nowrap;padding-bottom:6px}
.h-tt .lead{font-size:16px;color:#A1A1A6;max-width:420px}
/* hero */
.h-hero{position:relative;background:#000;color:#fff;min-height:700px;display:flex;align-items:flex-end;overflow:hidden}
.h-hero .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.h-hero .bg.d{object-position:46% 30%}
.h-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.9) 90%)}
.h-hero .tx{position:relative;z-index:1;padding:28px 20px 40px}
.h-hero .ey{color:var(--volt)}
.h-hero h1{font-weight:400;font-size:58px;line-height:.92;letter-spacing:-.055em}
.h-hero p{font-size:16px;color:#E5E5EA;margin:16px 0 24px;max-width:420px}
.h-hero .ctas{display:flex;gap:10px;flex-wrap:wrap}
/* fascia volt */
.h-band{background:var(--volt);overflow:hidden;white-space:nowrap;border-bottom:1px solid #000}
.h-band .tr{display:inline-flex;align-items:center;gap:24px;padding:16px 0;animation:marq 30s linear infinite}
.h-band span{font-size:26px;letter-spacing:-.03em;text-transform:uppercase}
.h-band i{font-style:normal;font-size:16px}
@media (prefers-reduced-motion:reduce){.h-band .tr{animation:none}}
.h-sec{padding:56px 20px}
/* livelli */
.h-lvs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.h-lv{background:var(--fog);border-radius:22px;padding:16px;display:flex;flex-direction:column;gap:2px;position:relative;overflow:hidden}
.h-lv .im{aspect-ratio:4/5;display:grid;place-items:center;margin-bottom:8px}
.h-lv .im img{width:90%;height:90%;object-fit:contain;transition:transform .4s cubic-bezier(.2,.8,.2,1)}
.h-lv:hover .im img{transform:scale(1.08) rotate(-4deg)}
.h-lv b{font-size:22px;letter-spacing:-.025em}
.h-lv span{font-size:13px;color:var(--mute)}
.h-lv em{position:absolute;right:16px;top:16px;font-style:normal;width:34px;height:34px;border-radius:50%;background:#fff;display:grid;place-items:center}
.h-lv:hover em{background:var(--volt)}
/* quiz */
.h-quiz{background:var(--volt);padding:48px 20px;display:flex;flex-direction:column;gap:24px}
.h-quiz .ey{color:#333}
.h-quiz h2{font-weight:400;font-size:46px;line-height:.95;letter-spacing:-.05em}
.h-quiz p{font-size:16px;margin-top:14px;color:#222;max-width:460px}
.h-quiz .steps{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px}
.h-quiz .steps span{background:rgba(0,0,0,.08);border-radius:980px;padding:9px 15px;font-size:14px}
/* caroselli */
.h-nav{display:flex;gap:8px}
.h-nav button{width:46px;height:46px;border-radius:50%;border:1px solid var(--line);display:grid;place-items:center;background:#fff}
.h-nav button:disabled{opacity:.35;cursor:default}
.h-nav svg{width:18px;height:18px}
.h-car{overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin:0 -20px;padding:0 20px;scroll-padding:0 20px}
.h-car::-webkit-scrollbar{display:none}
.h-track{display:flex;gap:12px;width:max-content}
.h-track::after{content:"";width:8px;flex:none}
.h-track>*{scroll-snap-align:start;flex:none}
.h-track .p-card{width:230px}
.h-track .p-card .im{border-radius:20px}
.h-track .p-rc{width:290px}
.p-card s{color:var(--mute);font-size:12px;margin-right:2px}
.p-card .cat{font-size:12px;color:var(--mute);margin-bottom:-2px}
/* abbigliamento */
.h-wg{display:grid;gap:10px}
.h-wt{position:relative;border-radius:24px;overflow:hidden;aspect-ratio:4/5;background:#111;display:block}
.h-wt img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.h-wt:hover img{transform:scale(1.05)}
.h-wt::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 55%,rgba(0,0,0,.55))}
.h-wt span{position:absolute;left:20px;bottom:18px;color:#fff;font-size:44px;letter-spacing:-.045em;line-height:1;z-index:1}
.h-wt small{display:block;font-size:13px;letter-spacing:0;margin-bottom:8px;opacity:.9}
.h-pers{display:grid;margin-top:10px;background:var(--volt);border-radius:28px;overflow:hidden}
.h-pers .tx{padding:28px 22px;display:flex;flex-direction:column;align-items:flex-start;gap:12px}
.h-pers .ey{color:#333;margin:0}
.h-pers h3{font-weight:400;font-size:42px;line-height:.95;letter-spacing:-.05em}
.h-pers p{font-size:16px;color:#222;max-width:420px}
.h-pers .vis{position:relative;background:#fff;aspect-ratio:1/1;display:grid;place-items:center}
.h-pers .vis img{width:86%;height:86%;object-fit:contain}
.h-pers .tag{position:absolute;right:16px;top:16px;background:#000;color:var(--volt);font-size:15px;letter-spacing:.02em;padding:8px 14px;border-radius:12px;transform:rotate(4deg)}
/* team */
.h-team{background:#000;color:#fff;padding:56px 20px}
.h-team .h-tt>a{color:#fff}
.h-tg{display:grid;gap:10px}
.h-feat{position:relative;display:block;border-radius:24px;overflow:hidden;aspect-ratio:4/5;background:#111}
.h-feat img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:76% 30%}
.h-feat::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.85))}
.h-feat .tx{position:absolute;left:20px;right:20px;bottom:20px;z-index:1;display:flex;flex-direction:column;gap:4px}
.h-feat .big{font-size:80px;line-height:.85;letter-spacing:-.06em;color:var(--volt)}
.h-feat b{font-size:26px;letter-spacing:-.02em}
.h-feat .tx>span:not(.big){font-size:14px;color:#C7C7CC}
.h-feat u{font-size:14px;color:var(--volt);text-decoration:none;margin-top:6px}
.h-ath{display:flex;flex-direction:column;gap:8px}
.h-ath a{display:flex;align-items:center;gap:14px;background:#1D1D1F;border-radius:20px;padding:12px 16px 12px 12px}
.h-ath img{width:68px;height:68px;border-radius:14px;background:#F5F5F7;object-fit:contain;padding:4px;flex:none}
.h-ath span{flex:1;font-size:13px;color:#A1A1A6}
.h-ath b{display:block;font-size:18px;color:#fff}
.h-ath em{font-style:normal;color:var(--volt)}
.h-ath .more{background:transparent;border:1px solid #3A3A3C;padding:16px}
/* servizi */
.h-serv{background:#000;color:#fff;padding:64px 20px;border-top:1px solid #1D1D1F}
.h-serv .ey{color:var(--volt)}
.h-serv .h-tt{flex-direction:column;align-items:flex-start;margin-bottom:28px}
.h-serv .h-tt h2{font-size:52px}
.h-sg{display:grid;gap:10px}
.h-sg a{position:relative;border-radius:24px;overflow:hidden;background:#1D1D1F;min-height:230px;display:flex;align-items:flex-end;transition:transform .2s}
.h-sg a:hover{transform:translateY(-3px)}
.h-sg img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.7}
.h-sg .s1{min-height:420px}
.h-sg .s1::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,0) 30%,rgba(0,0,0,.85))}
.h-sg .s3{background:var(--volt);color:#000}
.h-sg .tx{position:relative;z-index:1;padding:24px;display:flex;flex-direction:column;gap:6px}
.h-sg small{font-size:13px;color:#A1A1A6}
.h-sg .s3 small{color:#333}
.h-sg b{font-size:34px;letter-spacing:-.04em;line-height:1}
.h-sg .tx>span{font-size:15px;color:#C7C7CC;max-width:380px}
.h-sg .s3 .tx>span{color:#222}
.h-sg u{text-decoration:none;font-size:14.5px;color:var(--volt);margin-top:8px}
.h-sg .s3 u{color:#000}
/* club */
.h-club{margin:56px 20px 0;background:#000;color:#fff;border-radius:28px;padding:32px 24px;display:flex;flex-direction:column;gap:22px;position:relative;overflow:hidden}
.h-club::before{content:"-30%";position:absolute;right:-20px;bottom:-40px;font-size:220px;letter-spacing:-.08em;color:#1D1D1F;line-height:1}
.h-club>*{position:relative}
.h-club .ey{color:var(--volt)}
.h-club h2{font-weight:400;font-size:56px;letter-spacing:-.05em;line-height:.92}
.h-club p{font-size:15.5px;color:#C7C7CC;margin-top:14px;max-width:460px}
.h-club .r{display:flex;align-items:center;justify-content:space-between;gap:12px;flex-wrap:wrap}
.h-club .pr{font-size:34px;letter-spacing:-.03em}
.h-club .pr small{font-size:14px;color:#A1A1A6;margin-left:4px}
/* vicino a te */
.h-near{display:grid;gap:10px}
.h-near a{border-radius:24px;padding:26px;display:flex;flex-direction:column;gap:8px;min-height:240px}
.h-near .a{background:var(--fog)}
.h-near .b{background:#000;color:#fff}
.h-near .b .ey{color:#A1A1A6}
.h-near b{font-size:34px;letter-spacing:-.04em;line-height:1}
.h-near span:not(.ey){font-size:14.5px;color:var(--mute)}
.h-near .b span:not(.ey){color:#C7C7CC}
.h-near u{margin-top:auto;text-decoration:none;font-size:15px}
.h-near .b u{color:var(--volt)}
@container dev (min-width: 900px){
  .h-tt{margin-bottom:40px}
  .h-tt h2{font-size:84px}
  .h-hero{min-height:820px;align-items:center}
  .h-hero .bg.d{width:128%;right:auto;object-position:50% 25%}
  .h-hero::after{background:linear-gradient(90deg,rgba(0,0,0,.82) 0%,rgba(0,0,0,.35) 40%,rgba(0,0,0,0) 62%)}
  .h-hero .tx{padding:0 0 0 80px;max-width:640px}
  .h-hero h1{font-size:112px}
  .h-hero p{font-size:20px}
  .h-band span{font-size:40px}
  .h-band .tr{padding:22px 0;gap:36px}
  .h-sec{padding:112px 80px}
  .h-lvs{grid-template-columns:repeat(4,1fr);gap:16px}
  .h-lv{padding:24px;border-radius:28px}
  .h-lv b{font-size:32px}
  .h-lv span{font-size:15px}
  .h-quiz{flex-direction:row;align-items:center;justify-content:space-between;padding:96px 80px;gap:48px}
  .h-quiz h2{font-size:104px}
  .h-quiz p{font-size:19px}
  .h-quiz .r{display:flex;flex-direction:column;align-items:flex-end}
  .h-quiz .steps{justify-content:flex-end;max-width:400px}
  .h-car{margin:0 -80px;padding:0 80px;scroll-padding:0 80px}
  .h-track{gap:16px}
  .h-track .p-card{width:290px}
  .h-track .p-rc{width:360px}
  .h-track::after{width:64px}
  .h-wg{grid-template-columns:1fr 1fr;gap:16px}
  .h-wt{aspect-ratio:4/5;border-radius:32px}
  .h-wt span{font-size:88px;left:36px;bottom:32px}
  .h-pers{grid-template-columns:1.1fr 1fr;margin-top:16px;border-radius:32px;min-height:520px}
  .h-pers .tx{padding:64px;justify-content:center;gap:18px}
  .h-pers h3{font-size:84px}
  .h-pers p{font-size:19px}
  .h-pers .vis{aspect-ratio:auto}
  .h-pers .tag{font-size:18px;right:32px;top:32px;padding:10px 16px}
  .h-team{padding:112px 80px}
  .h-tg{grid-template-columns:1.45fr 1fr;gap:16px}
  .h-feat{aspect-ratio:auto;min-height:640px;border-radius:32px}
  .h-feat::after{background:linear-gradient(90deg,rgba(0,0,0,.7),rgba(0,0,0,0) 60%)}
  .h-feat img{object-position:70% 40%}
  .h-feat .tx{top:0;bottom:0;right:auto;width:52%;justify-content:center;padding:0 0 0 24px}
  .h-feat .big{font-size:180px}
  .h-feat b{font-size:40px}
  .h-ath{justify-content:space-between}
  .h-ath a{flex:1;border-radius:24px}
  .h-serv{padding:120px 80px}
  .h-serv .h-tt{flex-direction:row;align-items:flex-end;margin-bottom:48px}
  .h-serv .h-tt h2{font-size:120px}
  .h-serv .h-tt .lead{font-size:20px;padding-bottom:12px}
  .h-sg{grid-template-columns:1.3fr 1fr 1fr;grid-template-rows:300px 300px;gap:16px}
  .h-sg a{min-height:0;border-radius:32px}
  .h-sg .s1{grid-row:span 2}
  .h-sg .s2{grid-column:span 2}
  .h-sg .tx{padding:36px}
  .h-sg b{font-size:52px}
  .h-sg .s1 b{font-size:72px}
  .h-sg .tx>span{font-size:17px}
  .h-club{margin:112px 80px 0;flex-direction:row;align-items:center;justify-content:space-between;padding:72px 72px;border-radius:40px}
  .h-club::before{font-size:420px;right:-30px;bottom:-110px}
  .h-club h2{font-size:112px}
  .h-club p{font-size:19px}
  .h-club .r{flex-direction:column;align-items:flex-end}
  .h-club .pr{font-size:56px}
  .h-near{grid-template-columns:1fr 1fr;gap:16px}
  .h-near a{min-height:340px;padding:44px;border-radius:32px}
  .h-near b{font-size:56px}
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
t91Menu(screen);t91Mega(screen);t91Toast(screen);
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
out=S.link_fix(out)
open('T91_mockup_homepage.html','w').write(out); print('home built',len(out))
