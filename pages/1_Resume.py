"""
Rajasekaran M - Dedicated Resume & Curriculum Vitae Page
Provides direct original PDF viewing, downloadable PDF, and full browser routing.
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
    page_title=f"Resume | {PROFILE['name']}",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)

def load_css(css_file_path: str):
    if os.path.exists(css_file_path):
        with open(css_file_path, "r", encoding="utf-8") as f:
            st.html(f"<style>{f.read()}</style>")

load_css("styles/custom.css")

# Load Resume PDF bytes
resume_pdf_path = "assets/resume.pdf"
resume_bytes = None
b64_pdf = ""
if os.path.exists(resume_pdf_path):
    with open(resume_pdf_path, "rb") as f:
        resume_bytes = f.read()
        b64_pdf = base64.b64encode(resume_bytes).decode("utf-8")

# -----------------------------------------------------------------------------
# 2. Header & Navigation Back
# -----------------------------------------------------------------------------
st.html(f"""
<div class="nav-container">
    <div style="display: flex; align-items: center; gap: 16px;">
        <a href="./" target="_self" class="action-pill action-pill-primary" style="padding: 6px 14px; font-size: 0.85rem;">
            ← Back to Portfolio
        </a>
        <div class="nav-brand">{PROFILE['name']}</div>
    </div>
    <div class="status-pill">
        <span class="status-dot"></span>
        <span>{PROFILE['role']}</span>
    </div>
