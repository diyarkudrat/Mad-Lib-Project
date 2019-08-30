

# def enter_words(function_code):
#     noun = input("Enter noun: ")
#     adj = input("Enter adjective: ")
#     verb = input("Enter verb: ")
#     ing_verb = input("Enter verb ending in -ing: ")

# print("It's been a " + adj + " summer here in " + noun + " City. The " + adj
#     + " car has been " + ing_verb + " the whole season. I think it's time to " + verb + " the car.")

words = ('adjective','noun','adj','verb ending in -ing','verb')

def is_input_valid(input_of_list):
    if input_of_list == "":
        return false
    else:
        return True

def create_story(input):
    stored_list = list(input)
    for i in range(0, len(input)):
        invalid_input = True
        check = True
        while invalid_input:
            recieved_input = input("Enter " + input[i] + ": ")
            check = is_input_valid(recieved_input)
            if check == False:
                print("Invalid input. Try again")
            else:
                stored_list[i] = recieved_input
                invalid_input = False
    return stored_list










def select(function_code):
    if function_code == 'S':
        start_game = input("Press S to start game!")
        fun_game()

def mad_lib_game():
    running = True

    while running:
        selection = input("Press S to start the game!")
        running = enter_words(selection)
mad_lib_game()
