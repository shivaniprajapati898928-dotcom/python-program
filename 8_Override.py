# Create a base class Employee and a derived class Manager. Override a method to include managerial incentives in salary computation.

# Base class: Employee

class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    # Calculate total salary
    def calculate_salary(self):
        return self.salary

    # Display employee details
    def display_info(self):
        print("\n----- Employee Details -----")
        print(f"Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Base Salary: ₹{self.salary:.2f}")
        print("-----------------------------")


# Derived class: Manager
class Manager(Employee):
    def __init__(self, name, emp_id, salary, incentive):
        super().__init__(name, emp_id, salary)
        self.incentive = incentive

    # Override the method to include incentives
    def calculate_salary(self):
        total_salary = self.salary + self.incentive
        return total_salary

    # Override display method to show incentives
    def display_info(self):
        super().display_info()
        print(f"Incentive: ₹{self.incentive:.2f}")
        print(f"Total Salary (with Incentive): ₹{self.calculate_salary():.2f}")
        print("-----------------------------")


# Example usage
emp1 = Employee("Sumit singh", "E101", 90000)
mgr1 = Manager("Priya Singh", "M201", 60000, 15000)

emp1.display_info()
print(f"Total Salary: ₹{emp1.calculate_salary():.2f}")

mgr1.display_info()
