"""
Centralized Data Source for Rajasekaran M's Portfolio Website.
Contains verified credentials, projects, experience, skills, and links.
"""

PROFILE = {
    "name": "Rajasekaran M",
    "role": "AI/ML Engineer | GenAI & AWS Cloud",
    "status": "🟢 Open to AI/ML & Cloud Opportunities",
    "location": "Chennai, Tamil Nadu, India",
    "email": "rajakurunchi@gmail.com",
    "linkedin": "https://www.linkedin.com/in/rajasekaran-m-492808224/",
    "github": "https://github.com/rajasekaran12345",
    "credly": "https://www.credly.com/users/rajasekaran-m.584fa5f3",
    "about_me": (
        "I’m Rajasekaran — an AI/ML engineer passionate about turning ideas into "
        "intelligent, real-world solutions. I build with Machine Learning, Generative AI, "
        "Computer Vision, and AWS, with hands-on experience across projects and industry. "
        "As I begin my career, I’m looking for opportunities where I can learn fast, "
        "build boldly, and create meaningful impact."
    ),
    "stats": [
        {"metric": "5+", "label": "AWS Credly Badges"},
        {"metric": "100%", "label": "Cloud & AI Focus"},
        {"metric": "2+", "label": "Industrial Internships"},
        {"metric": "8.24", "label": "M.Sc. Data Science CGPA"}
    ]
}

CERTIFICATIONS = [
    {
        "id": "892a610e-f559-44bd-9d20-3e294fd6094e",
        "title": "AWS Data Visualization Demonstrated",
        "issuer": "Amazon Web Services Training and Certification",
        "category": "AWS Certification Badges",
        "issued_date": "Sep 19, 2026",
        "expires_date": "Sep 19, 2027",
        "is_expiring": True,
        "local_image": "assets/badges/aws_data_visualization.png",
        "remote_image": "https://images.credly.com/images/3e0dcc2b-b0d3-4f20-959a-5c16373d8ac3/blob",
        "verification_url": "https://www.credly.com/badges/892a610e-f559-44bd-9d20-3e294fd6094e",
        "skills": ["Data Visualization", "AWS QuickSight", "Business Intelligence", "Cloud Analytics"]
    },
    {
        "id": "983a74ba-a070-42a4-b779-ccf151c7983e",
        "title": "AWS MLOps Demonstrated",
        "issuer": "Amazon Web Services Training and Certification",
        "category": "AWS Certification Badges",
        "issued_date": "Sep 05, 2026",
        "expires_date": "Sep 05, 2027",
        "is_expiring": True,
        "local_image": "assets/badges/aws_mlops.png",
        "remote_image": "https://images.credly.com/images/60d4b86c-cbec-4d31-aeb1-5e86864305a1/blob",
        "verification_url": "https://www.credly.com/badges/983a74ba-a070-42a4-b779-ccf151c7983e",
        "skills": ["MLOps", "Amazon SageMaker", "CI/CD for ML", "Model Monitoring", "Containerization"]
    },
    {
        "id": "2762d8d7-acf0-42b4-8bf5-4b0a5943029f",
        "title": "AWS SimuLearn - AI Practitioner - Training Badge",
        "issuer": "Amazon Web Services Training and Certification",
        "category": "AWS Skill Builder",
        "issued_date": "Jul 26, 2026",
        "expires_date": "Lifetime / No Expiration",
        "is_expiring": False,
        "local_image": "assets/badges/aws_simulearn_ai_practitioner.png",
        "remote_image": "https://images.credly.com/images/198ccc47-6b2f-45c1-bff0-80b2c980ea40/blob",
        "verification_url": "https://www.credly.com/badges/2762d8d7-acf0-42b4-8bf5-4b0a5943029f",
        "skills": ["Artificial Intelligence", "Practical Simulation", "Model Evaluation", "Cloud Workflows"]
    },
    {
        "id": "f053a6f8-62c9-49fb-900b-e37da4a301f9",
        "title": "AWS Cloud Quest: Cloud Practitioner - Training Badge",
        "issuer": "Amazon Web Services Training and Certification",
        "category": "AWS Skill Builder",
        "issued_date": "Jul 06, 2026",
        "expires_date": "Lifetime / No Expiration",
        "is_expiring": False,
        "local_image": "assets/badges/aws_cloud_quest_cloud_practitioner.png",
        "remote_image": "https://images.credly.com/images/30816e43-2550-4e1c-be22-3f03c5573bb9/blob",
        "verification_url": "https://www.credly.com/badges/f053a6f8-62c9-49fb-900b-e37da4a301f9",
        "skills": ["Cloud Architecture", "AWS Core Services", "Security & IAM", "Serverless Basics"]
    },
    {
        "id": "ce369f08-951d-4ce2-a094-a053697cd27d",
        "title": "AWS Cloud Quest: Generative AI Practitioner - Training Badge",
        "issuer": "Amazon Web Services Training and Certification",
        "category": "AWS Skill Builder",
        "issued_date": "Jun 12, 2026",
        "expires_date": "Lifetime / No Expiration",
        "is_expiring": False,
        "local_image": "assets/badges/aws_cloud_quest_generative_ai.png",
        "remote_image": "https://images.credly.com/images/15fa08e6-ca73-4fa3-94ed-c36f7f157313/blob",
        "verification_url": "https://www.credly.com/badges/ce369f08-951d-4ce2-a094-a053697cd27d",
        "skills": ["Generative AI", "Amazon Bedrock", "Foundation Models", "Prompt Engineering"]
    }
]

