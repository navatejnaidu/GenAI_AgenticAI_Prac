import streamlit as st
import pickle
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Salary AI",
    page_icon=None,
    layout="centered"
)

# Premium Xbox-inspired green theme
st.markdown("""
<style>
.stApp {
    background: #0B0F0C;
    color: #E8F0EA;
}

.block-container {
    max-width: 850px;
    padding-top: 3rem;
    padding-bottom: 3rem;
}

/* Headings */
h1, h2, h3 {
    color: #F2F5F2 !important;
    letter-spacing: -0.8px;
}

p, label {
    color: #A8B5AA !important;
}

/* Main title */
h1 {
    font-weight: 750 !important;
}

/* Input field */
div[data-testid="stNumberInput"] input {
    background: #141A16;
    color: #A3FF12;
    border: 1px solid #344637;
    border-radius: 8px;
}

div[data-testid="stNumberInput"] input:focus {
    border-color: #7CFC00;
    box-shadow: 0 0 0 1px #7CFC00;
}

/* Xbox green button */
div.stButton > button {
    background: #107C10;
    color: #FFFFFF;
    border: 1px solid #20A820;
    border-radius: 8px;
    padding: 12px 20px;
    font-weight: 650;
    width: 100%;
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    background: #16A316;
    color: #FFFFFF;
    border-color: #7CFC00;
    box-shadow: 0 0 18px #107C1066;
    transform: translateY(-2px);
}

/* Salary result */
div[data-testid="stMetric"] {
    background: #141A16;
    border: 1px solid #29432D;
    border-left: 3px solid #107C10;
    padding: 20px;
    border-radius: 8px;
}

div[data-testid="stMetricLabel"] {
    color: #A8B5AA !important;
}

div[data-testid="stMetricValue"] {
    color: #7CFC00 !important;
}

/* Dividers */
hr {
    border-color: #26352A;
}

/* Graph container */
div[data-testid="stImage"],
div[data-testid="stPyplot"] {
    border-radius: 10px;
}

/* Footer */
div[data-testid="stCaptionContainer"] {
    color: #718075;
}
</style>
""", unsafe_allow_html=True)

# Load trained model
model = pickle.load(open(
    r"C:\Users\polin\Desktop\GenAI_AgenticAI_Prac\Python Prac\October\linear_regression_model.pkl",
    "rb"
))

# Header
st.caption("MACHINE LEARNING / SALARY ANALYTICS")

st.title("Salary Intelligence")

st.write(
    "Predict estimated salary using a machine learning regression model."
)

st.divider()

# Input
st.subheader("Prediction parameters")

years_experience = st.number_input(
    "Years of experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.5
)

# Prediction
if st.button("Generate Prediction"):
    experience_input = np.array([[years_experience]])
    prediction = model.predict(experience_input)[0]

    st.markdown("### Prediction result")

    st.metric(
        label="Estimated salary",
        value=f"${prediction:,.2f}"
    )

    # Regression graph
    x_values = np.linspace(0, 50, 200).reshape(-1, 1)
    y_values = model.predict(x_values)

    fig, ax = plt.subplots(figsize=(9, 4.5))

    fig.patch.set_facecolor("#141A16")
    ax.set_facecolor("#141A16")

    # Regression line
    ax.plot(
        x_values.flatten(),
        y_values,
        color="#7CFC00",
        linewidth=2.5,
        label="Regression line"
    )

    # Predicted point
    ax.scatter(
        [years_experience],
        [prediction],
        color="#FFFFFF",
        edgecolors="#7CFC00",
        linewidths=1.5,
        s=90,
        zorder=5,
        label="Your prediction"
    )

    ax.set_title(
        "Experience vs Predicted Salary",
        color="#E8F0EA",
        fontsize=13,
        pad=16
    )

    ax.set_xlabel(
        "Years of experience",
        color="#A8B5AA"
    )

    ax.set_ylabel(
        "Predicted salary ($)",
        color="#A8B5AA"
    )

    ax.tick_params(colors="#A8B5AA")

    for spine in ax.spines.values():
        spine.set_color("#344637")

    ax.grid(
        color="#29382D",
        linestyle="--",
        linewidth=0.6
    )

    ax.legend(
        facecolor="#141A16",
        edgecolor="#344637",
        labelcolor="#E8F0EA"
    )

    fig.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

st.divider()

st.caption(
    "P. Navatej  |  Python · Streamlit · Machine Learning"
)