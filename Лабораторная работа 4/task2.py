def get_count_char(str_): #функция считающая количество символов
    letters_dict = {}
    for letters in str_:
        if letters.isalpha() and letters not in letters_dict:
            letters_dict[letters] = 1
        elif letters.isalpha() and letters in letters_dict:
            letters_dict[letters] += 1
    return letters_dict


def get_count_percent_char(dict_): #функция считающая количество символов в процентном отношении к общему числу символов
    length = sum(dict_.values())
    for letters in dict_:
        dict_[letters] = ((dict_[letters] / length) * 100)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
#LENGTH = len(main_str)
print(get_count_char(main_str.lower())) #результат первой функции
print(get_count_percent_char(get_count_char(main_str.lower()))) #результат второй функции
print(sum(get_count_percent_char(get_count_char(main_str.lower())).values())) #проверка, что в сумме получается 100 процентов (в действительности там почти 100 процентов, видимо влияет машинная точность)
