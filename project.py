class Quiz:
    def __init__(self):
        self.point = 0

    def ask_question(self, question, correct_answer):
        user_answer = input(question)
        if user_answer == correct_answer:
            print('Correct answer')
            self.point += 1
            print('Points:', self.point)
        else:
            print('Wrong answer')
            self.point -= 1
            print('Points:', self.point)

if __name__ == "__main__":
    quiz = Quiz()

    quiz.ask_question('What is the capital of France?', 'Paris')
    quiz.ask_question('When did World War II end?', '1945')
    quiz.ask_question('Which is the largest country in the world?', 'Russia')
    quiz.ask_question('In which country would you find the Leaning Tower of Pisa?', 'Italy')
    quiz.ask_question('What is the currency of Japan?', 'Yen')
    quiz.ask_question('Who wrote the play "Romeo and Juliet"?', 'William Shakespeare')
    quiz.ask_question('What is the largest ocean on Earth?', 'Pacific')

    if quiz.point > 0:
        print('Congratulations! You scored', quiz.point, 'points. Well done!')
    elif quiz.point <= 0:
        print('Try again. Your score is', quiz.point, '. Better luck next time!')
    else:
        print('Your final score is', quiz.point, '. Good effort!')
