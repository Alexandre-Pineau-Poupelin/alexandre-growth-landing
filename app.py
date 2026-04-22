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
  --bg:    #06060b;
  --surf:  #0c0c15;
  --surf2: #111120;
  --bdr:   rgba(255,255,255,0.07);
  --bdr-a: rgba(99,102,241,0.38);
  --acc:   #6366f1;
  --acc-lo:rgba(99,102,241,0.1);
  --vio:   #8b5cf6;
  --cyn:   #22d3ee;
  --t1:    #ededf5;
  --t2:    #9090b8;
  --t3:    #44445c;
  --grn:   #22c55e;
  --r:     12px;
  --rL:    16px;
  --f:     'Inter', -apple-system, sans-serif;
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

.main .block-container,
[data-testid="block-container"] {
  max-width: 1204px !important;
  padding: 0 52px !important;
  margin: 0 auto !important;
}

/* Remove Streamlit's default markdown spacing */
[data-testid="stMarkdown"] > div { margin-bottom: 0 !important; }

/* ── Page width wrapper (passthrough — centering handled by block-container) ── */
.w { max-width: 100%; margin: 0; padding: 0; }

/* ── Section ── */
.sec { padding: 96px 0; border-top: 1px solid var(--bdr); }
.sec-last { padding: 96px 0 0; border-top: 1px solid var(--bdr); }

/* ── Eyebrow ── */
.ey {
  display: block;
  font-size: 11px; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 16px; line-height: 1.4;
  text-align: center;
}

/* ── Headings ── */
.h2 {
  font-size: clamp(28px, 3.3vw, 40px);
  font-weight: 700; line-height: 1.1;
  letter-spacing: -0.028em;
  color: var(--t1); margin-bottom: 12px;
  text-align: center;
}
.sdesc {
  font-size: 16px; color: var(--t2);
  line-height: 1.72; max-width: 720px;
  font-weight: 400; letter-spacing: -0.008em;
  margin: 0 auto; text-align: center;
}

/* ══════════════════════════════
   HERO
══════════════════════════════ */
.hero { padding: 110px 0 96px; text-align: center; }

.badge {
  display: inline-flex; align-items: center; gap: 10px;
  background: rgba(34,197,94,0.07);
  border: 1px solid rgba(34,197,94,0.18);
  border-radius: 100px;
  padding: 8px 18px; margin-bottom: 42px;
  font-size: 13px; font-weight: 500; color: #86efac; line-height: 1.4;
}
.bdot {
  display: inline-block; width: 7px; height: 7px;
  background: var(--grn); border-radius: 50%; flex-shrink: 0;
  animation: pdot 2.8s ease infinite;
}
@keyframes pdot {
  0%,100% { box-shadow: 0 0 0 0 rgba(34,197,94,0.4); }
  50%      { box-shadow: 0 0 0 7px rgba(34,197,94,0); }
}
.hero-role {
  font-size: 13px; font-weight: 600;
  letter-spacing: 0.18em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 18px; line-height: 1.4;
}
.hero-name {
  font-size: clamp(48px, 7vw, 86px);
  font-weight: 800; line-height: 0.97;
  letter-spacing: -0.044em; color: var(--t1); margin-bottom: 28px;
}
.hero-val {
  font-size: clamp(17px, 1.9vw, 20px);
  line-height: 1.72; color: var(--t2);
  max-width: 680px; margin: 0 auto 52px;
  font-weight: 400; letter-spacing: -0.01em; text-align: center;
}
.hero-val strong { color: var(--t1); font-weight: 500; }

