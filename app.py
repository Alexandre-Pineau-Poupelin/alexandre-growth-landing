import streamlit as st

st.set_page_config(
    page_title="Alexandre Pineau-Poupelin — Growth Systems Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ══════════════════════════════════════════════════════════════
# DESIGN SYSTEM
# ══════════════════════════════════════════════════════════════

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,300..900;1,14..32,300..900&display=swap');

:root {
  --bg:     #06060b;
  --surf:   #0d0d1a;
  --surf2:  #111126;
  --bdr:    rgba(255,255,255,0.07);
  --bdr-a:  rgba(99,102,241,0.35);
  --acc:    #6366f1;
  --acc-lo: rgba(99,102,241,0.10);
  --t1:     #ededf5;
  --t2:     #8888b0;
  --t3:     #44445a;
  --grn:    #22c55e;
  --r:      12px;
  --rL:     16px;
  --f:      'Inter', -apple-system, sans-serif;
}

html, body,
[data-testid="stApp"],
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.stApp, .main, section.main {
  background: var(--bg) !important;
  color: var(--t1) !important;
  font-family: var(--f) !important;
}

#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stHeader"] {
  display: none !important;
  visibility: hidden !important;
}

/* Container: 860px centered column for all content */
.main .block-container,
[data-testid="block-container"],
[data-testid="stMainBlockContainer"],
.stMainBlockContainer {
  max-width: 860px !important;
  width: 100% !important;
  padding: 0 28px !important;
  margin: 0 auto !important;
  box-sizing: border-box !important;
}

[data-testid="stMarkdown"] > div { margin-bottom: 0 !important; }

/* ── Native Streamlit — Projet Clé ── */
hr {
  border: none !important;
  border-top: 1px solid var(--bdr) !important;
  margin: 0 !important;
}
h5 {
  font-size: 11px !important; font-weight: 600 !important;
  letter-spacing: 0.2em !important; text-transform: uppercase !important;
  color: var(--acc) !important; margin: 0 0 12px !important;
  text-align: center !important;
}
h3 {
  font-size: clamp(22px, 2.8vw, 32px) !important;
  font-weight: 700 !important; line-height: 1.15 !important;
  letter-spacing: -0.028em !important;
  color: var(--t1) !important; margin: 4px 0 16px !important;
  text-align: center !important;
}
p:not([class]) {
  color: var(--t2) !important; font-size: 16px !important;
  line-height: 1.72 !important; letter-spacing: -0.008em !important;
  text-align: center !important;
  max-width: 600px !important; margin-left: auto !important; margin-right: auto !important;
}
[data-testid="stMarkdown"] p strong:only-child {
  font-size: 11px !important; font-weight: 700 !important;
  letter-spacing: 0.16em !important; text-transform: uppercase !important;
  color: var(--t3) !important;
}
[data-testid="stMetric"] {
  background: var(--surf) !important;
  border: 1px solid var(--bdr) !important;
  border-radius: var(--r) !important;
  padding: 22px 14px !important;
  text-align: center !important;
}
[data-testid="stMetricValue"] div {
  font-size: 28px !important; font-weight: 800 !important;
  letter-spacing: -0.04em !important;
  color: var(--t1) !important; line-height: 1 !important;
}
[data-testid="stMetricLabel"] {
  font-size: 11px !important; font-weight: 600 !important;
  color: var(--t3) !important; text-align: center !important;
  letter-spacing: 0.07em !important; text-transform: uppercase !important;
}
[data-testid="stMetricDelta"] { display: none !important; }
[data-testid="stMarkdown"] ul {
  padding: 0 !important; margin: 0 !important; list-style: none !important;
}
[data-testid="stMarkdown"] ul li {
  padding: 9px 0 !important;
  color: var(--t2) !important; font-size: 14px !important;
  line-height: 1.55 !important; letter-spacing: -0.008em !important;
  border-bottom: 1px solid rgba(255,255,255,0.04) !important;
  list-style-type: '→  ' !important;
}
[data-testid="stMarkdown"] ul li:last-child { border-bottom: none !important; }

