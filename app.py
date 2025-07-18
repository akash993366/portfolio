import streamlit as st
import base64
from PIL import Image
import os
import io

# Set page configuration
st.set_page_config(
    page_title="Akash Gupta | Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
def local_css():
    st.markdown("""
    <style>
        /* Import Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css');
        
        /* Global Styles */
        * {
            font-family: 'Inter', sans-serif;
            box-sizing: border-box;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        body {
            color: #1F2937;
            background-color: #F9FAFB;
        }
        
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }
        
        ::-webkit-scrollbar-track {
            background: #F3F4F6;
        }
        
        ::-webkit-scrollbar-thumb {
            background: #4338ca;
            border-radius: 4px;
        }
        
        ::-webkit-scrollbar-thumb:hover {
            background: #3730a3;
        }
        
        /* Main Container */
        .main {
            padding: 0rem 2rem 0rem 2rem;
        }
        
        /* Typography */
        h1 {
            color: #1E3A8A; 
            font-weight: 700; 
            letter-spacing: -0.5px; 
            margin-bottom: 0.5rem;
        }
        
        h2 {
            color: #1E3A8A; 
            font-weight: 600; 
            letter-spacing: -0.3px;
        }
        
        h3 {
            color: #1E3A8A; 
            font-weight: 600;
        }
        
        p {
            line-height: 1.6;
        }
        
        /* Cards and containers */
        .highlight {background-color: #f8fafc; padding: 1.5rem; border-radius: 0.75rem; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: transform 0.2s, box-shadow 0.2s;}
        .highlight:hover {transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);}
        
        .project-card {background-color: #f8fafc; padding: 1.5rem; border-radius: 0.75rem; height: 100%; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05); transition: transform 0.2s, box-shadow 0.2s;}
        .project-card:hover {transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);}
        
        /* Skill tags */
        .skill-tag {background-color: #EEF2FF; padding: 0.3rem 0.8rem; border-radius: 0.5rem; margin: 0.2rem; display: inline-block; font-size: 0.85rem; color: #4338ca; border: 1px solid #E0E7FF; transition: background-color 0.2s;}
        .skill-tag:hover {background-color: #E0E7FF;}
        
        /* Timeline styling */
        .timeline-item {border-left: 2px solid #1E3A8A; padding-left: 1.5rem; padding-bottom: 1.5rem; margin-left: 1rem; position: relative;}
        .timeline-item:before {content: ''; position: absolute; left: -0.5rem; top: 0; width: 1rem; height: 1rem; border-radius: 50%; background-color: #1E3A8A;}
        .timeline-date {font-weight: bold; color: #1E3A8A;}
        
        /* Streamlit Buttons */
        .stButton>button {
            background-color: #4338ca;
            color: white;
            padding: 0.6rem 1.5rem;
            border-radius: 30px;
            border: none;
            font-weight: 500;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(67, 56, 202, 0.3);
        }
        
        .stButton>button:hover {
            background-color: #3730a3;
            box-shadow: 0 6px 10px rgba(67, 56, 202, 0.4);
            transform: translateY(-2px);
        }
        
        /* Download button */
        .download-button {
            display: inline-flex;
            align-items: center;
            background-color: #1E3A8A;
            color: white !important;
            padding: 0.5rem 1rem;
            border-radius: 0.5rem;
            text-decoration: none !important;
            transition: background-color 0.2s;
            font-weight: 500;
        }

        .download-button:hover {
            background-color: #153175;
            color: white !important;
            text-decoration: none !important;
        }

        .download-button * {
            color: white !important;
            text-decoration: none !important;
        }


        
        /* Expander styling */
        .streamlit-expanderHeader {background-cocolor: white;}lor: #f8fafc; border-radius: 0.5rem; border: 1px solid #e2e8f0; padding: 0.75rem !important; margin-bottom: 0.5rem; transition: background-color 0.2s;}
        .streamlit-expanderHeader:hover {background-color: #EEF2FF;}
        .streamlit-expanderContent {border-radius: 0.5rem; padding: 1rem !important; background-color: #f8fafc; border: 1px solid #e2e8f0;}
        
        /* Progress bars */
        .stProgress > div > div > div > div {background-color: #1E3A8A;}
        
        /* Contact Section */
        .contact-card {
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            justify-content: center;
            background-color: #F3F4F6;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            height: 100%;
        }
        
        .contact-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .contact-icon {
            font-size: 2rem;
            color: #4338ca;
            margin-bottom: 1rem;
            justify-content: center;
        }
        
        .contact-info h3 {
            color: #111827;
            justify-content: center;
        }
        
        .contact-info a {
            color: #4338ca;
            word-break: break-word;
            justify-content: center;
        }
        
        /* Contact Form */
        .contact-form {
            max-width: 600px;
            margin: 1.5rem 0;
        }
        
        .form-group {
            margin-bottom: 1.25rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #374151;
        }
        
        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #D1D5DB;
            border-radius: 6px;
            font-size: 1rem;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }
        
        .contact-form input:focus,
        .contact-form textarea:focus {
            border-color: #4338ca;
            box-shadow: 0 0 0 3px rgba(67, 56, 202, 0.1);
            outline: none;
        }
        
        .submit-btn {
            background-color: #4338ca;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .submit-btn:hover {
            background-color: #3730a3;
            transform: translateY(-2px);
        }
        
        /* Footer */
        .footer {
            margin-top: 4rem;
            padding-top: 2rem;
            border-top: 1px solid #E5E7EB;
        }
        
        .footer-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
        }
        
        .footer-content p {
            margin: 0;
            color: #6B7280;
        }
        
        /* Social icons for footer */
        .social-icons {
            display: flex;
            gap: 1rem;
        }
        h1 span.emoji {
            color: unset !important;
        }

        .social-icons a {
            color: #4B5563;
            font-size: 1.25rem;
            transition: color 0.3s ease, transform 0.3s ease;
        }
        
        .social-icons a:hover {
            color: #4338ca;
            transform: translateY(-2px);
        }

        /* Animations */
        @keyframes fadeIn {from {opacity: 0;} to {opacity: 1;}}
        .fade-in {animation: fadeIn 0.5s ease-in-out;}
        
        @keyframes slideInFromLeft {from {transform: translateX(-30px); opacity: 0;} to {transform: translateX(0); opacity: 1;}}
        .slide-in-left {animation: slideInFromLeft 0.5s ease-in-out;}
        
        @keyframes slideInFromRight {from {transform: translateX(30px); opacity: 0;} to {transform: translateX(0); opacity: 1;}}
        .slide-in-right {animation: slideInFromRight 0.5s ease-in-out;}
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            
            .clickable-title-container-btn {
                padding: 1.5rem;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                text-align: center;
            }

            .clickable-title-container-btn h1 {
                font-size: 1.8rem;
                text-align: center;
                margin-top: 0.5rem;
                width: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                flex-wrap: wrap;
            }

            .clickable-title-container-btn h3 {
                font-size: 1rem;
                text-align: center;
                margin-top: 0.3rem;
            }
        }

        
        /* Centered Message */
        .centered-message {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 3rem 1rem;
            color: #6B7280;
        }

        /* Clickable Title Container - Unified Styling for Banner (with image) */
        .clickable-title-container-btn {
            background: linear-gradient(135deg, #EEF2FF 0%, #E0E7FF 100%);
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
            cursor: pointer; 
            transition: transform 0.2s, box-shadow 0.2s;
            animation: fadeIn 0.5s ease-in-out;
            display: flex; /* Use flexbox */
            align-items: center; /* Vertically align items */
            justify-content: flex-start; /* Align to start */
            text-align: left; /* Align text to left */
            gap: 25px; /* Space between image and text */
        }
        .clickable-title-container-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 10px rgba(0, 0, 0, 0.1);
        }
        .clickable-title-container-btn h1 {
            font-size: 3rem;
            background: linear-gradient(90deg, #1E3A8A 0%, #4338CA 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.5rem;
            text-align: left; /* Align text to left */
        }
        .clickable-title-container-btn h3 {
            color: #4338ca;
            margin-top: 0;
            font-weight: 500;
            letter-spacing: 0.5px;
            text-align: left; /* Align text to left */
        }
        /* Ensure the anchor tag doesn't affect appearance */
        .clickable-title-container-btn a {
            text-decoration: none;
            color: inherit;
        }
        
        .banner-profile-img-container {
            padding: 5px;
            border-radius: 50%;
            background: linear-gradient(135deg, #4338ca 0%, #1E3A8A 100%);
            width: 200px;
            height: 200px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            flex-shrink: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .banner-profile-img-container img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
        }

        .banner-profile-img-container .fas.fa-user {
            font-size: 50px;
            color: #EEF2FF;
        }


    </style>
    
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """, unsafe_allow_html=True)

def load_profile_image():
    try:
        # Try to find a specific image named 'profile_image.png' or similar
        # Includes the specific image names from your attachments
        potential_names = ['pp.jpeg', 'pp.jpg']
        for name in potential_names:
            if os.path.exists(os.path.join('assets', name)):
                image_path = os.path.join('assets', name)
                image = Image.open(image_path)
                buffered = io.BytesIO()
                image.save(buffered, format="PNG") # Always save as PNG for consistency
                img_str = base64.b64encode(buffered.getvalue()).decode()
                return img_str
        
        # Fallback if no specific image is found, try any image in assets
        if os.path.exists('assets'):
            for ext in ['.jpg', '.jpeg', '.png']:
                for file in os.listdir('assets'):
                    if file.lower().endswith(ext):
                        image_path = os.path.join('assets', file)
                        image = Image.open(image_path)
                        buffered = io.BytesIO()
                        image.save(buffered, format="PNG")
                        img_str = base64.b64encode(buffered.getvalue()).decode()
                        return img_str
                    
    except Exception as e:
        # Print error for debugging purposes in the console, but return None to avoid breaking the app
        print(f"Error loading profile image: {e}")
    return None # Return None if no image is found or an error occurs

def get_pdf_download_link(file_path, button_text):
    if file_path.endswith(".pdf") and os.path.exists(file_path):
        with open(file_path, "rb") as file:
            pdf_bytes = file.read()
        b64_pdf = base64.b64encode(pdf_bytes).decode()
        href = f'<a href="data:application/pdf;base64,{b64_pdf}" download="{os.path.basename(file_path)}" class="download-button">{button_text}</a>'
        return href
    return None

# Callback function to set session state for navigation
def navigate_to(page_name):
    st.session_state.page = page_name

def akash_gupta_banner():
    img_b64_str = load_profile_image()

    if img_b64_str:
        img_html = f'<img src="data:image/png;base64,{img_b64_str}" class="banner-profile-img" />'
    else:
        img_html = '<i class="fas fa-user"></i>'

    st.markdown(f"""
    <a href="?page=Home" target="_self" style="text-decoration: none; display: block; color: inherit;">
        <div class="clickable-title-container-btn">
            <div class="banner-profile-img-container">
                {img_html}
            </div>
            <div>
                <div class="slide-in-left" style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-size: 2rem;">👋</span>
                    <h1 style="margin: 0;">I'm Akash</h1>
                </div>
                <div class="slide-in-left">
                    <h3>AI/ML & GenAI Practitioner</h3>
                </div>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)
    col_contact, col_projects, col_resume = st.columns(3)
    with col_contact:
        if st.button("✉️ Contact Me", key="home_contact_btn", on_click=navigate_to, args=("Contact",), use_container_width=True):
            pass
    with col_projects:
        if st.button("🧑🏻‍💻 View Projects", key="home_projects_btn", on_click=navigate_to, args=("Projects",), use_container_width=True):
            pass
    with col_resume:
        if st.button("📄 View Resume", key="home_resume_btn", on_click=navigate_to, args=("Resume",), use_container_width=True):
            pass
            
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)

def main():
    local_css()

    # Initialize session state for page if not already set
    if 'page' not in st.session_state:
        st.session_state.page = st.query_params.get('page', 'Home') # Reads from URL query params

    # Display content based on current_page from session state
    if st.session_state.page == "Home":
        home_section()
    elif st.session_state.page == "Resume":
        resume_section()
    elif st.session_state.page == "Projects":
        project_section()
    elif st.session_state.page == "Contact":
        contact_section()

def home_section():
    akash_gupta_banner() # Use the reusable banner

    st.markdown('''
    <div class="highlight" style="
        margin-bottom: 20px;
        border-left: 4px solid #4338ca;
        padding-left: 1.5rem;
    ">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            I’m a tech enthusiast and Data Science consultant with 9+ years of helping global banks and insurers turn AI and ML into real-world results. I love building practical GenAI, NLP, and machine learning solutions that boost decisions, efficiency, and business outcomes.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    st.markdown('<h3 style="color: #4338ca; display: flex; align-items: center; gap: 10px; margin-top: 2rem;"><i class="fas fa-laugh-beam" style="color: #4338ca;"></i> Fun Facts About Me</h3>', unsafe_allow_html=True)
    st.markdown('''
        <div class="highlight" style="
            margin-bottom: 20px;
            border-left: 4px solid #4338ca;
            padding-left: 1.5rem;
        ">
        <p style="font-size: 1.1rem; line-height: 1.6;">
            Beyond data and algorithms, here’s a little more about what makes me, well… me:
            <ul style="list-style-type: disc; margin-left: 20px;">
                <li style="font-size: 1.1rem;">I love diving into sportsperson biographies, always chasing the next inspiring story.</li>
                <li style="font-size: 1.1rem;">I religiously follow cricket, player stats, match numbers, trivia; it's basically my second language.</li>
                <li style="font-size: 1.1rem;">Experimenting with new recipes is my kind of fun, especially when it involves fusion food.</li>
                <li style="font-size: 1.1rem;">Also, I’m on a mission to try every good filter coffee out there; recommendations welcome!</li>
            </ul>
        </p>
    </div>
    ''', unsafe_allow_html=True)

    
def resume_section():
    akash_gupta_banner() # Use the reusable banner

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #4338ca; border-bottom: 2px solid #4338ca; padding-bottom: 8px;">Professional Journey</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Download Resume button at the top
    resume_link = get_pdf_download_link("assets/resume.pdf", "📄 Download Resume")
    if resume_link:
        st.markdown('<div style="display: flex; justify-content: flex-end; margin-bottom: 20px;">' + resume_link + '</div>', unsafe_allow_html=True)

    # Create tabs for different resume sections
    tabs = st.tabs(["Experience", "Education", "Skills"])

    # Experience Tab
    with tabs[0]:
        st.markdown('<div class="slide-in-left">', unsafe_allow_html=True)
        st.markdown('<div class="timeline">', unsafe_allow_html=True)

        # EXL Service
        st.markdown('''
        <div class="timeline-item">
            <div class="timeline-date">2021 - Present</div>
            <div class="timeline-content">
                <h3>Lead Data Scientist</h3>
                <h4>EXL Service | Gurgaon, India</h4>
                <ul class="timeline-list">
                    <li>Built scalable <strong>ML/GenAI pipelines</strong> and led a 10-member team to deliver solutions across underwriting, claims, and audit operations.</li>
                    <li>Developed <strong>semantic search engine</strong> using Transformers (BERT, all-mpnet) + Q&A chains → <em>reduced claims retrieval time by 70%</em>.</li>
                    <li>Engineered <strong>Text2SQL LLM app</strong> for non-technical users to query databases → <em>reduced dev dependency by 60%</em>.</li>
                    <li>Created <strong>Enterprise Text Flag Library</strong> using LLMs (Gemini, SetFit) to extract structured insights from claim notes → <em>90% reduction in false positives/negatives</em>.</li>
                    <li>Designed <strong>premium forecasting tool</strong> using GLMs → <em>$12M+ annual increase in recovered premiums</em>.</li>
                </ul>
                <div class="timeline-tags">
                    <span class="skill-tag">GenAI</span>
                    <span class="skill-tag">BERT</span>
                    <span class="skill-tag">LLM</span>
                    <span class="skill-tag">ML Pipelines</span>
                    <span class="skill-tag">Vertex AI</span>
                    <span class="skill-tag">Leadership</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        # EY
        st.markdown('''
        <div class="timeline-item">
            <div class="timeline-date">2019 - 2021</div>
            <div class="timeline-content">
                <h3>Data Scientist</h3>
                <h4>EY | Gurgaon, India</h4>
                <ul class="timeline-list">
                    <li>Delivered a dynamic <strong>portfolio optimization platform</strong> with simulation, KPI forecasting, and model selection engine.</li>
                    <li>Led strategic analytics for Japanese M&A firm → <em>improved deal conversion by identifying key closure signals</em>.</li>
                </ul>
                <div class="timeline-tags">
                    <span class="skill-tag">Forecasting</span>
                    <span class="skill-tag">ML</span>
                    <span class="skill-tag">M&A Analytics</span>
                    <span class="skill-tag">XGBoost</span>
                    <span class="skill-tag">Keras</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        # Accenture
        st.markdown('''
        <div class="timeline-item">
            <div class="timeline-date">2015 - 2019</div>
            <div class="timeline-content">
                <h3>Senior Analyst</h3>
                <h4>Accenture | Gurgaon, India</h4>
                <ul class="timeline-list">
                    <li>Built scalable <strong>ETL pipelines</strong> using Python, Alteryx, and IBM DataStage for U.S. banking clients → <em>25% improvement in SLA compliance</em>.</li>
                    <li>Re-engineered <strong>fraud detection system</strong> using Random Forest with advanced features like device score, geo-deviation → <em>+7% recall uplift</em>.</li>
                    <li>Led productionization with Airflow + monitoring via PSI/KS metrics for drift detection and fraud ops visibility.</li>
                </ul>
                <div class="timeline-tags">
                    <span class="skill-tag">ETL</span>
                    <span class="skill-tag">Fraud Detection</span>
                    <span class="skill-tag">Random Forest</span>
                    <span class="skill-tag">DataStage</span>
                    <span class="skill-tag">Airflow</span>
                </div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Education Tab
    with tabs[1]:
        st.markdown('<div class="slide-in-right">', unsafe_allow_html=True)
        st.markdown('<div class="timeline">', unsafe_allow_html=True)
        # Education entries
        st.markdown('''
        <div class="timeline-item">
            <div class="timeline-date">2011 - 2015</div>
            <div class="timeline-content">
                <h3>Bechelor of Technology in ECE</h3>
                <h4>Maharaja Agrasen Institute of Technology (MAIT)</h4>
                <ul class="timeline-list">
                    <li>Specialized in Microprocessors and Embedded Systems</li>
                    <li>Overall Percentage: 82</li>
                </ul>
            </div>
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Skills Tab
    with tabs[2]:
        st.markdown('<div class="fade-in">', unsafe_allow_html=True)
        skill_col1, skill_col2 = st.columns(2)

        card_style = 'min-height: 340px; height: 100%;'

        with skill_col1:
            st.markdown('<h3><i class="fas fa-brain" style="color: #4338ca;"></i> AI/ML & GenAI Ecosystem</h3>', unsafe_allow_html=True)
            st.markdown(f'''
            <div class="highlight" style="{card_style}">
                <ul>
                    <li><strong>Languages:</strong> Python, SQL</li>
                    <li><strong>ML Algorithms:</strong> Linear/Logistic Regression, Decision Trees, Random Forest, SVM, KNN, Naive Bayes, PCA</li>
                    <li><strong>Boosting:</strong> AdaBoost, Gradient Boosting, CatBoost</li>
                    <li><strong>DL Frameworks:</strong> TensorFlow, PyTorch</li>
                    <li><strong>Deep Learning:</strong> CNN, LSTM, RNN</li>
                    <li><strong>GenAI & NLP:</strong> Transformers (BERT, GPT), LangChain, Prompt Engineering, RAGs, Text2SQL, Vector DBs, NER, TF-IDF, Regex, Dependency Parsing</li>
                    <li><strong>LLM Techniques:</strong> Fine-tuning, LoRA, Quantization</li>
                </ul>
            </div>
            ''', unsafe_allow_html=True)

            st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
            st.markdown('<h3><i class="fas fa-tools" style="color: #4338ca;"></i> MLOps & Engineering</h3>', unsafe_allow_html=True)
            st.markdown(f'''
            <div class="highlight" style="{card_style}">
                <ul>
                    <li><strong>Deployment:</strong> Docker, Vertex AI, Kubeflow, Concourse CI</li>
                    <li><strong>CI/CD:</strong> GitHub Actions, Git</li>
                    <li><strong>ETL & Pipelines:</strong> Airflow, Alteryx, IBM DataStage</li>
                    <li><strong>Big Data:</strong> Spark, Hadoop, Databricks</li>
                    <li><strong>Cloud Platforms:</strong> GCP, AWS SageMaker, Azure ML</li>
                </ul>
            </div>
            ''', unsafe_allow_html=True)
            #st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)

        with skill_col2:
            st.markdown('<h3><i class="fas fa-database" style="color: #4338ca;"></i> Data Science & Analytics</h3>', unsafe_allow_html=True)
            st.markdown(f'''
            <div class="highlight" style="{card_style}">
                <ul>
                    <li><strong>EDA & Stats:</strong> Pandas, NumPy, Scikit-learn, GLMs, GAMs, Statistical Modeling</li>
                    <li><strong>Visualization:</strong> Matplotlib, Seaborn, Plotly</li>
                    <li><strong>Specializations:</strong> Time Series Forecasting, A/B Testing, Experiment Design</li>
                </ul>
            </div>
            ''', unsafe_allow_html=True)

            st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)
            st.markdown('<h3><i class="fas fa-briefcase" style="color: #4338ca;"></i> Domain Expertise & Soft Skills</h3>', unsafe_allow_html=True)
            st.markdown(f'''
            <div class="highlight" style="{card_style}">
                <ul>
                    <li>Insurance, Banking, Financial Services</li>
                    <li>Use Cases: Claims Triage, Premium Forecasting, Fraud Detection, M&A Analysis</li>
                    <li>Project Leadership: Team management (10+ members), Product Ownership</li>
                    <li>Agile & Scrum Methodologies</li>
                    <li>Stakeholder Collaboration, Cross-functional Communication</li>
                    <li>Mentorship, Knowledge Sharing</li>
                </ul>
            </div>
            ''', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)
        #st.markdown('<div style="height: 30px;"></div>', unsafe_allow_html=True)


def project_section():
    akash_gupta_banner() # Use the reusable banner

    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #4338ca; border-bottom: 2px solid #4338ca; padding-bottom: 8px;">Featured Projects</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # Project filter tabs
    st.markdown('<div class="slide-in-left">', unsafe_allow_html=True)
    project_tabs = st.tabs(["Gen AI", "ML", "Analytics"])
    st.markdown('</div>', unsafe_allow_html=True)

    with project_tabs[0]:
        st.markdown('<div class="project-container fade-in">', unsafe_allow_html=True)

        projects = [
            {
                "title": "Enterprise Text Flag Factory (GenAI)",
                "icon": "fas fa-tags",
                "theme": "Text Flagging",
                "description": "Built an enterprise-grade flagging system to identify domain-specific tags in property and casualty claim notes using LLMs. Used a combination of GPT, Gemini, and fine-tuned sentence transformers for multi-intent detection across 30+ business flags. Engineered prompt chains with LangChain and custom validation logic, hosted via Streamlit for user testing. Integrated GCP’s Artifact Registry, GitHub Actions, and MLflow for end-to-end CI/CD and traceability. Achieved 90%+ precision and recall in pilot, drastically reducing manual audit time and standardizing interpretation across adjusters. Solution supports versioned pipelines for continued learning with human-in-the-loop architecture.",
                "technologies": ["Python", "LLMs", "LangChain", "Vertex AI", "MLflow", "Streamlit", "GitHub Actions"]
            },
            {
                "title": "Semantic Search in Claims",
                "icon": "fas fa-search",
                "theme": "Search Engine",
                "description": "Implemented a semantic search platform to allow adjusters to query claims with natural language across millions of historical notes. Replaced keyword logic with sentence-transformer embeddings (all-mpnet-base-v2) and created a vector DB on GCP using Faiss. Enabled retrieval augmented generation (RAG) with context injection via LangChain and integrated BERT-QA chains for summary answers. Delivered on Streamlit with GCP IAM-secured authentication. The solution reduced document lookup time by 70%, improved user satisfaction, and allowed claims handlers to investigate patterns across policy types and regions.",
                "technologies": ["Python", "Transformers", "Faiss", "LangChain", "GCP", "Streamlit"]
            },
            {
                "title": "Text2SQL GenAI App",
                "icon": "fas fa-database",
                "theme": "Natural Language SQL",
                "description": "Created an internal LLM app that allows business users to query insurance tables using natural language. Used OpenAI GPT-4 with SQL schema understanding and prompt tuning to generate context-aware SQL queries across multiple databases. Built a backend wrapper with SQLite and PostgreSQL connectors and frontend with Streamlit. Added result summarization with LLM and alert triggers for thresholds. Cut down BI team dependency by 60% and accelerated ad hoc reporting cycles.",
                "technologies": ["OpenAI GPT-4", "LangChain", "SQLAlchemy", "Streamlit", "PostgreSQL"]
            }
        ]

        for proj in projects:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f'''
                <div class="project-image-placeholder" style="background-color: #EEF2FF; height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center; border-radius: 10px;">
                    <i class="{proj['icon']}" style="font-size: 80px; color: #4338ca;"></i>
                    <p style="margin-top: 10px; color: #4338ca; font-weight: 500;">{proj['theme']}</p>
                </div>
                ''', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<h3 style="color: #4338ca; margin-bottom: 0.3rem;">{proj["title"]}</h3>', unsafe_allow_html=True)
                st.markdown(f'''
                <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;">{proj["description"]}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                ''' + "".join([f'<span class="skill-tag">{tech}</span>' for tech in proj['technologies']]) + '</div>', unsafe_allow_html=True)

            st.markdown('<div class="project-divider" style="border-top: 1px solid #e2e8f0; margin: 20px 0;"></div>', unsafe_allow_html=True)

    with project_tabs[1]:
        projects = [
            {
                "title": "Premium Audit Forecast Tool",
                "icon": "fas fa-chart-bar",
                "theme": "Forecasting",
                "description": "Developed a predictive tool for commercial insurance audit departments to estimate premium variances using historical payroll, classifications, and endorsements. Leveraged GLMs and ensemble tree models (XGBoost) to estimate high-risk segments. Built Streamlit dashboard with user filters for industry class, state, and time period. Added data drift monitoring via Vertex AI and experiment tracking using MLflow. Resulted in $12M/year improved audit selection and aligned actuarial forecasts with underwriting insight.",
                "technologies": ["Python", "XGBoost", "GLM", "MLflow", "Vertex AI", "Streamlit"]
            },
            {
                "title": "Suspense Premium Outlier (SPO) Model",
                "icon": "fas fa-exclamation-triangle",
                "theme": "Outlier Detection",
                "description": "Created SPO model for large commercial insurer to detect misclassified or mismatched premium entries. Used unsupervised DBSCAN clustering with manual labels to identify outliers. Feature set included payment frequency, prior premium delta, classification codes. Integrated alerts via dashboard, sent auto emails to operations for mismatches. Model enabled early triage, leading to faster correction and reconciliation of ~$50M worth of premiums annually.",
                "technologies": ["Python", "DBSCAN", "Streamlit", "SQL", "Feature Engineering"]
            }
        ]

        for proj in projects:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f'''
                <div class="project-image-placeholder" style="background-color: #EEF2FF; height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center; border-radius: 10px;">
                    <i class="{proj['icon']}" style="font-size: 80px; color: #4338ca;"></i>
                    <p style="margin-top: 10px; color: #4338ca; font-weight: 500;">{proj['theme']}</p>
                </div>
                ''', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<h3 style="color: #4338ca; margin-bottom: 0.3rem;">{proj["title"]}</h3>', unsafe_allow_html=True)
                st.markdown(f'''
                <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;">{proj["description"]}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                ''' + "".join([f'<span class="skill-tag">{tech}</span>' for tech in proj['technologies']]) + '</div>', unsafe_allow_html=True)

            st.markdown('<div class="project-divider" style="border-top: 1px solid #e2e8f0; margin: 20px 0;"></div>', unsafe_allow_html=True)

    with project_tabs[2]:
        projects = [
            {
                "title": "Fraud Detection Enhancement",
                "icon": "fas fa-shield-alt",
                "theme": "Fraud Detection",
                "description": "Redesigned a legacy fraud detection model for a top U.S. banking client. Transitioned from GLM to Random Forest, adding engineered features like device velocity, user-behavioral patterns, and geolocation shifts. Addressed class imbalance via SMOTE and implemented probability thresholds to manage false positives. Created a monitoring dashboard for model drift (KS, PSI metrics) and retraining triggers. The new pipeline improved detection recall by 8%, reduced fraud leakage, and aligned with compliance guidelines for explainability.",
                "technologies": ["Python", "Scikit-learn", "SQL", "SMOTE", "Random Forest"]
            },
            {
                "title": "TRANBI M&A Analytics",
                "icon": "fas fa-handshake",
                "theme": "Deal Analytics",
                "description": "Led analytics module for TRANBI, a Japan-based M&A platform. Built deal scoring and lead prioritization models using logistic regression and NLP-based profile match scoring between buyers and sellers. Created Power BI dashboards showing lead engagement, closure likelihood, and outreach effectiveness. Collaborated with Japanese PMs to localize content, manage iterations, and implement final solution. Resulted in improved match rates and deal conversion KPIs.",
                "technologies": ["Python", "Logistic Regression", "NLP", "Power BI", "Japanese Localization"]
            }
        ]

        for proj in projects:
            col1, col2 = st.columns([1, 2])
            with col1:
                st.markdown(f'''
                <div class="project-image-placeholder" style="background-color: #EEF2FF; height: 200px; display: flex; flex-direction: column; justify-content: center; align-items: center; border-radius: 10px;">
                    <i class="{proj['icon']}" style="font-size: 80px; color: #4338ca;"></i>
                    <p style="margin-top: 10px; color: #4338ca; font-weight: 500;">{proj['theme']}</p>
                </div>
                ''', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<h3 style="color: #4338ca; margin-bottom: 0.3rem;">{proj["title"]}</h3>', unsafe_allow_html=True)
                st.markdown(f'''
                <p style="font-size: 1.05rem; line-height: 1.6; margin-bottom: 1rem;">{proj["description"]}</p>
                <div style="display: flex; flex-wrap: wrap; gap: 8px;">
                ''' + "".join([f'<span class="skill-tag">{tech}</span>' for tech in proj['technologies']]) + '</div>', unsafe_allow_html=True)

            st.markdown('<div class="project-divider" style="border-top: 1px solid #e2e8f0; margin: 20px 0;"></div>', unsafe_allow_html=True)

    
    
def contact_section():
    akash_gupta_banner()
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    st.markdown('<h2 style="color: #4338ca; border-bottom: 2px solid #4338ca; padding-bottom: 8px;">Let\'s Connect</h2>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Feel free to reach out for collaborations, opportunities, or just a chat!</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact cards with icons
    st.markdown('<div class="slide-in-left">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('''
        <div class="contact-card">
            <div class="contact-icon">
                <i class="fas fa-envelope"></i>
            </div>
            <div class="contact-info">
                <h3>Email</h3>
                <a href="mailto:akashgupta993366@gmail.com">akashgupta993366@gmail.com</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col2:
        st.markdown('''
        <div class="contact-card">
            <div class="contact-icon">
                <i class="fab fa-linkedin"></i>
            </div>
            <div class="contact-info">
                <h3>LinkedIn</h3>
                <a href="https://www.linkedin.com/in/akash-gupta-399277143/" target="_blank">Akash Gupta</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    
    with col3:
        st.markdown('''
        <div class="contact-card">
            <div class="contact-icon">
                <i class="fas fa-phone-alt"></i>
            </div>
            <div class="contact-info">
                <h3>Phone</h3>
                <a href="tel:+919811371117">+91-9811371117</a>
            </div>
        </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Contact Form with improved styling
    st.markdown('<div class="slide-in-right" style="margin-top: 40px;">', unsafe_allow_html=True)
    st.markdown('<h3><i class="fas fa-paper-plane" style="color: #4338ca;"></i> Send me a message</h3>', unsafe_allow_html=True)
    
    contact_form = '''
    <form action="https://formsubmit.co/akashgupta993366@gmail.com" method="POST" class="contact-form">
        <input type="hidden" name="_captcha" value="false">
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" name="name" id="name" placeholder="Your name" required>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" name="email" id="email" placeholder="Your email" required>
        </div>
        <div class="form-group">
            <label for="message">Message</label>
            <textarea name="message" id="message" placeholder="Your message here" rows="5" required></textarea>
        </div>
        <button type="submit" class="submit-btn">
            <i class="fas fa-paper-plane"></i> Send Message
        </button>
    </form>
    '''
    
    st.markdown(contact_form, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown('<div class="footer fade-in">', unsafe_allow_html=True)
    st.markdown('''
    <div class="footer-content">
        <p>© 2025 Akash Gupta. All rights reserved.</p>
        <div class="social-icons">
            <a href="https://github.com/akash993366" target="_blank"><i class="fab fa-github"></i></a>
            <a href="https://www.linkedin.com/in/akash-gupta-399277143/" target="_blank"><i class="fab fa-linkedin"></i></a>
            <a href="https://x.com/_akashgupta_" target="_blank"><i class="fab fa-twitter"></i></a>
        </div>
    </div>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()