.btns { display: flex; gap: 12px; flex-wrap: wrap; align-items: center; justify-content: center; }
.btn-p {
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--acc); color: #fff !important;
  font-size: 14px; font-weight: 600;
  padding: 14px 28px; border-radius: 8px;
  text-decoration: none !important; letter-spacing: -0.012em;
  transition: background .2s, transform .15s, box-shadow .2s;
}
.btn-p:hover { background: #4f46e5; transform: translateY(-1px); box-shadow: 0 12px 32px rgba(99,102,241,0.3); }
.btn-s {
  display: inline-flex; align-items: center; gap: 8px;
  background: transparent; color: var(--t2) !important;
  font-size: 14px; font-weight: 500;
  padding: 14px 28px; border-radius: 8px;
  border: 1px solid var(--bdr);
  text-decoration: none !important; letter-spacing: -0.012em;
  transition: border-color .2s, color .2s, transform .15s;
}
.btn-s:hover { border-color: var(--bdr-a); color: var(--t1) !important; transform: translateY(-1px); }

/* ══════════════════════════════
   APPROACH CARDS
══════════════════════════════ */
.cards { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 44px; }
.card {
  flex: 1 1 calc(50% - 7px); min-width: 280px;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 30px 32px;
  transition: border-color .25s, background .2s;
}
.card:hover { border-color: rgba(99,102,241,0.28); background: var(--surf2); }
.c-ico { font-size: 22px; display: block; margin-bottom: 14px; line-height: 1; }
.c-ttl { font-size: 15px; font-weight: 600; color: var(--t1); margin-bottom: 8px; letter-spacing: -0.01em; line-height: 1.35; }
.c-dsc { font-size: 14px; color: var(--t2); line-height: 1.65; }

/* ══════════════════════════════
   PROJET CLÉ — Native Streamlit elements
══════════════════════════════ */

/* st.divider() → <hr> : section separator */
hr {
  border: none !important;
  border-top: 1px solid var(--bdr) !important;
  margin: 0 !important;
}

/* Eyebrow from ##### markdown */
h5 {
  font-size: 11px !important; font-weight: 600 !important;
  letter-spacing: 0.18em !important; text-transform: uppercase !important;
  color: var(--acc) !important; margin: 0 0 12px !important; line-height: 1.4 !important;
  text-align: center !important;
}

/* Section title from ### markdown */
h3 {
  font-size: clamp(26px, 3vw, 36px) !important;
  font-weight: 700 !important; line-height: 1.1 !important;
  letter-spacing: -0.028em !important;
  color: var(--t1) !important; margin: 4px 0 16px !important;
  text-align: center !important;
}

/* Description paragraph (no class = native markdown) */
p:not([class]) {
  color: var(--t2) !important; font-size: 16px !important;
  line-height: 1.72 !important; letter-spacing: -0.008em !important;
  text-align: center !important;
  max-width: 720px !important; margin-left: auto !important; margin-right: auto !important;
}

/* Actions sub-label: lone **bold** in a paragraph */
[data-testid="stMarkdown"] p strong:only-child {
  font-size: 11px !important; font-weight: 700 !important;
  letter-spacing: 0.16em !important; text-transform: uppercase !important;
  color: var(--t3) !important;
}

/* st.metric() card */
[data-testid="stMetric"] {
  background: var(--surf) !important;
  border: 1px solid var(--bdr) !important;
  border-radius: var(--r) !important;
  padding: 28px 20px !important;
  text-align: center !important;
}
[data-testid="stMetricValue"] div {
  font-size: 32px !important; font-weight: 800 !important;
  letter-spacing: -0.04em !important;
  color: var(--t1) !important; line-height: 1 !important;
}
[data-testid="stMetricLabel"] {
  font-size: 12px !important; font-weight: 500 !important;
  color: var(--t3) !important; text-align: center !important;
  letter-spacing: 0.03em !important; text-transform: uppercase !important;
}
[data-testid="stMetricDelta"] { display: none !important; }

/* Action list from st.markdown("- item") */
[data-testid="stMarkdown"] ul {
  padding: 0 !important; margin: 0 !important;
  list-style: none !important;
}
[data-testid="stMarkdown"] ul li {
  padding: 9px 0 !important;
  color: var(--t2) !important; font-size: 14px !important;
  line-height: 1.6 !important; letter-spacing: -0.008em !important;
  border-bottom: 1px solid rgba(255,255,255,0.04) !important;
  list-style-type: '→  ' !important;
}
[data-testid="stMarkdown"] ul li:last-child { border-bottom: none !important; }

/* ══════════════════════════════
   COMPÉTENCES
══════════════════════════════ */
.skills { display: flex; flex-wrap: wrap; gap: 14px; margin-top: 44px; }
.sg {
  flex: 1 1 calc(50% - 7px); min-width: 280px;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 30px 32px;
}
.sg-lbl {
  display: block; font-size: 11px; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--acc); margin-bottom: 20px; line-height: 1.4;
}
.sr {
  display: flex; align-items: center; gap: 12px;
  font-size: 14px; color: var(--t2);
  padding: 10px 0; border-bottom: 1px solid rgba(255,255,255,0.05);
  line-height: 1.45; letter-spacing: -0.008em;
}
.sr:last-child { border-bottom: none; }
.sd { width: 5px; height: 5px; background: var(--acc); border-radius: 50%; flex-shrink: 0; opacity: 0.65; }

