import streamlit as st

# Page configuration
st.set_page_config(
    page_title="West Capital Lending | Home Equity Line of Credit",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for professional styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;500;600;700&family=Source+Sans+Pro:wght@300;400;600;700&display=swap');
    
    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Root variables */
    :root {
        --primary-navy: #0A2540;
        --primary-gold: #C9A962;
        --accent-gold: #E8D5A3;
        --light-cream: #FDFBF7;
        --warm-white: #FFFFFF;
        --text-dark: #1A1A2E;
        --text-muted: #5A6C7D;
    }
    
    /* Global styles */
    .stApp {
        background: linear-gradient(180deg, #FDFBF7 0%, #FFFFFF 100%);
    }
    
    .main .block-container {
        padding-top: 0;
        padding-bottom: 2rem;
        max-width: 1200px;
    }
    
    /* Hero Section */
    .hero-container {
        background: linear-gradient(135deg, #0A2540 0%, #163D5C 50%, #0A2540 100%);
        padding: 4rem 3rem;
        border-radius: 0 0 40px 40px;
        margin: -6rem -4rem 3rem -4rem;
        position: relative;
        overflow: hidden;
    }
    
    .hero-container::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23C9A962' fill-opacity='0.05'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
        opacity: 0.5;
    }
    
    .logo-text {
        font-family: 'Playfair Display', serif;
        font-size: 2.2rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.5rem;
        letter-spacing: 1px;
    }
    
    .logo-subtext {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.9rem;
        color: #C9A962;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 2rem;
    }
    
    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: 3rem;
        font-weight: 600;
        color: #FFFFFF;
        line-height: 1.2;
        margin-bottom: 1rem;
    }
    
    .hero-subtitle {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.25rem;
        color: #E8D5A3;
        font-weight: 300;
        max-width: 600px;
        line-height: 1.6;
    }
    
    .gold-accent {
        color: #C9A962;
    }
    
    /* Section Headers */
    .section-header {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 600;
        color: #0A2540;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .section-subheader {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: #5A6C7D;
        text-align: center;
        margin-bottom: 2.5rem;
        font-weight: 300;
    }
    
    /* Benefit Cards */
    .benefit-card {
        background: #FFFFFF;
        border-radius: 20px;
        padding: 2rem 1.5rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(10, 37, 64, 0.08);
        border: 1px solid rgba(201, 169, 98, 0.15);
        transition: all 0.3s ease;
        height: 100%;
    }
    
    .benefit-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(10, 37, 64, 0.12);
        border-color: #C9A962;
    }
    
    .benefit-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .benefit-title {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: #0A2540;
        margin-bottom: 0.5rem;
    }
    
    .benefit-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.95rem;
        color: #5A6C7D;
        line-height: 1.5;
    }
    
    /* Stats Section */
    .stats-container {
        background: linear-gradient(135deg, #0A2540 0%, #163D5C 100%);
        border-radius: 24px;
        padding: 3rem 2rem;
        margin: 3rem 0;
    }
    
    .stat-item {
        text-align: center;
        padding: 1rem;
    }
    
    .stat-number {
        font-family: 'Playfair Display', serif;
        font-size: 2.8rem;
        font-weight: 700;
        color: #C9A962;
        line-height: 1;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.95rem;
        color: #E8D5A3;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Process Steps */
    .process-step {
        background: #FFFFFF;
        border-radius: 16px;
        padding: 1.5rem;
        position: relative;
        box-shadow: 0 4px 15px rgba(10, 37, 64, 0.06);
        border-left: 4px solid #C9A962;
    }
    
    .step-number {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 700;
        color: #C9A962;
        margin-bottom: 0.5rem;
    }
    
    .step-title {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: #0A2540;
        margin-bottom: 0.25rem;
    }
    
    .step-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.9rem;
        color: #5A6C7D;
    }
    
    /* CTA Section */
    .cta-container {
        background: linear-gradient(135deg, #C9A962 0%, #E8D5A3 100%);
        border-radius: 24px;
        padding: 3rem 2rem;
        text-align: center;
        margin: 3rem 0;
    }
    
    .cta-title {
        font-family: 'Playfair Display', serif;
        font-size: 2rem;
        font-weight: 600;
        color: #0A2540;
        margin-bottom: 1rem;
    }
    
    .cta-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: #0A2540;
        margin-bottom: 1.5rem;
        opacity: 0.9;
    }
    
    /* Custom Button */
    .custom-button {
        display: inline-block;
        background: #0A2540;
        color: #FFFFFF !important;
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        font-weight: 600;
        padding: 1rem 2.5rem;
        border-radius: 50px;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(10, 37, 64, 0.3);
    }
    
    .custom-button:hover {
        background: #163D5C;
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(10, 37, 64, 0.4);
        color: #FFFFFF !important;
    }
    
    .custom-button-light {
        background: #FFFFFF;
        color: #0A2540 !important;
    }
    
    .custom-button-light:hover {
        background: #FDFBF7;
        color: #0A2540 !important;
    }
    
    /* Info Cards */
    .info-card {
        background: rgba(201, 169, 98, 0.08);
        border-radius: 16px;
        padding: 1.5rem;
        border: 1px solid rgba(201, 169, 98, 0.2);
    }
    
    .info-card-title {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.85rem;
        font-weight: 600;
        color: #C9A962;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-bottom: 0.5rem;
    }
    
    .info-card-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1rem;
        color: #0A2540;
        line-height: 1.5;
    }
    
    /* Footer */
    .footer-container {
        background: #0A2540;
        padding: 2rem;
        border-radius: 24px 24px 0 0;
        margin-top: 3rem;
        text-align: center;
    }
    
    .footer-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.85rem;
        color: #E8D5A3;
        opacity: 0.8;
        line-height: 1.6;
    }
    
    .footer-logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 1rem;
    }
    
    /* Disclaimer */
    .disclaimer {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.75rem;
        color: #5A6C7D;
        line-height: 1.6;
        text-align: center;
        padding: 1.5rem;
        background: rgba(201, 169, 98, 0.05);
        border-radius: 12px;
        margin-top: 2rem;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        .hero-container {
            padding: 2rem 1.5rem;
            margin: -6rem -1rem 2rem -1rem;
        }
        
        .hero-title {
            font-size: 2rem;
        }
        
        .section-header {
            font-size: 1.5rem;
        }
        
        .stat-number {
            font-size: 2rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown("""
<div class="hero-container">
    <div class="logo-text">West Capital Lending</div>
    <div class="logo-subheader">Home Equity Solutions</div>
    <div class="hero-title">Unlock Your Home's <span class="gold-accent">Potential</span></div>
    <div class="hero-subtitle">Access up to $750,000 in home equity with funding in as little as 5 days. No appraisal required for loans under $400K.</div>
    <br><br>
    <a href="https://www.fundhelocfast.com" target="_blank" class="custom-button">Check Your Rate — No Credit Impact →</a>
</div>
""", unsafe_allow_html=True)

# Benefits Section
st.markdown("""
<div class="section-header">Why Choose West Capital Lending?</div>
<div class="section-subheader">Experience a streamlined approach to accessing your home equity</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">💰</div>
        <div class="benefit-title">Borrow Up to $750K</div>
        <div class="benefit-text">Access substantial funds from your home equity for debt consolidation, home improvements, or major purchases.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">⚡</div>
        <div class="benefit-title">Fast Funding</div>
        <div class="benefit-text">Get funded in as little as 5 business days. Our streamlined digital process eliminates unnecessary delays.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">🏠</div>
        <div class="benefit-title">No Appraisal Needed</div>
        <div class="benefit-text">For loans under $400K, skip the traditional appraisal process. We use advanced property valuation technology.</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">💳</div>
        <div class="benefit-title">Lower Rates</div>
        <div class="benefit-text">Enjoy rates significantly lower than credit cards or personal loans. Your home equity works for you.</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">✨</div>
        <div class="benefit-title">No Out-of-Pocket Costs</div>
        <div class="benefit-text">All fees are rolled into your loan amount. No upfront costs or hidden charges at closing.</div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">🛡️</div>
        <div class="benefit-title">Credit Flexible</div>
        <div class="benefit-text">Programs available for credit scores as low as 600. We believe in providing access to home equity for more homeowners.</div>
    </div>
    """, unsafe_allow_html=True)

# Stats Section
st.markdown("""
<div class="stats-container">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div class="stat-item">
            <div class="stat-number">$750K</div>
            <div class="stat-label">Maximum Line Amount</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">5 Days</div>
            <div class="stat-label">Funding Timeline</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">600+</div>
            <div class="stat-label">Minimum Credit Score</div>
        </div>
        <div class="stat-item">
            <div class="stat-number">$0</div>
            <div class="stat-label">Out-of-Pocket Costs</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# How It Works Section
st.markdown("""
<div class="section-header">How It Works</div>
<div class="section-subheader">A simple, transparent process from start to finish</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="process-step">
        <div class="step-number">01</div>
        <div class="step-title">Check Your Rate</div>
        <div class="step-text">Soft credit check with Experian only — zero impact to your score.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="process-step">
        <div class="step-number">02</div>
        <div class="step-title">Get Pre-Approved</div>
        <div class="step-text">See your personalized offers and choose the terms that work for you.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="process-step">
        <div class="step-number">03</div>
        <div class="step-title">Complete Application</div>
        <div class="step-text">5-minute digital application. No paperwork or branch visits required.</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="process-step">
        <div class="step-number">04</div>
        <div class="step-title">Get Funded</div>
        <div class="step-text">Receive your funds in as little as 5 business days via direct deposit.</div>
    </div>
    """, unsafe_allow_html=True)

# Loan Terms Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-header">Flexible Loan Terms</div>
<div class="section-subheader">Choose the repayment schedule that fits your budget</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">5 Year Term</div>
        <div class="info-card-text">Shortest term with lower total interest paid</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">10 Year Term</div>
        <div class="info-card-text">Balanced payments and interest</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">15 Year Term</div>
        <div class="info-card-text">Popular choice for most homeowners</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="info-card">
        <div class="info-card-title">30 Year Term</div>
        <div class="info-card-text">Lowest monthly payments</div>
    </div>
    """, unsafe_allow_html=True)

# Use Cases Section
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div class="section-header">Put Your Equity to Work</div>
<div class="section-subheader">Popular uses for your home equity line of credit</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">🔧</div>
        <div class="benefit-title">Home Improvements</div>
        <div class="benefit-text">Renovate your kitchen, add a bathroom, or make upgrades that increase your home's value.</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">💸</div>
        <div class="benefit-title">Debt Consolidation</div>
        <div class="benefit-text">Combine high-interest credit cards and loans into one lower monthly payment.</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="benefit-card">
        <div class="benefit-icon">🎓</div>
        <div class="benefit-title">Major Expenses</div>
        <div class="benefit-text">Fund education costs, medical expenses, or once-in-a-lifetime opportunities.</div>
    </div>
    """, unsafe_allow_html=True)

# CTA Section
st.markdown("""
<div class="cta-container">
    <div class="cta-title">Ready to See What You Qualify For?</div>
    <div class="cta-text">It only takes 5 minutes. Start with a soft credit check that won't affect your score.</div>
    <a href="https://www.fundhelocfast.com" target="_blank" class="custom-button custom-button-light">Start Your Application →</a>
</div>
""", unsafe_allow_html=True)

# Key Features Summary
st.markdown("""
<div class="section-header">Program Highlights</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card" style="margin-bottom: 1rem;">
        <div class="info-card-title">Loan Details</div>
        <div class="info-card-text">
            • Line amounts from $15,000 to $750,000<br>
            • Fixed-rate options available<br>
            • Variable rate options in select states<br>
            • No prepayment penalties<br>
            • Draw feature to access additional funds
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="margin-bottom: 1rem;">
        <div class="info-card-title">Eligibility</div>
        <div class="info-card-text">
            • Credit scores from 600+<br>
            • Primary and secondary homes eligible<br>
            • Investment properties considered<br>
            • Maximum CLTV up to 85%<br>
            • Debt-to-income ratio up to 50%
        </div>
    </div>
    """, unsafe_allow_html=True)

# Disclaimer
st.markdown("""
<div class="disclaimer">
    <strong>Important Information:</strong> West Capital Lending HELOC is a home equity line of credit secured by your property. 
    Rates, terms, and conditions are subject to change and may vary based on creditworthiness, loan-to-value ratio, and other factors. 
    Not all applicants will qualify. This is not a commitment to lend. NMLS# [Your NMLS Number]. Equal Housing Lender.
    <br><br>
    Pre-qualification uses a soft credit inquiry (Experian only) which does not affect your credit score. 
    A hard credit inquiry will be required to complete the full application process.
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer-container">
    <div class="footer-logo">West Capital Lending</div>
    <div class="footer-text">
        Your trusted partner in home equity solutions.<br>
        © 2026 West Capital Lending. All rights reserved.<br><br>
        <a href="https://www.fundhelocfast.com" target="_blank" style="color: #C9A962;">www.fundhelocfast.com</a>
    </div>
</div>
""", unsafe_allow_html=True)
