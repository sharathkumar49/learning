class Employee:

    def __init__(self, first, last, pay, receiver_accnt):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.receiver_accnt = receiver_accnt

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def amount(self, amount):
        return self.pay + amount


    def transer_funds(self, amount):
        self.receiver = 'vinoth'
        self.pay -amount
        print("sending amount to {}")


5000

emp_1 = Employee('Corey', 'Schafer', 50000, 'lavanya')
emp_2 = Employee('Test', 'Employee', 60000)


print(emp_1.amount(1000))  # Employee.amount(emp_1, 1000)


print(emp_1.__dict__)
