"""
Employee Management System

This script defines a simple Employee class and functions for generating random employee data and scheduling shifts.

"""
import random
import openai
from datetime import datetime, timedelta
from collections import defaultdict
from icecream import ic

openai.api_key = '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'

role_availability = {
        "Opener": {"start": 700, "end": 1400},
        "Open Support": {"start": 900, "end": 1400},
        "Rush Support": {"start": 1000, "end": 1400},
        "Close Support": {"start": 1400, "end": 2000},
        "Closer": {"start": 1600, "end": 2130},
        "Shift Lead": {"start": 700, "end": 2130},
    }

class Employee:
    """
    Employee class for managing employee information and scheduling shifts.

    Attributes:
        - name (str): Name of the employee.
        - employee_id (str): Unique identifier for the employee.
        - role (str): Role of the employee (e.g., "Opener", "Shift Lead").
        - shifts (list): List of shifts the employee is available for.
        - rating (float): Employee's rating on a scale from 3.0 to 5.0.
        - trained (bool): Flag indicating whether the employee is trained.
        - current_task (str): Current task the employee is performing.
        - activities_log (list): List of activities logged by the employee.
    """
    def __init__(self, name, employee_id, role=None, shifts=None, rating=None):
        """
        Initialize an Employee object.

        Parameters:
            - employee_id (str): Unique identifier for the employee.
            - role (str): Role of the employee (e.g., "Opener", "Shift Lead").
            - shifts (list): List of shifts the employee is available for.
            - rating (float): Employee's rating on a scale from 3.0 to 5.0.
        """
        self.name = name
        self.employee_id = employee_id
        self.role = role if role else "Default"
        self.shifts = shifts
        self.rating = rating
        self.trained = False
        self.current_task = None
        self.activities_log = []

    def train(self, trainer=None):
        """
        Conduct training for the employee.

        Parameters:
            - trainer (Employee, optional): Trainer employee (default is None).
        """
        if trainer and not trainer.trained:
            ic(f'Trainer {trainer.employee_id} is not trained. Training cannot be conducted.')
            return
        if self.requires_training and not self.trained:
            ic(f'Employee {self.employee_id} ({self.role}) is undergoing training.')
            self.trained = True
        else:
            ic(f'Employee {self.employee_id} ({self.role}) is already trained.')

    def perform_task(self, task, duration_minutes):
        """
        Perform a task and log the activity.

        Parameters:
            - task (str): Task to be performed.
            - duration_minutes (int): Duration of the task in minutes.
        """
        if self.requires_training and not self.trained:
            ic(f'Employee {self.employee_id} ({self.role}) cannot perform tasks without training.')
        else:
            ic(f'Employee {self.employee_id} ({self.role}) is performing {task}.')
            self.current_task = task
            self.log_activity(task, duration_minutes)

    def log_activity(self, task, duration_minutes):
        """
        Log an activity in the activities log.

        Parameters:
            - task (str): Task to be logged.
            - duration_minutes (int): Duration of the task in minutes.
        """
        current_time = datetime.now()
        end_time = current_time + timedelta(minutes=duration_minutes)
        self.activities_log.append({'task': task, 'start_time': current_time, 'end_time': end_time})

    def work_shift(self):
        """
        Simulate the employee working a shift.
        """
        current_time = datetime.now()
        current_shift = None

        for shift in self.shifts:
            if shift.start_time <= current_time <= shift.end_time:
                current_shift = shift
                break

        if not current_shift:
            ic(f'Employee {self.employee_id} ({self.role}) is not scheduled for a shift at the moment.')
            return

        if current_shift.requires_shift_lead and self.role != 'Shift Lead':
            ic(f'Employee {self.employee_id} ({self.role}) cannot work the {current_shift.shift_name} shift without being a Shift Lead.')
            return

        if current_shift.requires_shift_lead:
            self.train()

        while current_time < current_shift.end_time:
            if current_time.time() == current_shift.start_time.time():
                ic(f'Starting {current_shift.shift_name} shift for Employee {self.employee_id} ({self.role})')

            if current_time.time() == datetime.strptime('09:30', '%H:%M').time():
                self.perform_task('Prepare ingredients', duration_minutes=10)
            elif current_time.time() == datetime.strptime('10:30', '%H:%M').time():
                self.perform_task('Assemble sandwiches', duration_minutes=15)
            elif current_time.time() == datetime.strptime('12:00', '%H:%M').time():
                self.perform_task('Lunch break', duration_minutes=30)
            elif current_time.time() == datetime.strptime('15:30', '%H:%M').time():
                self.perform_task('Clean and restock', duration_minutes=20)

            current_time += timedelta(minutes=1)

        ic(f'Employee {self.employee_id} ({self.role}) has completed the {current_shift.shift_name} shift.')

