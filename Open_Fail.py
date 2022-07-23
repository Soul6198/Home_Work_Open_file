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

def strings_counting(file:str) -> int:
    with open(file, 'r', encoding="UTF-8") as f:
        return sum(1 for _ in f)

def rewriting(file_for_writing: str, base_path, location):
    files = []
    for i in list(os.listdir(os.path.join(base_path, location))):
        arr = [strings_counting(os.path.join(base_path, location, i)), os.path.join(base_path, location, i), i]
        files.append(arr)
    for file_from_list in sorted(files):
        opening_files = open(file_for_writing, 'a', encoding="UTF-8")
        opening_files.write(f'{file_from_list[2]}\n')
        opening_files.write(f'{file_from_list[0]}\n')
        with open(file_from_list[1], 'r', encoding="UTF-8") as file:
            counting = 1
            for line in file:
                opening_files.write(f'line in № {counting} in file {file_from_list[2]} : {line}')
                counting += 1
        opening_files.write(f'\n')
        opening_files.close()


pprint(cook_book)
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 3))
open("123.txt", "w", encoding="UTF-8")
file_for_writing = os.path.abspath('123.txt')
base_path = os.getcwd()
location = os.path.abspath('txts_for_Opening and reading a file, writing to a file')
rewriting(file_for_writing, base_path, location)