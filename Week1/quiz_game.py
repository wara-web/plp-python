print("Hellow there, welcome to python simple quiz game")
print("Remember! If you misspell any of your answers, you will be marked wrong\nWelcome and enjoy the game")

score =0
question_no= 0

playing= input("Do you wish to play?").lower()
if playing =='yes':
    question_no +=1
    quiz = input(f'\n{question_no}. what do we call the code lines that are never executed in python?').lower()
    if quiz == 'comment':
        score += 1
        print('correct! one point earned.')

    else:
        print('Incorrect. The answer is either a comment, or dead code')


    question_no +=1
    quiz = input(f'\n{question_no}. what do we call variables that belong to the global scope?').lower()
    if quiz == 'global variables':
        score += 1
        print('correct! one point earned.')

    else:
        print('Incorrect. The answer is global variables')

    question_no +=1
    quiz = input(f'\n{question_no}. what operators do we use to combine conditional statements?').lower()
    if quiz == 'logical operators':
        score += 1
        print('correct! one point earned.')

    else:
        print('Incorrect. The answer is logical operators')
    question_no +=1
    quiz = input(f'\n{question_no}. what do we call an odered unchangeable data collection type?').lower()
    if quiz == 'tuple':
        score += 1
        print('correct! one point earned.')

    else:
        print('Incorrect. The answer is tuple')

else:
    print("Thank you! you have been eliminated. try again next time!!!!")
    quit()

print(f'you scored {score} correct')
