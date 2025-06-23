import streamlit as st
import base64

# Page configuration
st.set_page_config(
    page_title="Aditya Sarda | Portfolio", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for modern styling
def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Hero Section */
    .hero-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(20px);
        border-radius: 30px;
        padding: 60px 40px;
        margin: 20px 0 40px 0;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        text-align: center;
        animation: fadeInUp 1s ease-out;
    }
    
    .hero-title {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #fff, #f0f8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 20px;
        font-weight: 700;
    }
    
    .hero-subtitle {
        font-size: 1.3rem;
        color: rgba(255, 255, 255, 0.9);
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* Contact Info */
    .contact-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 20px;
        margin: 30px 0;
    }
    
    .contact-item {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        color: white;
        text-decoration: none;
        padding: 15px 25px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 50px;
        transition: all 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .contact-item:hover {
        background: rgba(255, 255, 255, 0.25);
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
    }
    
    /* Stats Grid */
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin: 40px 0;
    }
    
    .stat-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 30px 20px;
        border-radius: 20px;
        text-align: center;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        color: white;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .stat-label {
        color: rgba(255, 255, 255, 0.8);
        font-size: 1.1rem;
    }
    
    /* Tab Content */
    .tab-content {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(20px);
        border-radius: 25px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Section Titles */
    .section-title {
        font-size: 2.5rem;
        color: #333;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 15px;
        font-weight: 600;
    }
    
    .section-icon {
        color: #667eea;
        font-size: 2.2rem;
    }
    
    /* Cards */
    .card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 30px;
        border-radius: 20px;
        margin-bottom: 25px;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.5);
    }
    
    .card:hover {
        transform: translateY(-8px);
    }
    
    .card-title {
        color: #333;
        margin-bottom: 15px;
        font-size: 1.4rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .card-content {
        color: #666;
        line-height: 1.7;
        font-size: 1rem;
    }
    
    /* Project Cards */
    .project-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 35px;
        border-radius: 25px;
        margin-bottom: 30px;
        color: white;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .project-card:hover {
        transform: translateY(-10px) scale(1.02);
    }
    
    .project-title {
        font-size: 1.6rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 600;
    }
    
    .project-description {
        line-height: 1.8;
        opacity: 0.95;
        font-size: 1.05rem;
    }
    
    /* Download Button */
    .download-btn {
        display: inline-flex;
        align-items: center;
        gap: 15px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        padding: 20px 40px;
        border-radius: 50px;
        text-decoration: none;
        font-size: 1.2rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
        border: none;
        cursor: pointer;
    }
    
    .download-btn:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
        color: white;
        text-decoration: none;
    }
    
    /* Animations */
    @keyframes fadeInUp {
        from {
            opacity: 0;
            transform: translateY(30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .fadeInUp {
        animation: fadeInUp 0.8s ease-out;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .hero-title {
            font-size: 2.5rem;
        }
        
        .stats-grid {
            grid-template-columns: 1fr;
        }
        
        .contact-grid {
            grid-template-columns: 1fr;
        }
        
        .tab-content {
            padding: 25px;
        }
    }
    
    /* Streamlit specific overrides */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        justify-content: center;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 50px;
        padding: 10px;
        backdrop-filter: blur(10px);
    }
    
    .stTabs [data-baseweb="tab"] {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 25px;
        color: white;
        font-weight: 500;
        padding: 12px 24px;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    .stTabs [aria-selected="true"] {
        background: rgba(255, 255, 255, 0.3);
        color: white;
    }
    
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Hero Section
st.markdown("""
<div class="hero-container fadeInUp">
    <h1 class="hero-title">👋 Hi, I'm Aditya Sarda</h1>
    <div class="hero-subtitle">
        M.Sc. Economics student at the University of Heidelberg<br>
        📊 Passionate about data, behavioral finance, and building smart dashboards
    </div>
    
    <div class="contact-grid">
        <div class="contact-item">
            <i class="fas fa-envelope"></i>
            adityasarda000@gmail.com
        </div>
        <div class="contact-item">
            <i class="fab fa-github"></i>
            GitHub: adityasarda2000
        </div>
        <div class="contact-item">
            <i class="fab fa-linkedin"></i>
            LinkedIn: adityasarda
        </div>
    </div>
    
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">₹985M+</div>
            <div class="stat-label">Sales Analyzed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">15+</div>
            <div class="stat-label">Cities Covered</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">$24.9M</div>
            <div class="stat-label">Revenue Tracked</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🎓 Education", "📊 Projects", "📜 Certifications", "📥 CV Download"])

with tab1:
    st.markdown("""
    <div class="tab-content">
        <h2 class="section-title">
            <i class="fas fa-graduation-cap section-icon"></i>
            Education
        </h2>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fas fa-university"></i>
                M.Sc. Economics
            </h3>
            <div class="card-content">
                <strong>University of Heidelberg</strong> | 2022–Present<br><br>
                Specializing in advanced economic theory, econometrics, and behavioral finance with a focus on data-driven analysis. 
                Coursework includes advanced statistical methods, financial modeling, and economic research methodologies.
            </div>
        </div>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fas fa-chart-bar"></i>
                B.Sc. in Statistics
            </h3>
            <div class="card-content">
                <strong>University of Mumbai – KC College</strong> | 2018–2021<br><br>
                Comprehensive foundation in statistical methods, probability theory, and data analysis techniques. 
                Strong background in mathematical statistics, regression analysis, and statistical computing.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown("""
    <div class="tab-content">
        <h2 class="section-title">
            <i class="fas fa-project-diagram section-icon"></i>
            Featured Projects
        </h2>
        
        <div class="project-card">
            <h3 class="project-title">
                <i class="fas fa-chart-line"></i>
                Sales Insights Dashboard (2025)
            </h3>
            <div class="project-description">
                Built multiple interactive Power BI dashboards analyzing ₹985M+ in sales across 15+ cities. 
                Utilized MySQL for data extraction, DAX for complex calculations, and M Code for data transformation. 
                Created comprehensive KPIs and automated reporting systems that improved decision-making efficiency by 40%. 
                Implemented advanced filtering mechanisms and real-time data refresh capabilities.
            </div>
        </div>
        
        <div class="project-card">
            <h3 class="project-title">
                <i class="fas fa-bicycle"></i>
                AdventureWorks Analysis (2025)
            </h3>
            <div class="project-description">
                Developed refined dashboards using fictional bike company data showcasing $24.9M revenue analysis with 2.2% return rate optimization. 
                Incorporated advanced filtering mechanisms, dynamic KPIs, and interactive drilldowns. 
                Implemented predictive analytics to forecast sales trends and customer behavior patterns using statistical modeling techniques.
            </div>
        </div>
        
        <div class="project-card">
            <h3 class="project-title">
                <i class="fas fa-brain"></i>
                Bayesian Belief Adjustment Research (2024)
            </h3>
            <div class="project-description">
                Delivered comprehensive seminar on Bayesian methodology in economics, explaining how individuals and markets update beliefs based on new information. 
                Created interactive models demonstrating real-world applications in financial markets and behavioral economics research. 
                Developed mathematical frameworks for belief updating in uncertain environments.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="tab-content">
        <h2 class="section-title">
            <i class="fas fa-certificate section-icon"></i>
            Certifications & Skills
        </h2>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fas fa-table"></i>
                Advanced Excel
            </h3>
            <div class="card-content">
                <strong>NIIT Mumbai</strong> | 2019–2020<br>
                Advanced data analysis, pivot tables, macros, and financial modeling
            </div>
        </div>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fab fa-google"></i>
                Google Digital Analytics
            </h3>
            <div class="card-content">
                <strong>Google</strong> | 2020<br>
                Web analytics, conversion tracking, and digital marketing metrics
            </div>
        </div>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fas fa-chart-bar"></i>
                PowerBI for Business Intelligence
            </h3>
            <div class="card-content">
                <strong>Professional Certification</strong> | 2025<br>
                Dashboard creation, DAX formulas, data modeling, and visualization
            </div>
        </div>
        
        <div class="card">
            <h3 class="card-title">
                <i class="fas fa-calculator"></i>
                Financial Analysis Using Excel
            </h3>
            <div class="card-content">
                <strong>Professional Certification</strong> | 2025<br>
                Financial modeling, valuation techniques, and risk analysis
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="tab-content">
        <h2 class="section-title">
            <i class="fas fa-download section-icon"></i>
            Download CV
        </h2>
        
        <div style="text-align: center; padding: 40px 0;">
            <p style="font-size: 1.2rem; margin-bottom: 30px; color: #666; line-height: 1.6;">
                Get a detailed overview of my experience, skills, and achievements.<br>
                Complete portfolio with project details, academic background, and professional certifications.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Center the download button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📄 Download CV (PDF)", key="download_cv"):
            st.info("CV download functionality - Replace this with your actual CV file link!")
            # You can replace this with actual file download logic
            # st.download_button(
            #     label="📄 Download CV (PDF)",
            #     data=open("your_cv.pdf", "rb").read(),
            #     file_name="Aditya_Sarda_CV.pdf",
            #     mime="application/pdf"
            # )

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)