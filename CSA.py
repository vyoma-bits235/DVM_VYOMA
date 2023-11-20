
import csv

class Course:
    def __init__(self, name, department, instructor, examination_date):
        self.name = name
        self.department = department
        self.instructor = instructor
        self.examination_date = examination_date
        self.sections = []

    def get_all_sections(self):
        return self.sections

    def __str__(self):
        print("Course:", self.name)
        print("Department:", self.department)
        print("Instructor:", self.instructor)
        print("Examination Date:", self.examination_date)

    def populate_new_sections(self, sections):
        if not self.sections:
            self.sections.append(sections)

class Section:
    def __init__(self, course, day, slot, type):
        self.course = course
        self.day = day
        self.slot = slot
        self.type = type
        self.occupied_slots = {day: [slot]}

    def get_occupied_slots(self):
        return self.occupied_slots

    def is_clash(self, other_section):
        return ((self.day in other_section.day or other_section.day in self.day )and (self.slot in other_section.slot or other_section.slot in self.slot ))

class Timetable:
    def __init__(self):
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
    def remove_course(self,course):
        self.courses.remove(course)

    def check_for_clashes(self):
        examination_clashes = []
        lecture_section_clashes = []

        for course1 in self.courses:
            for course2 in self.courses:
                if course1 != course2 and course1.examination_date == course2.examination_date:
                    examination_clashes.append((course1.name, course2.name))
        for course1 in self.courses:
            for course2 in self.courses:
                for section1 in course1.get_all_sections():
                    for section2 in course2.get_all_sections():
                        if course1!=course2 and section1[0].is_clash(section2[0]):
                            print(section1[0].is_clash(section2[0]))
                            lecture_section_clashes.append((section1[0].course.name, section1[0].type, section2[0].course.name, section2[0].type))

        return examination_clashes, lecture_section_clashes

    def export_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(['Course', 'Department', 'Instructor', 'Examination Date', 'Day', 'Slot', 'Type'])

            for course in self.courses:
                for section in course.get_all_sections():
                    writer.writerow([course.name, course.department, course.instructor, course.examination_date, section[0].day, section[0].slot, section[0].type])
def extract(detail):
    

    from csv import reader


    with open(detail, 'r') as read_obj:
  
        csv_reader = reader(read_obj)

        list_of_rows = list(csv_reader)
        list_of_rows.pop(0)
        return(list_of_rows)


timetable = Timetable()
def populate_course():
    
    with open('BOOKdvm.csv', 'r') as read_obj:
        o=input("which subject you want to add,all in capitals separated by comma and space between multiple WORD")
        o=list(o.split(","))
        l=[]
        
        csv_reader = csv.reader(read_obj) 

	
        list_of_csv = list(csv_reader) 

        for i in o:
            for j in list_of_csv:
                if j[1]==i:
                    l.append(j)
              
            
            
        with open('final.csv','w',newline="") as read_final:
            



            fields = ["COURSE_TITLE","SUBJECT","TEACHER","EXAMINA/DATE","DAY","HOUR","TYPE"
] 


          

	
	
            write = csv.writer(read_final)
	
            write.writerow(fields)
            write.writerows(l)
            return o
            

print("courses availaible:")
ty=["M1","THERMO","GENCHEM","EG","PHYSICS LABORATORY","MEOW","CHEMISTRY LABORATORY"
]
for i in ty:
    print(i)



o=populate_course()
print("YOU COULD ONLY ADD SECTIONS OF THESE COURSES ONLY OTHERWISWE IT WILL SAY NO SECTION",o)
P=extract("final.csv")

r,t,y,d,q,w,e=tuple(P[0])





IO=0
while True:
    if IO!=0:
        
        if input("DONE ADING, WANT TO EXIT TYPE exit otherwise type anything")=="exit":
            break
    IO=IO+1
    a=input("Enter code")
    b=input("Enter section")
    O=0
    for i in P:
        if i[0]==a and i[-1]==b:
            O+=1
            a,b,c,d,e,f,g=tuple(i)
            
        else:
            pass
    if O==0:
            print("NO SUCH SECTION")
            continue
        
    
    course2=Course(a,b,c,d)
    section2=Section(course2,e,f,g)
    course2.populate_new_sections([section2])
    timetable.enroll_course(course2)
    examination_clashes, lecture_section_clashes = timetable.check_for_clashes()
    if examination_clashes:
        print("Examination clashes:")
        timetable.remove_course(course2)
    
        for clash in examination_clashes:
           
            print("- " + clash[0] + " and " + clash[1])
        print("PLZ CHOOSE ANOTHER SECTION")
    elif lecture_section_clashes:
        print("Lecture/section clashes:")
        timetable.remove_course(course2)
        for clash in lecture_section_clashes:
            print("- " + clash[0] + " (" + clash[1] + ") and " + clash[2] + " (" + clash[3] + ")")
        print("PLZ CHOOSE ANOTHER SECTION")

    else:
        pass
    
timetable.export_to_csv("timetable1.csv")
print("done")


