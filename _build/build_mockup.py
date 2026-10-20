import sys,os
os.chdir(sys.argv[1])
src=open('T91_presentazione_nuovo_sito.html').read()
head=src[:src.index('</head>')].replace('<title>Il nuovo T91</title>','<title>T91 · Pagina prodotto</title>')
svg=src[src.index('<svg width="0"'):src.index('</svg>',src.index('<svg width="0"'))+6]
tpls=src[src.index('<template id="tpl-pdp">'):src.index('<script>')]
js=src[src.index('<script>'):src.index('</script>')]
cut=js.index('tick();setInterval(tick,1000);')+len('tick();setInterval(tick,1000);')
js=js[:cut]+"\n})();\n"
out=head+'<style>html,body{height:100%;overflow:hidden}.screen{position:fixed!important;inset:0;width:100%;height:100%}</style>\n</head>\n<body>\n'+svg+'\n<div class="screen" data-screen><div class="scroller"></div></div>\n'+tpls+js+'</script>\n</body>\n</html>\n'
out=out.replace('href="#" data-link="home"','href="T91_mockup_homepage.html" data-link="home"')
open('T91_mockup_pagina_prodotto.html','w').write(out); print('built',len(out))
