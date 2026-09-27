"""
Rajasekaran M - Professional AI/ML & Cloud Engineer Portfolio Website
Built with Streamlit & Bespoke Dark Glassmorphism Styling.
Fully compatible with local execution and Streamlit Community Cloud.
"""

import os
import base64
import streamlit as st
from data.portfolio_data import (
    PROFILE,
    CERTIFICATIONS,
    PROJECTS,
    INTERNSHIPS,
    EDUCATION,
    SKILLS_CATEGORIES
)

# -----------------------------------------------------------------------------
# 1. Page Configuration
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title=f"{PROFILE['name']} | {PROFILE['role']}",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# -----------------------------------------------------------------------------
# 2. Helpers for Assets & Base64 Encoding
# -----------------------------------------------------------------------------
def get_file_base64(file_path: str) -> str:
    """Reads a file and returns its base64 string."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def load_css(css_file_path: str):
    """Loads and injects custom CSS into the Streamlit app via st.html."""
    if os.path.exists(css_file_path):
        with open(css_file_path, "r", encoding="utf-8") as f:
            css_data = f.read()
            st.html(f"<style>{css_data}</style>")

# Inject custom styles
load_css("styles/custom.css")

# Load Avatar and Resume
avatar_b64 = get_file_base64("assets/profile.png")
avatar_src = f"data:image/png;base64,{avatar_b64}" if avatar_b64 else "https://github.com/rajasekaran12345.png"

resume_pdf_path = "assets/resume.pdf"
resume_bytes = None
if os.path.exists(resume_pdf_path):
    with open(resume_pdf_path, "rb") as f:
        resume_bytes = f.read()

# -----------------------------------------------------------------------------
# 3. Top Navigation Bar (Clean Name without Thunderbolt)
# -----------------------------------------------------------------------------
st.html(f"""
<div class="nav-container">
    <div class="nav-brand">{PROFILE['name']}</div>
    <div class="nav-links">
        <a href="#about" class="nav-item">About</a>
        <a href="#certifications" class="nav-item">Certifications</a>
        <a href="#projects" class="nav-item">Projects</a>
        <a href="#experience" class="nav-item">Experience</a>
        <a href="#skills" class="nav-item">Skills</a>
        <a href="Resume" target="_self" class="nav-item" style="color: var(--accent-cyan); font-weight: 700;">Resume ↗</a>
        <a href="#contact" class="nav-item">Contact</a>
    </div>
    <div class="status-pill">
        <span class="status-dot"></span>
        <span>Open to Opportunities</span>
    </div>
</div>
""")

# -----------------------------------------------------------------------------
# 4. Hero Section (Plain text email without hyperlink, no thunderbolt)
# -----------------------------------------------------------------------------
col_hero_avatar, col_hero_info = st.columns([1, 3.5], gap="large")

with col_hero_avatar:
    st.html(f"""
    <div style="display: flex; justify-content: center; align-items: center; padding-top: 10px;">
        <img src="{avatar_src}" class="hero-avatar" alt="{PROFILE['name']}">
    </div>
    """)

with col_hero_info:
    st.html(f"""
    <div>
        <div class="status-pill" style="margin-bottom: 8px;">
            <span class="status-dot"></span>
            <span>{PROFILE['location']}</span>
        </div>
        <div class="hero-name">{PROFILE['name']}</div>
        <div class="hero-role-badge">{PROFILE['role']}</div>
        <p style="color: var(--text-secondary); font-size: 1.05rem; line-height: 1.6; margin: 0 0 16px 0;">
            Specializing in Deep Learning, Computer Vision (YOLO-OBB), Generative AI (RAG & Agentic workflows), 
            and scalable AWS Cloud & MLOps infrastructure.
        </p>
        <div class="action-btn-row">
            <a href="Resume" target="_self" class="action-pill action-pill-primary">📄 View / Download Resume</a>
            <a href="#certifications" class="action-pill">🎖️ View Certifications</a>
            <a href="{PROFILE['linkedin']}" target="_blank" class="action-pill">💼 LinkedIn</a>
            <a href="{PROFILE['github']}" target="_blank" class="action-pill">🐙 GitHub</a>
            <a href="{PROFILE['credly']}" target="_blank" class="action-pill">🌐 Credly</a>
            <div class="action-pill-static">✉️ {PROFILE['email']}</div>
        </div>
    </div>
    """)

st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 5. Quick Stats Row
# -----------------------------------------------------------------------------
stat_cols = st.columns(4)
for i, stat in enumerate(PROFILE["stats"]):
    with stat_cols[i]:
        st.html(f"""
        <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 14px; padding: 18px 20px; text-align: center; backdrop-filter: blur(12px);">
            <div style="font-size: 1.8rem; font-weight: 800; color: #ffffff; background: linear-gradient(135deg, #ffffff, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">{stat['metric']}</div>
            <div style="font-size: 0.82rem; font-weight: 600; color: var(--accent-cyan); text-transform: uppercase; letter-spacing: 0.5px; margin-top: 4px;">{stat['label']}</div>
        </div>
        """)

# -----------------------------------------------------------------------------
# 6. About Me Section
# -----------------------------------------------------------------------------
st.markdown('<div id="about"></div>', unsafe_allow_html=True)
st.html(f"""
<div class="section-title">
    <span>💡</span> About Me
