import streamlit as st

# --- CONTACT SECTION ---
st.subheader("📫 Contact")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📧 Email:\nadityasarda000@gmail.com", icon="📧")
with col2:
    st.info("🐙 GitHub:\n[@adityasarda2000](https://github.com/adityasarda2000)", icon="🐙")
with col3:
    st.info("💼 LinkedIn:\n[@adityasarda](https://linkedin.com/in/adityasarda)", icon="💼")

# --- STATS SECTION ---
st.subheader("📊 Key Stats")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Sales Analyzed", value="₹985M+")
with col2:
    st.metric(label="Cities Covered", value="15+")
with col3:
    st.metric(label="Revenue Tracked", value="$24.9M")
