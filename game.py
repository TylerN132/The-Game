# Get the player's name
name = input("Please enter character name: ")
print(f"Welcome, {name}!\n")

# Story setup
print("You awaken in a dark forest, a crisp brush of wind sends chills down your spine.")
print("Your head aches as you feel something drip down. Dazed, you look around and notice a light on the ground.\n")

# Choices
print("What do you do?")
print("1. Crawl to the light")
print("2. Check your head")
print("3. Yell for help")

# Get player choice
choice = input("\nEnter the number of your choice: ")

# Process first choice
if choice == "1":
    print("\nYou slowly crawl towards the mysterious light, unsure of what lies ahead.")
    print("You find a flashlight on the ground and pick it up, revealing a corpse next to you and an overturned vehicle.")
elif choice == "2":
    print("\nYou touch your head and feel a warm, sticky substance. It's blood.")
    print("You feel dizzy and collapse... GAME OVER.")
    exit()
elif choice == "3":
    print("\nYou yell for help, but your voice fades into the silence of the forest.")
    print("The darkness grows around you... GAME OVER.")
    exit()
else:
    print("\nYou hesitate too long, and the darkness seems to grow around you... GAME OVER.")
    exit()

# Continue only if player chose to crawl to the light
print("\nWhat do you do next?")
print("1. Check the corpse")
print("2. Check the vehicle")
print("3. Begin walking into the woods")

# Ensure valid input for second choice
valid_choices = ["1", "2", "3"]
next_choice = ""

while next_choice not in valid_choices:
    next_choice = input("\nEnter the number of your choice: ")

    if next_choice == "1":
        print("\nYou roll the corpse over to reveal a face half torn apart.")
        print("The part of the face you can see is familiar, but you cannot recall who it is.")
        print("In the corpse's pants is a wallet with a picture of the two of you.")
    elif next_choice == "2":
        print("\nYou walk over to the overturned vehicle and notice it is a 1964 Mustang.")
        print("You shine the light inside and begin looking for anything useful.")
        print("You open the glove compartment and find a half-empty bottle of whiskey and some camping equipment in the back seat.")
    elif next_choice == "3":
        print("\nYou feel like you should go back and check the corpse and the car first.")
    else:
        print("\nInvalid choice! Please enter 1, 2, or 3.")

# Continue the story after making a choice
print("\nYou move to the back of the car and begin searching the camping equipment.")
print("You find a compass and a first aid kit.")
print("As you grab the first aid kit, a sharp jolt of pain reminds you of the wound to your head.")

# NEW DECISION: Using the First Aid Kit or Moving On
valid_choices = ["1", "2"]
next_choice = ""

while next_choice not in valid_choices:
    print("\nWhat will you do now?")
    print("1. Use the first aid kit on your head wound")
    print("2. Take the first aid kit and compass and begin walking into the woods")
    print("You begin to hear howling in the distance, urging you to make a decision.")

    next_choice = input("\nEnter the number of your choice: ")

    if next_choice == "1":
        print("\nYou carefully clean and bandage your wound, stopping the bleeding.")
        print("You feel more stable and ready to continue your journey.")
    elif next_choice == "2":
        print("\nYou decide to keep moving despite the pain.")
        print("The howling in the distance grows closer as you step into the darkness of the woods...")
    else:
        print("\nInvalid choice! Please enter 1 or 2.")
