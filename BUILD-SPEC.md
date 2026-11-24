# BUILD-SPEC â€” Curso AI FILMMAKING (formato ARCKHÉ AI)

> Contrato compartilhado para construÃ§Ã£o paralela das trilhas. **Leia tambÃ©m**
> `/home/nmaldaner/.claude/skills/formato-curso/references/MASTER_COMPLETO.md` e
> `SVG-FUTURISTA.md` (regras de formato + biblioteca de diagramas). Use os arquivos
> **`curso/trilha1/index.html`** e **`curso/trilha1/modulo-1-1.html`** como REFERÃŠNCIA-OURO
> (copie nav, `<style>`, scripts, estrutura â€” troque sÃ³ a cor e o conteÃºdo).

## Identidade
- **Curso:** AI FILMMAKING â€” Do Conceito ao Filme Final
- **Emoji:** ðŸŽ¬
- **Repo / Pages:** `https://linnoff88-dev.github.io/
- **Estrutura:** 7 trilhas (= blocos), 31 mÃ³dulos no roadmap (= liÃ§Ãµes). ConteÃºdo real escrito p/ ~22; restantes entram como cards "EM CONSTRUÃ‡ÃƒO".

## Mapa de cores das 7 trilhas

| T | Nome trilha | Cor ARCKHÉ | text / bg / border | Light-mode acento | SVG primÃ¡rio / forte / fill |
|---|-------------|-----------|--------------------|-------------------|------------------------------|
| 1 | Fundamentos do CARCKHÉ | amber | `text-amber-400` `bg-amber-500/20` `border-amber-500/30` `from-amber-900/30` | `#92400e` rgb `217,119,6` | `#fbbf24` / `#f59e0b` / `#1f1604` |
| 2 | PrÃ©-ProduÃ§Ã£o e Roteiro | orange | `text-orange-400` `bg-orange-500/20` `border-orange-500/30` `from-orange-900/30` | `#c2410c` rgb `234,88,12` | `#fb923c` / `#f97316` / `#241405` |
| 3 | AtuaÃ§Ã£o e DireÃ§Ã£o | rose | `text-rose-400` `bg-rose-500/20` `border-rose-500/30` `from-rose-900/30` | `#9f1239` rgb `225,29,72` | `#fb7185` / `#f43f5e` / `#2a0f16` |
| 4 | CARCKHÉtografia e Visual | blue | `text-blue-400` `bg-blue-500/20` `border-blue-500/30` `from-blue-900/30` | `#2563eb` rgb `37,99,235` | `#60a5fa` / `#3b82f6` / `#0e1622` |
| 5 | IA Visual e GeraÃ§Ã£o | teal | `text-teal-400` `bg-teal-500/20` `border-teal-500/30` `from-teal-900/30` | `#0d9488` rgb `13,148,136` | `#2dd4bf` / `#14b8a6` / `#0c1f1c` |
| 6 | Som, EdiÃ§Ã£o e PÃ³s-ProduÃ§Ã£o | emerald | `text-emerald-400` `bg-emerald-500/20` `border-emerald-500/30` `from-emerald-900/30` | `#059669` rgb `5,150,105` | `#34d399` / `#10b981` / `#0e2018` |
| 7 | ProduÃ§Ã£o e Carreira | purple | `text-purple-400` `bg-purple-500/20` `border-purple-500/30` `from-purple-900/30` | `#7c3aed` rgb `124,58,237` | `#c084fc` / `#a855f7` / `#1a1230` |

Cor secundÃ¡ria dos SVGs = ciano `#38bdf8` (sempre). BotÃµes "Ver Completo"/CTA usam `bg-<cor>-600 hover:bg-<cor>-500`.

## NAV global (IDÃŠNTICO em todas as pÃ¡ginas, sÃ³ muda o caminho e a trilha ativa)

