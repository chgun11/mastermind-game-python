import os
from random import randint


# Main Menu
def main_menu():
    print("""-----------------------------------
|      Welcome to Mastermind      |
|     ~ A code-breaking game ~    |
-----------------------------------
|         ~ Main Menu ~           |
|                                 |
|    [1] Play Game                |
|    [2] Learn How To Play        |
|    [3] About MasterMind         |
|    [0] Exit Game                |
-----------------------------------""")

    # I miss Python :(
    # I wish I could do more Python
    # Catch Error, using Try/ Except ValueError, Anything that is not an integer
    while True:
        try:
            select_menu = int(input("> Enter Menu: "))
        except ValueError:
            error_message(133)
            continue
        else:
            if select_menu == 1:
                menu_01(1)
                break
            elif select_menu == 17027376:
                menu_01(0)
                break
            elif select_menu == 2:
                menu_02()
                break
            elif select_menu == 3:
                menu_03()
                break
            elif select_menu == 0:
                thank_you()
            else:
                error_message(888)


# Menu 1
def menu_01(god_mode_code):
    # Display Game Start-Up Info
    game_interface()

    # Declare Lists
    comp_answer = []
    user_answer = []
    guess_history_records = []

    # Nested function to generate Random Answer
    def random_answer():
        for y in range(4):
            comp_answer.append(randint(1, 6))
        if god_mode_code == 0:
            print(comp_answer)
        else:
            pass

    # produce TRUE condition for while Loop
    repeat = 1

    # while Loop for play again
    while repeat == 1:
        # Generate Random Answer
        random_answer()

        # Counter for user Attempts
        tries = 1

        # Counter for Chances Left
        chances_left = 10

        # while Loop for maximum of 10 chances
        while chances_left > 0:
            # while Loop for input again if answer is wrong
            while True:
                # print How Many Chances Left
                print("[Chances Left = {}]".format(chances_left))

                # Declares and Resets user_answer List
                user_answer = []

                # display userHistory
                guess_history(guess_history_records)

                # Using try/ Exception to catch non-integer value, with ValueError Exception
                try:
                    for x in range(1, 5):
                        if x == 1:
                            user_entry = int(input("> Guess {}st Color: ".format(x)))
                            if user_entry == 999:
                                thank_you()
                        elif x == 2:
                            user_entry = int(input("> Guess {}nd Color: ".format(x)))
                            if user_entry == 999:
                                thank_you()
                        elif x == 3:
                            user_entry = int(input("> Guess {}rd color: ".format(x)))
                            if user_entry == 999:
                                thank_you()
                        elif x == 4:
                            user_entry = int(input("> Guess {}th color: ".format(x)))
                            if user_entry == 999:
                                thank_you()

                        # Ensure input is within color code options
                        while user_entry < 1 or user_entry > 6:
                            error_message(598)
                            if x == 1:
                                user_entry = int(input("> Guess {}st Color: ".format(x)))
                                if user_entry == 999:
                                    thank_you()
                            elif x == 2:
                                user_entry = int(input("> Guess {}nd Color: ".format(x)))
                                if user_entry == 999:
                                    thank_you()
                            elif x == 3:
                                user_entry = int(input("> Guess {}rd Color: ".format(x)))
                                if user_entry == 999:
                                    thank_you()
                            elif x == 4:
                                user_entry = int(input("> Guess {}th Color: ".format(x)))
                                if user_entry == 999:
                                    thank_you()
                        else:
                            # If No problem, Append to user_answer List
                            user_answer.append(user_entry)

                    # Append each wrong user answer to form a Nested List, guess_history_list, then the items can then be accessed
                    guess_history_records.append(user_answer)

                    # God Mode
                    if god_mode_code == 0:
                        god_mode(comp_answer, user_answer)
                    else:
                        pass
                except ValueError:
                    error_message(540)
                    continue
                else:
                    # Declare variables to check Answer
                    correctColor_correctPosition = 0
                    correctColor_wrongPosition = 0

                    # MasterMind Logic
                    # Checks if user_answer[index] == comp_answer[index] uses for loop to loop 4 times, to get and check 4 items
                    # Also checks if user_answer item is in comp_ans List
                    for x in range(4):
                        if (comp_answer[x] != user_answer[x]) and (user_answer[x] in comp_answer):
                            correctColor_wrongPosition += 1
                        elif (comp_answer[x] == user_answer[x]) and (user_answer[x] in comp_answer):
                            correctColor_correctPosition += 1

                    # Result of Pegs
                    if correctColor_correctPosition == 4:
                        # Using game_won() to display Game Completed Message, passing in 'tries'
                        game_won(tries)
                        chances_left = -1
                        break
                    else:
                        # Using answer_hint() to display hint to User
                        answer_hint(user_answer, correctColor_wrongPosition, correctColor_correctPosition)

                    # Increment tries
                    tries += 1
                    chances_left -= 1

                    # If User Ran Out of Tries
                    if chances_left == 0:
                        print("""------------------------------------
|   Sorry, You ran out of chances  |
|        Try Harder Next Time      |
------------------------------------""")
                        break

        # Prompt to Play Again
        bottom_menu(1)
        repeat = int(input("~ Enter Menu: "))

        if repeat == 1:
            print("---------------------------------------")
            print("|    You Selected To PLAY AGAIN! :D   |")
            print("---------------------------------------")

            game_interface()

            # Resets Lists before looping
            guess_history_records = []
            comp_answer = []
    else:
        if repeat == 2:
            main_menu()
        elif repeat == 0:
            thank_you()


