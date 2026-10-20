# Come rigenerare i mockup

La pagina prodotto vive dentro `T91_presentazione_nuovo_sito.html` (template `tpl-pdp`).
Dopo una modifica alla presentazione, rigenera i mockup a tutto schermo:

```
python3 _build/build_mockup.py .
python3 _build/build_home.py .
python3 _build/build_racchette.py .
```

- `build_mockup.py` → `T91_mockup_pagina_prodotto.html`
- `build_home.py` → `T91_mockup_homepage.html` (contenuti della homepage nel file stesso)
- `build_racchette.py` → `T91_mockup_racchette.html`
- `shared.py` → barra superiore, header, menu mobile e footer comuni
