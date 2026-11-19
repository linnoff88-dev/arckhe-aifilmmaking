# BUILD-SPEC — Curso AI FILMMAKING (formato INEMA.CLUB)

> Contrato compartilhado para construção paralela das trilhas. **Leia também**
> `/home/nmaldaner/.claude/skills/formato-curso/references/MASTER_COMPLETO.md` e
> `SVG-FUTURISTA.md` (regras de formato + biblioteca de diagramas). Use os arquivos
> **`curso/trilha1/index.html`** e **`curso/trilha1/modulo-1-1.html`** como REFERÊNCIA-OURO
> (copie nav, `<style>`, scripts, estrutura — troque só a cor e o conteúdo).

## Identidade
- **Curso:** AI FILMMAKING — Do Conceito ao Filme Final
- **Emoji:** 🎬
- **Repo / Pages:** `https://inematds.github.io/aifilmmaking/`
- **Estrutura:** 7 trilhas (= blocos), 31 módulos no roadmap (= lições). Conteúdo real escrito p/ ~22; restantes entram como cards "EM CONSTRUÇÃO".

## Mapa de cores das 7 trilhas

| T | Nome trilha | Cor INEMA | text / bg / border | Light-mode acento | SVG primário / forte / fill |
|---|-------------|-----------|--------------------|-------------------|------------------------------|
| 1 | Fundamentos do Cinema | amber | `text-amber-400` `bg-amber-500/20` `border-amber-500/30` `from-amber-900/30` | `#92400e` rgb `217,119,6` | `#fbbf24` / `#f59e0b` / `#1f1604` |
| 2 | Pré-Produção e Roteiro | orange | `text-orange-400` `bg-orange-500/20` `border-orange-500/30` `from-orange-900/30` | `#c2410c` rgb `234,88,12` | `#fb923c` / `#f97316` / `#241405` |
| 3 | Atuação e Direção | rose | `text-rose-400` `bg-rose-500/20` `border-rose-500/30` `from-rose-900/30` | `#9f1239` rgb `225,29,72` | `#fb7185` / `#f43f5e` / `#2a0f16` |
| 4 | Cinematografia e Visual | blue | `text-blue-400` `bg-blue-500/20` `border-blue-500/30` `from-blue-900/30` | `#2563eb` rgb `37,99,235` | `#60a5fa` / `#3b82f6` / `#0e1622` |
| 5 | IA Visual e Geração | teal | `text-teal-400` `bg-teal-500/20` `border-teal-500/30` `from-teal-900/30` | `#0d9488` rgb `13,148,136` | `#2dd4bf` / `#14b8a6` / `#0c1f1c` |
| 6 | Som, Edição e Pós-Produção | emerald | `text-emerald-400` `bg-emerald-500/20` `border-emerald-500/30` `from-emerald-900/30` | `#059669` rgb `5,150,105` | `#34d399` / `#10b981` / `#0e2018` |
| 7 | Produção e Carreira | purple | `text-purple-400` `bg-purple-500/20` `border-purple-500/30` `from-purple-900/30` | `#7c3aed` rgb `124,58,237` | `#c084fc` / `#a855f7` / `#1a1230` |

Cor secundária dos SVGs = ciano `#38bdf8` (sempre). Botões "Ver Completo"/CTA usam `bg-<cor>-600 hover:bg-<cor>-500`.

## NAV global (IDÊNTICO em todas as páginas, só muda o caminho e a trilha ativa)

7 botões de trilha. **Mobile** = `T1`..`T7`; **desktop** = label curto:
`Fundamentos · Pré-Produção · Atuação · Cinematografia · IA Visual · Pós-Produção · Carreira`.

Caminhos relativos:
- **Landing `index.html`:** logo → `index.html`; trilha N → `curso/trilhaN/index.html`.
- **Trilha index / módulo (`curso/trilhaN/...`):** logo → `../../index.html`; própria trilha → `index.html`; trilha M → `../trilhaM/index.html`.

A trilha ATIVA: `text-<cor>-400 bg-<cor>-500/10`. Inativas: `text-neutral-400 hover:text-<corM>-400 hover:bg-<corM>-500/10 transition-colors`.

**`<style>` light-mode:** como cada página vê 7 cores no nav, inclua no bloco light-mode os overrides de **todas as 7 cores de acento** (use a tabela acima) — igual ao bloco da landing descrito no MASTER Sec.1.5. A cor PRINCIPAL da página (própria trilha) também precisa dos overrides `bg/border /20 /10 /30`. Adicione sempre as 2 regras de borda dark (`#374151`) e a regra `html:not(.dark) svg[role="img"]{filter:saturate(.82) brightness(.96)}`.

## Conteúdo por módulo (FONTE = arquivos em `doc/`)

Cada módulo real: **6–8 tópicos**, **500–800 linhas**, **≥1 SVG inline** (cor da trilha + ciano), VARIEDADE de componentes (≥2 grids ✓/✗, ≥1 timeline, ≥2 tip box, code/mono box quando útil — ex.: YAML, prompts), e termina com **Resumo do Módulo** + nav p/ próximo. Reaproveite os **prompts e exemplos reais** do material (não invente exemplos genéricos). Toda página de módulo inclui um box "📝 Tarefa" com o exercício do material-fonte. Tom: direto, prático, confiante (PT-BR).