# Menu 2
def menu_02():
    print("""---------------------------------------------------------------------
|                       ~ Rules of the Game ~                       |
---------------------------------------------------------------------
|                                                                   |
|   * The computer picks a sequence of Colors                       |
|   * The Colors are the Color Codes                                |
|   * There can be more than 1 duplicate Color                      |
|                                                                   |
|   * Enter your 4 guesses into the command prompt, line by line    |
|   * For each CORRECT color guess in the CORRECT position          |
|        The computer will inform how many is CORRECT               |
|                                                                   |
|   * For each WRONG color guess in the WRONG position              |
|        The computer will inform how many is WRONG                 |
|                                                                   |
|   * The game is WON when the colors are guessed                   |
|        In the CORRECT positions                                   |
---------------------------------------------------------------------
|   To start playing MasterMind.....                                |
|                                                                   |
|   1. Start the Game by Entering '1' in the Main Menu              |
|   2. To choose colors, Enter Color Code                           |
|   3. Fill up 4 Colors                                             |
|   4. Guess until ALL the colors are in the CORRECT position       |
|   5. You have only 10 chances to Guess correctly                  |
---------------------------------------------------------------------""")

    # Using try/ Exception to catch non-integer value, with ValueError Exception
    while True:
        try:
            bottom_menu(2)
            repeat = int(input("> Enter Menu: "))
        except ValueError:
            error_message(888)
        else:
            if repeat == 1:
                main_menu()
            elif repeat == 0:
                thank_you()
            else:
                error_message(888)
                continue


# Menu 3
def menu_03():
    print("""-------------------------------------------------------------------------------
|                           ~ About MasterMind ~                              |
|                                                                             |
|    Mastermind or Master Mind is a code-breaking game for two players.       |
|    The modern game with pegs was invented in 1970 by Mordecai Meirowitz,    |
|    an Israeli postmaster and telecommunications expert. It resembles an     |
|    earlier pencil and paper game called Bulls and Cows that may date        |
|    back a century or more.                                                  |
-------------------------------------------------------------------------------""")

    # Using try/ Exception to catch non-integer value, with ValueError Exception
    while True:
        try:
            bottom_menu(3)
            repeat = int(input("> Enter Menu: "))
        except ValueError:
            error_message(888)
        else:
            if repeat == 1:
                main_menu()
            elif repeat == 0:
                thank_you()
            else:
                error_message(888)
                continue


# Thank You
def thank_you():
    print("""--------------------------------------------------------------
|             ~ You CHOSE to Exit the Program ~              |
|       ~Thank you for using the Mastermind Program !!       |
--------------------------------------------------------------
|                                                            |
|              - MasterMind 2020 // CSC 1024 -               |
|                                                            |
|               ~ Gun Ching Hern (1702 7376) ~               |
--------------------------------------------------------------""")
    os.system("pause")
    exit()


# Game Interface
def game_interface():
    print("""-------------------------------------------------------------------------
|              HOW TO PLAY?                |         Color Code         |
-------------------------------------------------------------------------
|   1. Choose 4 Color Codes                |                            |
|   2. Click ENTER after each Color Code   |       1 - Black            |
|   3. Follow the hint and keep guessing   |       2 - White            |
|                                          |       3 - Red              |
|   IMPORTANT:                             |       4 - Blue             |
|        ** ENTER Color Code               |       5 - Green            |
|                                          |       6 - Pink             |
-------------------------------------------------------------------------
>>>>>>>>>>>>>>>>>>>>>>>>>>>>   Game Started   <<<<<<<<<<<<<<<<<<<<<<<<<<<\n""")


# User History
def guess_history(nested_list):
    # if nothing in nested List
    # if list is empty, list == False
    # so just, 'not' List
    if not nested_list:
        pass
    else:
        print("---------------------------------")
        print("|       Your Guess History      |")
        print("---------------------------------")
        for x in nested_list:
            print(x)
        print("---------------------------------")


