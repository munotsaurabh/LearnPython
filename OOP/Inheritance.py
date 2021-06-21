class Student:                  # This is the parent class
  def __init__(self, name, school):
    self.name = name
    self.school = school
    self.marks = []
  
  def average(self):
    return sum(self.marks) / len(self.marks)

class WorkingStudent(Student): #This is inheritance. This syntax extends the base class i.e Student class
  def __init__(self, name, school, salary): #This is the child class
    super().__init__(name, school) #Extend name and school property of the base class
    self.salary = salary

  def weekly_salary(self):
    return self.salary * 5

virat = Student ('Virat', 'DPS') 
print ("Virat's school is: " +virat.school)

rohit = WorkingStudent ('Rohit', 'MVS', 50)
print (f"Rohit's salary is: {rohit.salary}")
rohit.marks.append(55)
rohit.marks.append(97)

print (f"Rohit's average marks: {rohit.average()}")
print (f"Rohit's weekly salary: {rohit.weekly_salary()}")