PROJECTS = [
    {
        "name": "Vehicle Survey using YOLO-OBB & Object Detection",
        "category": "Computer Vision & Edge AI",
        "repo_url": "https://github.com/rajasekaran12345/Vechicle-Survey-using-object-detection-YOLOV11l",
        "tech_stack": ["Python", "Ultralytics YOLOv11l", "YOLO-OBB", "BoT-SORT", "PyTorch", "OpenCV"],
        "description": (
            "An intelligent computer vision system built to conduct real-time traffic and vehicle surveys. "
            "Integrates the state-of-the-art YOLOv11l object detection backbone with oriented bounding boxes (OBB) "
            "and the BoT-SORT multi-object tracking algorithm to monitor, track, and classify incoming and "
            "outgoing vehicles across complex urban traffic scenes."
        ),
        "highlights": [
            "Real-time vehicle counting and lane trajectory monitoring",
            "Multi-class classification for cars, bikes, buses, and trucks",
            "BoT-SORT motion tracking algorithm with orientation awareness",
            "High-throughput OpenCV video processing pipeline"
        ]
    },
    {
        "name": "Movie Review Sentiment Analysis NLP",
        "category": "Natural Language Processing & Deep Learning",
        "repo_url": "https://github.com/rajasekaran12345/movie-review-sentiment-analysis",
        "tech_stack": ["Python", "NLP", "RNN", "LSTM", "BiLSTM", "Streamlit UI", "PyTorch / TensorFlow"],
        "description": (
            "An end-to-end natural language sentiment classification pipeline engineered to predict positive "
            "and negative audience sentiments from textual reviews. Employs recurrent deep learning architectures "
            "(Simple RNN, LSTM, and Bidirectional LSTM) wrapped in an interactive, real-time Streamlit web interface."
        ),
        "highlights": [
            "Bidirectional LSTM sequence modeling for context-sensitive sentiment classification",
            "End-to-end text tokenization, padding, and embedding pipeline",
            "Interactive Streamlit web interface for live user text inference",
            "Confidence scoring, sentiment probability visualization, and latency benchmarking"
        ]
    }
]

INTERNSHIPS = [
    {
        "role": "AI/ML Computer Vision Intern",
        "company": "Lesoko Technologies Pvt. Ltd.",
        "location": "Chennai, Tamil Nadu",
        "period": "Jan 2026 – Mar 2026",
        "highlights": [
            "Annotated, cleaned, and preprocessed high-resolution drone-based thermal images for industrial computer vision inspection.",
            "Engineered oriented bounding box (YOLO-OBB) models to detect micro-cracks and defect patterns in solar panels.",
            "Collaborated with computer vision engineers to enhance defect prediction recall across varying thermal contrast levels."
        ]
    },
    {
        "role": "SAP BW & Power BI Data Analyst Intern",
        "company": "Client Linx Software Pvt. Ltd.",
        "location": "Chennai, Tamil Nadu",
        "period": "May 2025 – Jun 2025",
        "highlights": [
            "Mastered SAP BW fundamentals including data flow architecture, InfoProviders, extraction routines, and process chains.",
            "Designed executive Power BI dashboards with Power Query ETL, DAX measures, calculated metrics, and dimensional models.",
            "Automated reporting workflows, streamlining cross-departmental data reconciliation and stakeholder visual presentations."
        ]
    }
]

EDUCATION = [
    {
        "degree": "Master of Science in Applied Data Science (M.Sc.)",
        "institution": "SRM Institute of Science and Technology",
        "period": "2024 – 2026",
        "score": "CGPA: 8.24 / 10",
        "details": "Specializing in Machine Learning, Generative AI, Computer Vision, and Big Data Architecture."
    },
    {
        "degree": "Bachelor of Science in Computer Science (B.Sc.)",
        "institution": "B. S. Abdur Rahman Crescent Institute of Science and Technology",
        "period": "2021 – 2024",
        "score": "Percentage: 70.49%",
        "details": "Foundations in Algorithms, Object-Oriented Programming, Database Management Systems, and Software Engineering."
    }
]

SKILLS_CATEGORIES = [
    {
        "category": "Generative AI & LLMs",
        "icon": "✨",
        "skills": ["RAG (Retrieval-Augmented Generation)", "MCP (Model Context Protocol)", "Agentic AI Workflows", "Prompt Engineering", "LLM Applications", "LangChain"]
    },
    {
        "category": "Computer Vision & Deep Learning",
        "icon": "👁️",
        "skills": ["Ultralytics YOLO (v8 / v11)", "YOLO-OBB (Oriented Bounding Boxes)", "BoT-SORT Tracking", "OpenCV", "PyTorch", "TensorFlow", "Thermal Image Processing"]
    },
    {
        "category": "AWS Cloud & MLOps",
        "icon": "☁️",
        "skills": ["Amazon Bedrock", "Amazon SageMaker", "AWS Lambda", "Amazon ECR", "Amazon API Gateway", "Amazon S3", "AWS AgentCore", "ML Inference Endpoints"]
    },
    {
        "category": "Data Science & Development",
        "icon": "⚡",
        "skills": ["Python (NumPy, Pandas, Scikit-learn)", "SQL & Relational Databases", "Power BI & DAX", "SAP BW Fundamentals", "Streamlit UI Development", "Git & GitHub"]
    }
]
