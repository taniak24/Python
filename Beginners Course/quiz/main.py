from multiple_choice import Question

question_prompts = [
    "What is the capital of France?\n(a) London\n(b) Paris\n(c) Berlin\n(d) Rome \n\n",
    "What is the chemical symbol for water?\n(a) Wo\n(b) H2O\n(c) Wa\n(d) H2 \n\n",
    "Who wrote 'Romeo and Juliet'?\n(a) William Shakespeare\n(b) Charles Dickens\n(c) Jane Austen\n(d) Mark Twain \n\n"
]

#the right answer of the questions
questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a"),
]

#function 
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
        print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    
run_test(questions)