/* ── Content column: fills block-container (centering above) ── */
.col {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* ── Sections ── */
.sec      { padding: 88px 0; border-top: 1px solid var(--bdr); }
.sec-last { padding: 88px 0 0; border-top: 1px solid var(--bdr); }

/* ── Eyebrow ── */
.ey {
  display: block;
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 14px;
  text-align: center;
}

/* ── Section headings ── */
.h2 {
  font-size: clamp(26px, 3.2vw, 38px);
  font-weight: 700; line-height: 1.1;
  letter-spacing: -0.028em;
  color: var(--t1); margin-bottom: 14px;
  text-align: center;
}
.sdesc {
  font-size: 16px; color: var(--t2);
  line-height: 1.72; max-width: 560px;
  font-weight: 400; letter-spacing: -0.008em;
  margin: 0 auto; text-align: center;
}

/* ══════════════════════════════
   HERO
══════════════════════════════ */
.hero { padding: 100px 0 88px; text-align: center; }

.badge {
  display: inline-flex; align-items: center; gap: 9px;
  background: rgba(34,197,94,0.06);
  border: 1px solid rgba(34,197,94,0.16);
  border-radius: 100px;
  padding: 7px 16px; margin-bottom: 38px;
  font-size: 13px; font-weight: 500; color: #86efac;
}
.bdot {
  display: inline-block; width: 6px; height: 6px;
  background: var(--grn); border-radius: 50%;
  animation: pdot 2.8s ease infinite;
}
@keyframes pdot {
  0%,100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50%      { box-shadow: 0 0 0 6px rgba(34,197,94,0); }
}

.hero-role {
  font-size: 12px; font-weight: 600;
  letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 16px;
}
.hero-name {
  font-size: clamp(44px, 6.5vw, 78px);
  font-weight: 800; line-height: 0.96;
  letter-spacing: -0.044em; color: var(--t1); margin-bottom: 26px;
}
.hero-val {
  font-size: clamp(16px, 1.8vw, 18px);
  line-height: 1.74; color: var(--t2);
  max-width: 560px; margin: 0 auto 42px;
  font-weight: 400; letter-spacing: -0.01em;
}
.hero-val strong { color: var(--t1); font-weight: 500; }

/* ── Buttons ── */
.btns { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; justify-content: center; }
.btn-p {
  display: inline-flex; align-items: center; gap: 7px;
  background: var(--acc); color: #fff !important;
  font-size: 14px; font-weight: 600;
  padding: 12px 24px; border-radius: 8px;
  text-decoration: none !important; letter-spacing: -0.01em;
  transition: background .18s, transform .14s, box-shadow .18s;
}
.btn-p:hover { background: #4f46e5; transform: translateY(-1px); box-shadow: 0 10px 26px rgba(99,102,241,0.28); }
.btn-s {
  display: inline-flex; align-items: center; gap: 7px;
  background: transparent; color: var(--t2) !important;
  font-size: 14px; font-weight: 500;
  padding: 12px 24px; border-radius: 8px;
  border: 1px solid var(--bdr);
  text-decoration: none !important; letter-spacing: -0.01em;
  transition: border-color .18s, color .18s, transform .14s;
}
.btn-s:hover { border-color: var(--bdr-a); color: var(--t1) !important; transform: translateY(-1px); }

/* ══════════════════════════════
   APPROCHE — CARDS
══════════════════════════════ */
.cards { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 40px; }
.card {
  flex: 1 1 calc(50% - 6px); min-width: 240px;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 26px 28px;
  transition: border-color .2s, background .18s;
  box-sizing: border-box;
}
.card:hover { border-color: rgba(99,102,241,0.25); background: var(--surf2); }
.c-ico { font-size: 20px; display: block; margin-bottom: 12px; }
.c-ttl { font-size: 14px; font-weight: 600; color: var(--t1); margin-bottom: 7px; letter-spacing: -0.01em; line-height: 1.35; }
.c-dsc { font-size: 13px; color: var(--t2); line-height: 1.65; }

/* ══════════════════════════════
   PROJET CLÉ
══════════════════════════════ */
.proj-sec { padding: 88px 0; border-top: 1px solid var(--bdr); }

.proj-eyebrow {
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 14px;
  text-align: center; display: block;
}
.proj-title {
  font-size: clamp(22px, 2.8vw, 32px);
  font-weight: 700; line-height: 1.15;
  letter-spacing: -0.028em;
  color: var(--t1); margin-bottom: 16px;
  text-align: center;
}
.proj-desc {
  font-size: 16px; color: var(--t2);
  line-height: 1.72; max-width: 560px;
  margin: 0 auto 36px; text-align: center;
  letter-spacing: -0.008em;
}

/* Metrics */
.metrics-row { display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 36px; }
.metric {
  flex: 1 1 calc(25% - 8px); min-width: 120px;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--r); padding: 22px 14px;
  text-align: center; box-sizing: border-box;
}
.m-val {
  font-size: 28px; font-weight: 800;
  letter-spacing: -0.04em; color: var(--t1);
  line-height: 1; margin-bottom: 8px;
}
.m-lbl {
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.07em; text-transform: uppercase;
  color: var(--t3);
}

/* Action list */
.proj-sub {
  font-size: 11px; font-weight: 700;
  letter-spacing: 0.2em; text-transform: uppercase;
  color: var(--t3); margin-bottom: 18px;
  text-align: center; display: block;
}
.proj-actions { display: flex; gap: 0; }
.proj-col {
  flex: 1;
  background: var(--surf); border: 1px solid var(--bdr);
  overflow: hidden;
}
.proj-col:first-child { border-radius: var(--r) 0 0 var(--r); border-right: none; }
.proj-col:last-child  { border-radius: 0 var(--r) var(--r) 0; }
.proj-item {
  display: flex; align-items: flex-start; gap: 10px;
  padding: 11px 18px;
  border-bottom: 1px solid rgba(255,255,255,0.04);
  font-size: 13px; color: var(--t2);
  line-height: 1.5; letter-spacing: -0.008em;
}
.proj-item:last-child { border-bottom: none; }
.proj-arrow { color: var(--acc); flex-shrink: 0; opacity: 0.65; margin-top: 1px; }

/* ══════════════════════════════
   COMPÉTENCES
══════════════════════════════ */
.skills { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 40px; }
.sg {
  flex: 1 1 calc(50% - 6px); min-width: 240px;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 26px 28px;
  box-sizing: border-box;
}
.sg-lbl {
  display: block; font-size: 11px; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 16px;
}
.sr {
  display: flex; align-items: center; gap: 10px;
  font-size: 13px; color: var(--t2);
  padding: 9px 0; border-bottom: 1px solid rgba(255,255,255,0.04);
  line-height: 1.45; letter-spacing: -0.008em;
}
.sr:last-child { border-bottom: none; }
.sd { width: 4px; height: 4px; background: var(--acc); border-radius: 50%; flex-shrink: 0; opacity: 0.6; }

/* ══════════════════════════════
   STACK
══════════════════════════════ */
.pills { display: flex; flex-wrap: wrap; gap: 9px; margin-top: 30px; justify-content: center; }
.pill {
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: 8px; padding: 10px 16px;
  font-size: 13px; font-weight: 500; color: var(--t2);
  transition: border-color .18s, color .18s;
  cursor: default; letter-spacing: -0.01em;
}
.pill:hover { border-color: var(--bdr-a); color: var(--t1); }

/* ══════════════════════════════
   OBJECTIF
══════════════════════════════ */
.obj {
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL);
  padding: 62px 48px; text-align: center;
}
.obj-h2 {
  font-size: clamp(22px, 2.8vw, 34px);
  font-weight: 700; letter-spacing: -0.028em;
  color: var(--t1); margin-bottom: 16px; line-height: 1.12;
}
.obj-sub {
  font-size: 16px; color: var(--t2);
  line-height: 1.72; max-width: 460px;
  margin: 0 auto 30px; letter-spacing: -0.01em;
}
.rpills { display: flex; justify-content: center; gap: 8px; flex-wrap: wrap; margin-bottom: 32px; }
.rpill {
  background: var(--acc-lo); border: 1px solid rgba(99,102,241,0.2);
  border-radius: 100px; padding: 7px 18px;
  font-size: 13px; font-weight: 600; color: #a5b4fc; letter-spacing: -0.01em;
}

