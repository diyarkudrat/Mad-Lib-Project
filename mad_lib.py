
words = ['adjective','noun','adj','verb ending in -ing','verb','adjective','adjective','number','name']


def is_input_valid(input_of_list):
    if input_of_list == "":
        return False
    elif input_of_list == " ":
        return False
    else:
        return True

def create_story(val):
    stored_list = val[0:9]
    print(stored_list)
    for i in range(0, len(val)):
        invalid_input = True
        check = True
        while invalid_input:
            recieved_input = input("Enter " + val[i] + ": ")
            check = is_input_valid(recieved_input)
            if check == False:
                print("Invalid input. Try again")
            else:
                stored_list[i] = recieved_input
                invalid_input = False
    return stored_list

def print_story_out(function_code, given_word):
    if function_code == 'S':
        print("It's been a " + given_word[0] + " summer here in " + given_word[1] + " City. The " +
        given_word[2] + " car has been " + given_word[3] + " the whole season. I think it's time to " +
        given_word[4] + " the car and buy a new one. The new car should be " + given_word[5] + " and " +
        given_word[6] + " and worth " + given_word[7] + ". The new car's name will be " + given_word[8] + ".")
    else:
        print("Nothing selected")

def mad_lib_game():
    running = True

    while running:
        print("Welcome to the Mad Lib Game!")
        print('Press Q to quit')

        function_code = input('Press S to continue!')
        if function_code == 'S':
            print_story_out(function_code, create_story(words))
        elif function_code == 'Q':
            running = False
        else:
            print("not an option")

mad_lib_game()
