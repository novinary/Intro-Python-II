import re
from room import Room
from player import Player

# Declare all the room
room = {
    'lumbridge': Room("Lumbridge", """Welcome to Lumbridge!"""),
    'entrance': Room("Entrance", """Please come in!"""),
    'weaponstore': Room("Weapon Store", """Variety of weapons to choose from."""),
    'bank': Room("Bank", """Access your personal bank here"""),
    'library': Room("Library", """All information about Lumbridge is available here. From our people to weapons."""),
    'dine': Room("Dining Hall", """Incredible feast are freshly prepared everyday""")
}

# # Link rooms together
room['lumbridge'].n_to = room['entrance']
room['entrance'].s_to = room['lumbridge']
room['entrance'].n_to = room['weaponstore']
room['entrance'].w_to = room['bank']
room['entrance'].e_to = room['library']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Bob", room['lumbridge'])

print("\n")
print(" ──────▄▀▀▀▀▀▀▀▄─────── ")
print(" ─────▐─▄█▀▀▀█▄─▌────── ")
print(" ─────▐─▀█▄▄▄█▀─▌────── ")
print(" ──────▀▄▄▄▄▄▄▄▀─────── ")
print(" ─────▐▀▄▄▐█▌▄▄▀▌────── ")
print(" ──────▀▄▄███▄▄▀─────── ")
print(" █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ ")
print(" █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█ ")
print(" █░░║║║╠─║─║─║║║║║╠─░░█ ")
print(" █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█ ")
print(" █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ ")
print("\n")

# Write a loop that:
#
# * Prints the current room name/description
print("\nWelcome " + player.name + "! \nWe are very excited for you to begin your quest. \n")

print("You are currently in the world: " + player.current_room.name + ".")
print(player.current_room.description + "\n")

selection = input("Where would you like to head today, N-North, S-South, E-East, or W-West \n or Q-Quit: ")
selection = selection.upper()

# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
if len(re.findall("[NSEWRQ]", selection)) == 1:
    while selection != 'Q':
        if selection == 'N':
            if hasattr(player.current_room, 'n_to'):
                player.current_room = player.current_room.n_to
                print('Welcome to  the ' + str(player.current_room.name))
                break
            else:
                print("Apologies but there is nothing in that direction.")
        elif selection == 'S':
            if hasattr(player.current_room, 's_to'):
                player.current_room = player.current_room.s_to
                print('Welcome to the ' + player.current_room.name)
                break
            else:
                print("Apologies but there is nothing in that direction.")
        elif selection == 'E':
            if hasattr(player.current_room, 'e_to'):
                player.current_room = player.current_room.e_to
                print('Welcome to the ' + player.current_room.name)
                break
            else:
                print("Aologies but there is nothing in that direction.")
        elif selection == 'W':
            if hasattr(player.current_room, 'w_to'):
                lady.current_room = player.current_room.w_to
                print('Welcome to the ' + player.current_room.name)
                break
            else:
                print("Apologies but there is nothing in that direction.")
        else:
            print("Please select a valid command!")