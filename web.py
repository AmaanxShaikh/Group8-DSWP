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
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap');
    
    /* Global Styles */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
    background: linear-gradient(
        rgba(10, 15, 26, 0.45), 
        rgba(17, 24, 39, 0.50)
    ), url('https://raw.githubusercontent.com/amaanxshaikh/nyc-citi-bike-streamlit/main/Image/background.jpg');
    background-size: 150%;
    background-position: center;
    background-attachment: fixed;
    background-repeat: no-repeat;
}

@media (max-width: 768px) {
    .stApp {
        background-size: cover;
        background-attachment: scroll;
    }
}
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Main Header */
    .main-header {
        font-family: 'Poppins', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        background: linear-gradient(135deg, #00D4FF 0%, #7B68EE 50%, #FF6B9D 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: -1px;
    }
    
    .project-title {
        font-family: 'Poppins', sans-serif;
        font-size: 1.8rem;
        font-weight: 600;
        color: #E2E8F0;
        text-align: center;
        margin-bottom: 0.5rem;
        letter-spacing: 0.5px;
    }
    
    .subtitle {
        font-family: 'Inter', sans-serif;
        font-size: 1.05rem;
        color: #FFFFFF;
        text-align: center;
        font-weight: 500;
        margin-bottom: 1rem;
        max-width: 600px;
        margin-left: auto;
        margin-right: auto;
        line-height: 1.6;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }
    
    /* Badge */
    .badge-container {
        display: flex;
        justify-content: center;
        gap: 0.8rem;
        margin-bottom: 2.5rem;
    }
    
    .badge {
        background: rgba(0, 212, 255, 0.1);
        border: 1px solid rgba(0, 212, 255, 0.3);
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        color: #00D4FF;
        font-weight: 500;
    }
    
    .badge-alt {
        background: rgba(123, 104, 238, 0.1);
        border: 1px solid rgba(123, 104, 238, 0.3);
        color: #7B68EE;
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Poppins', sans-serif;
        font-size: 1.4rem;
        font-weight: 600;
        color: #E2E8F0;
        margin-top: 3rem;
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.8rem;
    }
    
    .section-header::before {
        content: '';
        width: 4px;
        height: 24px;
        background: linear-gradient(180deg, #00D4FF, #7B68EE);
        border-radius: 2px;
    }
    
    /* Cards Base */
    .card {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.8), rgba(15, 23, 42, 0.9));
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.1);
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
    }
    
    .card:hover {
        border-color: rgba(0, 212, 255, 0.3);
        transform: translateY(-4px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    /* Highlight Boxes */
    .highlight-box {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.8));
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid rgba(0, 212, 255, 0.2);
        position: relative;
        overflow: hidden;
    }
    
    .highlight-box::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, #00D4FF, #7B68EE);
    }
    
    .highlight-box h4 {
        color: #E2E8F0 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        margin-bottom: 1rem;
    }
    
    .highlight-box p, .highlight-box li {
        color: #FFFFFF !important;
        line-height: 1.8;
    }
    
    .highlight-box-alt::before {
        background: linear-gradient(90deg, #FF6B9D, #C850C0);
    }
    
    .highlight-box-alt {
        border-color: rgba(255, 107, 157, 0.2);
    }
    
    /* Navigation Cards */
    .nav-card {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.9), rgba(15, 23, 42, 0.95));
        border-radius: 20px;
        padding: 2.5rem 2rem;
        border: 1px solid rgba(148, 163, 184, 0.1);
        text-align: center;
        position: relative;
        overflow: hidden;
        transition: all 0.4s ease;
    }
    
    .nav-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #00D4FF, #7B68EE);
    }
    
    .nav-card:hover {
        transform: translateY(-8px);
        border-color: rgba(0, 212, 255, 0.4);
        box-shadow: 0 25px 50px rgba(0, 212, 255, 0.15);
    }
    
    .nav-card-alt::before {
        background: linear-gradient(90deg, #FF6B9D, #C850C0);
    }
    
    .nav-card-alt:hover {
        border-color: rgba(255, 107, 157, 0.4);
        box-shadow: 0 25px 50px rgba(255, 107, 157, 0.15);
    }
    
    .nav-icon {
        width: 70px;
        height: 70px;
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(0, 212, 255, 0.15), rgba(123, 104, 238, 0.15));
        border: 1px solid rgba(0, 212, 255, 0.3);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.5rem auto;
        font-size: 1.4rem;
        font-weight: 700;
        color: #00D4FF;
        font-family: 'Poppins', sans-serif;
    }
    
    .nav-icon-alt {
        background: linear-gradient(135deg, rgba(255, 107, 157, 0.15), rgba(200, 80, 192, 0.15));
        border-color: rgba(255, 107, 157, 0.3);
        color: #FF6B9D;
    }
    
    .nav-card h3 {
        color: #E2E8F0;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.25rem;
        margin-bottom: 0.8rem;
    }
    
    .nav-card p {
        color: #FFFFFF;
        font-size: 0.95rem;
        line-height: 1.6;
        margin-bottom: 1.8rem;
    }
    
    .nav-btn {
        display: inline-block;
        padding: 0.9rem 2rem;
        border-radius: 10px;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        font-size: 0.9rem;
        text-decoration: none !important;
        transition: all 0.3s ease;
        background: linear-gradient(135deg, #00D4FF, #7B68EE);
        color: white !important;
    }
    
    .nav-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 10px 30px rgba(0, 212, 255, 0.4);
    }
    
    .nav-btn-alt {
        background: linear-gradient(135deg, #FF6B9D, #C850C0);
    }
    
    .nav-btn-alt:hover {
        box-shadow: 0 10px 30px rgba(255, 107, 157, 0.4);
    }
    
    /* Contribution Cards */
    .contrib-card {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.6), rgba(15, 23, 42, 0.8));
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid rgba(148, 163, 184, 0.1);
        height: 100%;
    }
    
    .contrib-card h4 {
        color: #E2E8F0 !important;
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.05rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
        gap: 0.6rem;
    }
    
    .contrib-card h4::before {
        content: '';
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: linear-gradient(135deg, #00D4FF, #7B68EE);
    }
    
    .contrib-card-alt h4::before {
        background: linear-gradient(135deg, #FF6B9D, #C850C0);
    }
    
    .contrib-card li {
        color: #FFFFFF !important;
        line-height: 2;
        font-size: 0.95rem;
    }
    
    /* Team Cards */
    .team-card {
        background: linear-gradient(145deg, rgba(30, 41, 59, 0.7), rgba(15, 23, 42, 0.85));
        padding: 2rem 1.5rem;
        border-radius: 16px;
        text-align: center;
        border: 1px solid rgba(148, 163, 184, 0.1);
        transition: all 0.3s ease;
        position: relative;
        overflow: hidden;
    }
    
    .team-card::before {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00D4FF, #7B68EE);
        transform: scaleX(0);
        transition: transform 0.3s ease;
    }
    
    .team-card:hover::before {
        transform: scaleX(1);
    }
    
    .team-card:hover {
        transform: translateY(-6px);
        border-color: rgba(0, 212, 255, 0.3);
    }
    
    .team-avatar {
        width: 56px;
        height: 56px;
        border-radius: 14px;
        background: linear-gradient(135deg, #00D4FF, #7B68EE);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1.2rem auto;
        font-size: 1.1rem;
        font-weight: 700;
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    
    .team-avatar-alt {
        background: linear-gradient(135deg, #FF6B9D, #C850C0);
    }
    
    .team-name {
        font-family: 'Poppins', sans-serif;
        color: #E2E8F0;
        font-weight: 600;
        font-size: 1rem;
        margin-bottom: 0.3rem;
    }
    
    .team-role {
        color: #E2E8F0;
        font-size: 0.85rem;
        font-weight: 500;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 3rem 0 2rem 0;
        margin-top: 4rem;
        border-top: 1px solid rgba(148, 163, 184, 0.1);
    }
    
    .footer-title {
        color: #E2E8F0 !important;
        font-size: 1rem;
        font-weight: 600;
        font-family: 'Poppins', sans-serif;
        margin-bottom: 0.4rem;
    }
    
    .footer-subtitle {
        color: #E2E8F0 !important;
        font-size: 0.9rem;
        margin-bottom: 0.8rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    .footer-copy {
        color: #CBD5E1;
        font-size: 0.8rem;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(
            rgba(15, 23, 42, 0.60), 
            rgba(30, 41, 59, 0.65)
        );
    }
    
    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem;
    }
    
    .sidebar-header {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .sidebar-logo {
        width: 50px;
        height: 50px;
        border-radius: 12px;
        background: linear-gradient(135deg, #00D4FF, #7B68EE);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto 1rem auto;
        font-size: 1.2rem;
        font-weight: 700;
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    
    .sidebar-title {
        font-family: 'Poppins', sans-serif;
        font-weight: 600;
        font-size: 1.1rem;
        color: #E2E8F0;
        margin-bottom: 0.3rem;
    }
    
    .sidebar-subtitle {
        color: #E2E8F0;
        font-size: 0.85rem;
    }
    
    /* Links */
    a {
        color: #00D4FF !important;
        text-decoration: none;
        font-weight: 500;
        transition: color 0.2s ease;
    }
    
    a:hover {
        color: #7B68EE !important;
    }
    
    /* Divider */
    .divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.2), transparent);
        margin: 2rem 0;
    }
    
    /* Stats Row */
    .stats-row {
        display: flex;
        justify-content: center;
        gap: 3rem;
        margin: 2rem 0;
    }
    
    .stat-item {
        text-align: center;
    }
    
    .stat-value {
        font-family: 'Poppins', sans-serif;
        font-size: 2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #00D4FF, #7B68EE);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .stat-label {
        color: #E2E8F0;
        font-size: 0.85rem;
        font-weight: 600;
        margin-top: 0.3rem;
        text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.5);
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.markdown('<div class="main-header">🎓 Data Science with Python</div>', unsafe_allow_html=True)
st.markdown('<div class="project-title">NYC Citi Bike Data Analysis</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A comprehensive data science project exploring urban mobility patterns and bike-sharing behavior in New York City</div>', unsafe_allow_html=True)

st.markdown("""
    <div class="badge-container">
        <span class="badge">Master's Project</span>
        <span class="badge badge-alt">Data Science</span>
    </div>
""", unsafe_allow_html=True)

# Stats Row
st.markdown("""
    <div class="stats-row">
        <div class="stat-item">
            <div class="stat-value">2013</div>
            <div class="stat-label">Program Launch</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">40M+</div>
            <div class="stat-label">Annual Rides</div>
        </div>
        <div class="stat-item">
            <div class="stat-value">1,500+</div>
            <div class="stat-label">Stations</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Project Overview
st.markdown('<div class="section-header"> Project Overview</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("""
    <div class="highlight-box">
        <h4>About NYC Citi Bike</h4>
        <p>
            The <strong style="color: #00D4FF;">NYC Citi Bike</strong> program stands as one of North America's largest 
            bike-sharing systems, transforming urban transportation since 2013. This project conducts an in-depth 
            analysis of trip-level data to reveal meaningful patterns in urban mobility and commuter behavior.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="highlight-box highlight-box-alt">
        <h4>Research Objectives</h4>
        <ul style="margin: 0; padding-left: 1.2rem;">
            <li>Data preprocessing & quality assessment</li>
            <li>Temporal & spatial pattern discovery</li>
            <li>User behavior segmentation</li>
            <li>Predictive modeling & forecasting</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Navigation Section
st.markdown('<div class="section-header"> Explore the Project</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("""
        <div class="nav-card">
            <div class="nav-icon">📊</div>
            <h3>Preprocessing & EDA</h3>
            <p>Data cleaning, validation, feature engineering, and comprehensive exploratory visual analysis.</p>
            <a href='https://amaan-citi-bike-analysis.streamlit.app/' target='_blank' class="nav-btn">
                Explore Analysis →
            </a>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="nav-card nav-card-alt">
            <div class="nav-icon nav-icon-alt">📈</div>
            <h3>Case Studies & AI Prediction</h3>
            <p>Applied case studies, machine learning models, and data-driven business recommendations.</p>
            <a href='https://bramha007-dswp-proj-app-7eb1wn.streamlit.app/' target='_blank' class="nav-btn nav-btn-alt">
                View Case Studies →
            </a>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Contributions Section
st.markdown('<div class="section-header"> Key Contributions</div>', unsafe_allow_html=True)

contrib_col1, contrib_col2 = st.columns(2, gap="large")

with contrib_col1:
    st.markdown("""
    <div class="contrib-card">
        <h4> Academic Excellence</h4>
        <ul style="margin: 0; padding-left: 1.2rem;">
            <li>End-to-end data science workflow</li>
            <li>Statistical and ML foundations</li>
            <li>Rigorous scientific methodology</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with contrib_col2:
    st.markdown("""
    <div class="contrib-card contrib-card-alt">
        <h4> Practical Impact</h4>
        <ul style="margin: 0; padding-left: 1.2rem;">
            <li>Real-world transportation insights</li>
            <li>Actionable recommendations</li>
            <li>Stakeholder-focused deliverables</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Team Section
st.markdown('<div class="section-header">👥 Project Team</div>', unsafe_allow_html=True)

team_col1, team_col2, team_col3 = st.columns(3, gap="large")

with team_col1:
    st.markdown("""
        <div class='team-card'>
            <div class="team-avatar">👨‍🎓</div>
            <p class='team-name'>Mohammed Amaan Shaikh</p>
            <p class='team-role'>Master's Student, DKE</p>
        </div>
    """, unsafe_allow_html=True)

with team_col2:
    st.markdown("""
        <div class='team-card'>
            <div class="team-avatar">👨‍🎓</div>
            <p class='team-name'>Nitish Kamlesh Choudhary</p>
            <p class='team-role'>Master's Student, DKE</p>
        </div>
    """, unsafe_allow_html=True)

with team_col3:
    st.markdown("""
        <div class='team-card'>
            <div class="team-avatar team-avatar-alt">👩‍🎓</div>
            <p class='team-name'>Yashashwini Sidramappa Awate</p>
            <p class='team-role'>Master's Student, DKE</p>
        </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
    <div class='footer'>
        <p class='footer-title'>Master's Project — Data Science with Python</p>
        <p class='footer-subtitle'>🚴 NYC Citi Bike Data Analysis</p>
        <p class='footer-copy'>Built with Python & Streamlit | © 2025</p>
    </div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
        <div class="sidebar-header">
            <div class="sidebar-logo">🚴</div>
            <div class="sidebar-title">Citi Bike Analysis</div>
            <div class="sidebar-subtitle">Navigation Guide</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    This dashboard serves as the main landing page for the NYC Citi Bike Data Science project.
    
    **Quick Links**
    -  Preprocessing & EDA
    -  Case Studies & Prediction
    """)
    
    st.markdown("---")
    
    st.markdown(" Resources")
    st.markdown("""
    - [NYC Citi Bike System Data](https://citibikenyc.com/system-data)
    - [Project Repository](https://code.ovgu.de/ratu79ge/bike-share-data-science/-/tree/main?ref_type=heads)
    - [Background Image Credits](https://unsplash.com/de/fotos/person-die-mit-dem-fahrrad-auf-einer-strasse-in-der-stadt-fahrt-y5CDsA0hQ7g)
    """)
