"""
Order Processor

This script defines an OrderProcessor class for handling customer orders and simulating order processing for various purchase channels.

Usage:
    - Create an instance of OrderProcessor with the current time and a menu.
    - Use the handle_customer_order method to simulate processing a customer order.

"""

import random
from datetime import datetime, timedelta

class OrderProcessor:
    """
    OrderProcessor class for handling customer orders and simulating order processing.

    Attributes:
        - current_time (datetime): Current time used for order processing simulation.
        - menu (dict): Menu containing available items and their details.
    """
    def __init__(self, current_time, menu):
        """
        Initialize an OrderProcessor object.

        Parameters:
            - current_time (datetime): Current time for order processing simulation.
            - menu (dict): Menu containing available items and their details.
        """
        self.current_time = current_time
        self.menu = menu

    def handle_customer_order(self, customer):
        """
        Simulate handling a customer order.

        Parameters:
            - customer (dict): Customer information, including name.

        This method simulates the processing of a customer order, considering various purchase channels.
        """
        rush_chance = self.calculate_rush_chance(customer)
        if random.random() < rush_chance:
            self.current_time += timedelta(minutes=random.randint(10, 30))

        purchase_channel = random.choice(['in-store', 'online', 'doordash', 'ubereats', 'catering', 'curbside'])
        customer['purchase_channel'] = purchase_channel

        efficiency = 1.0
        simultaneous_orders_mapping = {0.4: 1, 0.6: 2, 0.8: 3, 0.9: 3, 1: 5}
        num_simultaneous_orders = simultaneous_orders_mapping.get(efficiency, 1)

        for _ in range(num_simultaneous_orders):
            temp_order_info = None
            if purchase_channel in ['in-store', 'online']:
                order_number = self.generate_order_number()
                order_id = f'{order_number}-{customer["name"].replace(" ", "_")}'
                temp_order_info, processing_time = self.take_order(customer, purchase_channel, order_id)
                self.simulate_chip_purchase(customer)
            elif purchase_channel in ['doordash', 'ubereats']:
                order_number = self.generate_order_number()
                order_id = f'{order_number}-{customer["name"].replace(" ", "_")}'
                temp_order_info, processing_time = self.process_delivery_order(customer, purchase_channel, order_id)
            elif purchase_channel == 'catering':
                order_number = self.generate_order_number()
                order_id = f'{order_number}-{customer["name"].replace(" ", "_")}'
                temp_order_info, processing_time = self.process_catering_order(customer, order_id)
            elif purchase_channel == 'curbside':
                order_number = self.generate_order_number()
                order_id = f'{order_number}-{customer["name"].replace(" ", "_")}'
                temp_order_info, processing_time = self.process_curbside_order(customer, order_id)

            if purchase_channel == 'in-store':
                dine_in_processing_time = self.calculate_dine_in_processing_time(customer)
                self.current_time += timedelta(minutes=dine_in_processing_time)

            self.current_time += timedelta(minutes=processing_time)
            self.process_temp_order(temp_order_info)

    def take_order(self, customer, order_type, order_id):
        """
        Simulate taking an order.

        Parameters:
            - customer (dict): Customer information.
            - order_type (str): Type of order (e.g., 'in-store', 'online').
            - order_id (str): Unique identifier for the order.

        Returns:
            tuple: Tuple containing order information and processing time.
        """
        order_name = customer['name']
        pickup_time = None
        phone_number = None

        if order_type in ['online', 'catering', 'future', 'curbside']:
            pickup_time = self.generate_pickup_time()

            if order_type != 'doordash' and order_type != 'ubereats':
                phone_number = self.generate_phone_number()



        order_details = self.generate_order_details()

        base_processing_time = 5
        variation = random.randint(-2, 2)
        processing_time = max(5, base_processing_time + variation)

        order_info = {
            'order_type': order_type,
            'order_id': order_id,
            'order_name': order_name,
            'pickup_time': pickup_time,
            'phone_number': phone_number,
            'order': order_details
        }

        return order_info, processing_time

    def generate_pickup_time(self, base_time=None, min_offset=10, max_offset=60):
        """
        Generate a random pickup time for an order.

        Parameters:
            - base_time (time, optional): Base time for generating pickup time (default is None).
            - min_offset (int): Minimum offset in minutes for pickup time (default is 10).
            - max_offset (int): Maximum offset in minutes for pickup time (default is 60).

        Returns:
            str: Formatted pickup time in HH:MM.
        """
        if base_time is None:
            base_time = self.current_time.time()

        pickup_time = datetime.combine(datetime.today(), base_time) + timedelta(minutes=random.randint(min_offset, max_offset))
        return pickup_time.time().strftime('%H:%M')

    def generate_phone_number(self):
        """
        Generate a random phone number.

        Returns:
            str: Randomly generated phone number.
        """
        area_code = random.randint(1000, 9999)
        prefix = random.randint(1000, 9999)
        line_number = random.randint(1000, 9999)

        return f'{area_code}-{prefix}-{line_number}'

    def generate_order_details(self, num_items=3):
        """
        Generate random order details.

        Parameters:
            - num_items (int): Number of items in the order (default is 3).

        Returns:
            dict: Dictionary containing randomly generated order details.
        """
        available_items = list(self.menu.keys())

        order_details = {}
        for i in range(1, num_items + 1):
            item_key = f'item{i}'
            if available_items:
                selected_item = random.choice(available_items)
                order_details[item_key] = selected_item
                available_items.remove(selected_item)
            else:
                order_details[item_key] = f'CustomItem{i}'

        return order_details

    def process_delivery_order(self, customer, delivery_service, order_id):
        """
        Simulate processing a delivery order.

        Parameters:
            - customer (dict): Customer information.
            - delivery_service (str): Delivery service (e.g., 'doordash', 'ubereats').
            - order_id (str): Unique identifier for the order.

        Returns:
            tuple: Tuple containing order information and processing time.
        """
        estimated_delivery_time = random.randint(15, 45)
        processing_time = random.randint(5, 15)
        order_info = {
            'order_type': delivery_service,
            'order_id': order_id,
            'order_name': f'{customer["name"]}',
            'estimated_delivery_time': estimated_delivery_time,
        }
        return order_info, processing_time

    def process_catering_order(self, customer, order_id):
        """
        Simulate processing a catering order.

        Parameters:
            - customer (dict): Customer information.
            - order_id (str): Unique identifier for the order.

        Returns:
            tuple: Tuple containing order information and processing time.
        """
        processing_time = random.randint(20, 60)
        order_info = {
            'order_type': 'catering',
            'order_id': order_id,
            'order_name': f'{customer["name"]}',
            'pickup_time': self.generate_pickup_time(),
            'phone_number': self.generate_phone_number(),
            'order': self.generate_order_details()
        }
        return order_info, processing_time

    def process_curbside_order(self, customer, order_id):
        """
        Simulate processing a curbside order.

        Parameters:
            - customer (dict): Customer information.
            - order_id (str): Unique identifier for the order.

        Returns:
            tuple: Tuple containing order information and processing time.
        """
        processing_time = random.randint(10, 30)
        order_info = {
            'order_type': 'curbside',
            'order_id': order_id,
            'order_name': f'{customer["name"]}',
            'pickup_time': self.generate_pickup_time(),
            'phone_number': self.generate_phone_number(),
            'order': self.generate_order_details()
        }
        return order_info, processing_time

    def calculate_rush_chance(self, customer):
        """
        Calculate the rush chance for a customer order.

        Parameters:
            - customer (dict): Customer information.

        Returns:
            float: Randomly generated rush chance.
        """
        # Placeholder 
        return random.uniform(0.2, 0.8)

    def simulate_chip_purchase(self, customer):
        """
        Simulate a chip purchase for a customer.

        Parameters:
            - customer (dict): Customer information.
        """
        # Placeholder 
        print(f'Simulating chip purchase for customer {customer["name"]}')

    def calculate_dine_in_processing_time(self, customer):
        """
        Calculate the dine-in processing time for a customer.

        Parameters:
            - customer (dict): Customer information.

        Returns:
            int: Randomly generated dine-in processing time in minutes.
        """
        # Placeholder 
        return random.randint(15, 45)

    def generate_order_number(self):
        """
        Generate a random order number.

        Returns:
            int: Randomly generated order number.
        """
        # Placeholder 
        return random.randint(1000, 9999)

    def process_temp_order(self, temp_order_info):
        """
        Simulate processing a temporary order.

        Parameters:
            - temp_order_info (dict): Temporary order information.
        """
        # Placeholder 
        print(f'Processing order: {temp_order_info}')