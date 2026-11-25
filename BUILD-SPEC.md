# BUILD-SPEC ê¢â¬â Curso AI FILMMAKING (formato ARCKHê AI)

> Contrato compartilhado para construêÂ§êÂ£o paralela das trilhas. **Leia tambêÂ©m**
> `/home/nmaldaner/.claude/skills/formato-curso/references/MASTER_COMPLETO.md` e
> `SVG-FUTURISTA.md` (regras de formato + biblioteca de diagramas). Use os arquivos
> **`curso/trilha1/index.html`** e **`curso/trilha1/modulo-1-1.html`** como REFERêÅ NCIA-OURO
> (copie nav, `<style>`, scripts, estrutura ê¢â¬â troque sêÂ³ a cor e o conteêÂºdo).

## Identidade
- **Curso:** AI FILMMAKING ê¢â¬â Do Conceito ao Filme Final
- **Emoji:** ê°Å¸Å½Â¬
- **Repo / Pages:** `https://linnoff88-dev.github.io/
- **Estrutura:** 7 trilhas (= blocos), 31 mêÂ³dulos no roadmap (= liêÂ§êÂµes). ConteêÂºdo real escrito p/ ~22; restantes entram como cards "EM CONSTRUêâ¡êÆO".

## Mapa de cores das 7 trilhas

| T | Nome trilha | Cor ARCKHê | text / bg / border | Light-mode acento | SVG primêÂ¡rio / forte / fill |
|---|-------------|-----------|--------------------|-------------------|------------------------------|
| 1 | Fundamentos do CARCKHê | amber | `text-amber-400` `bg-amber-500/20` `border-amber-500/30` `from-amber-900/30` | `#92400e` rgb `217,119,6` | `#fbbf24` / `#f59e0b` / `#1f1604` |
| 2 | PrêÂ©-ProduêÂ§êÂ£o e Roteiro | orange | `text-orange-400` `bg-orange-500/20` `border-orange-500/30` `from-orange-900/30` | `#c2410c` rgb `234,88,12` | `#fb923c` / `#f97316` / `#241405` |
| 3 | AtuaêÂ§êÂ£o e DireêÂ§êÂ£o | rose | `text-rose-400` `bg-rose-500/20` `border-rose-500/30` `from-rose-900/30` | `#9f1239` rgb `225,29,72` | `#fb7185` / `#f43f5e` / `#2a0f16` |
| 4 | CARCKHêtografia e Visual | blue | `text-blue-400` `bg-blue-500/20` `border-blue-500/30` `from-blue-900/30` | `#2563eb` rgb `37,99,235` | `#60a5fa` / `#3b82f6` / `#0e1622` |
| 5 | IA Visual e GeraêÂ§êÂ£o | teal | `text-teal-400` `bg-teal-500/20` `border-teal-500/30` `from-teal-900/30` | `#0d9488` rgb `13,148,136` | `#2dd4bf` / `#14b8a6` / `#0c1f1c` |
| 6 | Som, EdiêÂ§êÂ£o e PêÂ³s-ProduêÂ§êÂ£o | emerald | `text-emerald-400` `bg-emerald-500/20` `border-emerald-500/30` `from-emerald-900/30` | `#059669` rgb `5,150,105` | `#34d399` / `#10b981` / `#0e2018` |
| 7 | ProduêÂ§êÂ£o e Carreira | purple | `text-purple-400` `bg-purple-500/20` `border-purple-500/30` `from-purple-900/30` | `#7c3aed` rgb `124,58,237` | `#c084fc` / `#a855f7` / `#1a1230` |

Cor secundêÂ¡ria dos SVGs = ciano `#38bdf8` (sempre). BotêÂµes "Ver Completo"/CTA usam `bg-<cor>-600 hover:bg-<cor>-500`.

## NAV global (IDêÅ NTICO em todas as pêÂ¡ginas, sêÂ³ muda o caminho e a trilha ativa)

7 botêÂµes de trilha. **Mobile** = `T1`..`T7`; **desktop** = label curto:
`Fundamentos êÂ· PrêÂ©-ProduêÂ§êÂ£o êÂ· AtuaêÂ§êÂ£o êÂ· CARCKHêtografia êÂ· IA Visual êÂ· PêÂ³s-ProduêÂ§êÂ£o êÂ· Carreira`.

