class students:
    def __init__(self, name, usn, sem, kannada, english, phys, chem, mat):
        self.name=name
        self.usn=usn
        self.sem=sem
        self.kannada=kannada
        self.english=english
        self.phys=phys
        self.chem=chem
        self.mat=mat

    def create(self):
        Namelst.append(self.name)
        Usnlst.append(self.usn)
        Semlst.append(self.sem)
        Kannadalst.append(self.kannada)
        Englishlst.append(self.english)
        Physlst.append(self.phys)
        Chemlst.append(self.chem)
        Matlst.append(self.mat)
        print("\nstudent details added successfully!")

    def view(self):
        for viewing in range(0,len(Namelst)):
            print("\nName  : ", Namelst[viewing], "   USN : ", Usnlst[viewing], "   Semester  : ", Semlst[viewing], "   Kannada  : ", Kannadalst[viewing], "    English  : ", Englishlst[viewing] , "   Physics  : ", Physlst[viewing], "    Chemistry  : ", Chemlst[viewing], "    Maths  : ", Matlst[viewing])

    def delete(self, deleteStudent):
        self.deleteStudent=deleteStudent
        del(Namelst[self.deleteStudent])
        del(Usnlst[self.deleteStudent])
        del(Semlst[self.deleteStudent])
        del(Kannadalst[self.deleteStudent])
        del(Englishlst[self.deleteStudent])
        del(Physlst[self.deleteStudent])
        del(Chemlst[self.deleteStudent])
        del(Matlst[self.deleteStudent])
        print("\nDelete Successfull!")

    def search(self, searchStudent):
        self.searchStudent=searchStudent
        print("\nName  : ", Namelst[self.searchStudent], "   USN : ", Usnlst[self.searchStudent], "   Semester  : ", Semlst[self.searchStudent], "   Kannada  : ", Kannadalst[self.searchStudent], "    English  : ", Englishlst[self.searchStudent] , "   Physics  : ", Physlst[self.searchStudent], "    Chemistry  : ", Chemlst[self.searchStudent], "    Maths  : ", Matlst[self.searchStudent])

    def average(self):
        for ave in range(0,len(Namelst)):
            average=(int(int(Kannadalst[ave]) + int(Englishlst[ave]) + int(Physlst[ave]) + int(Chemlst[ave]) + int(Matlst[ave])))/5
            print("\nName : ", Namelst[ave], "    Average : ", average)

    def averageAboveGivenValue(self, givenValue):
        for ave in range(0,len(Namelst)):
            average1=(int(int(Kannadalst[ave]) + int(Englishlst[ave]) + int(Physlst[ave]) + int(Chemlst[ave]) + int(Matlst[ave])))/5
            Averagelst.append(average1)
        for ave1 in range(0, len(Averagelst)):
            if (Averagelst[ave1]>givenValue):
                print("\nName : ", Namelst[ave1], "   Average : ", Averagelst[ave1])
                sampleLst.append(Averagelst[ave1])
        if (len(sampleLst)==0):
            print("\nNo students with Average above ", givenValue)
        Averagelst.clear()
        sampleLst.clear()

    def failedStudents(self):
        for fail in range(0, len(Namelst)):
            if (int(Kannadalst[fail])<35 or int(Englishlst[fail])<35 or int(Physlst[fail])<35 or int(Chemlst[fail])<35 or int(Matlst[fail])<35):
                print("\nName : ", Namelst[fail], "   Kannada  : ", Kannadalst[fail], "    English  : ", Englishlst[fail] , "   Physics  : ", Physlst[fail], "    Chemistry  : ", Chemlst[fail], "    Maths  : ", Matlst[fail])
                sampleLst.append(Namelst[fail])
        if (len(sampleLst)==0):
            print("\nNo failed Students")
        sampleLst.clear()

    def passedStudents(self):
        for Pass in range(0, len(Namelst)):
            if (int(Kannadalst[Pass])>=35 and int(Englishlst[Pass])>=35 and int(Physlst[Pass])>35 and int(Chemlst[Pass])>=35 and int(Matlst[Pass])>=35):
                print("\nName : ", Namelst[Pass], "   Kannada  : ", Kannadalst[Pass], "    English  : ", Englishlst[Pass] , "   Physics  : ", Physlst[Pass], "    Chemistry  : ", Chemlst[Pass], "    Maths  : ", Matlst[Pass])
                sampleLst.append(Namelst[Pass])
        if (len(sampleLst)==0):
            print("\nNo passed Students")
        sampleLst.clear()


print("Welcome to Student Profile Management!")
Namelst, Usnlst, Semlst, Kannadalst, Englishlst, Physlst, Chemlst, Matlst, Averagelst, sampleLst=([] for i in range(10))
option=9
while(option!=0):
    option=int(input("\nEnter 1 to create new student\nEnter 2 to delete student\nEnter 3 to view the student list\nEnter 4 to search student by USN\nEnter 5 to get average of all the student\nEnter 6 to view the students with average greater than a given value\nEnter 7 to view the failed students\nEnter 8 to view the students passed\nEnter 0 to exit the program! "))
    if(option==0):
        print("\nProgram Completed! Thank you!")
        break
    elif(len(Namelst)==0 and option!=1):
        print("\nThere is no data to display!")
        continue

    elif (option==1):
        Name=input("\nEnter the name of the student : ")
        Usn=input("Enter the USN : ")
        Sem=input("Enter the semester : ")
        Kannada=input("Marks scored in Kannada : ")
        English=input("Marks scored in English : ")
        Phys=input("Marks scored in Physics : ")
        Chem=input("Marks scored in Chemistry : ")
        Mat=input("Marks scored in Maths : ")
        studentObj=students(Name, Usn, Sem, Kannada, English, Phys, Chem, Mat)
        studentObj.create()
    elif (option==2):
        deleteName=str(input("\nEnter the Name of the student you wish to delete."))
        if(deleteName in Namelst):
            delNameIndex=Namelst.index(deleteName)
        else:
            print("\nNo student called ", deleteName)
            continue
        studentObj.delete(delNameIndex)
        studentObj.view()
    elif (option==3):
        studentObj.view()
    elif (option==4):
        searchUsn=input("\nEnter the USN of the Student")
        if (searchUsn in Usnlst):
            searchUsnIndex=Usnlst.index(searchUsn)
        else:
            print("\nNo student with USN :  ", searchUsn)
            continue
        studentObj.search(searchUsnIndex)

    elif (option==5):
        studentObj.average()
    elif (option==6):
        userValue=float(input("\nEnter the Value : "))
        studentObj.averageAboveGivenValue(userValue)
    elif (option==7):
        studentObj.failedStudents()
    elif (option==8):
        studentObj.passedStudents()

    else:
        print("\nEnter Valid Number")
