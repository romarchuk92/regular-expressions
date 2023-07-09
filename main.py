from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
with open("phonebook_raw.csv", "r", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  new_list = []


## 1. Выполните пункты 1-3 задания.
## Ваш код

def name_sort():

  name_pattern = r'([А-Я])'
  name_sub = r' \1'
  for persons in contacts_list[1:]:
    persons_all = persons[0] + persons[1] + persons[2]
    if len((re.sub(name_pattern, name_sub, persons_all).split())) == 3:
      persons[0] = re.sub(name_pattern, name_sub, persons_all).split()[0]
      persons[1] = re.sub(name_pattern, name_sub, persons_all).split()[1]
      persons[2] = re.sub(name_pattern, name_sub, persons_all).split()[2]
      # res = ((re.sub(name_pattern, name_sub, persons_all).split()))
    elif len((re.sub(name_pattern, name_sub, persons_all).split())) == 2:
      persons[0] = re.sub(name_pattern, name_sub, persons_all).split()[0]
      persons[1] = re.sub(name_pattern, name_sub, persons_all).split()[1]
      persons[2] = ''
    elif len((re.sub(name_pattern, name_sub, persons_all).split())) == 1:
      persons[0] = re.sub(name_pattern, name_sub, persons_all).split()[0]
      persons[1] = ''
      persons[2] = ''
  return



def correct_phones():
  pattern = re.compile(r"(\+7|8).*?(\d{3}).*?(\d{3}).*?(\d{2}).*?(\d{2}).*?(\s)?\(?(доб.?)?\s?(\d{4})?\)?") 
  for phones in contacts_list:
    phones[5] = pattern.sub(r'+7(\2)\3-\4-\5\6\7\8', phones[5])  
  return



def duplicates_combining():
  for persons in contacts_list[1:]:
    first_name = persons[0]
    last_name = persons[1]
    for contact in contacts_list:
      new_first_name = contact[0]
      new_last_name = contact[1]
      if first_name == new_first_name and last_name == new_last_name:
        if persons[2] == '':
            persons[2] = contact[2]
        if persons[3] == '':
            persons[3] = contact[3]
        if persons[4] == '':
            persons[4] = contact[4]
        if persons[5] == '':
            persons[5] = contact[5]
        if persons[6] == '':
            persons[6] = contact[6]

  for contact in contacts_list:
    contact_end = contact[0:7]
    if contact_end not in new_list:
      new_list.append(contact)

  return new_list

 
if __name__ == "__main__":
  name_sort()
  correct_phones()
  duplicates_combining()



## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
  with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')

  # ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(new_list)