/* ══════════════════════════════
   CONTACT
══════════════════════════════ */
.contacts { display: flex; gap: 12px; margin-top: 40px; }
.cc {
  flex: 1;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 28px 18px;
  text-align: center; text-decoration: none; display: block;
  transition: border-color .18s, transform .14s, background .18s;
  box-sizing: border-box;
}
.cc:hover { border-color: rgba(99,102,241,0.28); background: var(--surf2); transform: translateY(-2px); }
.cc-ico { font-size: 24px; margin-bottom: 12px; display: block; }
.cc-lbl {
  display: block; font-size: 10px; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--t3); margin-bottom: 8px;
}
.cc-val { font-size: 13px; color: var(--acc); font-weight: 500; line-height: 1.4; }

/* ══════════════════════════════
   FOOTER
══════════════════════════════ */
.foot {
  border-top: 1px solid var(--bdr);
  margin-top: 88px; padding: 36px 0;
  text-align: center; font-size: 12px;
  color: var(--t3); letter-spacing: 0.02em;
}

/* ══════════════════════════════
   RESPONSIVE — tablet (≤ 900px)
══════════════════════════════ */
@media (max-width: 900px) {
  .main .block-container,
  [data-testid="block-container"],
  [data-testid="stMainBlockContainer"],
  .stMainBlockContainer { padding: 0 22px !important; }
  .sec, .sec-last, .proj-sec { padding: 68px 0; }

  .cards, .skills { gap: 10px; }
  .card, .sg { flex: 1 1 100% !important; min-width: 0 !important; }

  .metrics-row .metric { flex: 1 1 calc(50% - 5px) !important; }

  .contacts { flex-wrap: wrap; gap: 10px; }
  .cc { flex: 1 1 calc(50% - 5px) !important; min-width: 0 !important; }

  .obj { padding: 48px 32px; }
  .foot { margin-top: 68px; }
}

