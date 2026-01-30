# Create a combat function that takes the player's current health and the amount of damage received, and returns the player's new health. Health can't be less than 0.

def combat(health, damage):
    current_health = health - damage
    if current_health <= 0:
        return False
    else:
        return current_health