import random
from datetime import datetime, timedelta
from simulator.inventory import inventory
from simulator.management import EmployeeManagement
from simulator.orders import OrderProcessor
from simulator.employee import Employee
#from simulator.shop import Shop
#from simulator.truck import Truck

class GameState:
    def __init__(self):
        self.state = 'start'

    def set_state(self, state):
        self.state = state

class FranchiseSimulator:
    def __init__(self):
        self.game_state = GameState()
        self.menu = {
            '#1': ('BLT', ['Bacon', 'Lettuce', 'Tomato']),
            '#2': ('Jersey Shore Favorite', ['Provolone', 'Ham', 'Cappacuolo']),
            '#3': ('Ham and Provolone', ['Provolone', 'Ham']),
            '#4': ('The Number Four', ['Provolone', 'Prosciuttini', 'Cappacuolo']),
            '#5': ('The Super Sub', ['Provolone', 'Ham', 'Prosciuttini', 'Cappacuolo']),
            '#6': ('Roast Beef and Provolone', ['Provolone, Roast Beef']),
            '#7': ('Turkey and Provolone', ['Provolone', 'Turkey']),
            '#8': ('Club Sub', ['Provolone', 'Ham', 'Turkey', 'Bacon', 'Mayo']),
            '#9': ('Club Supreme', [ 'Swiss', 'Turkey', 'Roast Beef', 'Bacon', 'Mayo']),
            '#10': ('Tuna Fish', ['Tuna']),
            '#11': ('Stickball Special', ['Provolone', 'Ham', 'Salami']),
            '#12': ('Cancro Special', ['Provolone', 'Roast Beef', 'Pepperoni']),
            '#13': ('The Original Italian', ['Provolone', 'Ham', 'Prosciuttini', 'Cappacuolo', 'Salami', 'Pepperoni']),
            '#14': ('The Veggie', ['Swiss', 'Provolone', 'Bell Peppers']),
            '#16': ('Mikes Chicken Philly', ['Chicken', 'American Cheese', 'Onions', 'Peppers']),
            '#17': ('Mikes Famous Philly', ['Steak', 'American Cheese', 'Onions', 'Peppers']),
            '#26': ('Bacon Ranch Chicken Cheese Steak', ['Chicken', 'American Cheese','Bacon', 'Lettuce', 'Tomato', 'Ranch']),
            '#31': ('California Chicken Cheese Steak', ['Chicken', 'American Cheese','Lettuce', 'Tomato', 'Mayo']),
            '#42': ('Chipotle Chicken Cheese Steak', ['Chicken', 'American Cheese','Onions', 'Peppers','Chipotle Mayo']),
            '#43': ('Chipotle Cheese Steak', ['Steak', 'American Cheese','Onions', 'Peppers', 'Chipotle Mayo']),
            '#44': ('Buffalo Chicken Cheese Steak', ['Chicken', 'American Cheese','Franks Red Hot Sauce', 'Lettuce', 'Tomato', 'Blue Cheese']),
            '#55': ('Big Kahuna Chicken Cheese Steak', ['Chicken', 'American Cheese','Onions', 'Peppers', 'Mushrooms', 'Jalapenos']),
            '#56': ('Big Kahuna Cheese Steak', ['Steak', 'Cheese','Onions', 'Peppers', 'Mushrooms', 'Jalapenos']),
            '#64': ('Grilled Portabella Mushroom & Swiss', ['Portabella Mushrooms', 'Swiss Cheese' 'Bell Peppers', 'Onions']),
            '#65': ('Portabella Chicken Cheese Steak', ['Chicken', 'American Cheese','Chicken', 'Portabella Mushrooms', 'Peppers', 'Onions']),
            '#66': ('Portabella Cheese Steak', ['Steak', 'American Cheese','Steak', 'Portabella Mushrooms', 'Peppers', 'Onions'])
        }
        self.inventory = inventory
        self.employees = []
        self.customers = []
    

    def initialize_game(self):
        print('Experience Levels: (1) Less than 1 year (2) 2-5 years (3) 5+ years')
        experience = int(input('Choose franchisee experience level: '))
        print('Location Sizes: (1) Suburb Franchise  (2) Interstate Franchise')
        location = int(input('Choose franchise location size: '))

        standard_inventory = {}

        # SCALE INVENTORY, EMPLOYEE, CUSTOMER FROM EXPERIENCE / LOCATION
        inventory_scale = {
            1: 0.5,  
            2: 1.0,  
            3: 1.5   
        }

        employee_scale = {
            1: {1: 5, 2: 10},  
            2: {1: 8, 2: 15}, 
            3: {1: 12, 2: 20}  
        }

        customer_scale = {
            1: {1: 20, 2: 50},  
            2: {1: 40, 2: 100},  
            3: {1: 60, 2: 150}  
        }

        scaled_inventory = {}
        for category, items in standard_inventory.items():
            scaled_items = {item: int(amount * inventory_scale[experience]) for item, amount in items.items()}
            scaled_inventory[category] = scaled_items

        # Generating scaled counts for employees and initial customers based on location and experience
        employee_count = employee_scale[experience][location]
        customer_count = customer_scale[experience][location]

        print('Game initialized!')
        print('Scaled Inventory:', scaled_inventory)
        print('Employee count:', employee_count)
        print('Initial customer count:', customer_count)

        # Return or store the scaled_inventory, employee_count, and customer_count for further use in the game
        return scaled_inventory, employee_count, customer_count

