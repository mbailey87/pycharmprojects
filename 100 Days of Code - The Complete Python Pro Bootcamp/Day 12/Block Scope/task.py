#there is no block scope in python

game_level = 3
enemies = ['skel', 'zom', 'bat']

# if game_level < 5:
#     new_enemy = enemies[0]
#
# print(new_enemy) #unlike other languages this has access to whats in that if statement even though this print funtion isnt in the block of the if statement

# def create_enemy():
#     new_enemy = '' #declaring outside of the block will help prevent issues for if the if statement isnt true
#     if game_level < 5:
#         new_enemy = enemies[0]
#     print(new_enemy)

# print(new_enemy) #cant access because new enemy is part of a local scope


def is_prime(num):
    prime = True
    num_count = 0
    for i in range(2, num):
        if num % i == 0:
            num_count += 1
    if num_count > 0:
        prime = False
    print(prime)
    return prime
is_prime(11)
is_prime(4)
is_prime(17)
is_prime(85)
is_prime(73)