/* ══════════════════════════════
   STACK
══════════════════════════════ */
.pills { display: flex; flex-wrap: wrap; gap: 10px; margin-top: 36px; justify-content: center; }
.pill {
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: 8px; padding: 11px 20px;
  font-size: 14px; font-weight: 500; color: var(--t2);
  transition: border-color .2s, color .2s;
  cursor: default; letter-spacing: -0.012em; line-height: 1.4;
}
.pill:hover { border-color: var(--bdr-a); color: var(--t1); }

/* ══════════════════════════════
   OBJECTIF
══════════════════════════════ */
.obj {
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL);
  padding: 70px 48px; text-align: center;
}
.obj-h2 {
  font-size: clamp(26px, 3vw, 38px);
  font-weight: 700; letter-spacing: -0.028em;
  color: var(--t1); margin-bottom: 18px; line-height: 1.12;
}
.obj-sub {
  font-size: 17px; color: var(--t2);
  line-height: 1.72; max-width: 500px;
  margin: 0 auto 36px; letter-spacing: -0.01em;
}
.rpills { display: flex; justify-content: center; gap: 10px; flex-wrap: wrap; margin-bottom: 40px; }
.rpill {
  background: var(--acc-lo); border: 1px solid rgba(99,102,241,0.2);
  border-radius: 100px; padding: 9px 22px;
  font-size: 14px; font-weight: 600; color: #a5b4fc; letter-spacing: -0.012em; line-height: 1.4;
}

/* ══════════════════════════════
   CONTACT
══════════════════════════════ */
.contacts { display: flex; gap: 14px; margin-top: 44px; }
.cc {
  flex: 1;
  background: var(--surf); border: 1px solid var(--bdr);
  border-radius: var(--rL); padding: 34px 24px;
  text-align: center; text-decoration: none; display: block;
  transition: border-color .2s, transform .15s, background .2s;
}
.cc:hover { border-color: rgba(99,102,241,0.3); background: var(--surf2); transform: translateY(-2px); }
.cc-ico { font-size: 28px; margin-bottom: 16px; display: block; line-height: 1; }
.cc-lbl {
  display: block; font-size: 11px; font-weight: 700;
  letter-spacing: 0.16em; text-transform: uppercase;
  color: var(--t3); margin-bottom: 10px; line-height: 1.4;
}
.cc-val { font-size: 14px; color: var(--acc); font-weight: 500; line-height: 1.5; }

/* ══════════════════════════════
   FOOTER
══════════════════════════════ */
.foot {
  border-top: 1px solid var(--bdr);
  margin-top: 96px; padding: 40px 0;
  text-align: center; font-size: 13px;
  color: var(--t3); letter-spacing: 0.02em; line-height: 1.4;
}

/* ══════════════════════════════
   RESPONSIVE — tablet (≤ 900px)
══════════════════════════════ */
@media (max-width: 900px) {
  .main .block-container,
  [data-testid="block-container"] {
    padding: 0 32px !important;
  }

  .sec, .sec-last { padding: 72px 0; }

  .h2 { font-size: 28px !important; }

  .cards, .skills { gap: 12px; }
  .card, .sg { flex: 1 1 100% !important; min-width: 0 !important; }

  .contacts { flex-wrap: wrap; gap: 12px; }
  .cc { flex: 1 1 calc(50% - 6px) !important; min-width: 0 !important; }

  .obj { padding: 52px 36px; }
  .obj-h2 { font-size: 28px !important; }

  .rpills { gap: 8px; margin-bottom: 32px; }

  .foot { margin-top: 72px; }
}

