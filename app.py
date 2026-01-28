import streamlit as st

# Page configuration
st.set_page_config(
    page_title="West Capital Lending HELOC",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for single-screen flyer design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+Pro:wght@400;600;700;900&display=swap');
    
    /* Hide Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
    [data-testid="stToolbar"] {display: none;}
    
    /* Full viewport design */
    .stApp {
        background: linear-gradient(145deg, #0A2540 0%, #122D47 50%, #0A2540 100%);
    }
    
    .main .block-container {
        padding: 1.5rem 2rem 1rem 2rem;
        max-width: 1000px;
    }
    
    /* Flyer Container */
    .flyer-wrapper {
        text-align: center;
    }
    
    /* Logo */
    .logo {
        font-family: 'Playfair Display', serif;
        font-size: 1.6rem;
        font-weight: 700;
        color: #FFFFFF;
        margin-bottom: 0.2rem;
    }
    
    .logo-sub {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.7rem;
        color: #C9A962;
        letter-spacing: 4px;
        text-transform: uppercase;
        margin-bottom: 1.2rem;
    }
    
    /* Main Headline */
    .headline {
        font-family: 'Playfair Display', serif;
        font-size: 2.6rem;
        font-weight: 700;
        color: #FFFFFF;
        line-height: 1.1;
        margin-bottom: 0.4rem;
    }
    
    .headline-gold {
        color: #C9A962;
    }
    
    .subheadline {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        color: #A8B9CA;
        margin-bottom: 1.5rem;
    }
    
    /* Benefits Grid */
    .benefits-row {
        display: flex;
        justify-content: center;
        gap: 1rem;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
    }
    
    .benefit-box {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(201, 169, 98, 0.4);
        border-radius: 12px;
        padding: 0.9rem 1.2rem;
        min-width: 140px;
        flex: 1;
        max-width: 160px;
    }
    
    .benefit-icon {
        font-size: 1.4rem;
        margin-bottom: 0.3rem;
    }
    
    .benefit-value {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.3rem;
        font-weight: 900;
        color: #C9A962;
        line-height: 1.2;
    }
    
    .benefit-label {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.75rem;
        color: #A8B9CA;
        line-height: 1.3;
    }
    
    /* Soft Credit Callout */
    .soft-credit-box {
        background: linear-gradient(135deg, #C9A962 0%, #D4B978 100%);
        border-radius: 12px;
        padding: 1rem 2rem;
        margin-bottom: 1.5rem;
        display: inline-block;
    }
    
    .soft-credit-text {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.1rem;
        font-weight: 700;
        color: #0A2540;
    }
    
    .soft-credit-sub {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.85rem;
        color: #0A2540;
        opacity: 0.85;
    }
    
    /* CTA Button */
    .cta-button {
        display: inline-block;
        background: #FFFFFF;
        color: #0A2540 !important;
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 1.2rem;
        font-weight: 700;
        padding: 1rem 3rem;
        border-radius: 50px;
        text-decoration: none;
        transition: all 0.3s ease;
        box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
        margin-bottom: 0.8rem;
    }
    
    .cta-button:hover {
        transform: scale(1.05);
        box-shadow: 0 12px 40px rgba(201, 169, 98, 0.4);
        color: #0A2540 !important;
    }
    
    .cta-sub {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.85rem;
        color: #A8B9CA;
    }
    
    /* Footer Contact */
    .footer-contact {
        margin-top: 1.2rem;
        padding-top: 1rem;
        border-top: 1px solid rgba(201, 169, 98, 0.2);
    }
    
    .footer-email {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.9rem;
        color: #C9A962;
        margin-bottom: 0.3rem;
    }
    
    .footer-email a {
        color: #C9A962;
        text-decoration: none;
    }
    
    .footer-email a:hover {
        text-decoration: underline;
    }
    
    .footer-address {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.75rem;
        color: #A8B9CA;
        margin-bottom: 0.5rem;
    }
    
    .footer-licenses {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.7rem;
        color: #6B7C8D;
        line-height: 1.5;
    }
    
    .footer-disclaimer {
        font-family: 'Source Sans Pro', sans-serif;
        font-size: 0.6rem;
        color: #5A6A7A;
        margin-top: 0.5rem;
    }
    
    /* Mobile Responsive */
    @media (max-width: 600px) {
        .headline {
            font-size: 1.9rem;
        }
        .benefit-box {
            min-width: 100px;
            padding: 0.7rem 0.8rem;
        }
        .benefit-value {
            font-size: 1.1rem;
        }
        .cta-button {
            padding: 0.9rem 2rem;
            font-size: 1rem;
        }
    }
</style>
""", unsafe_allow_html=True)

# Flyer Content
st.markdown("""
<div class="flyer-wrapper">
    
    <!-- Logo -->
    <div class="logo">West Capital Lending</div>
    <div class="logo-sub">Home Equity Solutions</div>
    
    <!-- Headline -->
    <div class="headline">Tap Into Your <span class="headline-gold">Home Equity</span></div>
    <div class="subheadline">Fast funding. No hassle. Lower rates than credit cards.</div>
    
    <!-- Benefits Grid -->
    <div class="benefits-row">
        <div class="benefit-box">
            <div class="benefit-icon">💰</div>
            <div class="benefit-value">$750K</div>
            <div class="benefit-label">Borrow up to</div>
        </div>
        <div class="benefit-box">
            <div class="benefit-icon">⚡</div>
            <div class="benefit-value">5 Days</div>
            <div class="benefit-label">Fast funding</div>
        </div>
        <div class="benefit-box">
            <div class="benefit-icon">🏠</div>
            <div class="benefit-value">No Appraisal</div>
            <div class="benefit-label">Under $400K</div>
        </div>
        <div class="benefit-box">
            <div class="benefit-icon">✨</div>
            <div class="benefit-value">$0</div>
            <div class="benefit-label">Out-of-pocket</div>
        </div>
        <div class="benefit-box">
            <div class="benefit-icon">🛡️</div>
            <div class="benefit-value">600+</div>
            <div class="benefit-label">Credit score OK</div>
        </div>
    </div>
    
    <!-- Soft Credit Callout -->
    <div class="soft-credit-box">
        <div class="soft-credit-text">✓ Starts With a Soft Credit Check</div>
        <div class="soft-credit-sub">Zero impact to your credit score</div>
    </div>
    
    <br>
    
    <!-- CTA Button -->
    <a href="https://www.fundhelocfast.com" target="_blank" class="cta-button">See What You Qualify For →</a>
    <div class="cta-sub">Takes just 5 minutes</div>
    
    <!-- Footer with Contact Info -->
    <div class="footer-contact">
        <div class="footer-email"><a href="mailto:csalas@westcapitallending.com">csalas@westcapitallending.com</a></div>
        <div class="footer-address">17911 Von Karman Ave Suite 400, Irvine, CA 92614</div>
        <div class="footer-licenses">
            NMLS 234176 | NMLS 1566096<br>
            DRE 01849995 | DRE 02022356
        </div>
        <div class="footer-disclaimer">
            Equal Housing Lender. Rates & terms subject to change. Not all applicants will qualify.
        </div>
    </div>
    
</div>
""", unsafe_allow_html=True)
