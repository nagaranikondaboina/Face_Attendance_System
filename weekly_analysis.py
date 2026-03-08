import pandas as pd

data = pd.read_csv("attendance/attendance.csv")

count = data["Student"].value_counts()

for student, days in count.items():

    if days < 3:

        print("Alert: Student",student,
              "absent continuously. Inform mentor.")
