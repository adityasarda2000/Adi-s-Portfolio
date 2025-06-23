import streamlit as st

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
    ... (CSS content as above, trimmed for brevity)
    </style>
    """, unsafe_allow_html=True)

# Load CSS
load_css()

# Hero Section
st.markdown("""
<div class="hero-container">
    <h1 class="hero-title">👋 Hi, I'm Aditya Sarda</h1>
    <div class="hero-subtitle">
        M.Sc. Economics student at the University of Heidelberg<br>
        📊 Passionate about data, behavioral finance, and building smart dashboards
    </div>
    <div class="contact-info">
        <div class="contact-item">
            📧 adityasarda000@gmail.com
        </div>
        <div class="contact-item">
            🔗 GitHub: adityasarda2000
        </div>
        <div class="contact-item">
            💼 LinkedIn: adityasarda
        </div>
    </div>
    <div class="stats-container">
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
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">🎓 Education</h2>', unsafe_allow_html=True)
    ... (Education HTML code)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📊 Featured Projects</h2>', unsafe_allow_html=True)
    ... (Project HTML code)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📜 Certifications & Skills</h2>', unsafe_allow_html=True)
    ... (Certification HTML code)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="content-card">', unsafe_allow_html=True)
    st.markdown('<h2 class="section-title">📥 Download CV</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="download-section">
        <p class="download-description">
            Get a detailed overview of my experience, skills, and achievements.<br>
            Complete portfolio with project details, academic background, and professional certifications.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("📄 Download CV (PDF)", key="download_cv"):
            st.success("CV download functionality - Replace this with your actual CV file!")
            st.info("💡 To enable actual downloads, add your CV file and use st.download_button()")
            # Example for actual file download:
            # with open("aditya_sarda_cv.pdf", "rb") as file:
            #     st.download_button(
            #         label="📄 Download CV (PDF)",
            #         data=file,
            #         file_name="Aditya_Sarda_CV.pdf",
            #         mime="application/pdf"
            #     )

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
