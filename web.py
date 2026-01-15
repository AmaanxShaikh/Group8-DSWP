import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

st.set_page_config(
    page_title="NYC Citi Bike Data Analysis",
    page_icon="🚴",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 2.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00D4FF 0%, #7B68EE 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    
    .project-title {
        font-family: 'Poppins', sans-serif;
        font-size: 2.2rem;
        font-weight: 600;
        color: #00D4FF;
        text-align: center;
        margin-bottom: 0.3rem;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.1rem;
        color: #B8C5D6;
        text-align: center;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.6rem;
        font-weight: 600;
        color: #00D4FF;
        border-bottom: 3px solid #7B68EE;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
    }
    
    .team-card {
        background: linear-gradient(145deg, #1E2A3A, #2D3E50);
        padding: 1.8rem;
        border-radius: 12px;
        text-align: center;
        border-left: 5px solid #00D4FF;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        transition: transform 0.3s ease;
    }
    
    .team-card:hover {
        transform: translateY(-5px);
    }
    
    .team-name {
        font-family: 'Poppins', sans-serif;
        color: #FFFFFF;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 0.3rem;
    }
    
    .team-role {
        color: #B8C5D6;
        font-size: 0.9rem;
        font-weight: 500;
    }
    
    .footer {
        text-align: center;
        color: #B8C5D6;
        padding: 2rem 0;
        margin-top: 3rem;
        border-top: 2px solid #3D5A73;
    }
    
    .nav-card {
        background: linear-gradient(135deg, #00D4FF 0%, #7B68EE 100%);
        padding: 2.5rem;
        border-radius: 16px;
        color: white;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0, 212, 255, 0.3);
        transition: all 0.3s ease;
    }
    
    .nav-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 12px 35px rgba(0, 212, 255, 0.4);
    }
    
    .nav-card-pink {
        background: linear-gradient(135deg, #FF6B9D 0%, #C850C0 100%);
        box-shadow: 0 8px 25px rgba(255, 107, 157, 0.3);
    }
    
    .nav-card-pink:hover {
        box-shadow: 0 12px 35px rgba(255, 107, 157, 0.4);
    }
    
    .highlight-box {
        background: linear-gradient(145deg, #1E2A3A, #2D3E50);
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 4px solid #00D4FF;
        margin: 1rem 0;
    }
    
    .highlight-box h4 {
        color: #00D4FF !important;
    }
    
    .highlight-box p, .highlight-box li {
        color: #E0E7EF !important;
    }
    
    .highlight-box-pink {
        background: linear-gradient(145deg, #2A1E2E, #3D2D42);
        border-left: 4px solid #FF6B9D;
    }
    
    .highlight-box-pink h4 {
        color: #FF6B9D !important;
    }
    
    .contribution-card {
        background: linear-gradient(145deg, #1E2A3A, #2D3E50);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        border: 1px solid #3D5A73;
    }
    
    .contribution-card h4 {
        color: #00D4FF !important;
    }
    
    .contribution-card li {
        color: #E0E7EF !important;
    }
    
    .contribution-card-pink h4 {
        color: #FF6B9D !important;
    }
    
    .sidebar-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        color: #00D4FF;
    }
    
    a {
        color: #00D4FF !important;
        text-decoration: none;
        font-weight: 500;
    }
    
    a:hover {
        color: #7B68EE !important;
        text-decoration: underline;
    }
    
    .footer-title {
        color: #FFFFFF !important;
    }
    
    .footer-subtitle {
        color: #B8C5D6 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🎓 Data Science with Python</div>', unsafe_allow_html=True)
st.markdown('<div class="project-title">NYC Citi Bike Data Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A Master\'s-Level Data Science Project on Urban Mobility and Bike-Sharing Systems</div>', unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="section-header">📋 Project Overview</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("""
    <div class="highlight-box">
    <h4 style="margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif;">About NYC Citi Bike</h4>
    <p style="line-height: 1.7;">
    The <strong style="color: #00D4FF;">NYC Citi Bike</strong> program is one of North America's largest bike-sharing systems, 
    serving millions of riders since 2013. This project analyzes trip-level data to uncover patterns 
    in urban mobility and transportation behavior.
    </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box highlight-box-pink">
    <h4 style="margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif;">Research Objectives</h4>
    <ul style="line-height: 1.8; margin: 0; padding-left: 1.2rem;">
        <li>Data preprocessing & quality assessment</li>
        <li>Temporal & spatial pattern discovery</li>
        <li>User behavior analysis</li>
        <li>Predictive modeling</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="section-header">🧭 Project Navigation</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="nav-card">
            <div style="font-size: 3.5rem; margin-bottom: 1rem;">📊</div>
            <h3 style="color: white; margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif; font-size: 1.4rem;">
                Preprocessing & EDA
            </h3>
            <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6; opacity: 0.95; color: white;">
                Data cleaning, validation, feature engineering, and exploratory visual analysis.
            </p>
            <a href='https://amaan-citi-bike-analysis.streamlit.app/' target='_blank' 
               style='background: white; color: #0066CC !important; padding: 0.8rem 2rem; 
                      border-radius: 8px; text-decoration: none; font-weight: 600;
                      display: inline-block; font-family: Poppins, sans-serif;'>
                Explore EDA →
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="nav-card nav-card-pink">
            <div style="font-size: 3.5rem; margin-bottom: 1rem;">📈</div>
            <h3 style="color: white; margin-bottom: 0.8rem; font-family: 'Poppins', sans-serif; font-size: 1.4rem;">
                Case Studies & Prediction
            </h3>
            <p style="font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6; opacity: 0.95; color: white;">
                Applied case studies, predictive modeling, and data-driven recommendations.
            </p>
            <a href='https://bramha007-dswp-proj-app-7eb1wn.streamlit.app/' target='_blank' 
               style='background: white; color: #C850C0 !important; padding: 0.8rem 2rem; 
                      border-radius: 8px; text-decoration: none; font-weight: 600;
                      display: inline-block; font-family: Poppins, sans-serif;'>
                Explore Cases →
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="section-header">🎯 Contributions</div>', unsafe_allow_html=True)

contrib_col1, contrib_col2 = st.columns(2)

with contrib_col1:
    st.markdown("""
    <div class="contribution-card">
    <h4 style="margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">🎓 Academic Excellence</h4>
    <ul style="line-height: 2; margin: 0; padding-left: 1.2rem;">
        <li>End-to-end data science workflow</li>
        <li>Statistical and ML foundations</li>
        <li>Rigorous methodology</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with contrib_col2:
    st.markdown("""
    <div class="contribution-card contribution-card-pink">
    <h4 style="margin-bottom: 1rem; font-family: 'Poppins', sans-serif;">💡 Practical Impact</h4>
    <ul style="line-height: 2; margin: 0; padding-left: 1.2rem;">
        <li>Real-world transportation data</li>
        <li>Actionable insights</li>
        <li>Stakeholder-focused analysis</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown('<div class="section-header">👥 Project Team</div>', unsafe_allow_html=True)

team_col1, team_col2, team_col3 = st.columns(3)

with team_col1:
    st.markdown("""
        <div class='team-card'>
            <div style='font-size: 3.5rem; margin-bottom: 0.8rem;'>👨‍🎓</div>
            <p class='team-name'>Mohammed Amaan Shaikh</p>
            <p class='team-role'>Master's Student - DKE</p>
        </div>
    """, unsafe_allow_html=True)

with team_col2:
    st.markdown("""
        <div class='team-card'>
            <div style='font-size: 3.5rem; margin-bottom: 0.8rem;'>👨‍🎓</div>
            <p class='team-name'>Nitish Kamlesh Choudhary</p>
            <p class='team-role'>Master's Student - DKE</p>
        </div>
    """, unsafe_allow_html=True)

with team_col3:
    st.markdown("""
        <div class='team-card'>
            <div style='font-size: 3.5rem; margin-bottom: 0.8rem;'>👩‍🎓</div>
            <p class='team-name'>Yashashwini Sidramappa Awate</p>
            <p class='team-role'>Master's Student - DKE</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class='footer'>
        <p class='footer-title' style='font-size: 1.1rem; font-weight: 600; margin-bottom: 0.5rem; font-family: Poppins, sans-serif;'>
            Master's Project – Data Science with Python
        </p>
        <p class='footer-subtitle' style='font-size: 1rem; margin-bottom: 0.3rem;'>
            🚴 NYC Citi Bike Data Analysis
        </p>
        <p style='font-size: 0.85rem; color: #8A9DB5;'>
            Built with Python & Streamlit | © 2025
        </p>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3097/3097055.png", width=80)
    st.markdown("### 🚴 Navigation Guide")
    st.markdown("""
    This dashboard is the main landing page for the NYC Citi Bike Data Analysis project.
    
    **Quick Links:**
    - 📊 Preprocessing & EDA
    - 📈 Case Studies & Prediction
    """)
    
    st.markdown("---")
    st.markdown("### 📚 Resources")
    st.markdown("""
    - [NYC Citi Bike System Data](https://citibikenyc.com/system-data)
    - [Project Repository & Notebook](https://code.ovgu.de/ratu79ge/bike-share-data-science/-/tree/main?ref_type=heads)
    - [Streamlit Documentation](https://docs.streamlit.io)
    """)