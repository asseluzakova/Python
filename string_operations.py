def count_vowels(str):
    vowels='аеиоуыэюяАЕИОУЫЭЮЯ'
    counter=0
    for i in range(len(str)):
        if str[i] in vowels:
            counter+=1
    return counter

def reverse_string(str):
    return str[::-1]

def is_palindrome(str):s
    if str!=reverse_string(str): #str!=str[::-1]
        return "не равно"
    else:
        return 'равно'

def capitalize_string(text):
    splitted_text = text.split()
    cap_text = [word.capitalize() for word in splitted_text]
    return ' '.join(cap_text)