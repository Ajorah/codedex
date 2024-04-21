#######################################
# Terminal Game - Codédex Project     #
# @Author - James aka "__valentine."; #
# @Title  - CavEscape                 #
#######################################

def moveOn(x):                                  # Returns whether a choice can be made.
    if x >= 10:
        return False
    elif x < 10 and x >= 0:
        return True
    else:
        return False
    
def story():                                    # Sends progressive dialog that is checked against an index key of answer.
    dialog = [                                  # dialog [0 : 9] == 10
        'Welcome to the Gauntlet...\nYour first task is to find the lever...\nOr else...\n1) Look left\n2) Look right\n3) Look up\n',
        'You found the lever...\nIt\'s covered in a green liquid...\n1) Pull it\n2) Look around\n3) Look other direction\n',
        'A noise is heard as you hear a click, but your hand is stuck to the lever!\n1) Look around\n2) Break the shaft\n3) Push the lever back\n',
        'As you push the lever back, you hear a grinding noise...\nA path has revealed itself!\nBut you\'re still stuck!\n1) Break the shaft\n2) Look around\n3) Call for help\n',
        'As you scream for help, someone yells "Wait a second!"\n1) Wait a second\n2) Wait 2 seconds\n3) Scream for more help\n',
        'You hear a voice behind you... Look...\nThere is an opening in the wall!\n1) Rush the opening\n2) Wait\n3) Break the shaft\n',
        'The shaft breaks, but the opening slowly begins to close!\n1) Rush the opening\n2) Wait\n3) Put the shaft back\n',
        'You make it through just in time!\nYou hear a click...\n1) Wait for help\n2) Continue moving\n3) Run\n',
        'As the shaft closes, you hear another click\nYou feel a large rumbling...\n1) Run\n2) Wait\n3) Continue moving\n',
        'The rumbling gets worse...\nThere\'s another click!\nA shaft opens above you!\nYou look up and see a huge BOULDER!\n1) RUN!\n2) RUN!!\n3) RUN\n'
    ]
    answer = [                                  # answer [0 : 9] == 10
        '2',
        '1',
        '3',
        '3',
        '1',
        '3',
        '1',
        '2',
        '3',
        '2'
    ]
    progress = 0                                # Initialize progress to 0; The beginning;
    while moveOn(progress) == True:             # If moveOn == True at stage of progress, continue
        correct = int(answer[progress])         # Assign correct the value of the index of answer that is progress
        result = int(input(dialog[progress]))   # Assign result the value of the index of dialog that is progress
        if result == correct:                   # If the given response is correct:
            print("Success!")
            progress += 1
        elif result != correct:                 # If the given response is incorrect:
            print("Failure! Starting over...")
            progress = 0
        else:                                   # Prompt to play again.
            print("Victory!")
            again = int(input("Would you like to play again?\n0) Yes\n1) No\n"))
            if again == 1:
                progress = 0
            elif again == 0:
                progress = 11
                print("Thanks for playing!")
            else:
                progress = 11
                print("Invalid response. Exiting")

story()
