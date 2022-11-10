def get_count_char(str_):
    dict_ = {}
    str_ = str_.lower()
    for x in str_:
        if x.isalpha():
            if x in dict_:
                dict_[x] += 1
            else:
                dict_[x] = 1
    return dict_

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))

dict_new = get_count_char(main_str)

def get_symbols(dict_new):
    total_count = sum(dict_new.values())
    last_dict = {}
    for count in dict_new:
        last_dict[count] = round(dict_new[count]/total_count * 100, 2)
    return last_dict

final_str = get_symbols(dict_new)
print(final_str)
