import pandas as pd
records = [
    (45, 50, 40, 60, 5.5),
    (55, 60, 50, 70, 4.0),
    (35, 40, 30, 50, 3.0),
    (60, 65, 55, 80, 7.0),
    (25, 30, 20, 40, 4.5),
    (50, 55, 45, 65, 2.5),
    (40, 45, 35, 55, 4.2),
    (30, 35, 25, 45, 3.8),
    (65, 70, 60, 85, 4.5),
    (20, 25, 15, 35, 5.4)
]

df2 = pd.DataFrame.from_records(records, 
              columns=['Test Score','Writing Skills','Reading Skill','Attendance','Hours of Sleep'])
print(df2)

