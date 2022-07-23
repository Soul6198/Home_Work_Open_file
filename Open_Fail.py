from pprint import pprint
import os


with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ingredient_list = []
        for item in range(int(file.readline())):
            ingredient_dict = {}
            name, quantity, measure = file.readline().split(" |")
            ingredient_dict['ingredient_name'] = name.strip(' \n')
            ingredient_dict['quantity'] = int(quantity.strip(' \n'))
            ingredient_dict['measure'] = measure.strip(' \n')
            ingredient_list.append(ingredient_dict)
        cook_book[dish] = ingredient_list
        file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    client_list = {}
    for items in dishes:
        for keys, values in cook_book.items():
            if keys in items:
                for value in values:
                    value['quantity'] *= person_count
                    client_list[value.pop('ingredient_name')] = value
    return client_list

list_of_files = ['1.txt', '2.txt', '3.txt']


def documents_reader(list_of_files) -> dict:
  content = {}
  name_f = {}
  for values in list_of_files:
    with open(values) as file:
      list_of_sting = []
      for line in file:
        list_of_sting.append(line.strip())
    name_f[len(list_of_sting)] = values
    content[len(list_of_sting)] = list_of_sting
  return [content, name_f]

new_file = '123.txt'
list_d = documents_reader(list_of_files)

def documents_writer(new_file, list_d):
    sort_content = {}
    content = list_d[0]
    name_f = list_d[1]
    with open(new_file, "w+") as file:
        sorted_keys = sorted(content, key=content.get)
        sorted_keys.reverse()
        for values in sorted_keys:
            sort_content[values] = content[values]
        for keys, items in sort_content.items():
            for key_name, value_name in name_f.items():
                if key_name == keys:
                    file.write(f'Название файла: {value_name} \n')
            file.write(f'Количество строк: {str(keys)} \n')
            for sttri in items:
                file.write(f'{sttri} \n')
            file.write('\n')
print(documents_writer(new_file, list_d))



pprint(cook_book)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))