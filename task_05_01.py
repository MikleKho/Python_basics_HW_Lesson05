# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется
#  разделитель пробел.

# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1
# out
# The data is incorrect
import random

def make_text(symbols, number_words):
    list_words = " ".join(["".join(random.sample(symbols, len(symbols))) for i in range(number_words)])
    return list_words

def clean_text (text_in, del_text):
    text_out = text_in.split()
    while del_text in text_out:
        text_out.remove(del_text)
    return " ".join(text_out)

number_words = int(input('Введите количество слов ---> '))
if number_words < 1:
    print('The data is incorrect')
    exit()
text_in = make_text("абв", number_words)
print(f'Исходный текст ---> {text_in}')
del_text = 'абв'
print(f'Текст с удаленным "{del_text}" ---> {clean_text(text_in, del_text)}')