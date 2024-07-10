students = [
    {'name': 'fazi', 'house': 'g9', 'gender':'female'},
    {'name': 'muni', 'house': 'pindi', 'gender':'female'},
    {'name': 'sarmad', 'house': 'g9', 'gender':'male'},
    {'name': 'kitty', 'house': 'h8', 'gender': None},
]
for student in students:
    # print(student,students[student], sep=',')
    print(student['name'], student['house'], student ['gender'], sep=', ')