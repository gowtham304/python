class employee:
    empcount = 0
    salary = []

    def _init_(self, name, family, salary, dept):
        self.salary = salary
        self.name = name
        self.family = family
        self.dept = dept
        employee.empcount += 1
        employee.salary.append(self.salary)

    def avg_salary(self):
        sum = 0
        for salary in employee.salary:
            sum += salary
            avgsal = sum / employee.empcount
        return avgsal


emp1 = employee("gautam", "software", 100000, "webdev")
emp2 = employee("kranthi","sports",100000,"cricket")
print(emp1.avg_salary())
class fulltime(employee):
    def _init_(self,name,family,salary,dept):
        employee._init_(self,name,family,salary,dept)
        self.type="fulltime"
emp3=fulltime("sk","gamer",120000,"creative")
print(emp3.type)