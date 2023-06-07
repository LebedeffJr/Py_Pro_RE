## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

## 1. Выполните пункты 1-3 задания.
## Ваш код
def name_separation():
    all_l = []
    for row in contacts_list:
        person1 = row.pop(0)
        person2 = row.pop(0)
        name_list1 = person1.split()
        name_list2 = person2.split()
        new_list = name_list1 + name_list2 + row
        all_l.append(new_list)
    return all_l

def format_info():
    f_list = []
    for a in name_separation():
        if len(a) != 7:
            a.remove('')
        f_list.append(a)
    return f_list

desired_format = format_info()

def ph_num_f():
    pattern = r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?'
    repl = r'+7(\2)\3-\4-\5\7\8\9'
    for person in desired_format[1:]:
        person[5] = re.sub(pattern, repl, person[5])
    return desired_format

def remove_duplicates():
    person_dict = {}
    for person in desired_format[1:]:
        key = person[0]
        if key not in person_dict:
            person_dict[key] = person
        else:
            i = 0
            for el in person:
                if el not in person_dict[key]:
                    person_dict[key].insert(i, el)
                i += 1

    final_list = [desired_format[0]]
    for k, w in person_dict.items():
        final_list.append(w)
    return final_list

if __name__ == '__main__':

    ph_num_f()
    contacts_list = remove_duplicates()
## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
    with open("phonebook.csv", "w", encoding='utf8') as f:
        datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
        datawriter.writerows(contacts_list)
