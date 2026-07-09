# Modifying Global Scope

enemies = "saurabh"


def increase_enemies():
    global enemies
    enemies = "kumar"
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


