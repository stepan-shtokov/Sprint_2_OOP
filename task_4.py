class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name=None, hours=None, rest_days=None, email=None):

        if hours is None:
            hours = ((7 - (rest_days or 0)) * 8)

        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name=None, hours=None, rest_days=None, email=None):

        if email is None:
            email = f"{name}@email.com"

        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, value):
        cls.hourly_payment = value

    def salary(self):
        print(f'{self.hours}, {self.hourly_payment}')
        return self.hours * self.hourly_payment


emp_sal = EmployeeSalary.get_hours()
print(emp_sal.salary())