Caminhos relativos:
- **Landing `index.html`:** logo ê¢â â `index.html`; trilha N ê¢â â `curso/trilhaN/index.html`.
- **Trilha index / mêÂ³dulo (`curso/trilhaN/...`):** logo ê¢â â `../../index.html`; prêÂ³pria trilha ê¢â â `index.html`; trilha M ê¢â â `../trilhaM/index.html`.

A trilha ATIVA: `text-<cor>-400 bg-<cor>-500/10`. Inativas: `text-neutral-400 hover:text-<corM>-400 hover:bg-<corM>-500/10 transition-colors`.

**`<style>` light-mode:** como cada pêÂ¡gina vêÂª 7 cores no nav, inclua no bloco light-mode os overrides de **todas as 7 cores de acento** (use a tabela acima) ê¢â¬â igual ao bloco da landing descrito no MASTER Sec.1.5. A cor PRINCIPAL da pêÂ¡gina (prêÂ³pria trilha) tambêÂ©m precisa dos overrides `bg/border /20 /10 /30`. Adicione sempre as 2 regras de borda dark (`#374151`) e a regra `html:not(.dark) svg[role="img"]{filter:saturate(.82) brightness(.96)}`.

## ConteêÂºdo por mêÂ³dulo (FONTE = arquivos em `doc/`)

Cada mêÂ³dulo real: **6ê¢â¬â8 têÂ³picos**, **500ê¢â¬â800 linhas**, **ê¢â°Â¥1 SVG inline** (cor da trilha + ciano), VARIEDADE de componentes (ê¢â°Â¥2 grids ê¢Åâ/ê¢Åâ, ê¢â°Â¥1 timeline, ê¢â°Â¥2 tip box, code/mono box quando êÂºtil ê¢â¬â ex.: YAML, prompts), e termina com **Resumo do MêÂ³dulo** + nav p/ prêÂ³ximo. Reaproveite os **prompts e exemplos reais** do material (nêÂ£o invente exemplos genêÂ©ricos). Toda pêÂ¡gina de mêÂ³dulo inclui um box "ê°Å¸âÂ Tarefa" com o exercêÂ­cio do material-fonte. Tom: direto, prêÂ¡tico, confiante (PT-BR).

### Trilha 1 ê¢â¬â Fundamentos do CARCKHê (amber) êÂ· fonte `doc/bloco1.md` (+ `bloco3.md` êÂ§1-4)
- **1-1 A Estrutura do Diretor** ê¢â¬â IA executa direêÂ§êÂ£o, nêÂ£o cria intenêÂ§êÂ£o; o conceito de êâncora (filme=personagem, anêÂºncio=produto, clipe=ritmo); hierarquia e lêÂ³gica de cêÂ¢mera; as 4 perguntas (por que êÂ¢ngulo/movimento/duraêÂ§êÂ£o/luz); o conjunto de ferramentas. *(REFERêÅ NCIA-OURO ê¢â¬â jêÂ¡ construêÂ­do)*
- **1-2 Controle Espacial & Linguagem de CêÂ¢mera** ê¢â¬â movimentos (dolly in, tracking, orbit, pan/tilt); distêÂ¢ncia/enquadramento (close/mêÂ©dio/aberto); profundidade e paralaxe; estilo (steadycam/handheld/slow-mo); estrutura de prompt `sujeito + ambiente + movimento + estilo`; erro comum (movimentos demais). Img: `ex-samurai-bridge`.
- **1-3 O Que Torna Algo CARCKHêtogrêÂ¡fico** ê¢â¬â clareza + controle; êÂ¢ncora de atenêÂ§êÂ£o; espaêÂ§o negativo; composiêÂ§êÂ£o (simetria, regra dos terêÂ§os, êÂ¢ngulo holandêÂªs); paleta consistente; checklist final do diretor.

