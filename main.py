import pygame
import pickle
from pygame.locals import QUIT, MOUSEBUTTONDOWN

from simulator.simulator import FranchiseSimulator

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Franchise Simulator")

game = None  # Initialize game as None initially

# Define states for better management
MENU_STATE = 'menu'
PLAYING_STATE = 'playing'
current_state = MENU_STATE  # Set the initial state to the menu

def main():
    clock = pygame.time.Clock()
    global game, current_state  # Declare global game and current_state variables

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return
            elif event.type == MOUSEBUTTONDOWN:
                handle_mouse_click()

        if current_state == MENU_STATE:
            draw_menu()
        elif current_state == PLAYING_STATE:
            draw_game_state()

        pygame.display.flip()

        clock.tick(30)

def draw_menu():
    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)

    # Draw New Game button
    pygame.draw.rect(screen, (0, 255, 0), (300, 200, 200, 50))
    new_game_text = font.render("New Game", True, (0, 0, 0))
    screen.blit(new_game_text, (350, 210))

    # Draw Load Game button
    pygame.draw.rect(screen, (0, 0, 255), (300, 300, 200, 50))
    load_game_text = font.render("Load Game", True, (0, 0, 0))
    screen.blit(load_game_text, (350, 310))

def draw_game_state():
    screen.fill((255, 255, 255))

    font = pygame.font.Font(None, 36)

    # Draw game state (numbers from FranchiseSimulator)
    customers_text = font.render(f"Customers: {len(game.customers)}", True, (0, 0, 0))
    screen.blit(customers_text, (50, 50))

    inventory_text = font.render(f"Inventory: {game.inventory}", True, (0, 0, 0))
    screen.blit(inventory_text, (50, 100))

    employees_text = font.render(f"Employees: {len(game.employees)}", True, (0, 0, 0))
    screen.blit(employees_text, (50, 150))


def handle_mouse_click():
    global game, current_state  # Reference the global game and current_state variables

    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Check if New Game button is clicked
    if current_state == MENU_STATE and 300 <= mouse_x <= 500 and 200 <= mouse_y <= 250:
        print("New Game clicked")
        screen.fill((255, 255, 255))  # Clear the screen
        game = FranchiseSimulator()  # Start a new game
        current_state = PLAYING_STATE  # Change the state to playing

    # Check if Load Game button is clicked
    elif current_state == MENU_STATE and 300 <= mouse_x <= 500 and 300 <= mouse_y <= 350:
        print("Load Game clicked")
        game = load_game_from_saves()

def load_game_from_saves():
    try:
        with open('save_game.pkl', 'rb') as file:
            saved_data = pickle.load(file)
        return saved_data
    except FileNotFoundError:
        print("No saved game found.")
        return None

if __name__ == '__main__':
    main()
