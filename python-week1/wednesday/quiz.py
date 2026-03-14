from Questions import Questions

question_prompt = [
    "What color are apples? \n (a)Red/Green \n (b)Purple \n (c)Orange\n\n",
    "What color are Bananas? \n (a)Teal \n (b)Magenta \n (c)Yellow\n\n",
    "What color are strawberries? \n (a)Yellow \n (b)Red \n (c)Blue\n\n",
]

questions = [
    Questions(question_prompt[0], "a"),
    Questions(question_prompt[1], "c"),
    Questions(question_prompt[2], "b"),

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you score " + str(score) +"/"+ str(len(questions)))

run_test(questions)