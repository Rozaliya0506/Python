def int_func(text_user):
    word = text_user[0].upper() + text_user[1:]
    return word

user_input_word = input("Enter word:")
result = int_func(user_input_word)
print(result)

user_input_sentence = input("Enter sentence:")
for words in user_input_sentence.split(' '):
   print(f'{int_func(words)} ')













