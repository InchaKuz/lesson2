answers = {
    'Привет!': 'Привет!',
    'как дела': 'Отлично, а у тебя?',
    'Пока': 'Еще увидимся!'
}

def get_answer(question, answers):
    return answers.get(question)



def ask_user(answers):
    while  True:
        try:
            user_input = input('Скажи что-нибуть: ')
            get_answer(user_input, answers)
            print(get_answer(user_input, answers))    
        except EOFError:
            print('Пока!')
        except KeyboardInterrupt:
            print('Пока!')
        break

ask_user(answers) 