### Trilha 1 — Fundamentos do Cinema (amber) · fonte `doc/bloco1.md` (+ `bloco3.md` §1-4)
- **1-1 A Estrutura do Diretor** — IA executa direção, não cria intenção; o conceito de Âncora (filme=personagem, anúncio=produto, clipe=ritmo); hierarquia e lógica de câmera; as 4 perguntas (por que ângulo/movimento/duração/luz); o conjunto de ferramentas. *(REFERÊNCIA-OURO — já construído)*
- **1-2 Controle Espacial & Linguagem de Câmera** — movimentos (dolly in, tracking, orbit, pan/tilt); distância/enquadramento (close/médio/aberto); profundidade e paralaxe; estilo (steadycam/handheld/slow-mo); estrutura de prompt `sujeito + ambiente + movimento + estilo`; erro comum (movimentos demais). Img: `ex-samurai-bridge`.
- **1-3 O Que Torna Algo Cinematográfico** — clareza + controle; âncora de atenção; espaço negativo; composição (simetria, regra dos terços, ângulo holandês); paleta consistente; checklist final do diretor.

### Trilha 2 — Pré-Produção e Roteiro (orange) · fonte `doc/bloco1.md` (Aula 2) + `doc/bloco3.md` (Aula 7 + PROMPTS)
- **2-1 Do Roteiro à Cena: o Pipeline** — fluxo Roteiro→Storyboard→Personagem→Figurino→Ambiente→Lista de Planos→Frames; análise do roteiro (o que o público deve sentir); 7 etapas detalhadas. Img: `ex-samurai-bridge`.
- **2-2 Storyboard Estruturado** — Freepik/Magnific Spaces, fluxo por nós; esboço→render cinematográfico; lógica de direção plano a plano; arco narrativo (Espaço→Personagem→Ação→Movimento→Liberação); uso de `@referências`.
- **2-3 Personagem, Figurino, Ambiente & Lista de Planos** — com os **PROMPTS COMPLETOS reais** (roteiro 6 planos pós-apocalíptico, ficha de personagem, esboço grade 2x3, storyboard renderizado com travas, lista de planos). Use mono/code boxes para os prompts. Imgs: `ex-postapoc-wide`, `ex-postapoc-handle`.

### Trilha 3 — Atuação e Direção (rose) · fonte `doc/bloco6.md`
- **3-1 Diálogo e Atuação: Emoção por Baixo das Palavras** — subtexto, planos de reação, conflito, silêncio, atuação, enquadramento (Módulo 5). Img: `ex-dialogue-ots`.
- **3-2 Performance de Personagem com IA** — 6 mecânicas (motivação antes do movimento, microatuação, timing emocional, linguagem corporal, performance dos olhos, ritmo) + fórmulas de ouro (Aula 17).
- **3-3 Estrutura de Cena de Diálogo & Planos Emocionais** — 7 mecânicas de diálogo (Aula 19) + 6 mecânicas de planos emocionais (close-up, espaço negativo, push-in, distância, OTS, POV — Aula 18).

### Trilha 4 — Cinematografia e Visual (blue) · fonte `doc/bloco2.md` + `doc/bloco4.md` (Aula 12) + `doc/bloco3.md` (Aula 9)
- **4-1 Composição para Cinema** — pensamento visual (formato=câmera, ambiente=história, luz=emoção, personagem=contradição, cena=sequência); técnicas (diagonal, linhas de condução, terços, espaço negativo, simetria, macro, escala, contraste); composição como sequência no tempo.
- **4-2 Iluminação e Atmosfera** — negative fill, edge contrast, suavidade pela distância, luz motivada, regra 80/20, camadas de atmosfera, contraste de cor, luz dinâmica. Img: `ex-lighting-rim`.
- **4-3 Profundidade e Estrutura Espacial** — regra das 3 camadas, separação, profundidade de campo, escolha de lente (grande-angular vs tele), paralaxe; profundidade = emoção. Img: `ex-depth-layers`.
- **4-4 Tamanhos de Plano & Movimento de Câmera** — establishing→ECU (quando/por quê); 25+ movimentos (dolly vs zoom vs dolly zoom, truck, pan, tilt, crane, orbit, arc, whip pan, rack focus, handheld, dutch); guia prático intenção→movimento. Img: `ex-camera-move`.

