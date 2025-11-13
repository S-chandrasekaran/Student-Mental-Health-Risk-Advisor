from experta import *

class Student(Fact):
    """Student attributes"""
    pass

class MentalHealthAdvisor(KnowledgeEngine):

    @Rule(Student(attendance='low', grades='poor', mood='sad', sleep='irregular'))
    def high_risk(self):
        self.declare(Fact(risk='High'))

    @Rule(Student(attendance='medium', grades='average', mood='anxious'))
    def moderate_risk(self):
        self.declare(Fact(risk='Moderate'))

    @Rule(Student(attendance='high', grades='good', mood='happy'))
    def low_risk(self):
        self.declare(Fact(risk='Low'))
import streamlit as st
from pyknow import *

# Define the expert system class (reuse from above)
class Student(Fact): pass
class MentalHealthAdvisor(KnowledgeEngine):
    result = None

    @Rule(Student(attendance='low', grades='poor', mood='sad', sleep='irregular'))
    def high_risk(self):
        MentalHealthAdvisor.result = "High Risk: Immediate counseling recommended."

    @Rule(Student(attendance='medium', grades='average', mood='anxious'))
    def moderate_risk(self):
        MentalHealthAdvisor.result = "Moderate Risk: Monitor and suggest wellness activities."

    @Rule(Student(attendance='high', grades='good', mood='happy'))
    def low_risk(self):
        MentalHealthAdvisor.result = "Low Risk: No immediate concern."

# Streamlit UI
st.title("🧠 Student Mental Health Risk Advisor")

attendance = st.selectbox("Attendance", ["low", "medium", "high"])
grades = st.selectbox("Grades", ["poor", "average", "good"])
mood = st.selectbox("Mood", ["sad", "anxious", "happy"])
sleep = st.selectbox("Sleep Pattern", ["irregular", "regular"])

if st.button("Assess Risk"):
    engine = MentalHealthAdvisor()
    engine.reset()
    engine.declare(Student(attendance=attendance, grades=grades, mood=mood, sleep=sleep))
    engine.run()
    st.success(MentalHealthAdvisor.result)
