#Have very little time left to work on this so am going to concentrate 
#on writing functions rather than connecting this file to other files

number_of_questions = 0
def get_number_of_questions():
    number_of_questions = int(raw_input("How many questions should be in your quiz?"))
    #I don't think the "is not int" part is the correct syntax
    if number_of_questions < 0:
        print "Please enter an integer greater than 0"
        #Need to add something to show user number_of_questions prompt again
        #TO DO: Add code to account for case where user enters a character 
        #other than a number
    else:
        continue


def choose_questions(number_of_questions):
    list_of_questions = []
    for i in range(number_of_questions):
        #TO DO: Add code that will choose among available question_ids in a way
        #that meets basic requirements
        chosen_question = #
        list_of_questions.append(chosen_question)

    return list_of_questions
