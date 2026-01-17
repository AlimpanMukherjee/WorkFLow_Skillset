from operator import itemgetter
students=[{"name":"bob",'marks':98},
          {"name":"alice",'marks':78},
          {"name":"charlie",'marks':88},
          {"name":"david",'marks':92},
          {"name":"eve",'marks':85}]


sortedStudents=sorted(students,key=itemgetter('marks'),reverse=True)
for student in sortedStudents:
    print(student['name'])


for student in sortedStudents:
    print(student['marks'])

print(sortedStudents)