7 botÃµes de trilha. **Mobile** = `T1`..`T7`; **desktop** = label curto:
`Fundamentos Â· PrÃ©-ProduÃ§Ã£o Â· AtuaÃ§Ã£o Â· CARCKHÉtografia Â· IA Visual Â· PÃ³s-ProduÃ§Ã£o Â· Carreira`.

Caminhos relativos:
- **Landing `index.html`:** logo â†’ `index.html`; trilha N â†’ `curso/trilhaN/index.html`.
- **Trilha index / mÃ³dulo (`curso/trilhaN/...`):** logo â†’ `../../index.html`; prÃ³pria trilha â†’ `index.html`; trilha M â†’ `../trilhaM/index.html`.

A trilha ATIVA: `text-<cor>-400 bg-<cor>-500/10`. Inativas: `text-neutral-400 hover:text-<corM>-400 hover:bg-<corM>-500/10 transition-colors`.

**`<style>` light-mode:** como cada pÃ¡gina vÃª 7 cores no nav, inclua no bloco light-mode os overrides de **todas as 7 cores de acento** (use a tabela acima) â€” igual ao bloco da landing descrito no MASTER Sec.1.5. A cor PRINCIPAL da pÃ¡gina (prÃ³pria trilha) tambÃ©m precisa dos overrides `bg/border /20 /10 /30`. Adicione sempre as 2 regras de borda dark (`#374151`) e a regra `html:not(.dark) svg[role="img"]{filter:saturate(.82) brightness(.96)}`.

## ConteÃºdo por mÃ³dulo (FONTE = arquivos em `doc/`)

Cada mÃ³dulo real: **6â€“8 tÃ³picos**, **500â€“800 linhas**, **â‰¥1 SVG inline** (cor da trilha + ciano), VARIEDADE de componentes (â‰¥2 grids âœ“/âœ—, â‰¥1 timeline, â‰¥2 tip box, code/mono box quando Ãºtil â€” ex.: YAML, prompts), e termina com **Resumo do MÃ³dulo** + nav p/ prÃ³ximo. Reaproveite os **prompts e exemplos reais** do material (nÃ£o invente exemplos genÃ©ricos). Toda pÃ¡gina de mÃ³dulo inclui um box "ðŸ“ Tarefa" com o exercÃ­cio do material-fonte. Tom: direto, prÃ¡tico, confiante (PT-BR).

### Trilha 1 â€” Fundamentos do CARCKHÉ (amber) Â· fonte `doc/bloco1.md` (+ `bloco3.md` Â§1-4)
- **1-1 A Estrutura do Diretor** â€” IA executa direÃ§Ã£o, nÃ£o cria intenÃ§Ã£o; o conceito de Ã‚ncora (filme=personagem, anÃºncio=produto, clipe=ritmo); hierarquia e lÃ³gica de cÃ¢mera; as 4 perguntas (por que Ã¢ngulo/movimento/duraÃ§Ã£o/luz); o conjunto de ferramentas. *(REFERÃŠNCIA-OURO â€” jÃ¡ construÃ­do)*
- **1-2 Controle Espacial & Linguagem de CÃ¢mera** â€” movimentos (dolly in, tracking, orbit, pan/tilt); distÃ¢ncia/enquadramento (close/mÃ©dio/aberto); profundidade e paralaxe; estilo (steadycam/handheld/slow-mo); estrutura de prompt `sujeito + ambiente + movimento + estilo`; erro comum (movimentos demais). Img: `ex-samurai-bridge`.
- **1-3 O Que Torna Algo CARCKHÉtogrÃ¡fico** â€” clareza + controle; Ã¢ncora de atenÃ§Ã£o; espaÃ§o negativo; composiÃ§Ã£o (simetria, regra dos terÃ§os, Ã¢ngulo holandÃªs); paleta consistente; checklist final do diretor.