/* ══════════════════════════════
   RESPONSIVE — mobile (≤ 640px)
══════════════════════════════ */
@media (max-width: 640px) {
  .main .block-container,
  [data-testid="block-container"],
  [data-testid="stMainBlockContainer"],
  .stMainBlockContainer { padding: 0 18px !important; }
  .sec, .sec-last, .proj-sec { padding: 52px 0; }

  .hero { padding: 64px 0 48px; }
  .hero-name { font-size: 36px !important; letter-spacing: -0.035em !important; }
  .hero-val { font-size: 15px !important; margin-bottom: 32px !important; max-width: 100% !important; }
  .badge { font-size: 12px !important; padding: 6px 12px !important; }
  .btns { flex-direction: column; gap: 9px; }
  .btn-p, .btn-s { justify-content: center; width: 100%; max-width: 280px; }

  .h2  { font-size: 22px !important; }
  h3   { font-size: 20px !important; }
  .proj-title { font-size: 20px !important; }
  .sdesc, .proj-desc { max-width: 100% !important; font-size: 15px !important; }
  p:not([class]) { max-width: 100% !important; font-size: 15px !important; }
  [data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; }
  [data-testid="stHorizontalBlock"] > [data-testid="column"] {
    min-width: calc(50% - 7px) !important;
    flex: 1 1 calc(50% - 7px) !important;
  }

  .cards { flex-direction: column; }
  .card  { padding: 20px 22px; }
  .skills { flex-direction: column; }
  .sg    { padding: 20px 22px; }

  .metrics-row { gap: 8px; }
  .metrics-row .metric { flex: 1 1 calc(50% - 4px) !important; min-width: 0 !important; padding: 18px 10px !important; }
  .m-val { font-size: 22px !important; }

  .proj-actions { flex-direction: column; gap: 8px; }
  .proj-col { border-radius: var(--r) !important; }
  .proj-col:first-child { border-right: 1px solid var(--bdr) !important; }

  .pills { gap: 7px; margin-top: 20px; }
  .pill  { padding: 8px 13px !important; font-size: 12px !important; }

  .obj { padding: 36px 18px; }
  .obj-h2 { font-size: 20px !important; }
  .obj-sub { font-size: 14px !important; max-width: 100% !important; }
  .rpills { flex-direction: column; align-items: center; }
  .rpill  { text-align: center; }

  .contacts { flex-direction: column; }
  .cc { padding: 24px 16px; }

  .foot { margin-top: 52px; }
}

