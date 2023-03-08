class Employee:

    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # def raise_amount(self):
    #     pass


emp_1 = Employee("Corey", "Shafer", 50000)
emp_2 = Employee("John", "Doe", 60000)

print(Employee.__dict__)
