import streamlit as st
import matplotlib.pyplot as plt

st.title("🧪 Simple Test Accuracy Checker")

st.markdown("""
This tool helps you understand:

👉 If your test result is **positive**, what is the **real chance you are actually sick?**

No math knowledge needed 🙂
""")

# --- Inputs ---
st.header("📌 Step 1: Basic Information")

prevalence = st.slider(
    "How common is the disease in the population? (%)",
    0.0, 100.0, 10.0
) / 100

sensitivity = st.slider(
    "If someone IS sick, how often does the test correctly detect it? (%)",
    0.0, 100.0, 90.0
) / 100

specificity = st.slider(
    "If someone is NOT sick, how often does the test correctly say negative? (%)",
    0.0, 100.0, 90.0
) / 100

# --- Bayes Calculation ---
def calculate_real_chance(prevalence, sensitivity, specificity):
    sick = prevalence
    healthy = 1 - prevalence

    positive_if_sick = sensitivity
    positive_if_healthy = 1 - specificity

    top = positive_if_sick * sick
    bottom = top + (positive_if_healthy * healthy)

    return top / bottom if bottom != 0 else 0

# --- Result for Test 1 ---
result1 = calculate_real_chance(prevalence, sensitivity, specificity)

st.header("📊 Result")

st.success(
    f"If your test is POSITIVE 👉 There is a **{result1*100:.2f}% chance you are actually sick**"
)

# --- Second Test Option ---
st.header("🔁 Want to double-check with a second test?")

use_second = st.checkbox("Yes, run a second test")

result2 = None

if use_second:
    sensitivity2 = st.slider(
        "Second test: If sick, how often detected? (%)",
        0.0, 100.0, 90.0
    ) / 100

    specificity2 = st.slider(
        "Second test: If healthy, how often correctly negative? (%)",
        0.0, 100.0, 90.0
    ) / 100

    result2 = calculate_real_chance(result1, sensitivity2, specificity2)

    st.success(
        f"After SECOND positive test 👉 Chance you are actually sick = **{result2*100:.2f}%**"
    )

# --- Graph ---
st.header("📈 Visual Comparison")

labels = ["After 1 Test"]
values = [result1]

if result2 is not None:
    labels.append("After 2 Tests")
    values.append(result2)

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylabel("Chance of actually being sick")
ax.set_title("How certainty increases with testing")

st.pyplot(fig)

# --- Extra Explanation ---
st.markdown("""
---
### 🧠 Simple Explanation

- Even a "good" test can give false positives  
- If a disease is rare, many positive results may still be wrong  
- Doing a second test usually increases confidence  

This tool helps you see that clearly 👍
""")
