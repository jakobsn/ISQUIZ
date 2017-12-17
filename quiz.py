import random

def quiz(questions, answers):
    correct = 0
    total = 0
    with open(answers) as file:
        answers = file.read().replace("\n", "").split("!!")
        file.close()
    with open(questions) as file:
        questions = file.read().split("!!")
        file.close()
    qindex = []
    for i in range(len(questions)):
        qindex.append(i)
    random.shuffle(qindex)
    for q in qindex:
        print(questions[q])
        answer = input("Answer: ")
        realanswer = answers[q]
        if answer == realanswer:
            print("Correct")
            print("")
            correct += 1
        elif answer == "Q":
            break
        else:
            print("Wrong, correct answer was:", realanswer)
        total += 1
    print("SCORE:", correct, "/", total)

if __name__ == '__main__':
    print("")
    print("**************TDT4175 QUIZ**************")
    print("Type \'Q\' to exit")
    questions = quiz('questions.txt', 'answers.txt')