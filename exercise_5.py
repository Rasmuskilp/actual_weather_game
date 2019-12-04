#Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
def weather_game():
    print('what kind of weather will you have?')
    print('answer [y/n] to these questions')
    user_choice = input('will the weather be sunny?')
    if user_choice == 'y':
        print('take your shorts!')
        exit()
    user_choice = input('will the weather be stormy?')
    if user_choice == 'y':
        print('take rain coat')
        exit()
    user_choice = input('will the weather be rainy?')
    if user_choice == 'y':
        print('take your umbrella')
        exit()
    user_choice = input('will the weather be rainy and stormy?')
    if user_choice == 'y':
        print('stay home')
        exit()
    if not user_choice or user_choice[0].lower() != 'y':
        print("sorry, you broke the game!")
        exit(1)

# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'