### Trilha 2 ê¢â¬â PrêÂ©-ProduêÂ§êÂ£o e Roteiro (orange) êÂ· fonte `doc/bloco1.md` (Aula 2) + `doc/bloco3.md` (Aula 7 + PROMPTS)
- **2-1 Do Roteiro êÂ  Cena: o Pipeline** ê¢â¬â fluxo Roteiroê¢â âStoryboardê¢â âPersonagemê¢â âFigurinoê¢â âAmbienteê¢â âLista de Planosê¢â âFrames; anêÂ¡lise do roteiro (o que o pêÂºblico deve sentir); 7 etapas detalhadas. Img: `ex-samurai-bridge`.
- **2-2 Storyboard Estruturado** ê¢â¬â Freepik/Magnific Spaces, fluxo por nêÂ³s; esboêÂ§oê¢â ârender cARCKHêtogrêÂ¡fico; lêÂ³gica de direêÂ§êÂ£o plano a plano; arco narrativo (EspaêÂ§oê¢â âPersonagemê¢â âAêÂ§êÂ£oê¢â âMovimentoê¢â âLiberaêÂ§êÂ£o); uso de `@referêÂªncias`.
- **2-3 Personagem, Figurino, Ambiente & Lista de Planos** ê¢â¬â com os **PROMPTS COMPLETOS reais** (roteiro 6 planos pêÂ³s-apocalêÂ­ptico, ficha de personagem, esboêÂ§o grade 2x3, storyboard renderizado com travas, lista de planos). Use mono/code boxes para os prompts. Imgs: `ex-postapoc-wide`, `ex-postapoc-handle`.

### Trilha 3 ê¢â¬â AtuaêÂ§êÂ£o e DireêÂ§êÂ£o (rose) êÂ· fonte `doc/bloco6.md`
- **3-1 DiêÂ¡logo e AtuaêÂ§êÂ£o: EmoêÂ§êÂ£o por Baixo das Palavras** ê¢â¬â subtexto, planos de reaêÂ§êÂ£o, conflito, silêÂªncio, atuaêÂ§êÂ£o, enquadramento (MêÂ³dulo 5). Img: `ex-dialogue-ots`.
- **3-2 Performance de Personagem com IA** ê¢â¬â 6 mecêÂ¢nicas (motivaêÂ§êÂ£o antes do movimento, microatuaêÂ§êÂ£o, timing emocional, linguagem corporal, performance dos olhos, ritmo) + fêÂ³rmulas de ouro (Aula 17).
- **3-3 Estrutura de Cena de DiêÂ¡logo & Planos Emocionais** ê¢â¬â 7 mecêÂ¢nicas de diêÂ¡logo (Aula 19) + 6 mecêÂ¢nicas de planos emocionais (close-up, espaêÂ§o negativo, push-in, distêÂ¢ncia, OTS, POV ê¢â¬â Aula 18).

### Trilha 4 ê¢â¬â CARCKHêtografia e Visual (blue) êÂ· fonte `doc/bloco2.md` + `doc/bloco4.md` (Aula 12) + `doc/bloco3.md` (Aula 9)
- **4-1 ComposiêÂ§êÂ£o para CARCKHê** ê¢â¬â pensamento visual (formato=cêÂ¢mera, ambiente=histêÂ³ria, luz=emoêÂ§êÂ£o, personagem=contradiêÂ§êÂ£o, cena=sequêÂªncia); têÂ©cnicas (diagonal, linhas de conduêÂ§êÂ£o, terêÂ§os, espaêÂ§o negativo, simetria, macro, escala, contraste); composiêÂ§êÂ£o como sequêÂªncia no tempo.
- **4-2 IluminaêÂ§êÂ£o e Atmosfera** ê¢â¬â negative fill, edge contrast, suavidade pela distêÂ¢ncia, luz motivada, regra 80/20, camadas de atmosfera, contraste de cor, luz dinêÂ¢mica. Img: `ex-lighting-rim`.
- **4-3 Profundidade e Estrutura Espacial** ê¢â¬â regra das 3 camadas, separaêÂ§êÂ£o, profundidade de campo, escolha de lente (grande-angular vs tele), paralaxe; profundidade = emoêÂ§êÂ£o. Img: `ex-depth-layers`.
- **4-4 Tamanhos de Plano & Movimento de CêÂ¢mera** ê¢â¬â establishingê¢â âECU (quando/por quêÂª); 25+ movimentos (dolly vs zoom vs dolly zoom, truck, pan, tilt, crane, orbit, arc, whip pan, rack focus, handheld, dutch); guia prêÂ¡tico intenêÂ§êÂ£oê¢â âmovimento. Img: `ex-camera-move`.

