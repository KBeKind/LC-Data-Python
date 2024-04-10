# TODO 2: modify your quiz app to ask 5 questions

# TODO 1.2a: Assign question, correct_answer, and candidate_answer
question = "Who was the first American woman in space? "
correct_answer = "Sally Ride"
candidate_answer = ""
questions = ""
correct_answers = ""
candidate_answers = ""


def ask_for_name():
    # TODO 1.1: Ask for candidate's name
    candidate_name = input("What is your name? ")
    return candidate_name


def ask_question():
    # TODO 1.2b: Ask candidate the question and assign the response as candidate_answer
    print(question)
    a_candidate_answer = input("Your answer: ")

    return a_candidate_answer


def grade_quiz(a_candidate_answers):
    # TODO 1.2c: Let the candidate know if they have answered the question correctly or incorrectly
    grade = ""
    if a_candidate_answers == correct_answer:
        grade = "correct"
    else:
        grade = "incorrect"
    return grade


def run_program():
    candidate_name = ask_for_name()
    # TODO 1.1b: Ask for candidate's name and greet them by their name
    print("Hello", candidate_name)

    candidate_answers = ask_question()
    print(grade_quiz(candidate_answers))



run_program()