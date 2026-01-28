import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="West Capital Lending HELOC",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit UI elements
hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}
[data-testid="stToolbar"] {display: none;}
.stApp {
    background: #0A2540;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# Complete HTML page as a component
html_content = """
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Source+Sans+Pro:wght@400;600;700;900&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            background: linear-gradient(145deg, #0A2540 0%, #122D47 50%, #0A2540 100%);
            min-height: 100vh;
            font-family: 'Source Sans Pro', sans-serif;
        }
        
        .flyer-wrapper {
            text-align: center;
            padding: 20px;
            max-width: 900px;
            margin: 0 auto;
        }
        
        .logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: #FFFFFF;
            margin-bottom: 5px;
        }
        
        .logo-sub {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.75rem;
            color: #C9A962;
            letter-spacing: 4px;
            text-transform: uppercase;
            margin-bottom: 25px;
        }
        
        .headline {
            font-family: 'Playfair Display', serif;
            font-size: 2.8rem;
            font-weight: 700;
            color: #FFFFFF;
            line-height: 1.1;
            margin-bottom: 10px;
        }
        
        .headline-gold {
            color: #C9A962;
        }
        
        .subheadline {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 1.15rem;
            color: #A8B9CA;
            margin-bottom: 30px;
        }
        
        .benefits-row {
            display: flex;
            justify-content: center;
            gap: 12px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        
        .benefit-box {
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(201, 169, 98, 0.4);
            border-radius: 12px;
            padding: 15px 18px;
            min-width: 130px;
            flex: 1;
            max-width: 155px;
        }
        
        .benefit-icon {
            font-size: 1.5rem;
            margin-bottom: 8px;
        }
        
        .benefit-value {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 1.4rem;
            font-weight: 900;
            color: #C9A962;
            line-height: 1.2;
        }
        
        .benefit-label {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.8rem;
            color: #A8B9CA;
            line-height: 1.3;
        }
        
        .soft-credit-box {
            background: linear-gradient(135deg, #C9A962 0%, #D4B978 100%);
            border-radius: 12px;
            padding: 18px 35px;
            margin-bottom: 30px;
            display: inline-block;
        }
        
        .soft-credit-text {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 1.2rem;
            font-weight: 700;
            color: #0A2540;
        }
        
        .soft-credit-sub {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.9rem;
            color: #0A2540;
            opacity: 0.85;
        }
        
        .cta-button {
            display: inline-block;
            background: #FFFFFF;
            color: #0A2540;
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 1.25rem;
            font-weight: 700;
            padding: 18px 50px;
            border-radius: 50px;
            text-decoration: none;
            transition: all 0.3s ease;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.3);
            margin-bottom: 12px;
        }
        
        .cta-button:hover {
            transform: scale(1.05);
            box-shadow: 0 12px 40px rgba(201, 169, 98, 0.4);
        }
        
        .cta-sub {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.9rem;
            color: #A8B9CA;
            margin-bottom: 10px;
        }
        
        .footer-contact {
            margin-top: 25px;
            padding-top: 20px;
            border-top: 1px solid rgba(201, 169, 98, 0.2);
        }
        
        .footer-email {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 1rem;
            margin-bottom: 8px;
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
            font-size: 0.85rem;
            color: #A8B9CA;
            margin-bottom: 10px;
        }
        
        .footer-licenses {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.8rem;
            color: #7B8C9D;
            line-height: 1.6;
        }
        
        .footer-disclaimer {
            font-family: 'Source Sans Pro', sans-serif;
            font-size: 0.7rem;
            color: #5A6A7A;
            margin-top: 10px;
        }
        
        @media (max-width: 600px) {
            .headline {
                font-size: 2rem;
            }
            .benefit-box {
                min-width: 45%;
                padding: 12px 10px;
            }
            .benefit-value {
                font-size: 1.2rem;
            }
            .cta-button {
                padding: 15px 35px;
                font-size: 1.1rem;
            }
            .soft-credit-box {
                padding: 15px 25px;
            }
        }
    </style>
</head>
<body>
    <div class="flyer-wrapper">
        
        <div class="logo">West Capital Lending</div>
        <div class="logo-sub">Home Equity Solutions</div>
        
        <div class="headline">Tap Into Your <span class="headline-gold">Home Equity</span></div>
        <div class="subheadline">Fast funding. No hassle. Lower rates than credit cards.</div>
        
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
        
        <div class="soft-credit-box">
            <div class="soft-credit-text">✓ Starts With a Soft Credit Check</div>
            <div class="soft-credit-sub">Zero impact to your credit score</div>
        </div>
        
        <br><br>
        
        <a href="https://www.fundhelocfast.com" target="_blank" class="cta-button">See What You Qualify For →</a>
        <div class="cta-sub">Takes just 5 minutes</div>
        
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
</body>
</html>
"""

# Render the HTML component
components.html(html_content, height=750, scrolling=False)