/* ══════════════════════════════
   RESPONSIVE — small mobile (≤ 420px)
══════════════════════════════ */
@media (max-width: 420px) {
  .main .block-container,
  [data-testid="block-container"],
  [data-testid="stMainBlockContainer"],
  .stMainBlockContainer { padding: 0 14px !important; }
  .hero-name { font-size: 30px !important; }
  [data-testid="stMetric"] { padding: 18px 10px !important; }
  [data-testid="stMetricValue"] div { font-size: 22px !important; }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="hero">
    <div class="badge"><span class="bdot"></span>Disponible &middot; Ouvert aux opportunités CDI</div>
    <p class="hero-role">Growth Systems Engineer</p>
    <h1 class="hero-name">Alexandre<br>Pineau-Poupelin</h1>
    <p class="hero-val">
      J&rsquo;assemble <strong>acquisition, automation et conversion</strong> en systèmes scalables.<br>
      De la génération à la qualification jusqu&rsquo;au CRM, chaque étape est conçue pour produire du pipeline exploitable par les équipes sales.
    </p>
    <div class="btns">
      <a href="#projet" class="btn-p">&#9889; Voir le projet clé</a>
      <a href="mailto:alexandre.pineaupoupelin@gmail.com" class="btn-s">Me contacter &rarr;</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# APPROCHE
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="sec">
    <span class="ey">Approche</span>
    <h2 class="h2">Je construis des systèmes, pas des campagnes</h2>
    <p class="sdesc">La différence entre une campagne et un système : l&rsquo;une s&rsquo;arrête dès qu&rsquo;on coupe le budget. L&rsquo;autre tourne, mesure et s&rsquo;améliore seul.</p>
    <div class="cards">
      <div class="card">
        <span class="c-ico">🔗</span>
        <div class="c-ttl">Système end-to-end</div>
        <div class="c-dsc">Acquisition &rarr; qualification &rarr; conversion &rarr; revenu. Chaque étape est connectée et mesurée.</div>
      </div>
      <div class="card">
        <span class="c-ico">⚙️</span>
        <div class="c-ttl">Automatisation sans friction</div>
        <div class="c-dsc">Chaque tâche répétable est automatisée. Le pipeline grossit sans avoir besoin de recruter.</div>
      </div>
      <div class="card">
        <span class="c-ico">📊</span>
        <div class="c-ttl">Data-driven</div>
        <div class="c-dsc">Chaque décision s&rsquo;appuie sur la donnée. Pas de vanity metrics &mdash; que du pipeline et du revenu.</div>
      </div>
      <div class="card">
        <span class="c-ico">🔁</span>
        <div class="c-ttl">Itération continue</div>
        <div class="c-dsc">Ce qui ne fonctionne pas, on coupe vite. Ce qui marche, on accélère. Décisions rapides, cycle court.</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# PROJET CLÉ — Native Streamlit (zéro risque HTML brut)
# ══════════════════════════════════════════════════════════════

st.divider()

st.markdown("##### Cas concret · B2B · PME Tech")
st.markdown("### Construction d'un système d'acquisition B2B — de zéro à 368 K€")
st.markdown(
    "Point de départ : aucun système structuré, pas de pipeline exploitable. "
    "Mission : concevoir un système d'acquisition B2B capable de générer, qualifier "
    "et transmettre des leads directement exploitables par les équipes sales."
)

st.write("")

_m1, _m2, _m3, _m4 = st.columns(4)
_m1.metric("MQL générés",       "322")
_m2.metric("Clients signés",    "24")
_m3.metric("CA généré",         "368 K€")
_m4.metric("Taux MQL → client", "7,45 %")

st.write("")
st.markdown("**Ce que j'ai mis en place**")
st.write("")

_a1, _a2 = st.columns(2)
with _a1:
    st.markdown(
        "- Sourcing multi-sources + enrichissement data\n"
        "- Segmentation par ICP + lead scoring\n"
        "- Séquences email automatisées\n"
        "- Activation multicanale (email + calls)"
    )
with _a2:
    st.markdown(
        "- Intégration CRM HubSpot complète\n"
        "- Orchestration des workflows via n8n\n"
        "- Alignement marketing → sales\n"
        "- Transmission des leads qualifiés en temps réel"
    )

st.write("")


# ══════════════════════════════════════════════════════════════
# COMPÉTENCES
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="sec">
    <span class="ey">Compétences</span>
    <h2 class="h2">Ce que je maîtrise</h2>
    <div class="skills">
      <div class="sg">
        <span class="sg-lbl">Acquisition</span>
        <div class="sr"><span class="sd"></span>Google Ads (Search, Performance Max)</div>
        <div class="sr"><span class="sd"></span>SEO (stratégie + contenu)</div>
        <div class="sr"><span class="sd"></span>Outbound (cold email, LinkedIn)</div>
      </div>
      <div class="sg">
        <span class="sg-lbl">Automation</span>
        <div class="sr"><span class="sd"></span>n8n (workflows complexes)</div>
        <div class="sr"><span class="sd"></span>CRM automation (HubSpot)</div>
        <div class="sr"><span class="sd"></span>Enrichissement data &amp; APIs</div>
        <div class="sr"><span class="sd"></span>Intégrations IA (LLMs)</div>
      </div>
      <div class="sg">
        <span class="sg-lbl">Funnel &amp; Conversion</span>
        <div class="sr"><span class="sd"></span>Structuration MQL &rarr; SQL &rarr; clients</div>
        <div class="sr"><span class="sd"></span>Optimisation de conversion</div>
        <div class="sr"><span class="sd"></span>UX &amp; parcours utilisateur</div>
      </div>
      <div class="sg">
        <span class="sg-lbl">Data</span>
        <div class="sr"><span class="sd"></span>Tracking (GA4, GTM)</div>
        <div class="sr"><span class="sd"></span>Analyse de performance</div>
        <div class="sr"><span class="sd"></span>Dashboarding &amp; reporting</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# STACK
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="sec">
    <span class="ey">Stack</span>
    <h2 class="h2">Outils &amp; technologies</h2>
    <p class="sdesc">Une stack utilisée pour orchestrer le sourcing, la qualification, l&rsquo;automation et le suivi CRM.</p>
    <div class="pills">
      <span class="pill">⚙️&nbsp; n8n</span>
      <span class="pill">🔶&nbsp; HubSpot</span>
      <span class="pill">📢&nbsp; Google Ads</span>
      <span class="pill">🔍&nbsp; SEO</span>
      <span class="pill">📧&nbsp; Brevo</span>
      <span class="pill">📊&nbsp; GA4 + GTM</span>
      <span class="pill">🤖&nbsp; LLMs / IA</span>
      <span class="pill">🔌&nbsp; APIs data</span>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# OBJECTIF
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="sec">
    <div class="obj">
      <span class="ey">Objectif</span>
      <h2 class="obj-h2">Prêt à construire le prochain<br>système d&rsquo;acquisition</h2>
      <p class="obj-sub">Je recherche un CDI dans une startup ou scale-up avec de vrais enjeux d&rsquo;acquisition &mdash; là où il reste des systèmes à construire, pas à maintenir.</p>
      <div class="rpills">
        <span class="rpill">Growth Engineer</span>
        <span class="rpill">Automation Engineer</span>
        <span class="rpill">Growth Systems Engineer</span>
      </div>
      <div class="btns">
        <a href="mailto:alexandre.pineaupoupelin@gmail.com" class="btn-p">&#9993; M&rsquo;écrire directement</a>
        <a href="https://calendly.com/alexandre-pineaupoupelin/30min" target="_blank" class="btn-s">&#128197; Planifier un échange</a>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="sec-last">
    <span class="ey">Contact</span>
    <h2 class="h2">Prenons contact</h2>
    <p class="sdesc">Vous recrutez sur un rôle growth, automation ou marketing ops&nbsp;? Échangeons.</p>
    <div class="contacts">
      <a class="cc" href="mailto:alexandre.pineaupoupelin@gmail.com">
        <span class="cc-ico">&#9993;&#65039;</span>
        <span class="cc-lbl">Email</span>
        <span class="cc-val">alexandre.pineaupoupelin@gmail.com</span>
      </a>
      <a class="cc" href="https://linkedin.com/in/alexandre-pineau-poupelin" target="_blank">
        <span class="cc-ico">&#128188;</span>
        <span class="cc-lbl">LinkedIn</span>
        <span class="cc-val">Voir le profil &rarr;</span>
      </a>
      <a class="cc" href="https://calendly.com/alexandre-pineaupoupelin/30min" target="_blank">
        <span class="cc-ico">&#128197;</span>
        <span class="cc-lbl">Calendly</span>
        <span class="cc-val">Planifier 30 min &rarr;</span>
      </a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="col">
  <div class="foot">
    Alexandre Pineau-Poupelin &middot; Growth Systems Engineer &middot; 2026
  </div>
</div>
""", unsafe_allow_html=True)
