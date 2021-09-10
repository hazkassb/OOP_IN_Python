class Student:
    def __init__(self, name: str, id: int, course_enrolled: str, annual_fee: float) -> None:
        self.name = name
        self.id = id
        self.course_enrolled = course_enrolled
        self.annual_fee = annual_fee
    
    def __str__(self) -> str:
        return 'Name = %s \nid = %s \ncourse_enrolled = %s \nannual_fee = %s' % (self.name, self.id, self.course_enrolled, self.annual_fee)

    def __lt__(self, other) -> bool:
        return self.annual_fee < other.annual_fee
    
    def __gt__(self, other) -> bool:
        return self.annual_fee > other.annual_fee
    

class ArtsStudent(Student):
    def __init__(self, name: str, id: int, course_enrolled: str, annual_fee: float, project_grade: str) -> None:
        super().__init__(name, id, course_enrolled, annual_fee)
        self.project_grade = project_grade
    
    def __str__(self) -> str:
        return super().__str__() + '\nProject Grade = ' + self.project_grade
    
class CommerceStudent(Student):
    def __init__(self, name: str, id: int, course_enrolled: str, annual_fee: float, internship_company: str) -> None:
        super().__init__(name, id, course_enrolled, annual_fee)
        self.internship_company = internship_company
    
    def __str__(self) -> str:
        return super().__str__() + "\ninternship_company = " + self.internship_company

class TechStudent(Student):
    def __init__(self, name: str, id: int, course_enrolled: str, annual_fee: float, internshipCompany: str, project_grade: str) -> None:
        super().__init__(name, id, course_enrolled, annual_fee)
        self.internship_company = internshipCompany
        self.project_grade = project_grade
    