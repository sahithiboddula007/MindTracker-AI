import streamlit as st
import datetime
import sqlite3

# DB setup
conn = sqlite3.connect('mindtrack.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS entries (date TEXT, mood TEXT, stress INTEGER, sleep REAL, study REAL, tasks INTEGER, notes TEXT)")
conn.commit()
conn.close()

st.title("🧠 MindTrack AI - Student Wellness Assistant")
st.write("Your personal AI wellness coach for stress-free studying")

menu = st.sidebar.selectbox("Navigate", ["Daily Check-in", "AI Wellness Coach", "Dashboard"])

if menu == "Daily Check-in":
    st.header("😊 How are you feeling today?")
    mood = st.selectbox("Mood", ["Happy 😊", "Calm 😌", "Stressed 😣", "Anxious 😰", "Tired 😴"])
    stress = st.slider("Stress Level (1-10)", 1, 10, 5)
    sleep = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)
    study = st.number_input("Study Hours", 0.0, 16.0, 4.0)
    notes = st.text_area("Quick Note")
    if st.button("Save Entry"):
        conn = sqlite3.connect('mindtrack.db')
        c = conn.cursor()
        c.execute("INSERT INTO entries VALUES (?,?,?,?,?,?,?)", (str(datetime.date.today()), mood, stress, sleep, study, 3, notes))
        conn.commit()
        conn.close()
        st.success("✅ Saved! Great job Sahithi!")
        st.balloons()

elif menu == "AI Wellness Coach":
    st.header("🤖 AI Wellness Coach")
    q = st.text_area("How are you feeling? Ex: I am stressed about exams")
    if st.button("Get Support"):
        if "stress" in q.lower() or "exam" in q.lower():
            st.info("Exams are stressful 😔. Try 4-7-8 breathing, 25-min pomodoro, and write 3 things you can control. You got this!")
        else:
            st.info("You are doing your best! 🌟 Take 5-min breaks, prioritize 3 tasks, celebrate small wins.")

elif menu == "Dashboard":
    st.header("📊 Your Wellness")
    conn = sqlite3.connect('mindtrack.db')
    c = conn.cursor()
    c.execute("SELECT * FROM entries")
    rows = c.fetchall()
    conn.close()
    if rows:
        st.write(rows)
    else:
        st.warning("No entries yet. Go to Daily Check-in!")