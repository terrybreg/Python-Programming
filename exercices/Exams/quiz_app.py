# quiz_app.py — Graphical interface for the Campaign Audit Quiz (Streamlit)
# Terry Bregmestre
#
# HOW TO RUN IT
#   1. Put this file in the same folder as campaign_audit.py and campaigns_A.csv
#   2. In the terminal:  pip install streamlit
#   3. Then:             streamlit run quiz_app.py
#   4. The quiz opens in the browser (in a Codespace, click "Open in Browser").
#
# WHAT IT DOES
#   I reuse the functions of campaign_audit.py (reading the CSV, CTR / CPA / ROAS,
#   the five answers, saving result.csv). This file only adds the interface:
#   - tab "Dashboard": key numbers, a table of the indicators and two charts
#   - tab "Quiz": the five questions in a form, the score and the corrections
#   - tab "Results": the history of result.csv

import os
import pandas as pd
import streamlit as st

import campaign_audit as audit

st.set_page_config(page_title="Campaign Audit Quiz", page_icon="📊", layout="wide")


# I load and compute the data only once: Streamlit re-runs the whole script at every
# click, so st.cache_data keeps the result in memory instead of re-reading the file
@st.cache_data
def load_data():
    campaigns = audit.load_campaigns(audit.DATA_FILE)
    return audit.add_indicators(campaigns)


# Turn my list of campaigns into a table (DataFrame) that Streamlit can display and chart
def to_table(campaigns):
    rows = []
    for c in campaigns:
        rows.append({
            "Campaign": c["name"],
            "Channel": c["channel"],
            "CTR (%)": round(c["ctr"], 2),
            "CPA (€)": round(c["cpa"], 2) if c["cpa"] is not None else None,
            "ROAS": round(c["roas"], 2) if c["roas"] is not None else None,
            "Conversions": int(c["conversions"]),
        })
    return pd.DataFrame(rows)


# If the CSV cannot be read, I show a clear message instead of a crash
try:
    campaigns = load_data()
except FileNotFoundError:
    st.error("campaigns_A.csv was not found. Put it in the same folder as quiz_app.py.")
    st.stop()
except KeyError as error:
    st.error(f"Column {error} was not found in the CSV file.")
    st.stop()

questions = audit.build_questions(campaigns)
table = to_table(campaigns)
campaign_names = sorted(c["name"] for c in campaigns)
channel_names = sorted({c["channel"] for c in campaigns})

# Memory between clicks: has the player already submitted, and what was the result
if "submitted" not in st.session_state:
    st.session_state.submitted = False
    st.session_state.score = 0
    st.session_state.details = []


# ---------- Header ----------
st.title("📊 Campaign Audit Quiz")
st.caption("Quarterly advertising export · CTR, CPA and ROAS · five questions")

tab_dashboard, tab_quiz, tab_results = st.tabs(["Dashboard", "Quiz", "Results"])


# ---------- Tab 1: dashboard ----------
with tab_dashboard:
    # Four key numbers at the top
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Campaigns analysed", len(campaigns), help="Campaigns with an empty impressions cell are excluded")
    col2.metric("Total cost", f"{sum(c['cost'] for c in campaigns):,.0f} €".replace(",", " "))
    col3.metric("Total revenue", f"{sum(c['revenue'] for c in campaigns):,.0f} €".replace(",", " "))
    col4.metric("Total conversions", f"{int(sum(c['conversions'] for c in campaigns)):,}".replace(",", " "))

    # A warning for the campaigns that lose money (ROAS below 1)
    losing = [c["name"] for c in campaigns if c["roas"] is not None and c["roas"] < 1]
    if losing:
        st.warning("ROAS below 1, these campaigns lose money: " + ", ".join(losing))

    st.subheader("Indicators by campaign")
    st.dataframe(table, hide_index=True, width="stretch")
    st.caption("An empty CPA means the campaign had zero conversions.")

    # Two charts side by side
    left, right = st.columns(2)
    with left:
        st.subheader("CTR by campaign (%)")
        st.bar_chart(table.set_index("Campaign")["CTR (%)"], horizontal=True)
    with right:
        st.subheader("ROAS by campaign")
        st.bar_chart(table.set_index("Campaign")["ROAS"], horizontal=True)

    st.subheader("Conversions by channel")
    st.bar_chart(table.groupby("Channel")["Conversions"].sum().sort_values(ascending=False))


# ---------- Tab 2: quiz ----------
with tab_quiz:
    st.info("Tip: the Dashboard tab shows the indicators. Try to answer without looking!")

    # A form sends all the answers at once when the player clicks the button,
    # instead of reloading the page after every answer
    with st.form("quiz_form"):
        player_name = st.text_input("Your name")

        q1 = st.selectbox("1. " + questions[0][0], campaign_names, index=None, placeholder="Choose a campaign")
        q2 = st.selectbox("2. " + questions[1][0], campaign_names, index=None, placeholder="Choose a campaign")
        q3 = st.number_input("3. " + questions[2][0], min_value=0, max_value=len(campaigns), step=1, value=None)
        q4 = st.selectbox("4. " + questions[3][0], channel_names, index=None, placeholder="Choose a channel")
        q5 = st.number_input("5. " + questions[4][0], min_value=0.0, max_value=100.0, step=0.01,
                             format="%.2f", value=None)

        submitted = st.form_submit_button("Submit my answers", type="primary")

    # When the button is clicked: I check that everything is filled, then I correct
    if submitted:
        answers = [q1, q2, q3, q4, q5]
        if not player_name.strip():
            st.error("Please type your name.")
        elif any(a is None for a in answers):
            st.error("Please answer the five questions.")
        else:
            score = 0
            details = []
            for (question, correct, kind), answer in zip(questions, answers):
                if kind == "integer":
                    answer = int(answer)
                ok = audit.is_correct(answer, correct, kind)
                score += ok
                details.append((question, answer, correct, ok))
            audit.save_result(audit.RESULT_FILE, player_name.strip(), score, len(questions))
            st.session_state.submitted = True
            st.session_state.score = score
            st.session_state.details = details

    # Show the score and the correction of each question
    if st.session_state.submitted:
        score = st.session_state.score
        st.subheader(f"Final score: {score}/{len(questions)}")
        st.progress(score / len(questions))
        if score == len(questions):
            st.balloons()
        for question, answer, correct, ok in st.session_state.details:
            shown = f"{correct:.2f}" if isinstance(correct, float) else correct
            answer = f"{answer:.2f}" if isinstance(answer, float) else answer
            if ok:
                st.success(f"✅ {question} — {answer}")
            else:
                st.error(f"❌ {question} — your answer: {answer} · correct answer: {shown}")
        st.caption("Your result was saved in result.csv.")


# ---------- Tab 3: results history ----------
with tab_results:
    st.subheader("Previous games (result.csv)")
    if os.path.exists(audit.RESULT_FILE):
        history = pd.read_csv(audit.RESULT_FILE)
        st.dataframe(history.iloc[::-1], hide_index=True, width="stretch")
    else:
        st.write("No game saved yet.")
