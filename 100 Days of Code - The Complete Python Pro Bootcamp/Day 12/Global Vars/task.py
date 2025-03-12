# Modifying Global Scope

enemies = 1


# def increase_enemies(): this is bad because you dont want to change things in the global scope
#     global enemies
#     enemies += 1
#     print(f"enemies inside function: {enemies}")
#
#
# increase_enemies()
# print(f"enemies outside function: {enemies}")

def increase_enemies(enemy):
    enemy += 1
    print(enemy)
    return enemy

increase_enemies(enemies)


