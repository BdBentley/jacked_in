# Welcome to jacked_in. This is a text based game that is based off of retro cyberpunk 
# themes with fantastical modern tech. A player will navigate the "maze" gathering items
# in order to defeat the final boss character. You will be able to navigate between rooms
# and even confront the final boss. Enjoy!
# - Brian Bentley 1/7/2022

def showInstructions():
        # Show the main menu and commands.
        print('Welcome to jacked_in')
        print('While in virtual.city() you must collect all six items to defeat the CPU firewall Cryptoph.')
        print('Move commands: go North, go South, go East, go West')
        print('Move commands continued: Northwest, Northeast, Southwest, Southeast')
        print('Add to inventory: grab item, "item name"')

def showStatus(currentRoom, inventory, rooms):
    currentRoom = main(currentRoom)
    inventory = main(inventory)
    rooms = main(rooms)
    print(currentRoom)
    print(inventory)
    print(rooms)

    # Show the players current room
    # Show the players inventory

def main():
    # Create a dictionary with rooms linked to other rooms.
    # Create an inventory which starts empty.
    rooms = {

        'Mother Board':{'West': 'Network Card', 'Northwest': 'Graphics Card', 'North': 'RGB Header', 'Northeast': 'Ram', 'East': 'Socket', 'South': 'USB Port'},
        'Network Card': {'East': 'Mother Board', 'item': 'MAC Address'},
        'Graphics Card': {'Southeast': 'Mother Board', 'item': 'CPU Plans'},
        'RGB Header': {'South': 'Mother Board', 'item': 'Chromatic Abberation'},
        'RAM': {'Southwest': 'Mother Board', 'item': 'Crypto_cracker.py'},
        'SSD Storage': {'Southwest': 'Mother Board', 'item': 'algo_database'},
        'USB Port': {'East': 'Keyboard','North': 'Mother Board'},
        'Keyboard': {'West': 'USB Port', 'item': 'user_input'},
        'Socket': {'West': 'Mother Board', 'East': 'CPU'},
        'Ethernet Port': {'North': 'Network Card'}


    }

    # This will start the player in the Ethernet Port.
    currentRoom = 'Ethernet Port'

    # Create a constant running loops
    while True:

        # Show the players current condition.
        # Exit the loop if the player enters the CPU room with all items,
        # exit the loop if player enters the room without the items.
            
        # Prompt the players next move.

        # Create an inventory that will print the players current inventory.

        # Create a function that will allow the player to move between rooms.

        inventory = []

        print("Please choose from the following options below: ")
        print('Press 1 to move.')
        print('Press 2 to show current status.')
        print('Press 3 to pick up item.')
        choice = int(input())

        if choice == 1:
            print('Please type a direction to move: ')
            move = input()
            if move == rooms(''):
                currentRoom = rooms

        elif choice == 2:
            showStatus()
            break

        elif choice == 3:
            print('Would you like to pickup the item? "y" or "n" ')
            item_choice = str(input())
            if item_choice == 'y':
                inventory += rooms.items
            else:
                break

showInstructions()
main()
showStatus()