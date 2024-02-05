import pygame
from pygame.locals import *
import icecream as ic

pygame.init()

class POS:
    def __init__(self):
        self.active_menu = "Payroll"
        self.selected_item = None
        self.items = {
            '#1': ('BLT', ['Bacon', 'Lettuce', 'Tomato'], 8.99),
            '#2': ('Jersey Shore Favorite', ['Provolone', 'Ham', 'Cappacuolo'], 9.99),
            '#3': ('Ham and Provolone', ['Provolone', 'Ham'], 7.99),
            '#4': ('The Number Four', ['Provolone', 'Prosciuttini', 'Cappacuolo'], 10.99),
            '#5': ('The Super Sub', ['Provolone', 'Ham', 'Prosciuttini', 'Cappacuolo'], 12.99),
            '#6': ('Roast Beef and Provolone', ['Provolone', 'Roast Beef'], 11.99),
            '#7': ('Turkey and Provolone', ['Provolone', 'Turkey'], 9.99),
            '#8': ('Club Sub', ['Provolone', 'Ham', 'Turkey', 'Bacon', 'Mayo'], 13.99),
            '#9': ('Club Supreme', ['Swiss', 'Turkey', 'Roast Beef', 'Bacon', 'Mayo'], 14.99),
            '#10': ('Tuna Fish', ['Tuna'], 8.99),
            '#11': ('Stickball Special', ['Provolone', 'Ham', 'Salami'], 10.99),
            '#12': ('Cancro Special', ['Provolone', 'Roast Beef', 'Pepperoni'], 11.99),
            '#13': ('The Original Italian', ['Provolone', 'Ham', 'Prosciuttini', 'Cappacuolo', 'Salami', 'Pepperoni'], 14.99),
            '#14': ('The Veggie', ['Swiss', 'Provolone', 'Bell Peppers'], 9.99),
            '#16': ('Mikes Chicken Philly', ['Chicken', 'American Cheese', 'Onions', 'Peppers'], 11.99),
            '#17': ('Mikes Famous Philly', ['Steak', 'American Cheese', 'Onions', 'Peppers'], 12.99),
            '#26': ('Bacon Ranch Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Bacon', 'Lettuce', 'Tomato', 'Ranch'], 13.99),
            '#31': ('California Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Lettuce', 'Tomato', 'Mayo'], 12.99),
            '#42': ('Chipotle Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Onions', 'Peppers', 'Chipotle Mayo'], 14.99),
            '#43': ('Chipotle Cheese Steak', ['Steak', 'American Cheese', 'Onions', 'Peppers', 'Chipotle Mayo'], 13.99),
            '#44': ('Buffalo Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Franks Red Hot Sauce', 'Lettuce', 'Tomato', 'Blue Cheese'], 14.99),
            '#55': ('Big Kahuna Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Onions', 'Peppers', 'Mushrooms', 'Jalapenos'], 13.99),
            '#56': ('Big Kahuna Cheese Steak', ['Steak', 'Cheese', 'Onions', 'Peppers', 'Mushrooms', 'Jalapenos'], 12.99),
            '#64': ('Grilled Portabella Mushroom & Swiss', ['Portabella Mushrooms', 'Swiss Cheese', 'Bell Peppers', 'Onions'], 11.99),
            '#65': ('Portabella Chicken Cheese Steak', ['Chicken', 'American Cheese', 'Chicken', 'Portabella Mushrooms', 'Peppers', 'Onions'], 14.99),
            '#66': ('Portabella Cheese Steak', ['Steak', 'American Cheese', 'Steak', 'Portabella Mushrooms', 'Peppers', 'Onions'], 13.99)
        }
        self.sale_items = []

    def update(self):
        # Update logic for POS system
        pass

    def draw(self, screen):
        # Draw elements on the screen for POS system
        screen.fill((255, 255, 255))  # Fill screen with white

        # Draw menu buttons at the top
        font = pygame.font.Font(None, 36)

        # Menu buttons
        menu_buttons = ["Payroll", "Management", "Employee"]

        # Spacing and initial position for menu buttons
        button_spacing = 20
        x_button_position = 10

        for button in menu_buttons:
            button_text = font.render(button, True, (0, 0, 0))
            screen.blit(button_text, (x_button_position, 10))  # Adjust the Y-coordinate as needed
            x_button_position += button_text.get_width() + button_spacing

        # Get screen size
        screen_width, screen_height = screen.get_size()

        # Draw menu items as boxes with item numbers in the middle
        menu_items = [
            '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10',
            '#11', '#12', '#13', '#14', '#16', '#17', '#26', '#31', '#42', '#43',
            '#44', '#55', '#56', '#64', '#65', '#66'
        ]

        # Calculate the maximum width of all boxes
        max_box_width = max([font.render(item, True, (0, 0, 0)).get_width() + 20 for item in menu_items])

        # Calculate the starting X position to center the boxes
        x_position = (screen_width - max_box_width * len(menu_items) - 20 * (len(menu_items) - 1)) // 2

        # Calculate the Y position to center the boxes vertically
        y_position = (screen_height - font.get_height()) // 2 + 50  # Add 50 for spacing from the top

        item_rects = {}

        for item in menu_items:
            text = font.render(item, True, (0, 0, 0))

            # Create a box around the text
            item_rect = pygame.Rect(x_position, y_position, max_box_width, text.get_height() + 20)
            pygame.draw.rect(screen, (0, 0, 0), item_rect, 2)

            # Update item_rects dictionary
            item_rects[item] = item_rect

            # Calculate position to center the text in the box
            text_x = x_position + (max_box_width - text.get_width()) / 2
            text_y = y_position + (text.get_height() + 20 - text.get_height()) / 2

            screen.blit(text, (text_x, text_y))  # Adjust the Y-coordinate as needed
            x_position += max_box_width + 20  # Add 20 for spacing between boxes

        # Draw sale section on the right
        self.draw_sale_section(screen, font)

        # Draw other POS elements
        if self.active_menu == "Payroll":
            self.draw_payroll(screen)
        elif self.active_menu == "Management":
            self.draw_management(screen)
        elif self.active_menu == "Employee":
            self.draw_employee(screen)

        return item_rects  # Return the item_rects dictionary

    def draw_sale_section(self, screen, font):
        # Draw the sale section on the right
        sale_section_width = screen.get_width() // 4
        sale_section_height = screen.get_height()
        sale_section_x = 3 * screen.get_width() // 4
        sale_section_y = 0

        # Use a variable to control transparency level
        void_transparency = 0.75
        void_color = (255, 0, 0, int(void_transparency * 255))

        pygame.draw.rect(screen, (200, 200, 200), (sale_section_x, sale_section_y, sale_section_width, sale_section_height))

        sale_font = pygame.font.Font(None, 28)
        sale_text_margin = 10  # Adjust this value to set the margin from the bottom
        button_height = 30
        button_margin = 10

        # Initialize sale_text_y before the if condition
        sale_text_y = 0  

        if self.selected_item is not None:
            selected_name, selected_ingredients, selected_price = self.items.get(self.selected_item, ("", [], 0.0))

            pygame.draw.rect(screen, (0, 0, 0), (sale_section_x + 10, sale_text_y, sale_section_width - 20, 30), 2)

            selected_name_text = font.render(selected_name, True, (0, 0, 0))
            screen.blit(selected_name_text, (sale_section_x + 20, sale_text_y + 5))

            sale_text_y += 40

            for ingredient in selected_ingredients:
                ingredient_text = sale_font.render(ingredient, True, (0, 0, 0))
                screen.blit(ingredient_text, (sale_section_x + 20, sale_text_y))
                sale_text_y += ingredient_text.get_height() + 5

            pygame.draw.line(screen, (0, 0, 0), (sale_section_x + 10, sale_text_y), (sale_section_x + sale_section_width - 10, sale_text_y), 2)

            total_price_text = sale_font.render(f"Total: ${selected_price:.2f}", True, (0, 0, 0))
            screen.blit(total_price_text, (sale_section_x + 20, sale_text_y + 10))

            # Draw tax (assuming 8% tax rate)
            tax = selected_price * 0.08
            tax_text = sale_font.render(f"Tax (8%): ${tax:.2f}", True, (0, 0, 0))
            screen.blit(tax_text, (sale_section_x + 20, sale_text_y + 40))

            # Draw total amount
            total_amount = selected_price + tax
            total_amount_text = sale_font.render(f"Total Amount: ${total_amount:.2f}", True, (0, 0, 0))
            screen.blit(total_amount_text, (sale_section_x + 20, sale_text_y + 70))

        # Calculate sale_text_y dynamically based on the screen height, leaving space for the new buttons
        sale_text_y = screen.get_height() - button_height - button_margin - sale_text_margin - 200

        # Draw Pay button
        pay_button_rect = pygame.Rect(sale_section_x + 10, sale_text_y + 10, (sale_section_width - 30) // 3, button_height)
        pygame.draw.rect(screen, (0, 255, 0), pay_button_rect, 0)
        pay_button_text = font.render("Pay", True, (0, 0, 0))
        screen.blit(pay_button_text, (pay_button_rect.x + 10, sale_text_y + 15))

        # Draw Void button
        void_button_rect = pygame.Rect(pay_button_rect.x + pay_button_rect.width + 5, sale_text_y + 10, (sale_section_width - 30) // 3, button_height)
        
        # Check if the mouse is not over the button before changing color
        if not void_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, void_color, void_button_rect)

        void_button_text = font.render("Void", True, (0, 0, 0))
        screen.blit(void_button_text, (void_button_rect.x + 10, sale_text_y + 15))

        # Draw Discount button
        discount_button_rect = pygame.Rect(void_button_rect.x + void_button_rect.width + 5, sale_text_y + 10, (sale_section_width - 30) // 3, button_height)
        pygame.draw.rect(screen, (0, 0, 255), discount_button_rect, 0)
        discount_button_text = font.render("Discount", True, (0, 0, 0))
        screen.blit(discount_button_text, (discount_button_rect.x + 10, sale_text_y + 15))

        return {
            "pay_button": pay_button_rect,
            "void_button": void_button_rect,
            "discount_button": discount_button_rect
        }

    def draw_payroll(self, screen):
        # Draw elements specific to Payroll menu
        pass

    def draw_management(self, screen):
        # Draw elements specific to Management menu
        pass

    def draw_employee(self, screen):
        # Draw elements specific to Employee menu
        pass

if __name__ == "__main__":
    pos = POS()

    # Set up Pygame screen in fullscreen mode
    screen = pygame.display.set_mode((0, 0), FULLSCREEN)
    pygame.display.set_caption("Pygame POS System")

    clock = pygame.time.Clock()
    item_rects = {}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button clicked
                # Check if the mouse click is inside any of the item boxes
                for item_number, item_rect in item_rects.items():
                    if item_rect.collidepoint(event.pos):
                        pos.selected_item = item_number
                        pos.sale_items.append(pos.selected_item)
                        print(f"Selected item: {pos.selected_item}")

        item_rects = pos.draw(screen)  # Update item_rects inside the while loop

        pos.update()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
