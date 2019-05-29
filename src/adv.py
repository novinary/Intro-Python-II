from room import Room
import re

selection = input ("Select N for North, S for South, E for East, or W for West: ")

if len(re.findall("[nNsSeEwW]", selection)) != 1:
    print("Please select a valid direction.")
else:
    print("The user has selected " + selection.upper())

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
room['lumbridge'].n_to = room['entrance']s
room['entrance'].s_to = room['lumbridge']
room['entrance'].n_to = room['weaponstore']
room['entrance'].w_to = room['bank']
room['entrance'].e_to = room['library']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
