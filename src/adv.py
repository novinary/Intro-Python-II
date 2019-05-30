import re
from room import Room
from player import Player
from os import system, name 
from time import sleep 

# define clear function
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

# Declare all the room
room = {
    'lumbridge': Room("Lumbridge", """Welcome to the kingdom of Lumbridge!""",[]),
    'entrance': Room("Entrance", """Please come in!""",['grass','rocks', 'dust']),
    'weaponstore': Room("Weapon Store", """Variety of weapons to choose from.""",['sword', 'dagger', 'knife']),
    'bank': Room("Bank", """Access your personal bank here""",['100 gbp']),
    'library': Room("Library", """All information about Lumbridge is available here. From our people to weapons.""",['Modern History', 'Mountain Trolls', 'Varrock City']),
    'dine': Room("Dining Hall", """Incredible feast are freshly prepared everyday""",['Cake', 'Baguette', 'Meatloaf'])
}

# # Link rooms together
room['lumbridge'].n_to = room['entrance']
room['entrance'].s_to = room['lumbridge']
room['entrance'].n_to = room['weaponstore']
room['entrance'].w_to = room['bank']
room['entrance'].e_to = room['library']
room['weaponstore'].s_to = room['entrance']
room['bank'].w_to = room['entrance']
room['bank'].n_to = room['library']
room['library'].s_to = room['bank']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Bob", room['lumbridge'], ['wood', 'lighter', 'tuna'])
clear()
welcome_msg = """
 ──────▄▀▀▀▀▀▀▀▄─────── 
 ─────▐─▄█▀▀▀█▄─▌────── 
 ─────▐─▀█▄▄▄█▀─▌────── 
 ──────▀▄▄▄▄▄▄▄▀─────── 
 ─────▐▀▄▄▐█▌▄▄▀▌────── 
 ──────▀▄▄███▄▄▀─────── 
 █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█ 
 █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█ 
 █░░║║║╠─║─║─║║║║║╠─░░█ 
 █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█ 
 █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█ 
 """
print(welcome_msg)

# Write a loop that:
#
# * Prints the current room name/description
print("\nWelcome " + player.name + "! \nWe are very excited for you to begin your quest. \n")

print("You are currently logged into the world: " + player.current_room.name + ".\n" + player.current_room.description + "\n\n")

def room_items():
    output = ''
    for i in player.current_room.room_items:
        output += (" " + i + "\n✿ ❀ ❁ ✾ ✽ ❃\n\n")
    return output

selection = ""
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while selection != 'Q':
    selection = input("Where would you like to head today, N-North, S-South, E-East, or W-West \n or R-Check your Inventory or Q-Quit: ")
    selection = selection.upper()
    if len(re.findall("[NSEWRQ]", selection)) == 1:
        if selection == 'N':
            if hasattr(player.current_room, 'n_to'):
                clear()
                player.current_room = player.current_room.n_to
                print('Welcome to the ' + player.current_room.name + '\n' + player.current_room.description + "\n\n")
                if len(player.current_room.room_items) != 0:
                    print ('This room has following items:\n')
                    print(room_items())
                    print("\n\n") 
                else:
                    print("No items in this room\n\n") 
            else:
                clear()
                print("Apologies but there is nothing in that direction.")
        elif selection == 'S':
            if hasattr(player.current_room, 's_to'):
                clear()
                player.current_room = player.current_room.s_to
                print('Welcome to the ' + player.current_room.name + '\n' + player.current_room.description + "\n\n")
                if len(player.current_room.room_items) != 0:
                    print ('This room has following items:\n')
                    print(room_items())
                    print("\n\n") 
                else:
                    print("No items in this room\n\n") 
            else:
                clear()
                print("Apologies but there is nothing in that direction.")
        elif selection == 'E':
            if hasattr(player.current_room, 'e_to'):
                clear()
                player.current_room = player.current_room.e_to
                print('Welcome to the ' + player.current_room.name + '\n' + player.current_room.description + "\n\n")
                if len(player.current_room.room_items) != 0:
                    print ('This room has following items:\n')
                    print(room_items())
                    print("\n\n") 
                else:
                    print("No items in this room\n\n") 
            else:
                clear()
                print("Aologies but there is nothing in that direction.")
        elif selection == 'W':
            if hasattr(player.current_room, 'w_to'):
                clear()
                player.current_room = player.current_room.w_to
                print('Welcome to the ' + player.current_room.name + '\n' + player.current_room.description + "\n\n")
                if len(player.current_room.room_items) != 0:
                    print ('This room has following items:\n')
                    print(room_items())
                    print("\n\n") 
                else:
                    print("No items in this room\n\n") 
            else:
                clear()
                print("Apologies but there is nothing in that direction.")
        elif selection == 'R':
            clear()
            print("Items in your inventory:\n\n")
            for i in player.inventory:
                print("  " + i)
                print("✿ ❀ ❁ ✾ ✽ ❃")
            print('\n\n')
        elif selection == 'Q':
            clear()
            print("Goodbye for now.")
            quit()
        else:
            clear()
            print("Please select a valid command!")
