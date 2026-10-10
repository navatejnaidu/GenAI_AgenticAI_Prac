import streamlit as st
from ollama import Client

client = Client(host="http://localhost:11434")

st.set_page_config(
    page_title="Custom LLM model by Navatej - Ollama",
    layout="centered"
)

# =========================
# GAMING UI CSS
# =========================

st.markdown("""
<style>

/* Main background */
.stApp {
    background:
        radial-gradient(circle at top right, rgba(255, 0, 0, 0.18), transparent 35%),
        radial-gradient(circle at bottom left, rgba(180, 0, 0, 0.12), transparent 30%),
        linear-gradient(135deg, #050505 0%, #0b0b0b 45%, #120000 100%);
    color: #ffffff;
}

/* Add subtle gaming grid */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background-image:
        linear-gradient(rgba(255, 0, 0, 0.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255, 0, 0, 0.035) 1px, transparent 1px);
    background-size: 35px 35px;
    pointer-events: none;
    z-index: 0;
}

/* Main content */
.block-container {
    max-width: 900px;
    padding-top: 45px;
    position: relative;
    z-index: 1;
}

/* Title */
h1 {
    color: #ff1a1a !important;
    text-align: center;
    font-family: "Arial Black", Arial, sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    text-shadow:
        0 0 5px #ff0000,
        0 0 15px rgba(255, 0, 0, 0.8),
        0 0 30px rgba(255, 0, 0, 0.4);
}

/* Normal text */
p, label {
    color: #dddddd !important;
}

/* Prompt box */
.stTextArea textarea {
    background: #080808 !important;
    color: #ffffff !important;
    border: 1px solid #8b0000 !important;
    border-radius: 8px !important;
    box-shadow:
        0 0 8px rgba(255, 0, 0, 0.25),
        inset 0 0 15px rgba(255, 0, 0, 0.04);
    font-family: Consolas, monospace !important;
}

/* Prompt box when selected */
.stTextArea textarea:focus {
    border: 1px solid #ff0000 !important;
    box-shadow:
        0 0 10px rgba(255, 0, 0, 0.6),
        0 0 25px rgba(255, 0, 0, 0.2) !important;
}

/* Generate button */
.stButton > button {
    width: 100%;
    height: 55px;
    background: linear-gradient(90deg, #650000, #d40000, #650000) !important;
    color: white !important;
    border: 1px solid #ff2020 !important;
    border-radius: 8px !important;
    font-weight: bold !important;
    font-size: 17px !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    box-shadow:
        0 0 8px rgba(255, 0, 0, 0.5),
        0 0 20px rgba(255, 0, 0, 0.2);
    transition: 0.2s ease-in-out;
}

/* Button hover */
.stButton > button:hover {
    background: linear-gradient(90deg, #a00000, #ff0000, #a00000) !important;
    border-color: #ff5555 !important;
    box-shadow:
        0 0 15px rgba(255, 0, 0, 0.8),
        0 0 35px rgba(255, 0, 0, 0.4);
    transform: translateY(-2px);
}

/* Response success box */
.stAlert {
    background: rgba(20, 0, 0, 0.85) !important;
    border: 1px solid #8b0000 !important;
    border-radius: 8px !important;
}

/* Response container */
.response-box {
    background: linear-gradient(
        135deg,
        rgba(15, 15, 15, 0.98),
        rgba(30, 0, 0, 0.95)
    );
    border: 1px solid #990000;
    border-left: 4px solid #ff0000;
    border-radius: 10px;
    padding: 25px;
    margin-top: 20px;
    color: #eeeeee;
    font-family: Consolas, monospace;
    line-height: 1.7;
    box-shadow:
        0 0 10px rgba(255, 0, 0, 0.25),
        inset 0 0 25px rgba(255, 0, 0, 0.03);
}

/* Console header */
.console-header {
    background: #080808;
    border: 1px solid #700000;
    border-radius: 10px;
    padding: 12px 18px;
    margin-bottom: 25px;
    font-family: Consolas, monospace;
    color: #ff3333;
    box-shadow: 0 0 15px rgba(255, 0, 0, 0.15);
}

/* Status */
.status {
    color: #ff3333;
    font-family: Consolas, monospace;
    font-size: 13px;
    letter-spacing: 1px;
}

/* Divider */
hr {
    border-color: #550000 !important;
}

/* Spinner */
.stSpinner > div {
    border-top-color: #ff0000 !important;
}

/* Hide Streamlit branding */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)


# =========================
# GAMING CONSOLE HEADER
# =========================

st.markdown("""
<div class="console-header">
    <div class="status">
        ● SYSTEM ONLINE &nbsp; | &nbsp;
        OLLAMA CORE &nbsp; | &nbsp;
        MODEL: DEEPSEEK-R1:1.5B
    </div>
</div>
""", unsafe_allow_html=True)


# =========================
# TITLE
# =========================

st.title("Navatej")

st.markdown("""
<div style="
text-align:center;
color:#888;
font-family:Consolas,monospace;
font-size:14px;
margin-top:-15px;
margin-bottom:30px;
letter-spacing:3px;
">
CUSTOM GAMING GPT
</div>
""", unsafe_allow_html=True)


# =========================
# PROMPT
# =========================

prompt = st.text_area(
    "ENTER YOUR PROMPT:",
    height=200,
    placeholder=">> Type your command here..."
)


# =========================
# GENERATE RESPONSE
# =========================

if st.button("⚡ GENERATE RESPONSE"):

    # Fixed empty-prompt check
    if not prompt.strip():
        st.warning("Please enter a prompt.")

    else:

        with st.spinner("AI CORE PROCESSING..."):

            response = client.chat(
                model="deepseek-r1:1.5b",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.success("RESPONSE GENERATED!")

        # =========================
        # RESPONSE
        # =========================

        st.markdown(
            f"""
            <div class="response-box">
                <div style="
                    color:#ff2222;
                    font-weight:bold;
                    margin-bottom:15px;
                    letter-spacing:2px;
                ">
                    [ AI RESPONSE ]
                </div>

                {response["message"]["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# FOOTER
# =========================

st.markdown("""
<hr>

<div style="
text-align:center;
color:#555;
font-family:Consolas,monospace;
font-size:11px;
letter-spacing:2px;
">
LOCAL AI TERMINAL // POWERED BY OLLAMA
</div>
""", unsafe_allow_html=True)