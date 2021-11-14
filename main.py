import json


def getPerson(usr):
    f = open('persons.json', 'r')
    JsonParser = json.load(f)
    for name in JsonParser.items():
        if name[0] == usr:
            return name[1]["role"]
    return ""


class Course:
    def __init__(self, name, mark, attendance, isfree):
        self.name = name
        self.mark = mark
        self.attendance = attendance
        self.isfree = isfree


class Admin:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def addStudent(self, name, password):
        dict = {name: {"role": "student", "password": password, "courses": []}}
        f = open('persons.json', 'r')
        JsonParse = json.load(f)
        JsonParse.update(dict)
        f.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)
        file.close()


    def deletePerson(self, name):
        fh= open('persons.json', 'r')
        JsonParse = json.load(fh)
        try:
            del JsonParse[name]
        except:
            print("Wrong name")
        fh.close()
        fh= open('persons.json', 'w')
        json.dump(JsonParse, fh)
        fh.close()


    def addTeacher(self, name, password):
        dict = {name: {"role": "teacher", "password": password, "courses": [], "rateStudent": []}}
        file=  open('persons.json', 'r')
        JsonParse = json.load(file)
        JsonParse.update(dict)
        file.close()
        fh= open('persons.json', 'w')
        json.dump(JsonParse, fh)
        file.close()

    def update(self, name, password):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            JsonParse[name]["password"] = password
        except:
            print("Wrong username")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)
        file.close()
    def addCourse(self, name, isfree):
        dict = {name: {"mark": 0, "attendance": 0, "isfree": isfree}}
        if isfree:
            limit = int(input("Write a limit of the course"))
            dict[name].update({"limit": limit})
        fh= open('courses.json', 'r')
        JsonParse = json.load(fh)
        JsonParse.update(dict)
        fh.close()
        fh= open('courses.json', 'w')
        json.dump(JsonParse, fh)
    def updateCourse(self, name, isfree):
        f= open('courses.json', 'r')
        data = json.load(f)
        try:
            data[name]["isfree"] = isfree
        except:
            print("Wrong name of course")
        f.close()
        fh= open('courses.json', 'w')
        json.dump(data, fh)
        fh.close()



    def addStudentToCourse(self, name, nameOfStud): #TODO need to check
        course = {"name": name}
        f= open("courses.json", 'r')
        data = json.load(f)
        course.update(data[name])
        f.close
        f= open("persons.json", 'r')
        data1 = json.load(f)
        data1[nameOfStud]["courses"].append(course)
        f.close
        f= open("persons.json", 'w')
        json.dump(data1, f)
        f.close()

    def addTeacherToCourse(self, NameOfCourse, NameOfTeacher): #TODO need to check
        course = {"name": NameOfCourse}

        f= open("courses.json", 'r')
        data = json.load(f)
        course.update(data[NameOfCourse])
        f.close()

        f= open("persons.json", 'r')
        data1 = json.load(f)
        data1[NameOfTeacher]["courses"].append(course)
        f.close()

        f= open("persons.json", 'w')
        json.dump(data1, f)
        f.close()


class Teacher:
    def __init__(self, name, password, rate: [int]):
        self.name = name
        self.rate = rate
        self.password = password

    def getSubject(self):
        file= open("persons.json", 'r')
        JsonParse = json.load(file)
        try:
            return JsonParse[self.name]["courses"]
        except:
            return {}

    def markStudent(self, name, nameOfSub, mark):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            for i in range(0, len(JsonParse[name]["courses"])):
                if JsonParse[name]["courses"][i]["name"] == nameOfSub:
                    JsonParse[name]["courses"][i]["mark"] = mark
        except:
                print("Wrong name")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)

    def addStudentToCourse(self, name, nameOfStud):
        course = {"name": name}
        f= open("courses.json", 'r')
        JsonParse = json.load(f)
        course.update(JsonParse[name])
        f.close()
        f= open("persons.json", 'r')
        JsonParse2 = json.load(f)
        JsonParse2[nameOfStud]["courses"].append(course)
        f.close()
        f= open("persons.json", 'w')
        json.dump(JsonParse2, f)

    def deleteStudentFromCourse(self, name, nameOfStud):
        file= open('persons.json', 'r')
        JsonParce = json.load(file)
        try:
            for i in range(0, len(JsonParce[nameOfStud]["courses"])):
                if JsonParce[nameOfStud]["courses"][i]["name"] == name:
                    del JsonParce[nameOfStud]["courses"][i]
        except:
            print("Wrong name")
        file.close()
        f= open('persons.json', 'w')
        json.dump(JsonParce, f)

    def rateStudent(self, NameOfCourse, NameOfStudent, grade):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            for i in range(0, len(JsonParse[NameOfStudent]["courses"])):
                if JsonParse[NameOfStudent]["courses"][i]["name"] == NameOfCourse:
                    JsonParse[NameOfStudent]["courses"][i]["attendance"] = grade
        except:
            print("Something Wrong with a course or name ")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)