# Congratulations Message
def game_won(attempts):
    if attempts == 1:
        greet = "|            !! Congratulations !!!             |"
        what_are_you = "|       !!! You are a TRUE MasterMind !!!       |"
        try_line = "|     It took you {} TRY to GUESS CORRECTLY      |".format(attempts)
    else:
        greet = "|               !!! Good Job !!!                |"
        what_are_you = "|     ... Play More to be a MasterMind ...      |"
        try_line = "|     It took you {} TRIES to GUESS CORRECTLY    |".format(attempts)

    print("""-------------------------------------------------
{}
{}
|                                               |
{}
-------------------------------------------------""".format(greet, what_are_you, try_line))


# Hint By Computer
def answer_hint(my_list, salah, betul):
    global position0, position1, position2, position3

    # check position 0 in list
    if my_list[0] == 1:
        position0 = "Black"
    elif my_list[0] == 2:
        position0 = "White"
    elif my_list[0] == 3:
        position0 = "Red  "
    elif my_list[0] == 4:
        position0 = "Blue "
    elif my_list[0] == 5:
        position0 = "Green"
    elif my_list[0] == 6:
        position0 = "Pink "

    if my_list[1] == 1:
        position1 = "Black"
    elif my_list[1] == 2:
        position1 = "White"
    elif my_list[1] == 3:
        position1 = "Red  "
    elif my_list[1] == 4:
        position1 = "Blue "
    elif my_list[1] == 5:
        position1 = "Green"
    elif my_list[1] == 6:
        position1 = "Pink "

    if my_list[2] == 1:
        position2 = "Black"
    elif my_list[2] == 2:
        position2 = "White"
    elif my_list[2] == 3:
        position2 = "Red  "
    elif my_list[2] == 4:
        position2 = "Blue "
    elif my_list[2] == 5:
        position2 = "Green"
    elif my_list[2] == 6:
        position2 = "Pink "

    if my_list[3] == 1:
        position3 = "Black"
    elif my_list[3] == 2:
        position3 = "White"
    elif my_list[3] == 3:
        position3 = "Red  "
    elif my_list[3] == 4:
        position3 = "Blue "
    elif my_list[3] == 5:
        position3 = "Green"
    elif my_list[3] == 6:
        position3 = "Pink "

    print("""-----------------------------------------------------------------
|   These are your Guesses...         |      [Color Codes]      |
|-------------------------------------|-------------------------|
|   1st Color: {}                  |     1 - Black           |
|   2nd Color: {}                  |     2 - White           |
|   3rd Color: {}                  |     3 - Red             |
|   4th Color: {}                  |     4 - Blue            |
|                                     |     5 - Green           |
|                                     |     6 - Pink            |
-----------------------------------------------------------------
|         Correct Color, Wrong Position (White Peg) = {}         |
|         Correct Color, Correct Position (Red Peg) = {}         |
|                                                               |
|                       ~ TRY AGAIN ~                           |
|                                                               |
|                Enter '999' to Quit the Game                   |
-----------------------------------------------------------------""".format(position0, position1, position2, position3,
                                                                            salah, betul))


# Bottom Menu
def bottom_menu(inside_which_menu):
    print("-------------------------------")
    if inside_which_menu == 1:
        print("|    Play Again ?             |")
        print("|-----------------------------|")
        print("|    [1] Yes                  |")
    if inside_which_menu == 1:
        print("|    [2] Back To Main Menu    |")
    elif (inside_which_menu == 2) or (inside_which_menu == 3):
        print("|    [1] Back To Main Menu    |")
    print("|    [0] Exit MasterMind      |")
    print("-------------------------------")


# Error Messages
def error_message(error_number):
    if error_number == 888:
        print("""------------------------------------------
|    ERROR # 888                         |
|        * PLEASE enter a VALID Menu     |
------------------------------------------""")
    elif error_number == 133:
        print("""-----------------------------------------------------
|   ERROR # 133                                     |
|       * PLEASE enter a NUMBER to SELECT Menu      |
-----------------------------------------------------""")
    elif error_number == 598:
        print("""-----------------------------------------------------
|   ERROR # 598                                     |
|       * PLEASE enter a VALID Color Code           |
-----------------------------------------------------""")
    elif error_number == 540:
        print("""------------------------------------------------------
|    ERROR # 540                                     |
|        * PLEASE enter a VALID Color Code           |
|        *** Fields have been RESET                  |
------------------------------------------------------""")


# God Mode
def god_mode(original_ans, user_ans):
    print("\n<<----------- GOD Mode ---------------------------------------------------------------------------------->>")
    print("Computer Answer = {}".format(original_ans))
    print("User Answer     = {}".format(user_ans))
    print("<<----------- GOD Mode ---------------------------------------------------------------------------------->>\n")


# run program
if __name__ == '__main__':
    main_menu()
