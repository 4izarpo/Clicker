meme_dict = {'ЛОЛ': 'очень смешно',
            'КРИНЖ': 'что-то странное, стыдное',
            'РОФЛ': 'шутка',
            'ЩИЩ': 'одобрение или восторг',
            'КРИПОВЫЙ': 'страшный, пугающий',
            'АГРИТЬСЯ': 'злиться',
            'КД': 'Как дела?',
            'КД': 'Что делаешь?',
    
            }
print('Здраствуйте, наша прогрмаа создана для объяснения старшему поколению импорто замещенные либо сокращенные слова')
while True:
    word = input("Введите непонятное слово (большими буквами!Чтобы написать большими буквами зажмите SHIFT или нажмите CAPS LOCK): ").upper()
    
    
    if word in meme_dict.keys():
        # Что делать, если слово нашлось?
        print(meme_dict.get(word))
    else:
        # Что делать, если слово не нашлось?
        print('Либо наша программа старая, либо вы не правильно ввели слово')