#    start_menu()

    def read_names(self, filename):
        with open(filename, 'r') as file:
            names = file.readlines()
        return [name.strip() for name in names]


    def start_menu(self):
        print('Welcome to Jersey Mikes Franchise Simulator!')
        print('1. Start New Game')
        print('2. Load Existing Game')
        print('3. Exit')
        choice = input('Enter your choice: ')

        if choice == '1':
            self.game_state.set_state('playing')
            self.initialize_game()
        elif choice == '2':
            print('Loading existing game...')
            # Implement loading existing game logic
        elif choice == '3':
            print('Exiting the game...')
            exit()
        else:
            print('Invalid choice. Please enter a valid option.')
            self.start_menu()
    
    def hire_employees(self, num_employees):
        for _ in range(num_employees):
            employee = Employee(len(self.employees) + 1)
            self.employees.append(employee)
            print(f'Hired Employee {employee.employee_id}.')

    def simulate_shop_operations(self, num_orders):
        for _ in range(num_orders):
            customer = {'name': f'Customer{_}'}
            self.shop.order_processor.handle_customer_order(customer)

    def run_simulation(self, num_employees, num_potential_hires, num_employees_to_train, num_orders):
        scaled_inventory, employee_count, customer_count = self.initialize_game()
        self.hire_employees(num_employees)
        self.shop.employee_management.train_employees(num_employees_to_train)
        self.simulate_shop_operations(num_orders)
            
    chip_racks = {
        'rack1': {'RedDoritos': (24, 24), 'BlueDoritos': (24, 24), 'Cheetos': (30, 30)},
        'rack2': {'GardenSalsa': (30, 30), 'ClassicLays': (30, 30), 'BakedLays': (30, 30)},
        'shelf1': {'MVJalapeno': (30, 30)},
        'shelf2': {'MVBBQ': (15, 15), 'MVMVSeaSalt': (15, 15)},
        'shelf3': {'MVSeaSalt&Vinegar': (15, 15), 'MVDillPickle': (15, 15)},
    }

    # Function to simulate a customer purchasing chips from a rack
    def purchase_from_rack(rack):
        rack_copy = rack.copy()

        chips_to_buy = {}
        for chip, (max_quantity, current_quantity) in rack_copy.items():
            if current_quantity > 0:
                purchase_quantity = random.randint(0, current_quantity)  # Simulate a random purchase quantity
                chips_to_buy[chip] = purchase_quantity
                rack_copy[chip] = (max_quantity, max(0, current_quantity - purchase_quantity))

        return rack_copy, chips_to_buy