</div>
<div class="section-subtitle">A brief overview of my engineering philosophy, background, and vision.</div>
<div class="about-box">
    <div style="font-size: 1.8rem; line-height: 1; color: var(--accent-indigo); margin-bottom: 8px;">“</div>
    {PROFILE['about_me']}
    <div style="font-size: 1.8rem; line-height: 1; color: var(--accent-indigo); text-align: right; margin-top: -10px;">”</div>
</div>
""")

# -----------------------------------------------------------------------------
# 7. Credly Certifications Showcase (Hyperlinked Badges + Real Dates + Pure HTML)
# -----------------------------------------------------------------------------
st.markdown('<div id="certifications"></div>', unsafe_allow_html=True)
st.html("""
<div class="section-title">
    <span>🎖️</span> AWS Certifications & Credly Badges
</div>
<div class="section-subtitle">
    Verified digital credentials from Amazon Web Services. Click any badge to verify directly on Credly.
</div>
""")

# Render badge cards with st.html to guarantee zero Markdown code-block parsing
cert_cards_html = []
for cert in CERTIFICATIONS:
    local_b64 = get_file_base64(cert["local_image"])
    img_src = f"data:image/png;base64,{local_b64}" if local_b64 else cert["remote_image"]
    
    if cert["is_expiring"]:
        exp_badge_html = f'<span class="credly-date-val-exp">⏳ {cert["expires_date"]}</span>'
    else:
        exp_badge_html = f'<span class="credly-date-val-life">✅ {cert["expires_date"]}</span>'

    card_html = (
        f'<a href="{cert["verification_url"]}" target="_blank" class="credly-card-link">'
        f'<div class="credly-card">'
        f'<div class="credly-badge-img-wrapper">'
        f'<img src="{img_src}" class="credly-badge-img" alt="{cert["title"]}">'
        f'</div>'
        f'<div class="credly-title">{cert["title"]}</div>'
        f'<div class="credly-issuer">{cert["issuer"]}</div>'
        f'<div class="credly-dates-box">'
        f'<div class="credly-date-row"><span>Issued:</span><span class="credly-date-val">📅 {cert["issued_date"]}</span></div>'
        f'<div class="credly-date-row"><span>Expires:</span>{exp_badge_html}</div>'
        f'</div>'
        f'<div class="credly-verify-btn"><span>Verify on Credly</span> <span>↗</span></div>'
        f'</div>'
        f'</a>'
    )
    cert_cards_html.append(card_html)

grid_container_html = (
    '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 24px; margin-bottom: 45px;">'
    + ''.join(cert_cards_html)
    + '</div>'
)
st.html(grid_container_html)

# -----------------------------------------------------------------------------
# 8. Featured Projects Showcase
# -----------------------------------------------------------------------------
st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
st.html("""
<div class="section-title">
    <span>🚀</span> Featured Projects
</div>
<div class="section-subtitle">
    Spotlight production systems and deep learning implementations from my GitHub repository.
</div>
""")

proj_cols = st.columns(len(PROJECTS), gap="large")

for idx, proj in enumerate(PROJECTS):
    with proj_cols[idx]:
        tech_tags_html = "".join([f'<span class="tech-pill">{t}</span>' for t in proj["tech_stack"]])
        highlights_html = "".join([f'<li>{h}</li>' for h in proj["highlights"]])
        
        project_html = (
            f'<a href="{proj["repo_url"]}" target="_blank" class="project-card-link">'
            f'<div class="project-card">'
            f'<span class="project-cat-badge">{proj["category"]}</span>'
            f'<div class="project-title">{proj["name"]}</div>'
            f'<div class="project-desc">{proj["description"]}</div>'
            f'<ul class="project-highlights-list">{highlights_html}</ul>'
            f'<div class="tech-pills-row">{tech_tags_html}</div>'
            f'<div class="project-cta"><span>Explore on GitHub</span> <span>→</span></div>'
            f'</div>'
            f'</a>'
        )
        st.html(project_html)

st.markdown("<div style='margin-bottom: 40px;'></div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 9. Professional Experience & Internships
# -----------------------------------------------------------------------------
st.markdown('<div id="experience"></div>', unsafe_allow_html=True)
st.html("""
<div class="section-title">
    <span>💼</span> Internship Experience
</div>
<div class="section-subtitle">
    Hands-on industry engineering in Computer Vision, drone inspection, and Enterprise Business Analytics.
</div>
""")

for exp in INTERNSHIPS:
    bullets_html = "".join([f"<li>{b}</li>" for b in exp["highlights"]])
    st.html(f"""
    <div class="exp-card">
        <div class="exp-header">
            <span class="exp-role">{exp['role']}</span>
            <span class="exp-period">{exp['period']}</span>
        </div>
        <div class="exp-company">{exp['company']} &nbsp;•&nbsp; <span style="color: var(--text-muted); font-size: 0.85rem;">{exp['location']}</span></div>
        <ul class="exp-bullets">
            {bullets_html}
        </ul>
    </div>
    """)

# -----------------------------------------------------------------------------
# 10. Education
# -----------------------------------------------------------------------------
st.html("""
<div class="section-title" style="margin-top: 25px;">
    <span>🎓</span> Education & Academic Background
