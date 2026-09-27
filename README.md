# Rajasekaran M — Portfolio Website

A bespoke developer portfolio website engineered in Python with **Streamlit** and a custom **dark glassmorphic design system**.

## ✨ Features
- **Hero Presentation**: Direct role branding (`AI/ML Engineer | GenAI & AWS Cloud`), GitHub avatar, and one-click access to LinkedIn, GitHub, Credly, and Email.
- **Credly Badges Showcase**: Official AWS badges with high-resolution graphics, start and expiration dates, and direct hyperlinks to official Credly verification pages.
- **Featured Projects**: Highlights two core production AI GitHub repositories:
  - [Vehicle Survey using YOLO-OBB & Object Detection](https://github.com/rajasekaran12345/Vechicle-Survey-using-object-detection-YOLOV11l)
  - [Movie Review Sentiment Analysis NLP](https://github.com/rajasekaran12345/movie-review-sentiment-analysis)
- **Work Experience & Internships**: Detailed accomplishments at Lesoko Technologies (Computer Vision / YOLO-OBB) and Client Linx (SAP BW & Power BI).
- **Technical Skills Matrix**: Visual badges covering Generative AI, Computer Vision, AWS Cloud, and Software Development.
- **Resume Hub**: ATS-formatted resume with a single-click PDF download button.
- **Strict Privacy**: Zero phone numbers included anywhere on the site or in the codebase.

---

## 🚀 Local Hosting & Execution

1. **Activate your Python environment** (Python 3.11+ recommended).
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the portfolio website**:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at `http://localhost:8501`.

---

## 🌐 Deploying to Streamlit Community Cloud (share.streamlit.io)

Follow these simple steps when you are ready to publish:

1. **Push your code to a GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Rajasekaran M Portfolio"
   git branch -M main
   git remote add origin https://github.com/rajasekaran12345/portfolio.git
   git push -u origin main
   ```
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with your GitHub account.
3. Click **"New app"** and select:
   - **Repository**: `rajasekaran12345/portfolio`
   - **Branch**: `main`
   - **Main file path**: `app.py`
4. Click **Deploy!** Your portfolio will be live at `https://<your-custom-name>.streamlit.app` with free SSL and global availability.
