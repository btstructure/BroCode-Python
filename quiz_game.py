#we will need 4 functions

#starts a new game
def new_game():
    #a list of guesses
    guesses = []
    correct_guesses = 0
    #represents the first question
    question_number = 1

    for key in questions :
        print(key)
        #use a nested for loop to iterate through the values
        for i in options[question_number - 1]: #the first index in a collection starts at 0, which is why we are subtracting, this works as a counter
            print(i)
        guess = input("Enter your answer (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        #increment the question number by 1
        check_answer(questions.get(key), guess)
        question_number += 1


#check the users input against the correct answer
def check_answer():
    pass



def display_score():
    pass



def play_again():
    pass


#create a dictionary (key:value) of questions and answers

questions = {
    "What is the capital of France?": "A",
    "What is the capital of Turkey?": "C",
    "What is the capital of Germany?": "B",
    "What is the capital of USA?": "C",
}

#a list of lists of answers to the questions
options = [["A. Paris", "B.Coppenhagen", "C. Berlin", "D. Madrid"],
           ["A. Izmir", "B. Istanbul", "C. Ankara", "D. Antalya"],
           ["A. Munich", "B. Berlin", "C. Frankfurt", "D. Hamburg"],
           ["A. New York", "B. Washington", "C. Washington DC", "D. Los Angeles"]]
#we will need a score variable

new_game()