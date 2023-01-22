#--------------------------class subjects--------------------------
class subject:
    def __init__(self,subject,hours,students=None):
        self.subject=subject
        self.hours=hours
        self.students=students

#--------------------------class teachers--------------------------
class teacher:
    def __init__(self,subject,name,age,email=None,phoneN=None,adress=None):
        self.subject=subject
        self.name=name
        self.age=age
        self.email=email
        self.phoneN=phoneN
        self.adress=adress
        
    def add_email(self,email):
        self.email=email
    def add_phoneN(self,pn):
        self.phoneN=pn
    def add_adress(self,ad):
        self.adress=ad
        
#--------------------------class students--------------------------
class student:
    def __init__(self,id,name,age,teachers,email=None,phoneN=None,adress=None):
        self.id=id
        self.name=name
        self.age=age
        self.email=email
        self.phoneN=phoneN
        self.adress=adress
        self.teachers=teachers
        
    def add_email(self,email):
        self.email=email
        
    def add_phoneN(self,pn):
        self.phoneN=pn
        
    def add_adress(self,ad):
        self.adress=ad
        
    def show_teachers(self):
        if type(self.teachers)== tuple:
            t=""
            for i in range(len(self.teachers)):
                t+=self.teachers[i].name +" "
            return t
        else:
            return self.teachers.name
    def teacher_subject(self):
        return self.teachers.subject
    
    def show_student(self):
        print(f'''
            + student id: {self.id} 
                student name: {self.name} 
                student age:{self.age} 
                student email: {self.email}
                student phone number: {self.phoneN} 
                student adress: {self.adress} 
                student teachers: {self.show_teachers()}'''
            )

#----------------------------function--------------------------------
def add_students(n,info=4):
    global students_list
    while info<4:
        info+=1    
    p=len(students_list)+1
    for i in range(1,n+1):
        students_list.update({"s"+str(p):None})
        p+=1      
    return students_list

#--------------------------subjects list-----------------------------
subjects_list={
    "math":subject("math",5),
    "sti":subject("sti",4),
    "phy":subject("phy",5)
}

#--------------------------teachers list-----------------------------
teachers_list={
    "t1":teacher(subjects_list["math"],"adnan",40),
    "t2":teacher(subjects_list["sti"],"ahmed",41),
    "t3":teacher(subjects_list["math"],"hedi",42),
    "t4":teacher(subjects_list["phy"],"sousou",120)
}

#--------------------------students list-----------------------------
students_list={
    "s1":student("001","rayen",17,(teachers_list["t1"],teachers_list["t2"],teachers_list["t4"])),
    "s2":student("002","ela",17,(teachers_list["t1"],teachers_list["t2"],teachers_list["t4"])),
    "s3":student("003","omar",18,(teachers_list["t3"]))
}

students_list["s1"].add_email("rayenbenyoussef355@gmail.com")
students_list["s1"].add_phoneN(93071355)

students_list["s2"].add_adress("gharelmelh")


#-------------------------------show---------------------------------
students_list["s1"].show_student()
students_list["s2"].show_student()
students_list["s3"].show_student()
students_list=add_students(1)
print(students_list)