### Trilha 5 ê¢â¬â IA Visual e GeraêÂ§êÂ£o (teal) êÂ· fonte `doc/bloco3.md` + `doc/bloco4.md` (Aula 13) + `doc/bloco5.md`
- **5-1 Pipeline de Ferramentas de IA** ê¢â¬â funêÂ§êÂµes de Freepik/Seedance/Kling/Luma/Runway; controle de atenêÂ§êÂ£o, composiêÂ§êÂ£o, conexêÂ£o de planos; checklist final.
- **5-2 GeraêÂ§êÂ£o de Movimento no Seedance** ê¢â¬â ForêÂ§a+Tempo+Peso; sequêÂªncia (grandeê¢â âpequenoê¢â âpartêÂ­culas); cêÂ¢mera; reaêÂ§êÂ£o humana (mostrar, nêÂ£o nomear); detalhes mensurêÂ¡veis. Img: `ex-camera-move`.
- **5-3 Controle por YAML no Seedance 2** ê¢â¬â por que YAML; trava de identidade (`base: matching reference @image1...`); blocos cêÂ¢mera/aêÂ§êÂ£o/iluminaêÂ§êÂ£o/transiêÂ§êÂµes; regras (uma funêÂ§êÂ£o por campo, blocos de tempo `00_02`); transiêÂ§êÂµes (cut, whip pan, smash, match on action). Use **code box YAML**.
- **5-4 Efeitos Visuais PrêÂ¡ticos** ê¢â¬â LED volume, fogo prêÂ¡tico, suspensêÂ£o por cabos, chuva prêÂ¡tica, miniaturas, hêÂ­brido fêÂ­sico+digital; YAML p/ VFX; blueprint Luzê¢â âTexturaê¢â âMovimentoê¢â âAtmosferaê¢â âEmoêÂ§êÂ£o. Img: `ex-particles`.
- **5-5 CêÂ¢mera Lenta & Sistemas de PartêÂ­culas** ê¢â¬â overcranking (120/240fpsê¢â â24fps), rêÂ¡pidoê¢â âlentoê¢â ârêÂ¡pido, microatuaêÂ§êÂ£o, continuidade de luz; partêÂ­culas para esconder artefatos de morphing (oclusêÂ£o transicional, integraêÂ§êÂ£o volumêÂ©trica, suavizaêÂ§êÂ£o temporal, camadas cinêÂ©ticas). Imgs: `ex-slowmo-action`, `ex-particles`.
- **5-6 IntegraêÂ§êÂ£o com Luma e Runway** ê¢â¬â Uni-1 (inteligêÂªncia unificada, conversa em vez de prompt); fluxo: ficha de personagem ê¢â â dirigir plano ê¢â â animar; comparar modelos (Kling vs Ray); dirigir o parceiro criativo.

### Trilha 6 ê¢â¬â Som, EdiêÂ§êÂ£o e PêÂ³s-ProduêÂ§êÂ£o (emerald) êÂ· fonte `doc/bloco4.md` (Aula 11) + `doc/bloco5.md` (Aula 16)
- **6-1 EdiêÂ§êÂ£o CARCKHêtogrêÂ¡fica: Tipos de Corte** ê¢â¬â jump, match, cut on action, cross cutting, double, fast cutting; "ediêÂ§êÂ£o êÂ© a relaêÂ§êÂ£o entre planos"; gerarê¢â âassistirê¢â âanalisar o corte. *(REAL)*
- **6-2 Cenas de AêÂ§êÂ£o: 5 MecêÂ¢nicas** ê¢â¬â transformaêÂ§êÂ£o voadora, perseguiêÂ§êÂ£o urbana, capotamento, fuga com parkour, resgate na ponte; fêÂ³rmula Risco+Movimento+Quase Fracasso. Img: `ex-slowmo-action`. *(REAL)*
- **EM CONSTRUêâ¡êÆO (sêÂ³ cards, sem pêÂ¡gina):** 6-3 Design de Som & Foley êÂ· 6-4 Trilha & MêÂºsica êÂ· 6-5 Color Grading êÂ· 6-6 Mixagem & MasterizaêÂ§êÂ£o

