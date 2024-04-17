# TODO 2: modify your quiz app to ask 5 questions

# TODO 1.2a: Assign question, correct_answer, and candidate_answer
question = "Who was the first American woman in space? "
correct_answer = "Sally Ride"
candidate_answer = ""
questions = ["Who was the first American woman in space?", "True or false: 5 kilometer == 5000 meters?", "(5 + 3)/2 * 10 = ?", "Given the list [8, 'Orbit', 'Trajectory', 45], what entry is at index 2?", "What is the minimum crew size for the ISS?" ]
correct_answers = ["Sally Ride", "true", "40", "Trajectory", "3"]
candidate_answers = []
candidate_score = []

def ask_for_name():
    # TODO 1.1: Ask for candidate's name
    candidate_name = input("What is your name? ")
    return candidate_name


def ask_question():
    # TODO 1.2b: Ask candidate the question and assign the response as candidate_answer

    for aQuestion in questions:
        print(aQuestion)
        candidate_answers.append(input("Your answer: "))

    return candidate_answers


def grade_quiz():
    # TODO 1.2c: Let the candidate know if they have answered the question correctly or incorrectly
    score = 0

    for i in range(0, len(correct_answers), 1):
        if candidate_answers[i].lower() == correct_answers[i].lower():
            score += 1
            candidate_score.append(1)
        else:
            candidate_score.append(0)

    return score


def run_program():
    candidate_name = ask_for_name()
    # TODO 1.1b: Ask for candidate's name and greet them by their name
    print("Hello", candidate_name)

    ask_question()

    candidate_total = grade_quiz()

    for i in range(0, len(correct_answers), 1):
        print(f"{i+1}) {questions[i]} \n Your Answer: {candidate_answers[i]} \n Correct Answer: {correct_answers[i]}")


    print(f"Your total score is {candidate_total} out of {len(correct_answers)}")

    print(f"Your correct answer percentage is {(candidate_total/len(correct_answers)) * 100 }%")

    if candidate_total >= 4:
        print(f"You have PASSED!!!")
    else:
        print(f"You have FAILED!!!")


run_program()