import pandas as pd
import streamlit as st

st.set_page_config(page_title="Yijun Gu | Interactive Resume", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&family=Source+Serif+4:wght@400;600&display=swap');

    :root {
        --bg-a: #f5f7f4;
        --bg-b: #e7eef3;
        --ink: #1f2d3a;
        --muted: #4a5968;
        --card: rgba(255, 255, 255, 0.8);
        --accent: #0f766e;
        --line: rgba(31, 45, 58, 0.12);
    }

    .stApp {
        background: radial-gradient(circle at 5% 5%, #ffffff 0%, var(--bg-a) 45%, var(--bg-b) 100%);
    }

    html, body, [class*="css"] {
        font-family: 'Space Grotesk', sans-serif;
        color: var(--ink);
    }

    h1, h2, h3 {
        font-family: 'Source Serif 4', serif;
        letter-spacing: 0.2px;
    }

    .hero {
        padding: 1.1rem 1.2rem;
        border: 1px solid var(--line);
        border-radius: 16px;
        background: linear-gradient(135deg, rgba(15, 118, 110, 0.08), rgba(37, 99, 235, 0.08));
        margin-bottom: 0.9rem;
    }

    .hero-title {
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }

    .hero-sub {
        color: var(--muted);
        margin-top: 0.35rem;
    }

    .pill {
        display: inline-block;
        border: 1px solid var(--line);
        background: var(--card);
        border-radius: 999px;
        padding: 0.25rem 0.65rem;
        margin-right: 0.4rem;
        margin-top: 0.35rem;
        font-size: 0.85rem;
    }

    .section-card {
        border: 1px solid var(--line);
        border-radius: 14px;
        background: var(--card);
        padding: 0.75rem 0.9rem;
    }

    div[data-testid="stMetricValue"] {
        color: var(--accent);
        font-weight: 700;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

PROFILE = {
    "name": "Yijun Gu",
    "headline": "Analytics Professional | MMA Candidate at Rotman",
    "email": "yijun.gu@rotman.utoronto.ca",
    "summary": (
        "An analytics professional with experience at Payments Canada and RBC. "
        "Skilled in SQL, Python, and Power BI to deliver actionable insights, "
        "including 40 percent process efficiency gains and improved reporting accuracy."
    ),
}

skills_df = pd.DataFrame(
    {
        "Skill": [
            "Python",
            "SQL",
            "Excel",
            "R",
            "VBA",
            "Tableau",
            "Power BI",
            "Jira",
            "Confluence",
            "NielsenIQ",
            "Risk Assessment",
            "Compliance Review",
            "Market Analysis",
            "Case Analysis",
            "Financial Statement Analysis",
        ],
        "Category": [
            "Programming",
            "Programming",
            "Analytics Tools",
            "Programming",
            "Programming",
            "Analytics Tools",
            "Analytics Tools",
            "Collaboration",
            "Collaboration",
            "Analytics Tools",
            "Business",
            "Business",
            "Business",
            "Business",
            "Business",
        ],
        "Proficiency": [95, 92, 90, 82, 80, 84, 93, 86, 85, 88, 87, 84, 86, 83, 89],
    }
)

education_df = pd.DataFrame(
    [
        {
            "Institution": "University of Toronto, Rotman School of Management",
            "Program": "Master of Management Analytics Candidate (2026)",
            "Period": "Aug 2025 - Present",
            "Location": "Toronto, Canada",
        },
        {
            "Institution": "University of Toronto Scarborough",
            "Program": "B.B.A. Management and Finance, Minor in Applied Statistics",
            "Period": "Sep 2021 - Jun 2025",
            "Location": "Toronto, Canada",
        },
    ]
)

experience_df = pd.DataFrame(
    [
        {
            "Role": "Data Analyst",
            "Organization": "Payments Canada",
            "Location": "Toronto, Canada",
            "Period": "Jan 2026 - Present",
            "Type": "Co-op",
            "Result": "Developed forecasting solutions and reporting workflows that improved planning quality and supported business decision-making.",
        },
        {
            "Role": "Business Analyst",
            "Organization": "Royal Bank of Canada",
            "Location": "Toronto, Canada",
            "Period": "May 2024 - Dec 2024",
            "Type": "Co-op",
            "Result": "Supported transfer pricing operations and implemented process automation to improve workflow efficiency and consistency.",
        },
    ]
)

project_df = pd.DataFrame(
    [
        {
            "Project": "Predicting Loan Default with a Machine Learning Credit Model",
            "Period": "Feb 2025",
            "Tools": "Python, Pandas, Random Forest",
            "Outcome": "Cleaned 250,000-row dataset and built model with 85% accuracy and over 70% sensitivity.",
        }
    ]
)

role_skill_map = {
    "Data Analyst": ["Python", "SQL", "Power BI", "Excel", "Tableau"],
    "Risk Analyst": ["Risk Assessment", "Financial Statement Analysis", "SQL", "Python", "Compliance Review"],
    "Business Analyst": ["Excel", "SQL", "Market Analysis", "Case Analysis", "Power BI"],
}

with st.sidebar:
    st.header("🧭 Navigation & Focus")
    st.caption("Tailor this resume to the role you are applying for.")

    target_role = st.selectbox("🎯 Target role", options=list(role_skill_map.keys()))
    selected_category = st.selectbox(
        "🧩 Skill category",
        options=["All"] + sorted(skills_df["Category"].unique().tolist()),
    )
    min_proficiency = st.slider(
        "📈 Minimum proficiency",
        min_value=60,
        max_value=100,
        value=80,
        step=5,
    )
    skill_lens = st.radio(
        "🔍 Skill lens",
        options=["Role-matched", "Show all filtered"],
        horizontal=False,
    )
    top_n_skills = st.slider("🏅 Top skills to display", min_value=5, max_value=15, value=10, step=1)
    show_contact = st.checkbox("📬 Show contact", value=True)

filtered_skills = skills_df.copy()
if selected_category != "All":
    filtered_skills = filtered_skills[filtered_skills["Category"] == selected_category]
filtered_skills = filtered_skills[filtered_skills["Proficiency"] >= min_proficiency]

if skill_lens == "Role-matched":
    filtered_skills = filtered_skills[
        filtered_skills["Skill"].isin(role_skill_map[target_role])
    ]

filtered_skills = filtered_skills.sort_values("Proficiency", ascending=False).head(top_n_skills)

filtered_experience = experience_df.copy()

st.markdown(
    f"""
    <div class='hero'>
      <p class='hero-title'>{PROFILE['name']}</p>
      <p class='hero-sub'>{PROFILE['headline']}</p>
      <span class='pill'>🎓 MMA Candidate 2026</span>
      <span class='pill'>🎯 {target_role}</span>
    </div>
    """,
    unsafe_allow_html=True,
)

if show_contact:
    st.info(
        f"📧 {PROFILE['email']}"
    )

summary_col, stats_col = st.columns([2.2, 1])
with summary_col:
    st.markdown("### 👋 Professional Snapshot")
    st.markdown(f"<div class='section-card'>{PROFILE['summary']}</div>", unsafe_allow_html=True)
with stats_col:
    st.metric("🏢 Organizations", str(experience_df["Organization"].nunique()))
    st.metric("🛠️ Skills Listed", str(len(skills_df)))
    st.metric("✅ Skills Shown", str(len(filtered_skills)))

overview_tab, experience_tab, skills_tab, education_tab = st.tabs(
    ["🏠 Overview", "💼 Experience", "🧠 Skills & Charts", "🎓 Education & Projects"]
)

with overview_tab:
    st.subheader("🌟 Core Highlights")
    highlights = {
        "Data Analyst": [
            "Improved forecast accuracy through time-series modeling and data validation.",
            "Standardized weekly and monthly forecast pipeline for finance decisions.",
            "Built dashboards and self-service analytics to improve reporting speed.",
        ],
        "Risk Analyst": [
            "Managed annual transfer pricing audit documentation across multiple entities.",
            "Applied risk-oriented analytics and reconciliation to reduce reporting discrepancies.",
            "Built structured audit support artifacts to improve compliance readiness.",
        ],
        "Business Analyst": [
            "Delivered benchmarked performance metrics for stakeholder reporting.",
            "Built automation workflows that improved operational efficiency.",
            "Developed market and customer segmentation insights to support decisions.",
        ],
    }
    for point in highlights[target_role]:
        st.markdown(f"- {point}")

    st.subheader("📌 Experience At A Glance")
    st.dataframe(
        filtered_experience[["Role", "Organization", "Period", "Type"]],
        use_container_width=True,
        hide_index=True,
    )

with experience_tab:
    st.subheader("💼 Experience Detail")
    st.dataframe(
        filtered_experience[
            ["Role", "Organization", "Location", "Period", "Type", "Result"]
        ],
        use_container_width=True,
        hide_index=True,
    )

with skills_tab:
    st.subheader("🧠 Skills Table")
    if filtered_skills.empty:
        st.warning("No skills match current filters.")
    else:
        skills_view = filtered_skills.copy().reset_index(drop=True)
        skills_view.insert(0, "Rank", skills_view.index + 1)
        skills_view["Level"] = pd.cut(
            skills_view["Proficiency"],
            bins=[0, 79, 89, 100],
            labels=["Foundation", "Strong", "Expert"],
        )

        st.dataframe(
            skills_view[["Rank", "Skill", "Category", "Proficiency", "Level"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "Rank": st.column_config.NumberColumn("Rank", format="%d"),
                "Proficiency": st.column_config.ProgressColumn(
                    "Proficiency",
                    format="%d",
                    min_value=0,
                    max_value=100,
                ),
            },
        )

        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.subheader("📊 Proficiency")
            st.bar_chart(
                skills_view.set_index("Skill")[["Proficiency"]],
                use_container_width=True,
            )
        with chart_col2:
            st.subheader("🧱 Category Mix")
            category_df = (
                skills_view.groupby("Category", as_index=False)
                .size()
                .rename(columns={"size": "Count"})
                .set_index("Category")
            )
            st.bar_chart(category_df[["Count"]], use_container_width=True)

with education_tab:
    st.subheader("🎓 Education")
    st.table(education_df)

    st.subheader("🚀 Project Experience")
    st.table(project_df)

    st.caption("Tip: Use role focus in the sidebar to tailor your story before interviews.")