### Trilha 5 — IA Visual e Geração (teal) · fonte `doc/bloco3.md` + `doc/bloco4.md` (Aula 13) + `doc/bloco5.md`
- **5-1 Pipeline de Ferramentas de IA** — funções de Freepik/Seedance/Kling/Luma/Runway; controle de atenção, composição, conexão de planos; checklist final.
- **5-2 Geração de Movimento no Seedance** — Força+Tempo+Peso; sequência (grande→pequeno→partículas); câmera; reação humana (mostrar, não nomear); detalhes mensuráveis. Img: `ex-camera-move`.
- **5-3 Controle por YAML no Seedance 2** — por que YAML; trava de identidade (`base: matching reference @image1...`); blocos câmera/ação/iluminação/transições; regras (uma função por campo, blocos de tempo `00_02`); transições (cut, whip pan, smash, match on action). Use **code box YAML**.
- **5-4 Efeitos Visuais Práticos** — LED volume, fogo prático, suspensão por cabos, chuva prática, miniaturas, híbrido físico+digital; YAML p/ VFX; blueprint Luz→Textura→Movimento→Atmosfera→Emoção. Img: `ex-particles`.
- **5-5 Câmera Lenta & Sistemas de Partículas** — overcranking (120/240fps→24fps), rápido→lento→rápido, microatuação, continuidade de luz; partículas para esconder artefatos de morphing (oclusão transicional, integração volumétrica, suavização temporal, camadas cinéticas). Imgs: `ex-slowmo-action`, `ex-particles`.
- **5-6 Integração com Luma e Runway** — Uni-1 (inteligência unificada, conversa em vez de prompt); fluxo: ficha de personagem → dirigir plano → animar; comparar modelos (Kling vs Ray); dirigir o parceiro criativo.

### Trilha 6 — Som, Edição e Pós-Produção (emerald) · fonte `doc/bloco4.md` (Aula 11) + `doc/bloco5.md` (Aula 16)
- **6-1 Edição Cinematográfica: Tipos de Corte** — jump, match, cut on action, cross cutting, double, fast cutting; "edição é a relação entre planos"; gerar→assistir→analisar o corte. *(REAL)*
- **6-2 Cenas de Ação: 5 Mecânicas** — transformação voadora, perseguição urbana, capotamento, fuga com parkour, resgate na ponte; fórmula Risco+Movimento+Quase Fracasso. Img: `ex-slowmo-action`. *(REAL)*
- **EM CONSTRUÇÃO (só cards, sem página):** 6-3 Design de Som & Foley · 6-4 Trilha & Música · 6-5 Color Grading · 6-6 Mixagem & Masterização

### Trilha 7 — Produção e Carreira (purple) · fonte `doc/bloco7(1).md`
- **7-1 Narrativa Visual: Framework de 5 Cenas** — Setup→Conflito→Escalada→Emoção→Resolução (o relojoeiro e o pássaro mecânico); prompts Kling reais por cena; checklist do diretor (relevância 0.5–0.6, frases de câmera). Img: `ex-watchmaker`. *(REAL)*
- **EM CONSTRUÇÃO (só cards):** 7-2 Construção de Portfólio · 7-3 Pitch & Apresentação · 7-4 Monetização · 7-5 Cliente & Mercado · 7-6 Carreira em IA Filmmaking

## Imagens de exemplo (em `assets/`, já geradas)
`ex-samurai-bridge` `ex-postapoc-wide` `ex-postapoc-handle` `ex-lighting-rim` `ex-depth-layers` `ex-particles` `ex-slowmo-action` `ex-watchmaker` `ex-dialogue-ots` `ex-camera-move` · capas: `cover-wide` `cover-square`.

**Padrão de `<img>` seguro** (caminho a partir de `curso/trilhaN/`, com legenda e auto-hide se faltar):
```html
<figure class="mb-6 rounded-xl overflow-hidden border border-dark-600">
  <img src="../../assets/ex-NOME.png" alt="DESCRIÇÃO" loading="lazy" class="w-full h-auto"
       onerror="this.closest('figure').style.display='none'">
  <figcaption class="text-xs text-neutral-500 px-4 py-2 bg-dark-800">Exemplo cinematográfico — gerado com IA (flux2-klein) · ilustrativo</figcaption>
</figure>
```

## Padrão "EM CONSTRUÇÃO" (trilhas 6 e 7)
No index da trilha, após os cards reais, cards mudos:
```html
<div class="bg-dark-800/60 rounded-xl border border-dashed border-dark-600 p-6 mb-6 opacity-70">
  <div class="flex items-center justify-between mb-2">
    <span class="text-neutral-500 font-bold">6.3</span>
    <span class="text-xs px-2 py-0.5 rounded-full bg-primary/10 text-primary border border-primary/30">EM CONSTRUÇÃO</span>
  </div>
  <h3 class="text-2xl font-bold mb-2 text-neutral-400">🔊 Design de Som & Foley</h3>
  <p class="text-neutral-500 text-sm">Conteúdo em produção — disponível em breve.</p>
</div>
```
No "Mapa da trilha": módulos em construção entram como `<div>` (não `<a>`), sem âncora, com o badge. Não criar `modulo-X-Y.html` para eles.

## Stats por trilha (para header e landing)
T1: 3 mód · ~20 tóp · ~2h · Básico — T2: 3 · ~21 · ~2.5h · Básico — T3: 3 · ~20 · ~2h · Inter. — T4: 4 · ~28 · ~3h · Inter. — T5: 6 · ~40 · ~4.5h · Avançado — T6: 6 (2 prontos) · ~14 · ~2h · Inter. — T7: 6 (1 pronto) · ~8 · ~1h · Avançado.
