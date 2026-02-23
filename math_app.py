import streamlit as st

# កំណត់ការរៀបចំទំព័រ
st.set_page_config(page_title="កម្មវិធីដោះស្រាយលំហាត់គណិតវិទ្យា", layout="wide")

st.title("🇰🇭 កម្មវិធីដោះស្រាយលំហាត់គណិតវិទ្យា (ថ្នាក់ទី ៦)")
st.write("ជ្រើសរើសមេរៀនដើម្បីចាប់ផ្តើមដោះស្រាយលំហាត់")

# បង្កើតបញ្ជីមេរៀនតាមរូបភាពដែលអ្នកបានផ្ញើមក
lessons = [
    "មេរៀនទី ៦ : បរិមាត្រ",
    "មេរៀនទី ៧ : ផ្ទៃក្រឡា",
    "មេរៀនទី ៩ : តួចែករួមធំបំផុត-ពហុគុណរួមតូចបំផុត",
    "មេរៀនទី ១៤ : ល្បឿន",
    "មេរៀនទី ១៦ : ភាគរយ",
    "មេរៀនទី ២០ : មាឌ និងផ្ទៃក្រឡាសូលីត"
]

selected_lesson = st.sidebar.selectbox("មាតិកាមេរៀន", lessons)

# --- ការដោះស្រាយតាមមេរៀននីមួយៗ ---

if selected_lesson == "មេរៀនទី ៦ : បរិមាត្រ":
    st.header("📏 គណនាបរិមាត្រ")
    shape = st.selectbox("ជ្រើសរើសរូបរាង", ["ចតុកោណកែង", "ការ៉េ"])
    
    if shape == "ចតុកោណកែង":
        L = st.number_input("បញ្ចូលបណ្តោយ (m)", min_value=0.0)
        W = st.number_input("បញ្ចូលទទឹង (m)", min_value=0.0)
        if st.button("គណនា"):
            P = 2 * (L + W)
            st.success(f"បរិមាត្រចតុកោណកែងគឺ៖ {P} m")
            st.info(f"រូបមន្ត៖ $P = (L + W) \\times 2$")

elif selected_lesson == "មេរៀនទី ១៤ : ល្បឿន":
    st.header("🏃 គណនាល្បឿន ចម្ងាយ និងរយៈពេល")
    mode = st.radio("តើអ្នកចង់រកអ្វី?", ["ល្បឿន (V)", "ចម្ងាយ (D)", "រយៈពេល (T)"])
    
    if mode == "ល្បឿន (V)":
        d = st.number_input("បញ្ចូលចម្ងាយ (km)", min_value=0.0)
        t = st.number_input("បញ្ចូលរយៈពេល (h)", min_value=0.1)
        if st.button("គណនា"):
            v = d / t
            st.success(f"ល្បឿនមធ្យមគឺ៖ {v:.2f} km/h")

elif selected_lesson == "មេរៀនទី ១៦ : ភាគរយ":
    st.header("📊 គណនាភាគរយ")
    total = st.number_input("ចំនួនសរុប", min_value=1.0)
    percent = st.number_input("ភាគរយ (%)", min_value=0.0)
    if st.button("រកលទ្ធផល"):
        result = (total * percent) / 100
        st.success(f"លទ្ធផលគឺ៖ {result}")

# បន្ថែមមេរៀនផ្សេងៗទៀតតាមលំនាំខាងលើ...