import streamlit as st
import matplotlib.pyplot as plt

st.title("🧪 Diagnostic Test Accuracy (Bayes Theorem)")

st.markdown("Calculate the probability of disease given a positive test result.")

# --- Inputs for Test 1 ---
st.header("Test 1 Inputs")

prevalence = st.slider("Disease Prevalence (%)", 0.0, 100.0, 10.0) / 100
sensitivity = st.slider("Sensitivity (%)", 0.0, 100.0, 90.0) / 100
specificity = st.slider("Specificity (%)", 0.0, 100.0, 90.0) / 100

# --- Bayes Calculation Function ---
def bayes(prevalence, sensitivity, specificity):
    p_d = prevalence
    p_not_d = 1 - prevalence

    p_pos_given_d = sensitivity
    p_pos_given_not_d = 1 - specificity

    numerator = p_pos_given_d * p_d
    denominator = numerator + (p_pos_given_not_d * p_not_d)

    return numerator / denominator if denominator != 0 else 0

# --- Calculate Test 1 ---
posterior1 = bayes(prevalence, sensitivity, specificity)

st.subheader(f"✅ Test 1 Accuracy (P(Disease | Positive)) = {posterior1:.4f}")

# --- Option for Second Test ---
st.header("Optional: Add Second Test")

use_second_test = st.checkbox("Run Second Test")

posterior2 = None

if use_second_test:
    sensitivity2 = st.slider("Second Test Sensitivity (%)", 0.0, 100.0, 90.0) / 100
    specificity2 = st.slider("Second Test Specificity (%)", 0.0, 100.0, 90.0) / 100

    # Use posterior from first test as new prior
    posterior2 = bayes(posterior1, sensitivity2, specificity2)

    st.subheader(f"🔁 Test 2 Updated Accuracy = {posterior2:.4f}")

# --- Plotting ---
st.header("📊 Accuracy Comparison")

labels = ["Test 1"]
values = [posterior1]

if posterior2 is not None:
    labels.append("Test 2")
    values.append(posterior2)

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel("Probability")
ax.set_title("Accuracy Comparison")

st.pyplot(fig)
