import streamlit as st
import base64

st.set_page_config(layout="wide")

# ---------- BACKGROUND IMAGE FUNCTION ----------
def add_bg_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()

    st.markdown(f"""
<style>

/* REMOVE DEFAULT MARGIN & WIDTH LIMIT */
.block-container {{
    padding: 0rem !important;
    max-width: 100% !important;
}}

.main {{
    padding: 0rem !important;
}}

section.main > div {{
    max-width: 100% !important;
    padding: 0rem !important;
}}

/* HERO SECTION FULL WIDTH */
.hero-section {{
    background-image: url("data:image/png;base64,{encoded}");
    height: 100vh;
    width: 100vw;
    margin: 0;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
}}

.hero-title {{
    color: white;
    font-size: 48px;
    font-weight: bold;
}}

.hero-subtitle {{
    color: #FFFF00;
    font-size: 22px;
    font-weight: 600;
    margin-top: 10px;
}}

</style>
""", unsafe_allow_html=True)


# ---------- CALL BACKGROUND ----------
add_bg_image("career.png")

# ---------- HERO CONTENT ----------
st.markdown("""
<div class="hero-section">
    <div class="hero-title">
        🚀 Smart Engineering Career Path Analyzer
    </div>
    <div class="hero-subtitle">
        ✨ Discover Your Strengths. Build Your Future. Become Industry Ready!
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- BELOW CONTENT (NO CHANGE) ----------
st.write(" ")
st.write(" ")


# ------------------ ENGINEERING FIELDS ------------------

fields = [
"AI & Data Science",
"Computer Science",
"AI & ML",
"Mechanical",
"Civil",
"Automobile",
"Agriculture",
"Mechatronics"
]

# ------------------ CAREER DATABASE ------------------

career_db = {

"AI & Data Science": {
    "Data Scientist 📊": {
        "core": ["machine learning", "statistics", "data analysis"],
        "programming": ["python", "sql"],
        "soft": ["problem solving"]
    },
    "Data Analyst 📈": {
        "core": ["data analysis"],
        "programming": ["python", "sql"],
        "soft": ["communication"]
    }
},

"Computer Science": {
    "Software Developer 💻": {
        "core": ["data structures", "algorithms"],
        "programming": ["python", "java", "c++"],
        "soft": ["problem solving"]
    },
    "Cyber Security Analyst 🔐": {
        "core": ["network security"],
        "programming": ["python"],
        "soft": ["analysis"]
    }
},

"AI & ML": {
    "AI Engineer 🤖": {
        "core": ["machine learning", "deep learning"],
        "programming": ["python"],
        "soft": ["problem solving"]
    }
},

"Mechanical": {
    "Design Engineer ⚙": {
        "core": ["thermodynamics", "mechanics"],
        "programming": [],
        "soft": ["problem solving"]
    }
},

"Civil": {
    "Structural Engineer 🏗": {
        "core": ["structural analysis"],
        "programming": [],
        "soft": ["teamwork"]
    }
},

"Automobile": {
    "Automobile Engineer 🚗": {
        "core": ["automobile systems"],
        "programming": [],
        "soft": ["analysis"]
    }
},

"Agriculture": {
    "Agricultural Engineer 🌾": {
        "core": ["soil science", "farming"],
        "programming": [],
        "soft": ["management"]
    }
},

"Mechatronics": {
    "Robotics Engineer 🤖": {
        "core": ["robotics", "automation"],
        "programming": ["python"],
        "soft": ["problem solving"]
    }
}
}

# ------------------ USER INPUT ------------------

st.markdown("### 👤 Enter Your Name")
name = st.text_input("")

st.markdown("### 🎓 Select Engineering Field")
field = st.selectbox("", fields)

st.markdown("### 🧠 Core Engineering Skills")
core_input = st.text_input("Example: machine learning, thermodynamics")

st.markdown("### 💻 Programming Skills")
prog_input = st.text_input("Example: python, java")

st.markdown("### 🤝 Soft Skills")
soft_input = st.text_input("Example: communication, leadership")

st.markdown("---")

# ------------------ SESSION MEMORY (Chat Style Continue) ------------------

if "history" not in st.session_state:
    st.session_state.history = []


# ------------------ ANALYSIS ------------------

if st.button("🔍 Analyze Career Path"):

    core = [s.strip().lower() for s in core_input.split(",") if s]
    prog = [s.strip().lower() for s in prog_input.split(",") if s]
    soft = [s.strip().lower() for s in soft_input.split(",") if s]

    careers = career_db[field]
    results = []

    # Career Descriptions
    career_description = {
        "Data Scientist 📊": "Analyzes datasets, builds ML models, helps business decisions.",
        "Data Analyst 📈": "Collects and analyzes data to create actionable insights.",
        "Software Developer 💻": "Designs and builds software applications using programming.",
        "Cyber Security Analyst 🔐": "Protects systems and networks from cyber threats.",
        "AI Engineer 🤖": "Develops intelligent AI/ML models for various applications.",
        "Design Engineer ⚙": "Designs mechanical components and systems.",
        "Structural Engineer 🏗": "Plans and analyzes building structures for safety.",
        "Automobile Engineer 🚗": "Works on vehicle design, manufacturing, and testing.",
        "Agricultural Engineer 🌾": "Applies engineering to agriculture, machinery, irrigation.",
        "Robotics Engineer 🤖": "Designs and develops robotic systems and automation."
    }

    # Salary Ranges
    salary_db = {
        "Data Scientist 📊": "₹6L - ₹25L",
        "Data Analyst 📈": "₹4L - ₹12L",
        "Software Developer 💻": "₹4L - ₹18L",
        "Cyber Security Analyst 🔐": "₹5L - ₹20L",
        "AI Engineer 🤖": "₹7L - ₹30L",
        "Design Engineer ⚙": "₹3L - ₹10L",
        "Structural Engineer 🏗": "₹3.5L - ₹12L",
        "Automobile Engineer 🚗": "₹3L - ₹10L",
        "Agricultural Engineer 🌾": "₹3L - ₹8L",
        "Robotics Engineer 🤖": "₹5L - ₹20L"
    }

    # Top Companies
    top_companies = {
        "Data Scientist 📊": ["TCS", "Infosys", "Wipro", "Google"],
        "Data Analyst 📈": ["TCS", "Accenture", "Cognizant"],
        "Software Developer 💻": ["Microsoft", "Infosys", "Wipro", "Amazon"],
        "Cyber Security Analyst 🔐": ["Paladion", "TCS", "Infosys"],
        "AI Engineer 🤖": ["Google", "Microsoft", "Amazon"],
        "Design Engineer ⚙": ["L&T", "Tata Motors", "Ashok Leyland"],
        "Structural Engineer 🏗": ["L&T", "Shapoorji Pallonji"],
        "Automobile Engineer 🚗": ["Tata Motors", "Mahindra", "Hyundai"],
        "Agricultural Engineer 🌾": ["John Deere", "Mahindra Agro"],
        "Robotics Engineer 🤖": ["ABB", "Bosch", "TCS"]
    }

    # Certification Suggestions
    certifications = {
        "Data Scientist 📊": ["Coursera ML", "Udemy Python", "NPTEL DS"],
        "Data Analyst 📈": ["Power BI", "Excel Certification"],
        "Software Developer 💻": ["Java Certification", "Python Bootcamp"],
        "Cyber Security Analyst 🔐": ["CEH", "CompTIA Security+"],
        "AI Engineer 🤖": ["Deep Learning Specialization - Coursera"],
        "Design Engineer ⚙": ["SolidWorks Certification", "AutoCAD"],
        "Structural Engineer 🏗": ["STAAD Pro", "ETABS Training"],
        "Automobile Engineer 🚗": ["CATIA", "Automobile Design Course"],
        "Agricultural Engineer 🌾": ["GIS for Agriculture", "Farm Machinery Training"],
        "Robotics Engineer 🤖": ["Arduino Projects", "MATLAB Robotics"]
    }

    # Calculate Match Percentage
    for career, skills in careers.items():
        total_skills = len(skills["core"]) + len(skills["programming"]) + len(skills["soft"])
        match_count = 0
        for s in core:
            if any(s in skill for skill in skills["core"]):
                match_count += 1
 
        for s in prog:
            if any(s in skill for skill in skills["programming"]):
                match_count += 1

        for s in soft:
            if any(s in skill for skill in skills["soft"]):
                match_count += 1


        percentage = (match_count / total_skills) * 100 if total_skills > 0 else 0
        if match_count > 0 and percentage < 10:
          percentage = 10
        results.append((career, percentage, skills))

    results.sort(key=lambda x: x[1], reverse=True)

    # Show Top 3 Careers
    st.markdown("<h2 style='color:#00FFFF;'>🎯 Top Career Recommendations</h2>", unsafe_allow_html=True)
    top_results = results[:3]

    for idx, (career, percent, required) in enumerate(top_results, 1):
        st.subheader(f"🥇 {career} — {percent:.1f}% Match" if idx==1 else f"🥈 {career} — {percent:.1f}% Match" if idx==2 else f"🥉 {career} — {percent:.1f}% Match")
        st.progress(int(percent))
        st.info(career_description.get(career, "Description not available."))
        st.write(f"💰 Salary Range: {salary_db.get(career,'N/A')}")
        st.write(f"🏢 Top Companies: {', '.join(top_companies.get(career,[]))}")
        st.write(f"🎓 Recommended Certifications: {', '.join(certifications.get(career,[]))}")

        # Skill Gap
        missing_core = set(required["core"]) - set(core)
        missing_prog = set(required["programming"]) - set(prog)
        missing_soft = set(required["soft"]) - set(soft)

        if missing_core:
            st.warning(f"🧠 Improve Core Skills: {', '.join(missing_core)}")
        if missing_prog:
            st.warning(f"💻 Improve Programming: {', '.join(missing_prog)}")
        if missing_soft:
            st.warning(f"🤝 Improve Soft Skills: {', '.join(missing_soft)}")
        if not (missing_core or missing_prog or missing_soft):
            st.success("🎉 Excellent! You are highly aligned for this role.")

        # Effort Suggestions
        st.markdown("<h4 style='color:#FFD700;'>🚀 How To Succeed In This Career</h4>", unsafe_allow_html=True)
        st.write("✔ Do Internship in relevant companies")
        st.write("✔ Participate in Workshops & Technical Events")
        st.write("✔ Build Real-world Projects")
        st.write("✔ Complete Industry Certifications")
        st.write("✔ Maintain Strong LinkedIn & GitHub Profile")

        # Save history
        st.session_state.history.append(career)


    else:
        st.error("❌ No strong match found. Improve your core fundamentals.")

# ------------------ CHAT CONTINUATION ------------------

if st.session_state.history:
    st.markdown("<h3>📝 Previous Recommendations</h3>", unsafe_allow_html=True)
    for item in st.session_state.history:
        st.write(f"➡ {item}")