class Student:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def seeMarks(self):
        StrLine = ""
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            for i in range(0, len(JsonParse[self.name]["courses"])):
                StrLine = str(JsonParse[self.name]["courses"][i][mark]) + " " + StrLine
        except:
            print("Wrong name")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)
        file.close()
        return StrLine

    def seeTeachers(self):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        for item in JsonParse.items():
            if item[1]["role"] == 'teacher':
                print(item[0] + " " + item[1]["courses"][0]["name"])

    def seeFreeCourses(self):
        file= open('courses.json', 'r')
        JsonParse = json.load(file)
        for item in JsonParse.items():
            if item[1]["isfree"]:
                print(item[0] + " is free course")

    def rateTeacher(self, nameOfTeacher, rate):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            for item in JsonParse.items():
                if item[1]["role"] == 'teacher' and item[0] == nameOfTeacher:
                    item[1]["rateStudent"].append(rate)
        except:
            print("Wrong name")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)

    def CancelEnroll(self, NameOfCourse):
        file= open('persons.json', 'r')
        JsonParse = json.load(file)
        try:
            for i in range(0, len(JsonParse[self.name]["courses"])):
                if JsonParse[self.name]["courses"][i]["name"] == NameOfCourse:
                    del JsonParse[self.name]["courses"][i]
        except:
            print("Wrong name")
        file.close()
        file= open('persons.json', 'w')
        json.dump(JsonParse, file)
        file.close()

    def EnrollCourse(self, NameOfCourse):
        course = {"name": NameOfCourse}
        file= open("courses.json", 'r+')
        data = json.load(file)
        course.update(data[NameOfCourse])
        file.close()
        file= open("persons.json", 'r')
        data1 = json.load(file)
        data1[self.name]["courses"].append(course)
        file.close()
        file= open("persons.json", 'w')
        json.dump(data1, file)
        file.close()


def login(username, pswrd):
    file= open('persons.json', 'r')
    JsonParser = json.load(file)
    try:
        for JsonParser in JsonParser.items():
            if JsonParser[0] == username:
                if pswrd == JsonParser[1]["password"]:
                    return True
    except:
        return False
    return False


while True:
    name = input("your login:")
    password = input("your password:")
    if login(name, password):
        role = getPerson(name)
        while True:
            if role == "admin":
                admin = Admin(name, password)
                print(""""
                1. Add student
                2. Update student
                3. Delete student
                4. Add teacher
                5. Update teacher
                6. Delete teacher
                7. Add course
                8. Update course
                9. Delete course
                10.Add course to Student
                11.Add course to Teacher
                12.Log out
                """)
                choice = input()

                if choice == "1":
                    N = input("enter a name of Student")
                    P = input("enter a password of student:")
                    admin.addStudent(N, P)
                elif choice == "2":
                    N = input("enter a name of Student")
                    P = input("enter a password of student:")
                    admin.update(N, P)
                elif choice == "3":
                    N = input("enter a name of a Student")
                    admin.deletePerson(N)
                elif choice == "4":
                    N = input("enter name of teacher:")
                    P = input("enter password of teacher:")
                    admin.addTeacher(N, P)
                elif choice == "5":
                    N = input("enter a name of teacher:")
                    P = input("enter a password of teacher:")
                    admin.update(N, P)
                elif choice == "6":
                    N = input("enter a name of teacher:")
                    admin.deletePerson(N)
                elif choice == "7":
                    N = input("enter a name of course:")
                    isFree = bool(input("Is this course free ? True/False(PS:please enter with capitalized letter):"))
                    admin.addCourse(N, isFree)
                elif choice == "8":
                    N = input("enter a name of the course:")
                    isFree = bool(input("Is this course free ? True/False(PS:please enter with capitalized letter):"))
                    admin.updateCourse(N, isFree)
                elif choice == "9":
                    N = input("enter a name of course:")
                    admin.deletePerson(N)
                elif choice == "10":
                    NameOfCourse = input("enter a name of course:")
                    NameOfStudent = input("enter a name of Student")
                    admin.addStudentToCourse(NameOfCourse, NameOfStudent)
                elif choice == "11":
                    NameOfCourse = input("enter a name of course:")
                    NameOfTeacher = input("enter a name of teacher:")
                    admin.addTeacherToCourse(NameOfCourse, NameOfTeacher)
                elif choice == "12":
                    break
                else:
                    continue
            elif role == "teacher":
                print("""
                1. see courses
                2. add or delete course from student
                3. mark a student
                4. rate Student 
                """)
                choice = input()
                teacher = Teacher(name, password, [])
                if choice == "1":
                    print(teacher.getSubject())
                elif choice == "2":
                    f = input("add or delete student from course?")
                    NameOfCourse = input("enter a name of the course:")
                    NameOfStudent = input("enter a name of a Student")
                    if f == 'add':
                        teacher.addStudentToCourse(NameOfCourse, NameOfStudent)
                    elif f == 'delete':
                        teacher.deleteStudentFromCourse(NameOfCourse, NameOfStudent)
                elif choice == "3":
                    NameOfStudent = input("enter a name of a Student")
                    mark = int(input("enter a mark:"))
                    NameOfCourse = input("enter a course:")
                    teacher.markStudent(NameOfStudent, NameOfCourse, mark)
                elif choice == "4":
                    NameOfCourse = input("enter a name of the course:")
                    NameOfStudent = input("enter a name of a Student:")
                    try:
                        grade = int(input("enter a grade of Student:"))
                    except ValueError:
                        print("please enter a number")
                    teacher.rateStudent(NameOfCourse, NameOfStudent, grade)
                else:
                    break
            elif role == "student":
                student = Student(name, password)
                print("""
                    1. enroll course
                    2. See teachers
                    3. See all marks 
                    4. Rate Teacher
                    5.See Free Courses
                    6.Log out
                    """)
                choice = input()
                if choice == "1":
                    add = input("enroll or cancel a course")
                    course = input("enter a name of the course:")
                    if add == 'enroll':
                        student.EnrollCourse(course)
                    elif add == 'cancel':
                        student.CancelEnroll(course)
                elif choice == "2":
                    student.seeTeachers()
                elif choice == "3":
                    student.seeMarks()
                elif choice == "4":
                    name = input("enter a name of teacher:")
                    Grade = int(input("enter a grade:"))
                    student.rateTeacher(name, Grade)
                elif choice == "5":
                    student.seeFreeCourses()
                elif choice == "6":
                    break
                else:
                    continue
            else:
                print("try again")
                break
    else:
        print("Wrong password, Try again")