</div>
<div class="section-subtitle">
    Advanced academic grounding in Applied Data Science and Computer Science.
</div>
""")

edu_cols = st.columns(len(EDUCATION), gap="large")
for i, edu in enumerate(EDUCATION):
    with edu_cols[i]:
        st.html(f"""
        <div class="exp-card" style="height: 100%;">
            <div class="exp-header">
                <span class="exp-role" style="font-size: 1.05rem;">{edu['degree']}</span>
                <span class="exp-period">{edu['period']}</span>
            </div>
            <div class="exp-company" style="margin-bottom: 8px;">{edu['institution']}</div>
            <div style="display: inline-block; background: rgba(99, 102, 241, 0.15); border: 1px solid rgba(99, 102, 241, 0.3); color: #c7d2fe; font-size: 0.82rem; font-weight: 700; padding: 3px 10px; border-radius: 6px; margin-bottom: 10px;">
                {edu['score']}
            </div>
            <p style="color: var(--text-secondary); font-size: 0.88rem; line-height: 1.5; margin: 0;">
                {edu['details']}
            </p>
        </div>
        """)

# -----------------------------------------------------------------------------
# 11. Technical Skills Matrix
# -----------------------------------------------------------------------------
st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
st.html("""
<div class="section-title">
    <span>🛠️</span> Technical Skills & Competencies
</div>
<div class="section-subtitle">
    Core competencies across Artificial Intelligence, Cloud Infrastructure, and Software Engineering.
</div>
""")

skill_cols = st.columns(len(SKILLS_CATEGORIES), gap="medium")
for i, cat in enumerate(SKILLS_CATEGORIES):
    with skill_cols[i]:
        pills_html = "".join([f'<span class="skill-pill-tag">{s}</span>' for s in cat["skills"]])
        st.html(f"""
        <div class="skill-cat-card">
            <div class="skill-cat-title">
                <span>{cat['icon']}</span>
                <span>{cat['category']}</span>
            </div>
            <div class="skill-pills-wrap">
                {pills_html}
            </div>
        </div>
        """)

# -----------------------------------------------------------------------------
# 12. Resume Hub & Quick Download
# -----------------------------------------------------------------------------
st.markdown('<div id="resume"></div>', unsafe_allow_html=True)
st.html("""
<div class="section-title">
    <span>📄</span> Resume & Curriculum Vitae
</div>
<div class="section-subtitle">
    Review verified qualifications or download the ATS-ready PDF.
</div>
""")

resume_box_col1, resume_box_col2 = st.columns([1.8, 1], gap="large")

with resume_box_col1:
    st.html("""
    <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: var(--radius-md); padding: 24px 28px; backdrop-filter: blur(12px);">
        <h4 style="color: #ffffff; margin: 0 0 10px 0;">Official Candidate Resume</h4>
        <p style="color: var(--text-secondary); font-size: 0.92rem; line-height: 1.6; margin-bottom: 16px;">
            The official resume contains complete details on education, AWS credentials, industrial internships 
            at Lesoko Technologies and Client Linx, and production AI projects. Phone numbers have been strictly 
            withheld for privacy; direct contact is maintained via verified email and LinkedIn.
        </p>
        <a href="Resume" target="_self" class="action-pill action-pill-primary" style="font-size: 0.88rem;">
            📄 Open Dedicated Full Resume Page ↗
        </a>
    </div>
    """)

with resume_box_col2:
    if resume_bytes:
        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)
        st.download_button(
            label="📥 Download Official Resume (PDF)",
            data=resume_bytes,
            file_name="Rajasekaran_M_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.html(f"""
        <div style="text-align: center; margin-top: 14px;">
            <a href="{PROFILE['linkedin']}" target="_blank" style="color: var(--accent-cyan); text-decoration: none; font-size: 0.88rem; font-weight: 600;">
                Connect on LinkedIn ↗
            </a>
        </div>
        """)

# -----------------------------------------------------------------------------
# 13. Contact Hub & Footer (Plain Text Email, No Thunderbolt)
# -----------------------------------------------------------------------------
st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
st.html(f"""
<div class="portfolio-footer">
    <div class="footer-social-row">
        <span class="footer-plain-text">✉️ {PROFILE['email']}</span>
        <a href="{PROFILE['linkedin']}" target="_blank" class="footer-link">💼 LinkedIn</a>
        <a href="{PROFILE['github']}" target="_blank" class="footer-link">🐙 GitHub</a>
        <a href="{PROFILE['credly']}" target="_blank" class="footer-link">🌐 Credly</a>
    </div>
    <div style="color: var(--text-muted); font-size: 0.82rem; margin-top: 10px;">
        Designed & Engineered with Python & Streamlit • © 2026 {PROFILE['name']}. All Rights Reserved.
    </div>
</div>
""")
