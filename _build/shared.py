CDN='https://cdn.shopify.com/s/files/1/0826/8523/1445/files/'
LOGO='https://t91padel.com/cdn/shop/files/Logo_T91_Nero.svg?v=1698236978'
TOPBAR='''  <div class="p-top"><div class="l"><a href="#">Outlet</a><a href="#">Mystery Box</a><a href="#">Buoni regalo</a><a href="#">Trova T91 vicino a te</a></div><div class="r"><a class="pro" href="#">Sei un centro o un maestro? <u>Scopri il programma →</u></a><span class="lang"><b>IT</b> · EN</span></div></div>
'''
def HEAD(active=''):
    ON=' class="on"'
    nav=''.join('<a'+(ON if n==active else '')+' href="#">'+n+'</a>' for n in ['Racchette','Abbigliamento','Accessori','Team','Servizi','Blog'])
    return f'''  <header class="p-head" data-n="menu">
    <button class="p-burger js-menu" aria-label="Menu"><svg class="i"><use href="#i-burger"/></svg></button>
    <a class="p-logo" href="#" data-link="home"><img src="{LOGO}" alt="T91" onerror="this.outerHTML='<span class=&quot;fb&quot;>T91</span>'"></a>
    <nav class="p-nav">{nav}<a class="club" href="#">T91 Club</a></nav>
    <div class="p-icons"><svg class="i"><use href="#i-search"/></svg><svg class="i"><use href="#i-user"/></svg><button class="p-cart js-open" aria-label="Carrello"><svg class="i"><use href="#i-bag"/></svg><em class="js-count">0</em></button></div>
  </header>
'''
FOOTER='''  <footer class="p-foot">
    <div><div class="p-quizbox"><b>Trova la tua racchetta.</b><span>Fai il test in 60 secondi e ricevi il risultato su WhatsApp.</span><div class="in"><i>Il tuo numero WhatsApp</i><em>Inizia</em></div></div></div>
    <div>
      <div class="p-fcols">
        <div><h5>Shop</h5><ul><li>Racchette</li><li>Abbigliamento</li><li>Accessori</li><li>Outlet</li><li>Mystery Box</li></ul></div>
        <div><h5>Team</h5><ul><li>Team Pro</li><li>Ambassador</li><li>Team Under</li><li>Blog</li></ul></div>
        <div><h5>Servizi</h5><ul><li>T91 Care</li><li>T91 Repair</li><li>Protezione</li><li>Personalizza</li><li>Click &amp; Collect</li></ul></div>
        <div><h5>T91</h5><ul><li>Chi siamo</li><li>Centri e maestri</li><li>Trova T91 vicino a te</li><li>Assistenza</li><li>Spedizioni e resi</li></ul></div>
      </div>
      <div class="p-pay"><span>VISA</span><span>MASTERCARD</span><span>AMEX</span><span>PAYPAL</span><span>APPLE PAY</span><span class="k">Klarna.</span></div>
    </div>
    <div class="p-legal bt">T91 Padel · Osio Sotto (BG) · From players to players · <b>IT</b> · EN</div>
  </footer>
'''
MENU=f'''<div class="p-mm">
  <div class="mm-h"><a href="#" data-link="home"><img src="{LOGO}" alt="T91"></a><button class="x js-mclose" aria-label="Chiudi il menu"><svg class="i"><use href="#i-x"/></svg></button></div>
  <div class="mm-b">
    <div class="pane l1">
      <div class="srch"><svg class="i"><use href="#i-search"/></svg>Cerca racchette, abbigliamento…</div>
      <ul class="m-list">
        <li><button data-go="racchette">Racchette<svg class="i"><use href="#i-r"/></svg></button></li>
        <li><button data-go="abbigliamento">Abbigliamento<svg class="i"><use href="#i-r"/></svg></button></li>
        <li><button data-go="accessori">Accessori<svg class="i"><use href="#i-r"/></svg></button></li>
        <li><button data-go="team">Team<svg class="i"><use href="#i-r"/></svg></button></li>
        <li><button data-go="servizi">Servizi<svg class="i"><use href="#i-r"/></svg></button></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#"><span class="club">T91 Club</span></a></li>
      </ul>
      <a class="m-quiz" href="#"><span class="ic">?</span><span><b>Trova la tua racchetta</b><span>4 domande, risultato su WhatsApp</span></span></a>
      <div class="m-sec">Offerte</div>
      <ul class="m-small"><li><a href="#">Outlet</a></li><li><a href="#">Mystery Box</a></li><li><a href="#">Buoni regalo</a></li><li><a href="#">Trova T91 vicino a te</a></li></ul>
      <a class="m-pro" href="#"><span><b>Sei un centro o un maestro?</b><span>Scopri il programma T91</span></span><em>→</em></a>
      <div class="m-foot"><a href="#"><svg class="i"><use href="#i-user"/></svg>Accedi</a><a class="wa" href="#"><i></i>Assistenza WhatsApp</a><a class="lang" href="#"><b>IT</b><span>EN</span></a></div>
    </div>
    <div class="pane l2" data-pane="racchette">
      <button class="back js-mback"><svg class="i"><use href="#i-l"/></svg>Menu</button>
      <h4>Racchette</h4>
      <a class="all" href="#"><span><b>Vedi tutte le racchette</b><span>14 modelli, con i filtri</span></span><em>→</em></a>
      <div class="m-sec" style="margin-top:0">Per livello</div>
      <div class="chips"><a href="#">Principianti</a><a href="#">Intermedi</a><a href="#">Avanzati</a><a href="#">Pro</a></div>
      <div class="m-sec">Per stile di gioco</div>
      <div class="chips"><a href="#">Potenza</a><a href="#">Controllo</a><a href="#">Polivalenti</a></div>
      <div class="m-sec">Collezioni</div>
      <div class="cols2"><a class="coll" href="#"><img src="https://t91padel.com/cdn/shop/files/Racchetta_HOLO_arancione_in_carbonio_cell.webp?v=1791307714&width=400" alt=""><span>Holo</span></a><a class="coll" href="#"><img src="https://t91padel.com/cdn/shop/files/IRIART_3_COVER_CELL_65d0846d-c225-4464-8165-448e3490274c.webp?v=1791215341&width=400" alt=""><span>Signature Pro</span></a></div>
      <div class="cards2"><a class="v" href="#"><small>4 domande</small>Trova la tua racchetta</a><a class="f" href="#"><small>Fianco a fianco</small>Confronta le racchette</a></div>
    </div>
    <div class="pane l2" data-pane="abbigliamento">
      <button class="back js-mback"><svg class="i"><use href="#i-l"/></svg>Menu</button>
      <h4>Abbigliamento</h4>
      <a class="all" href="#"><span><b>Vedi tutto l'abbigliamento</b><span>Con i filtri per capo, taglia e colore</span></span><em>→</em></a>
      <ul class="sub-list"><li><a href="#">Uomo<span>T-shirt, polo, felpe…</span></a></li><li><a href="#">Donna<span>Top, gonne, leggings…</span></a></li><li><a href="#">Personalizzabili<span>Con il tuo nome</span></a></li></ul>
    </div>
    <div class="pane l2" data-pane="accessori">
      <button class="back js-mback"><svg class="i"><use href="#i-l"/></svg>Menu</button>
      <h4>Accessori</h4>
      <a class="all" href="#"><span><b>Vedi tutti gli accessori</b><span>Con il filtro per tipo</span></span><em>→</em></a>
      <div class="chips"><a href="#">Borse e zaini</a><a href="#">Overgrip e copritesta</a><a href="#">Palline</a><a href="#">Calze</a><a href="#">Cappellini</a><a href="#">Polsini</a><a href="#">Manicotto</a><a href="#">Ciabatte</a><a href="#">Teli</a></div>
    </div>
    <div class="pane l2" data-pane="team">
      <button class="back js-mback"><svg class="i"><use href="#i-l"/></svg>Menu</button>
      <h4>Team</h4>
      <ul class="sub-list"><li><a href="#">Team Pro<span>I nostri atleti</span></a></li><li><a href="#">Ambassador<span>Chi rappresenta T91</span></a></li><li><a href="#">Team Under<span>I giovani talenti</span></a></li></ul>
    </div>
    <div class="pane l2" data-pane="servizi">
      <button class="back js-mback"><svg class="i"><use href="#i-l"/></svg>Menu</button>
      <h4>Servizi</h4>
      <ul class="sub-list"><li><a href="#">T91 Care<span>Ritiro dell'usato</span></a></li><li><a href="#">T91 Repair<span>Riparazioni</span></a></li><li><a href="#">Protezione racchetta<span>Garanzia estesa</span></a></li><li><a href="#">Personalizzazione<span>Anche un pezzo</span></a></li><li><a href="#">Click &amp; Collect<span>Ritiro in negozio</span></a></li></ul>
    </div>
  </div>
</div>
'''
CSS='''
/* === barra superiore desktop === */
.p-top{display:none}
/* === menu mobile === */
.p-mm{position:absolute;inset:0;z-index:60;background:#fff;display:flex;flex-direction:column;transform:translateY(-102%);transition:transform .35s cubic-bezier(.2,.8,.2,1);font-family:'Questrial',sans-serif;color:var(--ink)}
.p-mm.open{transform:none}
.p-mm .mm-h{height:64px;padding:0 14px;display:flex;align-items:center;border-bottom:1px solid var(--line);flex:none}
.p-mm .mm-h img{height:28px;width:auto}
.p-mm .x{margin-left:auto;width:40px;height:40px;border-radius:50%;background:var(--fog);display:grid;place-items:center}
.p-mm .x svg{width:18px;height:18px}
.p-mm .mm-b{position:relative;flex:1;overflow:hidden}
.p-mm .pane{position:absolute;inset:0;overflow-y:auto;scrollbar-width:none;padding:14px 18px 28px;transition:transform .32s cubic-bezier(.2,.8,.2,1),opacity .32s;background:#fff}
.p-mm .pane::-webkit-scrollbar{display:none}
.p-mm .pane.l1.away{transform:translateX(-30%);opacity:0;pointer-events:none}
.p-mm .pane.l2{transform:translateX(100%)}
.p-mm .pane.l2.in{transform:none}
.p-mm .srch{display:flex;align-items:center;gap:10px;background:var(--fog);border-radius:14px;padding:12px 14px;color:var(--mute);font-size:15px;margin-bottom:10px}
.p-mm .srch svg{width:18px;height:18px}
.p-mm .m-list{list-style:none}
.p-mm .m-list li{border-bottom:1px solid var(--line)}
.p-mm .m-list button,.p-mm .m-list a{width:100%;display:flex;align-items:center;justify-content:space-between;padding:15px 2px;font-size:23px;letter-spacing:-.02em;text-align:left;font-family:inherit}
.p-mm .m-list svg{width:20px;height:20px;color:#C7C7CC}
.p-mm .m-list .club{display:inline-flex;background:var(--volt);border-radius:980px;padding:4px 14px;font-size:19px}
.p-mm .m-quiz{display:flex;align-items:center;gap:14px;background:#000;color:#fff;border-radius:18px;padding:16px;margin:18px 0 14px}
.p-mm .m-quiz .ic{width:44px;height:44px;border-radius:12px;background:var(--volt);color:#000;display:grid;place-items:center;flex:none;font-size:20px}
.p-mm .m-quiz b{display:block;font-size:17px}
.p-mm .m-quiz span span{font-size:13px;color:#A1A1A6}
.p-mm .m-sec{font-size:12.5px;color:var(--mute);margin:20px 0 6px}
.p-mm .m-small{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.p-mm .m-small a{display:block;background:var(--fog);border-radius:14px;padding:13px 14px;font-size:15px}
.p-mm .m-pro{display:flex;align-items:center;justify-content:space-between;gap:10px;border:1px solid var(--line);border-radius:16px;padding:14px 16px;margin-top:14px;font-size:14.5px}
.p-mm .m-pro b{display:block;font-size:15.5px}
.p-mm .m-pro span span{font-size:13px;color:var(--mute)}
.p-mm .m-pro em{font-style:normal;width:34px;height:34px;border-radius:50%;background:#000;color:var(--volt);display:grid;place-items:center;flex:none}
.p-mm .m-foot{display:flex;gap:8px;margin-top:20px;flex-wrap:wrap}
.p-mm .m-foot a{display:inline-flex;align-items:center;gap:8px;font-size:14px;border:1px solid var(--line);border-radius:980px;padding:9px 14px}
.p-mm .m-foot svg{width:18px;height:18px}
.p-mm .m-foot .wa i{width:8px;height:8px;border-radius:50%;background:#34C759}
.p-mm .m-foot .lang span{color:var(--mute)}
.p-mm .back{display:inline-flex;align-items:center;gap:4px;font-size:15px;color:var(--mute);padding:4px 0 10px;font-family:inherit}
.p-mm .back svg{width:18px;height:18px}
.p-mm h4{font-weight:400;font-size:34px;letter-spacing:-.03em;line-height:1;margin-bottom:16px}
.p-mm .all{display:flex;align-items:center;justify-content:space-between;background:#000;color:#fff;border-radius:18px;padding:18px;margin-bottom:20px}
.p-mm .all b{display:block;font-size:19px}
.p-mm .all span span{font-size:13px;color:#A1A1A6}
.p-mm .all em{font-style:normal;color:var(--volt);font-size:20px}
.p-mm .chips{display:flex;flex-wrap:wrap;gap:8px}
.p-mm .chips a{border:1px solid var(--line);border-radius:980px;padding:9px 15px;font-size:15px}
.p-mm .cols2{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.p-mm .coll{border-radius:16px;overflow:hidden;position:relative;aspect-ratio:1/1.05;background:#111;color:#fff;display:flex;align-items:flex-end;padding:12px;font-size:15px}
.p-mm .coll img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.85}
.p-mm .coll span{position:relative}
.p-mm .cards2{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:8px}
.p-mm .cards2 a{border-radius:16px;padding:14px;min-height:96px;display:flex;flex-direction:column;justify-content:flex-end;font-size:15px}
.p-mm .cards2 a small{font-size:12px;opacity:.7}
.p-mm .cards2 .v{background:var(--volt)}
.p-mm .cards2 .f{background:var(--fog)}
.p-mm .sub-list{list-style:none}
.p-mm .sub-list a{display:flex;justify-content:space-between;align-items:center;padding:14px 2px;border-bottom:1px solid var(--line);font-size:18px}
.p-mm .sub-list a span{font-size:13px;color:var(--mute)}
/* toast pagine non ancora disegnate */
.p-toast{position:absolute;left:50%;bottom:90px;transform:translate(-50%,20px);background:#000;color:#fff;font-family:'Questrial',sans-serif;font-size:13.5px;padding:11px 18px;border-radius:980px;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s;z-index:70;white-space:nowrap}
.p-toast.show{opacity:1;transform:translate(-50%,0)}
@container dev (min-width: 900px){
  .p-bar{display:none!important}
  .p-top{display:flex;justify-content:space-between;align-items:center;gap:16px;background:#000;color:#D2D2D7;font-size:12.5px;padding:0 40px;height:36px}
  .p-top .l{display:flex;gap:22px}
  .p-top .r{display:flex;gap:22px;align-items:center}
  .p-top a:hover{color:#fff}
  .p-top .pro{color:#fff}
  .p-top .pro u{color:var(--volt);text-decoration:none}
  .p-top .lang{color:#8E8E93}
  .p-top .lang b{color:#fff}
  .p-toast{bottom:40px}
}
'''
JS_MENU=r'''
function t91Menu(root,toastHost){
  const mm=root.querySelector('.p-mm'); if(!mm) return;
  const $$=s=>[...mm.querySelectorAll(s)], l1=mm.querySelector('.pane.l1');
  const back=()=>{$$('.pane.l2').forEach(p=>p.classList.remove('in'));l1.classList.remove('away');};
  root.querySelectorAll('.js-menu').forEach(b=>b.onclick=()=>mm.classList.add('open'));
  mm.querySelector('.js-mclose').onclick=()=>{mm.classList.remove('open');setTimeout(back,350);};
  $$('[data-go]').forEach(b=>b.onclick=()=>{$$('.pane.l2').forEach(p=>p.classList.toggle('in',p.dataset.pane===b.dataset.go));l1.classList.add('away');});
  $$('.js-mback').forEach(b=>b.onclick=back);
}
function t91Toast(host){
  let t=host.querySelector('.p-toast'); if(!t){t=document.createElement('div');t.className='p-toast';t.textContent='Questa pagina la disegniamo nei prossimi passi';host.appendChild(t);}
  host.addEventListener('click',e=>{const a=e.target.closest('a');if(!a||a.getAttribute('href')!=='#')return;e.preventDefault();if(a.dataset.link)return;t.classList.add('show');clearTimeout(t._h);t._h=setTimeout(()=>t.classList.remove('show'),1800);});
}
'''
