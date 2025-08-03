questions = {
    'Какой атомный номер  имеет водород': '1' ,
     'Сколько электронов в водороде': '1'
}


score = 0


for q, a in questions.items():
    user_answer = input(q + '')
    if user_answer.lower() == a.lower():
        print('Правильно')
    else:
        print('Неверно')
print(f'Ваш результат : {score} из {len(questions)}')