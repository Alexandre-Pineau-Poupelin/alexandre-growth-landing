import streamlit as st

st.set_page_config(
    page_title="Alexandre Pineau-Poupelin — Growth Systems Engineer",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ─── GLOBAL CSS ──────────────────────────────────────────────────────────────

st.markdown("""
<style>
  /* Reset & base */
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

  html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #080c14;
    color: #e2e8f0;
  }

  /* Hide Streamlit chrome */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container {
    padding: 0 !important;
    max-width: 100% !important;
  }

  /* ── Layout wrapper ── */
  .page-wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 24px;
  }

  /* ── Divider ── */
  .section-divider {
    border: none;
    border-top: 1px solid #1e2a3a;
    margin: 80px 0;
  }

  /* ── Section label ── */
  .section-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.15em;
    text-transform: uppercase;
    color: #4a6fa5;
    margin-bottom: 20px;
  }

  /* ── HERO ── */
  .hero-wrapper {
    padding: 120px 0 100px;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(99, 102, 241, 0.12);
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 100px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 500;
    color: #818cf8;
    margin-bottom: 36px;
  }
  .hero-badge::before {
    content: '';
    display: inline-block;
    width: 7px;
    height: 7px;
    background: #4ade80;
    border-radius: 50%;
    box-shadow: 0 0 0 3px rgba(74,222,128,0.2);
    animation: pulse 2s infinite;
  }
  @keyframes pulse {
    0%, 100% { box-shadow: 0 0 0 3px rgba(74,222,128,0.2); }
    50%       { box-shadow: 0 0 0 6px rgba(74,222,128,0.05); }
  }
  .hero-name {
    font-size: clamp(42px, 6vw, 68px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    color: #f8fafc;
    margin: 0 0 12px;
  }
  .hero-title {
    font-size: clamp(20px, 3vw, 28px);
    font-weight: 600;
    color: #6366f1;
    margin: 0 0 28px;
    letter-spacing: -0.01em;
  }
  .hero-subtitle {
    font-size: 17px;
    line-height: 1.7;
    color: #94a3b8;
    max-width: 580px;
    margin: 0 0 48px;
  }
  .hero-subtitle strong { color: #e2e8f0; font-weight: 500; }

  /* ── Buttons ── */
  .btn-row { display: flex; gap: 12px; flex-wrap: wrap; }
  .btn-primary {
    display: inline-flex; align-items: center; gap: 8px;
    background: #6366f1;
    color: #fff !important;
    font-size: 14px; font-weight: 600;
    padding: 12px 24px;
    border-radius: 8px;
    text-decoration: none;
    transition: background 0.2s, transform 0.15s;
  }
  .btn-primary:hover { background: #4f46e5; transform: translateY(-1px); }
  .btn-secondary {
    display: inline-flex; align-items: center; gap: 8px;
    background: transparent;
    color: #94a3b8 !important;
    font-size: 14px; font-weight: 500;
    padding: 12px 24px;
    border-radius: 8px;
    border: 1px solid #1e2a3a;
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s, transform 0.15s;
  }
  .btn-secondary:hover { border-color: #6366f1; color: #e2e8f0 !important; transform: translateY(-1px); }

  /* ── APPROCHE ── */
  .approach-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 32px;
  }
  .approach-card {
    background: #0d1520;
    border: 1px solid #1e2a3a;
    border-radius: 12px;
    padding: 24px;
    transition: border-color 0.2s;
  }
  .approach-card:hover { border-color: #6366f1; }
  .approach-card-icon {
    font-size: 22px;
    margin-bottom: 12px;
  }
  .approach-card-title {
    font-size: 15px;
    font-weight: 600;
    color: #f1f5f9;
    margin-bottom: 8px;
  }
  .approach-card-desc {
    font-size: 14px;
    color: #64748b;
    line-height: 1.6;
  }

  /* ── PROJET REVOLTE ── */
  .project-wrapper {
    background: linear-gradient(135deg, #0d1520 0%, #0f1b2d 100%);
    border: 1px solid #1e2a3a;
    border-radius: 16px;
    padding: 48px;
    position: relative;
    overflow: hidden;
  }
  .project-wrapper::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #06b6d4);
  }
  .project-tag {
    display: inline-block;
    background: rgba(99,102,241,0.12);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 6px;
    padding: 4px 10px;
    font-size: 12px;
    font-weight: 600;
    color: #818cf8;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 20px;
  }
  .project-title {
    font-size: 26px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 8px;
    letter-spacing: -0.02em;
  }
  .project-subtitle {
    font-size: 15px;
    color: #64748b;
    margin-bottom: 32px;
  }
  .metrics-row {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin: 32px 0;
  }
  .metric-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid #1e2a3a;
    border-radius: 10px;
    padding: 20px 16px;
    text-align: center;
  }
  .metric-value {
    font-size: 28px;
    font-weight: 800;
    color: #f8fafc;
    letter-spacing: -0.03em;
    line-height: 1;
  }
  .metric-accent { color: #6366f1; }
  .metric-label {
    font-size: 12px;
    color: #475569;
    margin-top: 6px;
    font-weight: 500;
  }
  .project-list {
    list-style: none;
    padding: 0;
    margin: 0;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 10px;
  }
  .project-list li {
    display: flex;
    align-items: flex-start;
    gap: 10px;
    font-size: 14px;
    color: #94a3b8;
    line-height: 1.5;
  }
  .project-list li::before {
    content: '→';
    color: #6366f1;
    font-weight: 600;
    flex-shrink: 0;
    margin-top: 1px;
  }

  /* ── COMPÉTENCES ── */
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
    margin-top: 32px;
  }
  .skill-group {
    background: #0d1520;
    border: 1px solid #1e2a3a;
    border-radius: 12px;
    padding: 28px;
  }
  .skill-group-title {
    font-size: 13px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #6366f1;
    margin-bottom: 16px;
  }
  .skill-item {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 14px;
    color: #94a3b8;
    padding: 6px 0;
    border-bottom: 1px solid #111827;
  }
  .skill-item:last-child { border-bottom: none; }
  .skill-dot {
    width: 5px; height: 5px;
    background: #6366f1;
    border-radius: 50%;
    flex-shrink: 0;
  }

  /* ── STACK ── */
  .stack-section { margin-top: 32px; }
  .stack-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 16px;
  }
  .stack-pill {
    background: #0d1520;
    border: 1px solid #1e2a3a;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    color: #94a3b8;
    transition: border-color 0.2s, color 0.2s;
    cursor: default;
  }
  .stack-pill:hover { border-color: #6366f1; color: #e2e8f0; }

  /* ── OBJECTIF ── */
  .objectif-wrapper {
    background: linear-gradient(135deg, #0d1520 0%, #100d1f 100%);
    border: 1px solid #1e2a3a;
    border-radius: 16px;
    padding: 48px;
    text-align: center;
  }
  .objectif-title {
    font-size: 28px;
    font-weight: 700;
    color: #f8fafc;
    margin-bottom: 16px;
    letter-spacing: -0.02em;
  }
  .objectif-desc {
    font-size: 16px;
    color: #64748b;
    max-width: 520px;
    margin: 0 auto 28px;
    line-height: 1.7;
  }
  .role-pills {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin-bottom: 32px;
    flex-wrap: wrap;
  }
  .role-pill {
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 100px;
    padding: 8px 20px;
    font-size: 14px;
    font-weight: 600;
    color: #818cf8;
  }

  /* ── CONTACT ── */
  .contact-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin-top: 32px;
  }
  .contact-card {
    background: #0d1520;
    border: 1px solid #1e2a3a;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    text-decoration: none;
    display: block;
    transition: border-color 0.2s, transform 0.15s;
  }
  .contact-card:hover { border-color: #6366f1; transform: translateY(-2px); }
  .contact-card-icon { font-size: 24px; margin-bottom: 12px; }
  .contact-card-label {
    font-size: 13px;
    font-weight: 600;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }
  .contact-card-value {
    font-size: 14px;
    color: #6366f1;
    font-weight: 500;
  }

  /* ── FOOTER ── */
  .footer {
    text-align: center;
    padding: 60px 0 40px;
    font-size: 13px;
    color: #1e2a3a;
  }

  /* ── Section headings ── */
  .section-heading {
    font-size: clamp(24px, 3.5vw, 34px);
    font-weight: 700;
    color: #f8fafc;
    letter-spacing: -0.025em;
    margin: 0 0 10px;
  }
  .section-sub {
    font-size: 16px;
    color: #64748b;
    margin: 0 0 4px;
    line-height: 1.6;
  }
</style>
""", unsafe_allow_html=True)

# ─── HERO ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <div class="hero-wrapper">
    <div class="hero-badge">Disponible · Ouvert aux opportunités CDI</div>
    <h1 class="hero-name">Alexandre<br>Pineau-Poupelin</h1>
    <p class="hero-title">Growth Systems Engineer</p>
    <p class="hero-subtitle">
      Je conçois des <strong>systèmes d'acquisition multi-canaux</strong> — inbound, outbound, automation —
      qui génèrent, qualifient et convertissent des leads en revenu.<br><br>
      Approche orientée <strong>performance</strong>, automatisation et scalabilité.
    </p>
    <div class="btn-row">
      <a href="#projet" class="btn-primary">⚡ Voir le projet clé</a>
      <a href="mailto:alexandre.pineaupoupelin@gmail.com" class="btn-secondary">✉ Me contacter</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── APPROCHE ────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <p class="section-label">Approche</p>
  <h2 class="section-heading">Je construis des systèmes,<br>pas des campagnes</h2>
  <p class="section-sub">
    Chaque levier est pensé en relation avec les autres — acquisition, qualification,
    conversion, revenu forment un seul système cohérent.
  </p>
  <div class="approach-grid">
    <div class="approach-card">
      <div class="approach-card-icon">🔗</div>
      <div class="approach-card-title">Système end-to-end</div>
      <div class="approach-card-desc">Acquisition → qualification → conversion → revenu. Chaque étape est connectée et mesurée.</div>
    </div>
    <div class="approach-card">
      <div class="approach-card-icon">⚙️</div>
      <div class="approach-card-title">Automatisation sans friction</div>
      <div class="approach-card-desc">Workflows orchestrés via n8n et APIs pour scaler sans dépendance aux ressources humaines.</div>
    </div>
    <div class="approach-card">
      <div class="approach-card-icon">📊</div>
      <div class="approach-card-title">Data-driven</div>
      <div class="approach-card-desc">Chaque décision s'appuie sur la donnée. Pas de vanity metrics — que du pipeline et du revenu.</div>
    </div>
    <div class="approach-card">
      <div class="approach-card-icon">🔁</div>
      <div class="approach-card-title">Itération continue</div>
      <div class="approach-card-desc">Test → mesure → optimisation. Cycle court pour valider rapidement et capitaliser sur ce qui fonctionne.</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── PROJET REVOLTE ──────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <p class="section-label">Projet clé</p>
  <div class="project-wrapper" id="projet">
    <div class="project-tag">Cas concret · B2B · PME Tech</div>
    <h2 class="project-title">Revolte — Système d'acquisition B2B automatisé</h2>
    <p class="project-subtitle">Structuration complète de l'acquisition dans une PME tech (mobilité électrique) avec un objectif de pipeline qualifié et scalable.</p>

    <div class="metrics-row">
      <div class="metric-card">
        <div class="metric-value">322</div>
        <div class="metric-label">MQL générés</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">24</div>
        <div class="metric-label">Clients signés</div>
      </div>
      <div class="metric-card">
        <div class="metric-value metric-accent">368K€</div>
        <div class="metric-label">CA généré</div>
      </div>
      <div class="metric-card">
        <div class="metric-value">7,45<span style="font-size:18px;color:#475569">%</span></div>
        <div class="metric-label">Taux MQL → client</div>
      </div>
    </div>

    <ul class="project-list">
      <li>Sourcing multi-sources + enrichissement data</li>
      <li>Segmentation par ICP + lead scoring</li>
      <li>Séquences email automatisées</li>
      <li>Activation multicanale (email + calls)</li>
      <li>Intégration CRM HubSpot complète</li>
      <li>Orchestration des workflows via n8n</li>
      <li>Alignement marketing → sales</li>
      <li>Transmission de leads qualifiés en temps réel</li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── COMPÉTENCES ─────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <p class="section-label">Compétences</p>
  <h2 class="section-heading">Ce que je maîtrise</h2>
  <div class="skills-grid">
    <div class="skill-group">
      <div class="skill-group-title">Acquisition</div>
      <div class="skill-item"><span class="skill-dot"></span>Google Ads (Search, Performance Max)</div>
      <div class="skill-item"><span class="skill-dot"></span>SEO (stratégie + contenu)</div>
      <div class="skill-item"><span class="skill-dot"></span>Outbound (cold email, LinkedIn)</div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">Automation</div>
      <div class="skill-item"><span class="skill-dot"></span>n8n (workflows complexes)</div>
      <div class="skill-item"><span class="skill-dot"></span>CRM automation (HubSpot)</div>
      <div class="skill-item"><span class="skill-dot"></span>Enrichissement data & APIs</div>
      <div class="skill-item"><span class="skill-dot"></span>Intégrations IA (LLMs)</div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">Funnel & Conversion</div>
      <div class="skill-item"><span class="skill-dot"></span>Structuration MQL → SQL → clients</div>
      <div class="skill-item"><span class="skill-dot"></span>Optimisation de conversion</div>
      <div class="skill-item"><span class="skill-dot"></span>UX & parcours utilisateur</div>
    </div>
    <div class="skill-group">
      <div class="skill-group-title">Data</div>
      <div class="skill-item"><span class="skill-dot"></span>Tracking (GA4, GTM)</div>
      <div class="skill-item"><span class="skill-dot"></span>Analyse de performance</div>
      <div class="skill-item"><span class="skill-dot"></span>Dashboarding & reporting</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── STACK ───────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <p class="section-label">Stack</p>
  <h2 class="section-heading">Outils & technologies</h2>
  <p class="section-sub">Les outils que j'utilise quotidiennement pour concevoir et opérer des systèmes d'acquisition.</p>
  <div class="stack-pills">
    <span class="stack-pill">⚙️ n8n</span>
    <span class="stack-pill">🔶 HubSpot</span>
    <span class="stack-pill">📢 Google Ads</span>
    <span class="stack-pill">🔍 SEO</span>
    <span class="stack-pill">📧 Brevo</span>
    <span class="stack-pill">📊 GA4 + GTM</span>
    <span class="stack-pill">🤖 LLMs / IA</span>
    <span class="stack-pill">🔌 APIs data</span>
    <span class="stack-pill">📋 Clay</span>
    <span class="stack-pill">📱 LinkedIn Sales Nav</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── OBJECTIF ────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <div class="objectif-wrapper">
    <p class="section-label" style="text-align:center;">Objectif</p>
    <h2 class="objectif-title">Prêt à construire le prochain<br>système d'acquisition</h2>
    <p class="objectif-desc">
      Je recherche un CDI dans une startup ou scale-up avec de vrais enjeux d'acquisition et
      de structuration du funnel — là où il reste des systèmes à construire, pas à maintenir.
    </p>
    <div class="role-pills">
      <span class="role-pill">Growth Engineer</span>
      <span class="role-pill">Automation Engineer</span>
      <span class="role-pill">Growth Systems Engineer</span>
    </div>
    <div class="btn-row" style="justify-content:center;">
      <a href="mailto:alexandre.pineaupoupelin@gmail.com" class="btn-primary">✉ Discutons-en</a>
      <a href="https://linkedin.com/in/alexandre-pineau-poupelin" class="btn-secondary">LinkedIn →</a>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── CONTACT ─────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <hr class="section-divider">
  <p class="section-label">Contact</p>
  <h2 class="section-heading">Prenons contact</h2>
  <p class="section-sub">Disponible pour des échanges sur des projets growth, automation ou systèmes d'acquisition.</p>
  <div class="contact-grid">
    <a class="contact-card" href="mailto:alexandre.pineaupoupelin@gmail.com">
      <div class="contact-card-icon">✉️</div>
      <div class="contact-card-label">Email</div>
      <div class="contact-card-value">alexandre.pineaupoupelin@gmail.com</div>
    </a>
    <a class="contact-card" href="https://linkedin.com/in/alexandre-pineau-poupelin" target="_blank">
      <div class="contact-card-icon">💼</div>
      <div class="contact-card-label">LinkedIn</div>
      <div class="contact-card-value">Voir le profil →</div>
    </a>
    <a class="contact-card" href="tel:+33600000000">
      <div class="contact-card-icon">📞</div>
      <div class="contact-card-label">Téléphone</div>
      <div class="contact-card-value">Sur demande</div>
    </a>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── FOOTER ──────────────────────────────────────────────────────────────────

st.markdown("""
<div class="page-wrapper">
  <div class="footer">
    Alexandre Pineau-Poupelin · Growth Systems Engineer · 2025
  </div>
</div>
""", unsafe_allow_html=True)
