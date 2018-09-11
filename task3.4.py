

dictionary_talk = {"Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Привет!" : "Привет!"}

def ask_user(dictionary_talk):
    while True:
        question = input(' ')
        q = dictionary_talk.get(question)
        print(q)
         
        

ask_user(dictionary_talk)





