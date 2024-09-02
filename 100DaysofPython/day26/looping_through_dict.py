from pandas.core.interchange import dataframe

from harvard_course_codes.dictionaries import student

student_dict = {
    "student_name": ["Fazila", "Roshan", "Beg"],
    "scores": [40,45,34]
}

# Looping through dict

# for (key, value) in student_dict.items():
#     print(key,value)

import pandas
student_dataframe = pandas.DataFrame(student_dict)
# print(student_dataframe)

# looping through dataframe
# for (key,value) in student_dataframe.items():
#     print(value)
# build in method

for(index,row) in student_dataframe.iterrows():
    if row.student_name == "Fazila":
        print(row.scores)