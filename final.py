startmessage = """\nYou are helping Professor Disco explore an ancient ruin. 
Do you want to explore the cave with the professor?"""
message0 = """
You and the professor enter the cave. You are in a round room with low ceilings. The walls are covered in stone tiles. 
There are two doors in front of you. One is made of stone and has moss growing on it.
The other door has rotted away, leaving only an archway. 
You can hear some noises from the arch. You think it's a small animal.
The professor decides to wait for you at the entrance and leaves you to explore alone."""
message1 = """
You make it through the stone door.
You are now in an underground passage. There is a fork in the passage. The left side is lit by torches that burn with 
green flames. The right side is pitch black."""
message2 = """
You make it through the archway.
In the next room, there is a trail of black slime on the floor, leading to one of two doors. 
The other door is the source of the animal noises from before."""
message3 = """
You enter the passage with green fire.
Beyond you, there are two closed-off passages. One has a door, and the other passage has caved in.
Suddenly, the door opens by itself."""
message6 = """
You make it through the door with the animal noises.
The noises are coming from a pile of reanimated skeletons on the floor. As you watch, a bear skeleton starts reforming.
You have some tools, and you can fight the moving skeleton or walk around it and continue."""
message7 = """
You enter the door that opens by itself, and it closes itself behind you. 
There is only one door ahead of you, and you decide to enter it."""
message8 = """
You clear the cave-in and continue.
Ahead, you can hear water rushing. like a river or a waterfall. 
To the side, you hear wind blowing over top of the ruins."""
message10 = """
You go around the animals and continue.
You hear a waterfall, which could lead to a lake or go out of the ruin. Or, go through the plain stone door ahead."""
message12 = """
You follow the sound of wind. There is a steep wall ahead, but you can see sunlight above.
You decide to climb the wall with your tools."""
message15 = """
You enter the plain stone door to find a pile of gold coins and tools that will help your research!
Congratulations! You made it through the guardians' questions and found the treasure!
There is a huge golden door on the other side of the treasure room, which may lead to more treasure.
As you watch, a door opens in the wall, leading to the forest outside."""
pw1 = "It begins!"
clue1 = "\nIz hkmoty!"
pw2 = "No, but a tin can."
clue2 = "\nCan a match box?"
hint2 = "No, but a --- ---."
pw3 = "short"
clue3 = "\nWhat word plus two letters is shorter?"
hint3 = "s----"
pw6 = "password"
clue6 = "\nvgyycuxj"
pw8 = "technology"
clue8 = "\nzkinturume"
pw10 = "skeleton"
clue10 = "\nyqkrkzut"
pw11 = "a stick"
clue11 = "\nWhat is brown and sticky?"
hint11 = "It is sticky indeed. Very stick-y. And most, but not all, are brown. It could be gray, white or green, maybe."
pw16 = "hi baby chuddles"
clue16 = "\nno hghe inajjrky"
pw17 = "finish"
clue17 = "\nlotoyn"
endmessage4 = """
You enter the pitch black passageway.
While walking along, you try to get your flashlight. Distracted, you trip over a stone and get a concussion
and are not found until it's too late.


You died. Try again!
"""
endmessage5 = """
You follow the black slime through a door.
It rises up in revolt against humanity and kills you.


You died. Try again!
"""
endmessage9 = """
You decide to fight off the skeletons.
You lose.


You died. Try again!
"""
endmessage11 = """
The passageway is a dead end, and you try to go back to the self-opening door. Unsure of how it opens, you touch it
to try to get it to open. You are sucked into the wall, as it survives on the life force of unsuspecting explorers.

You died. Try again!
"""
endmessage13 = """
You follow the sound of water.
You find a waterfall and a lake. You could escape over the lake, but there are sharp rocks at the bottom and you have 
no boat. While walking around in search of another way out, you slip on the wet, slimy stone and break your ankle.
You cannot get back up, and you cannot escape.


You died. Try again!
"""
endmessage16 = """
You climb up the cliff with your tools, but accidentally drop them back into the room you were in.
At the top, you are on a cliff, with no way down and no way to contact the professor.
Dropping forward or backward is not an option. You are carried off by a giant crow and never heard from again

You died. Try again!
"""
endmessage17 = """
You exit straight into the jungle, and find yourself near the entrance of the ruin. 
You made it out alive. Be grateful."""
endmessage18 = """
Don't be so greedy. You just died. Take your blessings and run with them, greedy child.


You died. Try again!
"""
alphabet = "abcdefghijklmnopqrstuvwxyz"


