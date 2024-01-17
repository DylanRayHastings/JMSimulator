import random
from simulator.employee import Employee

class EmployeeManagement:
    def __init__(self):
        self.employees = []
        self.potential_hires = []

    def generate_random_employee(self):
        employee_id = len(self.employees) + 1
        return Employee(employee_id)

    def schedule_interview(self, employee):
        employee.scheduled_for_interview = True
        print(f'Interview scheduled for Employee {employee.employee_id}.')

    def hire_employee(self, employee):
        self.employees.append(employee)
        print(f'Employee {employee.employee_id} hired.')

    def train_employees(self, num_employees_to_train):
        employees_to_train = random.sample(self.employees, num_employees_to_train)
        for employee in employees_to_train:
            if not employee.is_trained:
                employee.train()

    def print_employee_details(self, employee):
        print(f'Employee ID: {employee.employee_id}')
        print(f'Is Trained: {employee.is_trained}')
        print(f'Scheduled for Interview: {employee.scheduled_for_interview}')
        print()

    def simulate_employee_management(self, num_employees, num_potential_hires, num_employees_to_train):
        for _ in range(num_potential_hires):
            potential_hire = self.generate_random_employee()
            self.potential_hires.append(potential_hire)

        for potential_hire in self.potential_hires:
            self.print_employee_details(potential_hire)

            if not potential_hire.is_trained:
                self.train_employees(1)

            self.hire_employee(potential_hire)

        self.train_employees(num_employees_to_train)

        for employee in self.employees:
            self.print_employee_details(employee)