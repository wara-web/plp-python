import pyjokes

print('Hi, Welcome to random joke generator')
play = input('Do you wish to play?').lower()
if play =='yes':
    for j in range(11):
        joke = pyjokes.get_joke()

        print(joke)
    

else:
    print("Thank you for opting out. should you wish to play, please feel welcome.")