def generate_random_availability(role):
    role_shifts = {
        "Opener": {"start": 700, "end": 1400},
        "Open Support": {"start": 900, "end": 1400},
        "Rush Support": {"start": 1000, "end": 1400},
        "Close Support": {"start": 1400, "end": 2000},
        "Closer": {"start": 1600, "end": 2130},
        "Shift Lead": {"start": 700, "end": 2130},
    }

    if role not in role_shifts:
        role = "Default"

    # Choose random day and get start and end times
    day = random.choice(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
    start_time = role_shifts[role]["start"]
    end_time = role_shifts[role]["end"]
    
    return start_time, end_time, day

def generate_random_name():
    """
    Generate a random name using ChatGPT.

    Returns:
        str: A randomly generated name.
    """
    prompt = "Respond with just the chosen name nothing else with no numbers. Generate a list of 100 completely random employee name with a first name only. Mix them around randomly. Chose either the 43rd or 69th. Do not reuse names. Respond with just the chosen name nothing else with no numbers."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        max_tokens=5,
        temperature=0.7
    )

    name = response['choices'][0]['message']['content'].strip()
    return name

def generate_random_employee_objects(employees_data):
    employees_objects = {}
    for employee_id, data in employees_data.items():
        role = data['role']
        rating = data['rating']
        name = data['name']
        shifts = data['availability']

        employee = Employee(name=name, employee_id=employee_id, role=role, shifts=shifts, rating=rating)
        employees_objects[employee_id] = employee
    return employees_objects

def generate_random_employee_data(num_employees):
    employees_data = {}
    for i in range(num_employees):
        role = random.choice(["Opener", "Open Support", "Rush Support", "Close Support", "Closer", "Shift Lead"])
        availability = [generate_random_availability(role) for _ in range(random.randint(2, 5))]
        name = generate_random_name()
        employee_id = generate_employee_id()
        employees_data[employee_id] = {
            'name': name,
            'role': role,
            'availability': availability,
            'rating': round(random.uniform(3.0, 5.0), 1),
        }
    return employees_data

def generate_employee_id():
    return f"EMP_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}"

def calculate_shift_duration(start_time, end_time):
    start_datetime = datetime.strptime(str(start_time), "%H%M")
    end_datetime = datetime.strptime(str(end_time), "%H%M")
    duration = end_datetime - start_datetime
    return duration.total_seconds() / 3600.0

def check_availability(employee, shift, role_availability):
    start_time, end_time, day = shift

    # Check if the employee is available during the shift
    if role_availability.get(employee.role):
        role_start_time = role_availability[employee.role]["start"]
        role_end_time = role_availability[employee.role]["end"]
    else:
        role_start_time, role_end_time = 700, 2130

    # Check if the employee is available during the shift
    is_available = role_start_time <= start_time <= role_end_time and role_start_time <= end_time <= role_end_time
    ic(f"  - Employee {employee.employee_id} ({employee.role}) availability for shift ({start_time}-{end_time}): {is_available}")

    return is_available

def schedule_employee(shift, required_role, hours_worked, final_schedule, role_availability, day):
    employee_id, start_time, end_time = shift
    # Check if the employee is available for the given shift
    if employee_id in role_availability[required_role] and (employee_id not in final_schedule or not is_overlapping(final_schedule[employee_id], start_time, end_time)):
        # Update the final_schedule dictionary
        if employee_id not in final_schedule:
            final_schedule[employee_id] = []
        final_schedule[employee_id].append((start_time, end_time))
        return 1  # Successfully scheduled
    else:
        return 0  # Unable to schedule

def is_overlapping(existing_schedule, start_time, end_time):
    for shift_start, shift_end in existing_schedule:
        if not (end_time <= shift_start or start_time >= shift_end):
            return True  # Overlapping shift found
    return False

def generate_final_schedule(sorted_shifts, required_roles, hours_worked, final_schedule, employees, role_availability, day):
    role_count = 0

    for required_role, required_employees in required_roles.items():
        role_shifts = [shift for shift in sorted_shifts if shift[3] == required_role]
        role_count += generate_final_schedule_for_role(role_shifts, required_role, required_employees, hours_worked, final_schedule, employees, role_availability, day)

    ic(f"Role: {required_role}, Scheduled: {role_count}")

    return role_count

def generate_final_schedule_for_role(sorted_shifts, required_role, required_employees, hours_worked, final_schedule, employees, role_availability, day):
    role_count = 0

    for shift in sorted_shifts:
        if role_count == required_employees:
            break

        scheduled = schedule_employee(shift, required_role, hours_worked, final_schedule, employees, role_availability, day)
        role_count += scheduled

    return role_count