### Trilha 7 ê¢â¬â ProduêÂ§êÂ£o e Carreira (purple) êÂ· fonte `doc/bloco7(1).md`
- **7-1 Narrativa Visual: Framework de 5 Cenas** ê¢â¬â Setupê¢â âConflitoê¢â âEscaladaê¢â âEmoêÂ§êÂ£oê¢â âResoluêÂ§êÂ£o (o relojoeiro e o pêÂ¡ssaro mecêÂ¢nico); prompts Kling reais por cena; checklist do diretor (relevêÂ¢ncia 0.5ê¢â¬â0.6, frases de cêÂ¢mera). Img: `ex-watchmaker`. *(REAL)*
- **EM CONSTRUêâ¡êÆO (sêÂ³ cards):** 7-2 ConstruêÂ§êÂ£o de PortfêÂ³lio êÂ· 7-3 Pitch & ApresentaêÂ§êÂ£o êÂ· 7-4 MonetizaêÂ§êÂ£o êÂ· 7-5 Cliente & Mercado êÂ· 7-6 Carreira em IA Filmmaking

## Imagens de exemplo (em `assets/`, jêÂ¡ geradas)
`ex-samurai-bridge` `ex-postapoc-wide` `ex-postapoc-handle` `ex-lighting-rim` `ex-depth-layers` `ex-particles` `ex-slowmo-action` `ex-watchmaker` `ex-dialogue-ots` `ex-camera-move` êÂ· capas: `cover-wide` `cover-square`.

**PadrêÂ£o de `<img>` seguro** (caminho a partir de `curso/trilhaN/`, com legenda e auto-hide se faltar):
```html
<figure class="mb-6 rounded-xl overflow-hidden border border-dark-600">
  <img src="../../assets/ex-NOME.png" alt="DESCRIêâ¡êÆO" loading="lazy" class="w-full h-auto"
       onerror="this.closest('figure').style.display='none'">
  <figcaption class="text-xs text-neutral-500 px-4 py-2 bg-dark-800">Exemplo cARCKHêtogrêÂ¡fico ê¢â¬â gerado com IA (flux2-klein) êÂ· ilustrativo</figcaption>
</figure>
```

## PadrêÂ£o "EM CONSTRUêâ¡êÆO" (trilhas 6 e 7)
No index da trilha, apêÂ³s os cards reais, cards mudos:
```html
<div class="bg-dark-800/60 rounded-xl border border-dashed border-dark-600 p-6 mb-6 opacity-70">
  <div class="flex items-center justify-between mb-2">
    <span class="text-neutral-500 font-bold">6.3</span>
    <span class="text-xs px-2 py-0.5 rounded-full bg-primary/10 text-primary border border-primary/30">EM CONSTRUêâ¡êÆO</span>
  </div>
  <h3 class="text-2xl font-bold mb-2 text-neutral-400">ê°Å¸âÅ  Design de Som & Foley</h3>
  <p class="text-neutral-500 text-sm">ConteêÂºdo em produêÂ§êÂ£o ê¢â¬â disponêÂ­vel em breve.</p>
</div>
```
No "Mapa da trilha": mêÂ³dulos em construêÂ§êÂ£o entram como `<div>` (nêÂ£o `<a>`), sem êÂ¢ncora, com o badge. NêÂ£o criar `modulo-X-Y.html` para eles.

## Stats por trilha (para header e landing)
T1: 3 mêÂ³d êÂ· ~20 têÂ³p êÂ· ~2h êÂ· BêÂ¡sico ê¢â¬â T2: 3 êÂ· ~21 êÂ· ~2.5h êÂ· BêÂ¡sico ê¢â¬â T3: 3 êÂ· ~20 êÂ· ~2h êÂ· Inter. ê¢â¬â T4: 4 êÂ· ~28 êÂ· ~3h êÂ· Inter. ê¢â¬â T5: 6 êÂ· ~40 êÂ· ~4.5h êÂ· AvanêÂ§ado ê¢â¬â T6: 6 (2 prontos) êÂ· ~14 êÂ· ~2h êÂ· Inter. ê¢â¬â T7: 6 (1 pronto) êÂ· ~8 êÂ· ~1h êÂ· AvanêÂ§ado.