### Trilha 2 â€” PrÃ©-ProduÃ§Ã£o e Roteiro (orange) Â· fonte `doc/bloco1.md` (Aula 2) + `doc/bloco3.md` (Aula 7 + PROMPTS)
- **2-1 Do Roteiro Ã  Cena: o Pipeline** â€” fluxo Roteiroâ†’Storyboardâ†’Personagemâ†’Figurinoâ†’Ambienteâ†’Lista de Planosâ†’Frames; anÃ¡lise do roteiro (o que o pÃºblico deve sentir); 7 etapas detalhadas. Img: `ex-samurai-bridge`.
- **2-2 Storyboard Estruturado** â€” Freepik/Magnific Spaces, fluxo por nÃ³s; esboÃ§oâ†’render cARCKHÉtogrÃ¡fico; lÃ³gica de direÃ§Ã£o plano a plano; arco narrativo (EspaÃ§oâ†’Personagemâ†’AÃ§Ã£oâ†’Movimentoâ†’LiberaÃ§Ã£o); uso de `@referÃªncias`.
- **2-3 Personagem, Figurino, Ambiente & Lista de Planos** â€” com os **PROMPTS COMPLETOS reais** (roteiro 6 planos pÃ³s-apocalÃ­ptico, ficha de personagem, esboÃ§o grade 2x3, storyboard renderizado com travas, lista de planos). Use mono/code boxes para os prompts. Imgs: `ex-postapoc-wide`, `ex-postapoc-handle`.

### Trilha 3 â€” AtuaÃ§Ã£o e DireÃ§Ã£o (rose) Â· fonte `doc/bloco6.md`
- **3-1 DiÃ¡logo e AtuaÃ§Ã£o: EmoÃ§Ã£o por Baixo das Palavras** â€” subtexto, planos de reaÃ§Ã£o, conflito, silÃªncio, atuaÃ§Ã£o, enquadramento (MÃ³dulo 5). Img: `ex-dialogue-ots`.
- **3-2 Performance de Personagem com IA** â€” 6 mecÃ¢nicas (motivaÃ§Ã£o antes do movimento, microatuaÃ§Ã£o, timing emocional, linguagem corporal, performance dos olhos, ritmo) + fÃ³rmulas de ouro (Aula 17).
- **3-3 Estrutura de Cena de DiÃ¡logo & Planos Emocionais** â€” 7 mecÃ¢nicas de diÃ¡logo (Aula 19) + 6 mecÃ¢nicas de planos emocionais (close-up, espaÃ§o negativo, push-in, distÃ¢ncia, OTS, POV â€” Aula 18).

### Trilha 4 â€” CARCKHÉtografia e Visual (blue) Â· fonte `doc/bloco2.md` + `doc/bloco4.md` (Aula 12) + `doc/bloco3.md` (Aula 9)
- **4-1 ComposiÃ§Ã£o para CARCKHÉ** â€” pensamento visual (formato=cÃ¢mera, ambiente=histÃ³ria, luz=emoÃ§Ã£o, personagem=contradiÃ§Ã£o, cena=sequÃªncia); tÃ©cnicas (diagonal, linhas de conduÃ§Ã£o, terÃ§os, espaÃ§o negativo, simetria, macro, escala, contraste); composiÃ§Ã£o como sequÃªncia no tempo.
- **4-2 IluminaÃ§Ã£o e Atmosfera** â€” negative fill, edge contrast, suavidade pela distÃ¢ncia, luz motivada, regra 80/20, camadas de atmosfera, contraste de cor, luz dinÃ¢mica. Img: `ex-lighting-rim`.
- **4-3 Profundidade e Estrutura Espacial** â€” regra das 3 camadas, separaÃ§Ã£o, profundidade de campo, escolha de lente (grande-angular vs tele), paralaxe; profundidade = emoÃ§Ã£o. Img: `ex-depth-layers`.
- **4-4 Tamanhos de Plano & Movimento de CÃ¢mera** â€” establishingâ†’ECU (quando/por quÃª); 25+ movimentos (dolly vs zoom vs dolly zoom, truck, pan, tilt, crane, orbit, arc, whip pan, rack focus, handheld, dutch); guia prÃ¡tico intenÃ§Ã£oâ†’movimento. Img: `ex-camera-move`.