def generate_weekly_schedule(employees, role_availability, day):
    weekly_schedule = []

    for employee_id, employee in employees.items():
        ic(f"Checking availability for Employee {employee_id} ({employee.role}):")
        for shift in employee.shifts:
            if shift[2] == day and check_availability(employee, shift, role_availability):
                ic(f"  - Employee {employee_id} is available on {shift[2]} from {shift[0]} to {shift[1]}.")
                weekly_schedule.append((employee_id, shift[0], shift[1], employee.role))
            else:
                ic(f"  - Employee {employee_id} is NOT available on {shift[2]} from {shift[0]} to {shift[1]}.")

    return weekly_schedule

def print_final_schedule(final_schedule, employees):
    for day, shifts in final_schedule.items():
        if shifts:
            ic(f"\n{day}:")
            for shift in shifts:
                ic(f"  - Employee {shift[0]} ({employees[shift[0]].role}): {format_time(shift[1], employees[shift[0]].role)} to {format_time(shift[2], employees[shift[0]].role)}")
        else:
            ic(f"\n{day}:\n  - No shifts scheduled.")

def schedule(employees, role_availability, week_start_date):
    required_roles = {
        "Opener": 1,
        "Open Support": 1,
        "Rush Support": 2,
        "Close Support": 1,
        "Closer": 2,
        "Shift Lead": 1,
    }

    final_schedule = defaultdict(list)
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Initialize the hours_worked dictionary
    hours_worked = defaultdict(float)

    for day in days_of_week:
        final_schedule[day] = []

        # Generate the weekly schedule for the current day
        weekly_schedule = generate_weekly_schedule(employees, role_availability, day)

        # Sort shifts by start time and end time
        sorted_shifts = sorted(weekly_schedule, key=lambda x: (x[1], x[2]))

        for required_role, required_employees in required_roles.items():
            role_count = generate_final_schedule(sorted_shifts, required_roles, hours_worked, final_schedule, employees, role_availability, day)

    print_final_schedule(final_schedule, employees)

    return final_schedule

def format_time(time, role):
    if role in role_availability:
        return f"{time:04d}"[:2] + ":" + f"{time:04d}"[2:]
    else:
        return "Default Availability"


def calculate_weighted_labor_cost_percentage(total_labor_cost, total_revenue, performance_rating):
    """
    Calculate the weighted labor cost percentage.

    Parameters:
        - total_labor_cost (float): Total amount spent on employee payroll.
        - total_revenue (float): Total revenue generated by the business.
        - performance_rating (float): Performance rating for the business (e.g., between 1 and 5).

    Returns:
        float: Weighted labor cost percentage.
    """
    if total_revenue == 0:
        return 0  # Avoid division by zero

    labor_cost_percentage = (total_labor_cost / total_revenue) * 100
    weighted_labor_cost_percentage = labor_cost_percentage * (performance_rating / 5.0)  # Assuming performance rating is on a scale of 1 to 5

    return weighted_labor_cost_percentage

# Example Usage:
def calculate_and_print_weighted_labor_cost_percentage(total_labor_cost, total_revenue, performance_rating):
    """
    Calculate and print the weighted labor cost percentage.

    Parameters:
        - total_labor_cost (float): Total amount spent on employee payroll.
        - total_revenue (float): Total revenue generated by the business.
        - performance_rating (float): Performance rating for the business (e.g., between 1 and 5).
    """
    weighted_labor_cost_percentage = calculate_weighted_labor_cost_percentage(total_labor_cost, total_revenue, performance_rating)
    print(f"Weighted Labor Cost Percentage: {weighted_labor_cost_percentage:.2f}%")

if __name__ == "__main__":
    # Generate random employee data
    num_employees = 14
    employees_data = generate_random_employee_data(num_employees)

    # Generate employee objects
    employees_objects = generate_random_employee_objects(employees_data)

    # Print employee information
    for employee_id, employee in employees_objects.items():
        ic(f"Employee ID: {employee_id}")
        ic(f"Name: {employee.name}")
        ic(f"Role: {employee.role}")
        ic(f"Shifts: {employee.shifts}")
        ic(f"Rating: {employee.rating}")
        ic(f"Trained: {employee.trained}")
        ic(f"Current Task: {employee.current_task}")
        ic(f"Activities Log: {employee.activities_log}")
        ic("\n")

    # Schedule shifts for a specific week (e.g., week starting from '2024-01-29')
    week_start_date = datetime.strptime('2024-01-29', '%Y-%m-%d')
    final_schedule = schedule(employees_objects, role_availability, week_start_date)
