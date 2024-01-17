import random
from datetime import datetime, timedelta

class Employee:
    def __init__(self, employee_id, role, shifts, rating):
        self.employee_id = employee_id
        self.role = role
        self.shifts = shifts
        self.rating = rating
        self.trained = False
        self.current_task = None
        self.activities_log = []

    def train(self, trainer=None):
        if trainer and not trainer.trained:
            print(f'Trainer {trainer.employee_id} is not trained. Training cannot be conducted.')
            return

        if self.requires_training and not self.trained:
            print(f'Employee {self.employee_id} ({self.role}) is undergoing training.')
            self.trained = True
        else:
            print(f'Employee {self.employee_id} ({self.role}) is already trained.')

    def perform_task(self, task, duration_minutes):
        if self.requires_training and not self.trained:
            print(f'Employee {self.employee_id} ({self.role}) cannot perform tasks without training.')
        else:
            print(f'Employee {self.employee_id} ({self.role}) is performing {task}.')
            self.current_task = task
            self.log_activity(task, duration_minutes)

    def log_activity(self, task, duration_minutes):
        current_time = datetime.now()
        end_time = current_time + timedelta(minutes=duration_minutes)
        self.activities_log.append({'task': task, 'start_time': current_time, 'end_time': end_time})

    def work_shift(self):
        current_time = datetime.now()
        current_shift = None

        for shift in self.shifts:
            if shift.start_time <= current_time <= shift.end_time:
                current_shift = shift
                break

        if not current_shift:
            print(f'Employee {self.employee_id} ({self.role}) is not scheduled for a shift at the moment.')
            return

        if current_shift.requires_shift_lead and self.role != 'Shift Lead':
            print(f'Employee {self.employee_id} ({self.role}) cannot work the {current_shift.shift_name} shift without being a Shift Lead.')
            return

        if current_shift.requires_shift_lead:
            self.train()

        # PUT DUTIES HERE
        while current_time < current_shift.end_time:
            if current_time.time() == current_shift.start_time.time():
                print(f'Starting {current_shift.shift_name} shift for Employee {self.employee_id} ({self.role})')

            if current_time.time() == datetime.strptime('09:30', '%H:%M').time():
                self.perform_task('Prepare ingredients', duration_minutes=10)
            elif current_time.time() == datetime.strptime('10:30', '%H:%M').time():
                self.perform_task('Assemble sandwiches', duration_minutes=15)
            elif current_time.time() == datetime.strptime('12:00', '%H:%M').time():
                self.perform_task('Lunch break', duration_minutes=30)
            elif current_time.time() == datetime.strptime('15:30', '%H:%M').time():
                self.perform_task('Clean and restock', duration_minutes=20)

            current_time += timedelta(minutes=1)

        print(f'Employee {self.employee_id} ({self.role}) has completed the {current_shift.shift_name} shift.')