### Trilha 5 â€” IA Visual e GeraÃ§Ã£o (teal) Â· fonte `doc/bloco3.md` + `doc/bloco4.md` (Aula 13) + `doc/bloco5.md`
- **5-1 Pipeline de Ferramentas de IA** â€” funÃ§Ãµes de Freepik/Seedance/Kling/Luma/Runway; controle de atenÃ§Ã£o, composiÃ§Ã£o, conexÃ£o de planos; checklist final.
- **5-2 GeraÃ§Ã£o de Movimento no Seedance** â€” ForÃ§a+Tempo+Peso; sequÃªncia (grandeâ†’pequenoâ†’partÃ­culas); cÃ¢mera; reaÃ§Ã£o humana (mostrar, nÃ£o nomear); detalhes mensurÃ¡veis. Img: `ex-camera-move`.
- **5-3 Controle por YAML no Seedance 2** â€” por que YAML; trava de identidade (`base: matching reference @image1...`); blocos cÃ¢mera/aÃ§Ã£o/iluminaÃ§Ã£o/transiÃ§Ãµes; regras (uma funÃ§Ã£o por campo, blocos de tempo `00_02`); transiÃ§Ãµes (cut, whip pan, smash, match on action). Use **code box YAML**.
- **5-4 Efeitos Visuais PrÃ¡ticos** â€” LED volume, fogo prÃ¡tico, suspensÃ£o por cabos, chuva prÃ¡tica, miniaturas, hÃ­brido fÃ­sico+digital; YAML p/ VFX; blueprint Luzâ†’Texturaâ†’Movimentoâ†’Atmosferaâ†’EmoÃ§Ã£o. Img: `ex-particles`.
- **5-5 CÃ¢mera Lenta & Sistemas de PartÃ­culas** â€” overcranking (120/240fpsâ†’24fps), rÃ¡pidoâ†’lentoâ†’rÃ¡pido, microatuaÃ§Ã£o, continuidade de luz; partÃ­culas para esconder artefatos de morphing (oclusÃ£o transicional, integraÃ§Ã£o volumÃ©trica, suavizaÃ§Ã£o temporal, camadas cinÃ©ticas). Imgs: `ex-slowmo-action`, `ex-particles`.
- **5-6 IntegraÃ§Ã£o com Luma e Runway** â€” Uni-1 (inteligÃªncia unificada, conversa em vez de prompt); fluxo: ficha de personagem â†’ dirigir plano â†’ animar; comparar modelos (Kling vs Ray); dirigir o parceiro criativo.

### Trilha 6 â€” Som, EdiÃ§Ã£o e PÃ³s-ProduÃ§Ã£o (emerald) Â· fonte `doc/bloco4.md` (Aula 11) + `doc/bloco5.md` (Aula 16)
- **6-1 EdiÃ§Ã£o CARCKHÉtogrÃ¡fica: Tipos de Corte** â€” jump, match, cut on action, cross cutting, double, fast cutting; "ediÃ§Ã£o Ã© a relaÃ§Ã£o entre planos"; gerarâ†’assistirâ†’analisar o corte. *(REAL)*
- **6-2 Cenas de AÃ§Ã£o: 5 MecÃ¢nicas** â€” transformaÃ§Ã£o voadora, perseguiÃ§Ã£o urbana, capotamento, fuga com parkour, resgate na ponte; fÃ³rmula Risco+Movimento+Quase Fracasso. Img: `ex-slowmo-action`. *(REAL)*
- **EM CONSTRUÃ‡ÃƒO (sÃ³ cards, sem pÃ¡gina):** 6-3 Design de Som & Foley Â· 6-4 Trilha & MÃºsica Â· 6-5 Color Grading Â· 6-6 Mixagem & MasterizaÃ§Ã£o

