
# print("It's been a " + adj + " summer here in " + noun + " City. The " + adj + " car has been " + ing_verb + " the whole season. I think it's time to " + verb + " the car.")

def fun_game(function_code):
    noun = input("Enter noun: ")
    adj = input("Enter adjective: ")
    verb = input("Enter verb: ")
    ing_verb = input("Enter verb ending in -ing: ")

    print("It's been a " + adj + " summer here in " + noun + " City. The " + adj
        + " car has been " + ing_verb + " the whole season. I think it's time to " + verb + " the car.")

def select(function_code):
    if function_code == 'S':
        start_game = input("Press S to start game!")
        fun_game()


running = True
while running:
    selection = input("Press S to start the game!")
    running = fun_game(selection)
