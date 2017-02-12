class Employee:
    def __init__(self, fname, sname, salary, exper):
        self.fname = fname
        self.sname = sname
        self.salary = salary
        self.exper = exper

    def showempl(self):
        print("fName :", self.fname, "sName :", self.sname, "salary :", self.salary, "exper :", self.exper)


class Develop(Employee):
    def __init__(self, manager):
        self.manager = manager


    def showDev(self):
        return "fName :" + self.fname + "sName :" + self.sname + "salary :" + self.salary + "exper :" + self.exper + "manager :" + self.manager


class Designers(Develop):
    def __init__(self, effectivness):
        self.effectivness = effectivness

    def showDesign(self):
        return "fName :" + self.fname + "sName :" + self.sname + "salary :" + self.salary + "exper :" + self.exper + "manager :" + self.manager + "effect" + self.effectivness


class Manager(Designers):
    def __str__(self):
        pass
       # return "fName :" + self.fname + "sName :" +self.sname + "salary :" + self.salary + "exper :" + self.exper + "manager :" + self.manager + "effect" + self.effectivness

    usrEmpl = Employee(["Empl1", "Empl1", 100, 1], ["Empl2", "Empl2", 200, 2], ["Empl3", "Empl3", 300, 3])
#usrEmpl1 = Employee("Empl1", "Empl1", 100, 1)
#usrEmpl2 = Employee("Empl2", "Empl2", 200, 2)
#usrEmpl3 = Employee("Empl3", "Empl3", 300, 3)
#usrEmpl4 = Employee("Empl4", "Empl4", 400, 4)

    usrEmpl.showempl()
#usrEmpl1.showempl()
#usrEmpl2.showempl()
#usrEmpl3.showempl()
#usrEmpl4.showempl()