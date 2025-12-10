names= []
points = []
course = []

count = int(input("enter students number    :"))
for i in range(1,count+1,1):
    name = input("enter your name   :")
    names.append(name)
    total_unit = int(input("enter your total unit   :"))
    for i in range(1,total_unit+1,1):
        courses = int(input("enter your courses  :"))
        course.append(courses)
        point = float(input("enter your points   :"))
        points.append(point)

sumpoints = 0
summultiples = 0



print(f"Name {names} , Courses {course} , Points {points}")

