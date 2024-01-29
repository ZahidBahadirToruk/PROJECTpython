class Quiz:
    def __init__(self):
        self.point = 0
        self.questions = {
            'What is the capital of France?': 'Paris',
            'When did World War II end?': '1945',
            'Which is the largest country in the world?': 'Russia',
            'In which country would you find the Leaning Tower of Pisa?': 'Italy',
            'What is the currency of Japan?': 'Yen',
            'Who wrote the play "Romeo and Juliet"?': 'William Shakespeare',
            'What is the largest ocean on Earth?': 'Pacific'
        }

    def ask_question(self, question):
        user_answer = input(question + ' ')
        correct_answer = self.questions[question]
        if user_answer == correct_answer:
            print('Correct answer!')
            self.point += 1
            print('Points:', self.point)
        else:
            print('Wrong answer!')
            print('Points:', max(0, self.point - 1))  # Don't let the user go below 0 points

if __name__ == "__main__":
    quiz = Quiz()

    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")
    print("---------------------------------")

    for question in quiz.questions:
        quiz.ask_question(question)

    print("---------------------------------")
    # Display congratulatory or try again message based on the score
    if quiz.point > 3:
        print('Congratulations! You scored', quiz.point, 'points. Well done!')
    else:
        print('Your final score is', quiz.point, '. Good effort!')

