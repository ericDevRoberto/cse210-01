'''
Book of Mormon Quiz
Author: Eric Roberto Silva
'''
def main():
    print('Welcome to Book of Mormon Quiz')
    answer = input('Are you ready to play the Quiz ? (yes/no): ')
    while answer != "yes":
        if(answer == "no"):
            print("Thanks to play the game :D")
            break
        else:
            print("This response is invalid")
            answer = input('Are you ready to play the Quiz ?: ')
    
    if(answer == "yes"):
        question_one = ask_question("Question 1: What is the name of the great Nephite captain in the wars against Lamanites? ", "moroni")
        question_two = ask_question("Question 2: Who is the name of the writer of the book of Mormon? ", "Mormon")
        question_three = ask_question("Question 3: Who hid the book of Mormon plates? ", "moroni")
        question_four = ask_question("Question 4: Who is the most important person cited in the Book of Mormon? ", "Jesus")
        points = question_one + question_two + question_three + question_four
        show_pontuation(points, 4)

def ask_question(question, response):
    answer = input(question)
    if answer.lower() == response.lower():
        print("Correct!")
        return 1
    else:

        print('Wrong Answer :(')
        return 0

def show_pontuation(points, quantity_questions):
    print(f"Your pontuation is {(points/quantity_questions)*100}%")
    print("Great job finishing the game!!")

if __name__ == "__main__":
    main()