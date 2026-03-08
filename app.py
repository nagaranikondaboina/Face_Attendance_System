import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Face Recognition Attendance System")

st.header("Attendance Records")

data = pd.read_csv("attendance/attendance.csv")

st.dataframe(data)

st.header("Attendance Analysis")

attendance = data["Student"].value_counts()

fig, ax = plt.subplots()
attendance.plot(kind="bar", ax=ax)

st.pyplot(fig)
