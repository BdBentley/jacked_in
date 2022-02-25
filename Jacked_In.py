# Welcome to jacked_in. This is a text based game that is based off of retro cyberpunk 
# themes with fantastical modern tech. A player will navigate the "maze" gathering items
# in order to defeat the final boss character. You will be able to navigate between rooms
# and even confront the final boss. Enjoy!
# - Brian Bentley 1/20/2021

from calendar import c
import time

# This is the show instructions function
def showInstructions():
        # Show the main menu and commands.
        print('Welcome to jacked_in')
        time.sleep(.5)
        print('While in virtual.city() you must collect all six items to defeat the CPU firewall Cryptoph.')
        time.sleep(.5)
        print('Move commands: go North, go South, go East, go West')
        time.sleep(.5)
        print('Move commands continued: Northwest, Northeast, Southwest, Southeast')
        time.sleep(4)


# Set up the main function.
def main():

    # This is the callable show status function.
    def showStatus():
        print(f'You are currently in {currentRoom}')
        print(f'You have {inventory} in your inventory')
        print(f'This is a list of the rooms and directions you can take: {rooms}')
        time.sleep(2)

    # Show the players current room
    # Show the players inventory
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
        'Ethernet Port': {'North': 'Network Card'},
        'CPU': {}

    }

    # Call the show instructions function.
    showInstructions()

    # This will start the player in the Ethernet Port.
    currentRoom = 'Ethernet Port'
    inventory = []



    # Create a constant running loop
    while True:
        
        # This if statement checks if the player is in the last room without having a full inventory.
        if currentRoom == 'CPU' and len(inventory) != 6:
            print('The rogue CPU is now aware of your presence')
            print('\'You have come unprepared adventurer...\'')
            time.sleep(1)
            print('Cryptoph the rogue CPU attacks, you have been converted into corrupt bits')
            time.sleep(1)
            print('Game Over')
            break

        # This is the main game loop
        else:
            print('Your current location is: ' , currentRoom)
            print("Please choose from the following options below: ")
            time.sleep(.5)
            print('Press 1 to move.')
            print('Press 2 to show current status.')
            print('Press 3 to pick up item.')
            if rooms.item[currentRoom] == True:
                print(f'You see {rooms.item[currentRoom]} laying on the ground')
            choice = int(input())

            # Set up the players choice of moving, checking status, and picking up an item.
            if choice == 1:
                time.sleep(1)
                print(f'You are currently in {currentRoom}')
                time.sleep(.5)
                print('Please type a direction to move')
                time.sleep(.5)
                print('Example: North, South, East, West, Northwest, Northeast, Southwest, Southeast Exit\' ')
                time.sleep(.5)
                move = input()

                # If the move is in the room list, then the current room is the new room.
                if (move in rooms[currentRoom]):
                    currentRoom = rooms[currentRoom][move]
                
                # Let the player know that there is no room in this direction
                else:
                    print('There is no room in this direction')
            
            # Call the show status function.
            elif choice == 2:
                time.sleep(1)
                showStatus()

            # Add the current rooms item to the inventory
            elif choice == 3:
                time.sleep(1)
                if 'item' in currentRoom:
                    inventory.append(currentRoom['item'])
                else:
                    print('There is no item in this room.')
        


            
            


main()