</div>
""")

# -----------------------------------------------------------------------------
# 3. Action Bar (Download & Contact)
# -----------------------------------------------------------------------------
col_dl, col_contact = st.columns([1, 1.5], gap="large")

with col_dl:
    if resume_bytes:
        st.download_button(
            label="📥 Download Official Resume (PDF)",
            data=resume_bytes,
            file_name="Rajasekaran_M_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )

with col_contact:
    st.html(f"""
    <div style="display: flex; gap: 10px; flex-wrap: wrap; justify-content: flex-end; align-items: center; height: 100%;">
        <div class="action-pill-static">✉️ {PROFILE['email']}</div>
        <a href="{PROFILE['linkedin']}" target="_blank" class="action-pill">💼 LinkedIn</a>
        <a href="{PROFILE['github']}" target="_blank" class="action-pill">🐙 GitHub</a>
        <a href="{PROFILE['credly']}" target="_blank" class="action-pill">🌐 Credly</a>
    </div>
    """)

st.markdown("<div style='margin-bottom: 25px;'></div>", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 4. Two Display Modes: Original PDF Document & Interactive Web Breakdown
# -----------------------------------------------------------------------------
tab_doc, tab_web = st.tabs(["📄 Original Resume Document", "📋 Interactive Web Breakdown"])

with tab_doc:
    if b64_pdf:
        st.html(f"""
        <div style="border-radius: 16px; overflow: hidden; border: 1px solid var(--border-subtle); box-shadow: var(--shadow-card); background: #1e293b; padding: 8px;">
            <iframe src="data:application/pdf;base64,{b64_pdf}" width="100%" height="950px" style="border: none; border-radius: 12px; display: block;"></iframe>
        </div>
        """)
    else:
        st.warning("Resume PDF file not found.")

with tab_web:
    st.html(f"""
    <div style="background: var(--bg-card); border: 1px solid var(--border-subtle); border-radius: 20px; padding: 40px; box-shadow: var(--shadow-card); backdrop-filter: blur(16px); max-width: 1000px; margin: 0 auto;">
        
        <!-- Header -->
        <div style="text-align: center; border-bottom: 1px solid var(--border-subtle); padding-bottom: 24px; margin-bottom: 28px;">
            <div style="font-size: 2.4rem; font-weight: 800; color: #ffffff; letter-spacing: -0.5px;">{PROFILE['name']}</div>
            <div style="font-size: 1.15rem; font-weight: 700; color: var(--accent-cyan); margin: 6px 0 14px 0;">{PROFILE['role']}</div>
            <div style="display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; font-size: 0.9rem; color: var(--text-secondary);">
                <span class="footer-plain-text">✉️ {PROFILE['email']}</span>
                <span>•</span>
                <a href="{PROFILE['linkedin']}" target="_blank" style="color: #818cf8; text-decoration: none;">linkedin.com/in/rajasekaran-m</a>
                <span>•</span>
                <a href="{PROFILE['github']}" target="_blank" style="color: #818cf8; text-decoration: none;">github.com/rajasekaran12345</a>
                <span>•</span>
                <a href="{PROFILE['credly']}" target="_blank" style="color: #818cf8; text-decoration: none;">credly.com/users/rajasekaran-m</a>
            </div>
        </div>

        <!-- Career Objective -->
        <div style="margin-bottom: 28px;">
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 12px;">
                Professional Objective
            </div>
            <p style="color: var(--text-secondary); font-size: 0.96rem; line-height: 1.65; margin: 0;">
                AI/ML and Cloud Enthusiast with hands-on experience in Computer Vision, Generative AI, AWS, RAG, MCP, and Python. 
                Experienced in building AI projects and working with real-world computer vision data. 
                Seeking an AI/ML, GenAI, AWS Cloud, or MLOps internship/entry-level opportunity.
            </p>
        </div>

        <!-- Education -->
        <div style="margin-bottom: 28px;">
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 16px;">
                Education
            </div>
            <div class="exp-card" style="margin-bottom: 14px;">
                <div class="exp-header">
                    <span class="exp-role" style="font-size: 1.05rem;">Master of Science in Applied Data Science (M.Sc.)</span>
                    <span class="exp-period">2024 – 2026</span>
                </div>
                <div class="exp-company">SRM Institute of Science and Technology &nbsp;•&nbsp; <span style="color: var(--accent-cyan);">CGPA: 8.24 / 10</span></div>
            </div>
            <div class="exp-card">
                <div class="exp-header">
                    <span class="exp-role" style="font-size: 1.05rem;">Bachelor of Science in Computer Science (B.Sc.)</span>
                    <span class="exp-period">2021 – 2024</span>
                </div>
                <div class="exp-company">B. S. Abdur Rahman Crescent Institute of Science and Technology &nbsp;•&nbsp; <span style="color: var(--accent-cyan);">Percentage: 70.49%</span></div>
            </div>
        </div>

        <!-- Technical Skills -->
        <div style="margin-bottom: 28px;">
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 14px;">
                Technical Skills
            </div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px;">
                <div style="background: rgba(0,0,0,0.25); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
                    <div style="color: var(--accent-cyan); font-weight: 700; font-size: 0.85rem; margin-bottom: 6px;">PROGRAMMING</div>
                    <div style="color: #f1f5f9; font-size: 0.9rem;">Python, SQL</div>
                </div>
                <div style="background: rgba(0,0,0,0.25); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
                    <div style="color: var(--accent-cyan); font-weight: 700; font-size: 0.85rem; margin-bottom: 6px;">AI / ML</div>
                    <div style="color: #f1f5f9; font-size: 0.9rem;">Machine Learning, NLP, Computer Vision, YOLO, Scikit-learn</div>
                </div>
                <div style="background: rgba(0,0,0,0.25); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
                    <div style="color: var(--accent-cyan); font-weight: 700; font-size: 0.85rem; margin-bottom: 6px;">GENERATIVE AI</div>
                    <div style="color: #f1f5f9; font-size: 0.9rem;">RAG, MCP (Model Context Protocol), LLM Applications, Agentic AI</div>
                </div>
                <div style="background: rgba(0,0,0,0.25); padding: 14px; border-radius: 10px; border: 1px solid var(--border-subtle);">
                    <div style="color: var(--accent-cyan); font-weight: 700; font-size: 0.85rem; margin-bottom: 6px;">AWS / CLOUD</div>
                    <div style="color: #f1f5f9; font-size: 0.9rem;">Amazon Bedrock, Amazon SageMaker, AWS Lambda, Amazon ECR, Amazon API Gateway, AWS AgentCore</div>
                </div>
            </div>
        </div>

        <!-- Internships -->
        <div style="margin-bottom: 28px;">
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 16px;">
                Internship Experience
            </div>
            <div class="exp-card" style="margin-bottom: 14px;">
                <div class="exp-header">
                    <span class="exp-role">AI/ML Computer Vision Intern</span>
                    <span class="exp-period">Jan 2026 – Mar 2026</span>
                </div>
                <div class="exp-company">Lesoko Technologies Pvt. Ltd. &nbsp;•&nbsp; <span style="color: var(--text-muted); font-size: 0.85rem;">Chennai, India</span></div>
                <ul class="exp-bullets">
                    <li>Annotated, cleaned, and preprocessed drone-based thermal images for an AI inspection system using YOLO-OBB models.</li>
                    <li>Worked on an industrial project involving solar panel defect prediction using YOLO-oriented bounding boxes.</li>
                </ul>
            </div>
            <div class="exp-card">
                <div class="exp-header">
                    <span class="exp-role">SAP BW & Power BI Data Analyst Intern</span>
                    <span class="exp-period">May 2025 – Jun 2025</span>
                </div>
                <div class="exp-company">Client Linx Software Pvt. Ltd. &nbsp;•&nbsp; <span style="color: var(--text-muted); font-size: 0.85rem;">Chennai, India</span></div>
                <ul class="exp-bullets">
                    <li>Worked on SAP BW fundamentals including data flow design, InfoProviders, and process chains.</li>
                    <li>Built Power BI dashboards using Power Query, DAX measures, calculated columns, and data modeling.</li>
                </ul>
            </div>
        </div>

        <!-- Projects -->
        <div style="margin-bottom: 28px;">
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 16px;">
                Featured Projects
            </div>
            <div class="exp-card" style="margin-bottom: 14px;">
                <div class="exp-header">
                    <span class="exp-role">Vehicle Survey using YOLO-OBB & Object Detection</span>
                    <a href="https://github.com/rajasekaran12345/Vechicle-Survey-using-object-detection-YOLOV11l" target="_blank" style="color: var(--accent-cyan); font-size: 0.85rem; font-weight: 600; text-decoration: none;">GitHub Repo ↗</a>
                </div>
                <div class="exp-company">Python, PyTorch, OpenCV, Ultralytics, BoT-SORT Tracking</div>
                <ul class="exp-bullets">
                    <li>Developed a YOLO-based real-time vehicle detection and tracking system to monitor incoming and outgoing vehicles across multiple classes.</li>
                    <li>Implemented vehicle classification for cars, bikes, buses, and trucks using the Ultralytics YOLO framework with OpenCV-based video processing.</li>
                </ul>
            </div>
            <div class="exp-card">
                <div class="exp-header">
                    <span class="exp-role">Movie Review Sentiment Analysis NLP</span>
                    <a href="https://github.com/rajasekaran12345/movie-review-sentiment-analysis" target="_blank" style="color: var(--accent-cyan); font-size: 0.85rem; font-weight: 600; text-decoration: none;">GitHub Repo ↗</a>
                </div>
                <div class="exp-company">Python, NLP, RNN, LSTM, BiLSTM, Streamlit UI, PyTorch / TensorFlow</div>
                <ul class="exp-bullets">
                    <li>Engineered an end-to-end sentiment classification pipeline evaluating user reviews with bidirectional LSTM models.</li>
                    <li>Deployed an interactive Streamlit UI for real-time text inference, confidence visualization, and latency benchmarking.</li>
                </ul>
            </div>
        </div>

        <!-- AWS Certifications -->
        <div>
            <div style="font-size: 1.15rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px; color: #ffffff; border-bottom: 1px solid rgba(99, 102, 241, 0.3); padding-bottom: 6px; margin-bottom: 16px;">
                AWS Certifications & Badges (Credly Verified)
            </div>
            <ul style="color: #cbd5e1; font-size: 0.93rem; line-height: 1.8; margin: 0; padding-left: 20px;">
                <li><strong style="color: #ffffff;">AWS Data Visualization Demonstrated</strong> — Amazon Web Services (Issued Sep 19, 2026 | Expires Sep 19, 2027)</li>
                <li><strong style="color: #ffffff;">AWS MLOps Demonstrated</strong> — Amazon Web Services (Issued Sep 05, 2026 | Expires Sep 05, 2027)</li>
                <li><strong style="color: #ffffff;">AWS SimuLearn - AI Practitioner</strong> — Amazon Web Services (Issued Jul 26, 2026 | Lifetime)</li>
                <li><strong style="color: #ffffff;">AWS Cloud Quest: Cloud Practitioner</strong> — Amazon Web Services (Issued Jul 06, 2026 | Lifetime)</li>
                <li><strong style="color: #ffffff;">AWS Cloud Quest: Generative AI Practitioner</strong> — Amazon Web Services (Issued Jun 12, 2026 | Lifetime)</li>
            </ul>
        </div>

    </div>
    """)

# Bottom Back Button
st.html("""
<div style="text-align: center; margin-top: 30px; margin-bottom: 40px;">
    <a href="./" target="_self" class="action-pill action-pill-primary" style="padding: 12px 28px; font-size: 1rem;">
        ← Back to Portfolio Home
    </a>
</div>
""")