### Trilha 7 â€” ProduÃ§Ã£o e Carreira (purple) Â· fonte `doc/bloco7(1).md`
- **7-1 Narrativa Visual: Framework de 5 Cenas** â€” Setupâ†’Conflitoâ†’Escaladaâ†’EmoÃ§Ã£oâ†’ResoluÃ§Ã£o (o relojoeiro e o pÃ¡ssaro mecÃ¢nico); prompts Kling reais por cena; checklist do diretor (relevÃ¢ncia 0.5â€“0.6, frases de cÃ¢mera). Img: `ex-watchmaker`. *(REAL)*
- **EM CONSTRUÃ‡ÃƒO (sÃ³ cards):** 7-2 ConstruÃ§Ã£o de PortfÃ³lio Â· 7-3 Pitch & ApresentaÃ§Ã£o Â· 7-4 MonetizaÃ§Ã£o Â· 7-5 Cliente & Mercado Â· 7-6 Carreira em IA Filmmaking

## Imagens de exemplo (em `assets/`, jÃ¡ geradas)
`ex-samurai-bridge` `ex-postapoc-wide` `ex-postapoc-handle` `ex-lighting-rim` `ex-depth-layers` `ex-particles` `ex-slowmo-action` `ex-watchmaker` `ex-dialogue-ots` `ex-camera-move` Â· capas: `cover-wide` `cover-square`.

**PadrÃ£o de `<img>` seguro** (caminho a partir de `curso/trilhaN/`, com legenda e auto-hide se faltar):
```html
<figure class="mb-6 rounded-xl overflow-hidden border border-dark-600">
  <img src="../../assets/ex-NOME.png" alt="DESCRIÃ‡ÃƒO" loading="lazy" class="w-full h-auto"
       onerror="this.closest('figure').style.display='none'">
  <figcaption class="text-xs text-neutral-500 px-4 py-2 bg-dark-800">Exemplo cARCKHÉtogrÃ¡fico â€” gerado com IA (flux2-klein) Â· ilustrativo</figcaption>
</figure>
```

## PadrÃ£o "EM CONSTRUÃ‡ÃƒO" (trilhas 6 e 7)
No index da trilha, apÃ³s os cards reais, cards mudos:
```html
<div class="bg-dark-800/60 rounded-xl border border-dashed border-dark-600 p-6 mb-6 opacity-70">
  <div class="flex items-center justify-between mb-2">
    <span class="text-neutral-500 font-bold">6.3</span>
    <span class="text-xs px-2 py-0.5 rounded-full bg-primary/10 text-primary border border-primary/30">EM CONSTRUÃ‡ÃƒO</span>
  </div>
  <h3 class="text-2xl font-bold mb-2 text-neutral-400">ðŸ”Š Design de Som & Foley</h3>
  <p class="text-neutral-500 text-sm">ConteÃºdo em produÃ§Ã£o â€” disponÃ­vel em breve.</p>
</div>
```
No "Mapa da trilha": mÃ³dulos em construÃ§Ã£o entram como `<div>` (nÃ£o `<a>`), sem Ã¢ncora, com o badge. NÃ£o criar `modulo-X-Y.html` para eles.

## Stats por trilha (para header e landing)
T1: 3 mÃ³d Â· ~20 tÃ³p Â· ~2h Â· BÃ¡sico â€” T2: 3 Â· ~21 Â· ~2.5h Â· BÃ¡sico â€” T3: 3 Â· ~20 Â· ~2h Â· Inter. â€” T4: 4 Â· ~28 Â· ~3h Â· Inter. â€” T5: 6 Â· ~40 Â· ~4.5h Â· AvanÃ§ado â€” T6: 6 (2 prontos) Â· ~14 Â· ~2h Â· Inter. â€” T7: 6 (1 pronto) Â· ~8 Â· ~1h Â· AvanÃ§ado.