def brute_force(new_message):
    # Try every key value
    for key in range(len(alphabet)):
        new_alphabet = alphabet[key:] + alphabet[:key]
        attempt = ""
        for i in range(len(new_message)):
            index = alphabet.find(new_message[i])

            if index < 0:
                attempt += new_message[i]
            else:
                attempt += new_alphabet[index]

        print("Key: " + str(key) + " - " + attempt)


def shiftpassword(pw, clue):
    passed = False
    print("""
You have to give the correct password before continuing through the ruin. Find the password from this clue:""")
    print("The clue is: " + clue)
    password = input("""Enter the password below.
Enter \'help\' if you need help with the password. 
""").lower()
    while not passed:
        if password == pw:
            passed = True
            break
        elif password == 'help':
            brute_force(clue)
            print("You have to find the correct password from the possibilities given.")
            password = input("\nEnter the password now.\n")
        else:
            password = input()
    return passed


def riddle(pw, clue, hint):
    passed = False
    print("\nAnswer this riddle:")
    print(clue)
    print()
    password = input("""Enter the answer below.
Enter \'hint\' if you want a helpful hint. 
""")
    while not passed:
        if password == pw:
            passed = True
            break
        elif password == 'hint':
            print(hint)
            password = input("\nTry the riddle out again! Answer below:\n")
        else:
            password = input()
    return passed


def end(message):
    print()
    print(message)
    direction = input("""To exit, type \'exit\'.
To try again, type \'b\'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            break
        if direction == "b":
            dirt = True
            print("""
            
            
            
            
            
            
            
            
            
            
            
    
    
    
    
    
            
            
            
            
            """)
            fork0(message0)
        else:
            direction = input()


def straight_to_end_pw(message, pw, clue, endmessage):
    print(message)
    print()
    direction = input("""To continue, type \'a\'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            end(endmessage)
            break
        else:
            direction = input()


def fork15(message):
    shiftpassword(pw15, clue15)
    print(message)
    print()
    direction = input("""To continue, type 'a'.
To go outside, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            end(endmessage18)
            break
        elif direction == "b":
            dirt = True
            end(endmessage17)
            break
        else:
            direction = input()


def fork10(message):
    shiftpassword(pw10, clue10)
    print(message)
    print()
    direction = input("""To go towards the waterfall, type 'a'.
To go toward the plain door, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            end(endmessage13)
            break
        elif direction == "b":
            dirt = True
            fork15(message15)
            break
        else:
            direction = input()


def fork8(message):
    shiftpassword(pw8, clue8)
    print(message)
    print()
    direction = input("""To go towards the sound of wind, type 'a'.
To go towards water, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            straight_to_end_pw(message12, pw16, clue16, endmessage16)
            break
        elif direction == "b":
            dirt = True
            end(endmessage13)
            break
        else:
            direction = input()


def fork6(message):
    shiftpassword(pw6, clue6)
    print(message)
    print()
    direction = input("""To go around the skeletons and continue, type 'a'.
To fight the skeletons, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "b":
            dirt = True
            end(endmessage9)
            break
        elif direction == "a":
            dirt = True
            fork10(message10)
            break
        else:
            direction = input()


def fork3(message):
    shiftpassword(pw3, clue3)
    print(message)
    print()
    direction = input("""To go through the self-opening door, type 'a'.
To clear the cave-in and continue that way, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            straight_to_end_pw(message7, pw11, clue11, endmessage11)
            break
        elif direction == "b":
            dirt = True
            fork8(message8)
            break
        else:
            direction = input()


def fork2(message):
    riddle(pw2, clue2, hint2)
    print(message)
    print()
    direction = input("""To go towards the slime, type 'a'.
To go towards the animal noise, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            end(endmessage5)
            break
        elif direction == "b":
            dirt = True
            fork6(message6)
            break
        else:
            direction = input()


def fork1(message):
    shiftpassword(pw1, clue1)
    print(message)
    print()
    direction = input("""To follow the green torches, type 'a'.
To go through the dark passage, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            fork3(message3)
            break
        elif direction == "b":
            dirt = True
            end(endmessage4)
            break
        else:
            direction = input()


def fork0(message):
    print(message)
    print()
    direction = input("""To go through the stone door, type 'a'.
To go through the archway, type 'b'.
""").lower()
    dirt = False
    while not dirt:
        if direction == "a":
            dirt = True
            fork1(message1)
            break
        elif direction == "b":
            dirt = True
            fork2(message2)
            break
        else:
            direction = input()


def forkstart(message):
    print(message)
    print()
    direction = input("""Type 'yes' or 'no'.
""")
    dirt = False
    while not dirt:
        if direction == "yes":
            dirt = True
            fork0(message0)
        elif direction == "no":
            print("\nEven though you don't want to explore, Professor P shoves you into the cave anyway.")
            fork0(message0)
            dirt = True
        else:
            direction = input()


forkstart(startmessage)