/* ══════════════════════════════
   RESPONSIVE — mobile (≤ 640px)
══════════════════════════════ */
@media (max-width: 640px) {
  /* Layout */
  .main .block-container,
  [data-testid="block-container"] {
    padding: 0 20px !important;
  }

  /* Sections */
  .sec, .sec-last { padding: 60px 0; }

  /* Hero */
  .hero { padding: 72px 0 56px; }
  .hero-name { font-size: 40px !important; letter-spacing: -0.035em !important; }
  .hero-val  { font-size: 16px !important; margin-bottom: 40px !important; }
  .badge     { font-size: 12px !important; padding: 7px 14px !important; }
  .btns      { flex-direction: column; gap: 10px; }
  .btn-p, .btn-s { justify-content: center; width: 100%; max-width: 320px; }

  /* Headings */
  .h2  { font-size: 24px !important; }
  h3   { font-size: 22px !important; }
  h5   { font-size: 11px !important; }

  /* Description */
  p:not([class]) { font-size: 15px !important; }

  /* Approach cards → 1 column */
  .cards { flex-direction: column; }
  .card  { flex: 1 1 100% !important; min-width: 0 !important; padding: 24px; }

  /* Skills → 1 column */
  .skills { flex-direction: column; }
  .sg     { flex: 1 1 100% !important; min-width: 0 !important; padding: 24px; }

  /* Pills */
  .pills { gap: 8px; margin-top: 24px; }
  .pill  { padding: 9px 16px !important; font-size: 13px !important; }

  /* Objectif */
  .obj    { padding: 44px 20px; }
  .obj-h2 { font-size: 24px !important; }
  .obj-sub { font-size: 15px !important; margin-bottom: 28px; }
  .rpills { flex-direction: column; align-items: center; }
  .rpill  { width: 100%; max-width: 280px; text-align: center; }
  .btns[style*="justify-content:center"] { align-items: center; }

  /* Contact → 1 column */
  .contacts { flex-direction: column; }
  .cc { flex: 1 1 100% !important; padding: 28px 20px; }

  /* Native Streamlit columns → stack on mobile */
  [data-testid="stHorizontalBlock"] {
    flex-wrap: wrap !important;
  }
  [data-testid="stHorizontalBlock"] > [data-testid="column"] {
    min-width: calc(50% - 7px) !important;
    flex: 1 1 calc(50% - 7px) !important;
  }

  /* Footer */
  .foot { margin-top: 60px; padding: 32px 0; font-size: 12px; }
}

/* ══════════════════════════════
   RESPONSIVE — small mobile (≤ 420px)
══════════════════════════════ */
@media (max-width: 420px) {
  .main .block-container,
  [data-testid="block-container"] {
    padding: 0 16px !important;
  }

  .hero-name { font-size: 34px !important; }

  /* Metric columns → 2×2 grid */
  [data-testid="stHorizontalBlock"] > [data-testid="column"] {
    min-width: calc(50% - 7px) !important;
    flex: 1 1 calc(50% - 7px) !important;
  }

  [data-testid="stMetric"] { padding: 20px 12px !important; }
  [data-testid="stMetricValue"] div { font-size: 26px !important; }
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# HERO
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="w">
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
<div class="w">
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
# PROJET REVOLTE
# ══════════════════════════════════════════════════════════════

# ══════════════════════════════════════════════════════════════
# PROJET CLÉ — 100 % native Streamlit
# ══════════════════════════════════════════════════════════════

st.divider()

st.markdown("##### Cas concret · B2B · PME Tech")
st.markdown("### Construction d'un système d'acquisition B2B — de zéro à 368 K€")
st.markdown(
    "Point de départ : aucun système structuré, pas de pipeline exploitable. "
    "Mission : concevoir un système d'acquisition B2B capable de générer, qualifier et transmettre des leads directement exploitables par les équipes sales."
)

st.write("")

# ── Métriques ──
_m1, _m2, _m3, _m4 = st.columns(4)
_m1.metric("MQL générés",        "322")
_m2.metric("Clients signés",     "24")
_m3.metric("CA généré",          "368 K€")
_m4.metric("Taux MQL → client",  "7,45 %")

st.write("")
st.markdown("**Ce que j'ai mis en place**")
st.write("")

# ── Actions (2 colonnes) ──
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
<div class="w">
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
<div class="w">
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
<div class="w">
  <div class="sec">
    <div class="obj">
      <span class="ey" style="text-align:center;">Objectif</span>
      <h2 class="obj-h2">Prêt à construire le prochain<br>système d&rsquo;acquisition</h2>
      <p class="obj-sub">Je recherche un CDI dans une startup ou scale-up avec de vrais enjeux d&rsquo;acquisition &mdash; là où il reste des systèmes à construire, pas à maintenir.</p>
      <div class="rpills">
        <span class="rpill">Growth Engineer</span>
        <span class="rpill">Automation Engineer</span>
        <span class="rpill">Growth Systems Engineer</span>
      </div>
      <div class="btns" style="justify-content:center;">
        <a href="mailto:alexandre.pineaupoupelin@gmail.com" class="btn-p">&#9993; M&rsquo;écrire directement</a>
        <a href="https://linkedin.com/in/alexandre-pineau-poupelin" class="btn-s">LinkedIn &rarr;</a>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# CONTACT
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="w">
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
      <div class="cc">
        <span class="cc-ico">&#128222;</span>
        <span class="cc-lbl">Téléphone</span>
        <span class="cc-val">Sur demande</span>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════

st.markdown("""
<div class="w">
  <div class="foot">
    Alexandre Pineau-Poupelin &middot; Growth Systems Engineer &middot; 2026
  </div>
</div>
""", unsafe_allow_html=True)
