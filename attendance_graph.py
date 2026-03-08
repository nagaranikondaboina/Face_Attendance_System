import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("attendance/attendance.csv")

attendance = data["Student"].value_counts()

attendance.plot(kind="bar")

plt.title("Student Attendance Analysis")
plt.xlabel("Students")
plt.ylabel("Number of Days Present")

plt.show()
