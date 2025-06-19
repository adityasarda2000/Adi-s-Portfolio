import streamlit as st

st.set_page_config(page_title="Aditya Sarda | Portfolio", layout="wide")

st.title("👋 Hi, I'm Aditya Sarda")
st.markdown("""
M.Sc. Economics student at the University of Heidelberg  
📊 Passionate about data, behavioral finance, and building smart dashboards.
""")

# Contact info section
st.markdown("📫 **Email:** adityasarda000@gmail.com")
st.markdown("🔗 [GitHub](https://github.com/adityasarda2000) | [LinkedIn](https://linkedin.com/in/adityasarda)")

st.markdown("---")

# Tabs for navigation
tab1, tab2, tab3, tab4 = st.tabs(["Education", "Projects", "Certifications", "CV Download"])

with tab1:
    st.subheader("🎓 Education")
    st.write("**M.Sc. Economics**, University of Heidelberg (2022–Present)")
    st.write("**B.Sc. in Statistics**, University of Mumbai – KC College (2018–2021)")

with tab2:
    st.subheader("📈 Featured Projects")

    st.markdown("""
    - **Sales Insights (2025):** Built multiple interactive Power BI dashboards for ₹985M+ in sales across 15+ cities using MySQL + DAX + M Code.  
    - **AdventureWorks (2025):** Created refined dashboards using fictional bike company data ($24.9M revenue, 2.2% return rate), incorporating advanced filters, KPIs, and drilldowns.  
    - **Bayesian Belief Adjustment (2024):** Delivered a seminar explaining how individuals update beliefs based on new data using Bayesian methods.
    """)

with tab3:
    st.subheader("📜 Certifications")
    st.write("- **Advanced Excel**, NIIT Mumbai (2019–2020)")
    st.write("- **Google Digital Analytics** (2020)")
    st.write("- **PowerBI for Business Intelligence** (2025)")
    st.write("- **Financial Analysis Using Excel** (2025)")

with tab4:
    st.subheader("📄 Download My CV")
    with open("Aditya Sarda June.pdf", "rb") as f:
        st.download_button("Download Resume", f, file_name="Aditya_Sarda_CV.pdf")

