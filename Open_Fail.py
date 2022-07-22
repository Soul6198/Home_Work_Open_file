from pprint import pprint

file_name = "receipes.txt"
file_name_1 = '3.txt'

def file_read(file_name):
    with open(file_name) as file:
        book = {}
        for line in file:
            name = line.strip()
            ingridients = []
            for item in range(int(file.readline())):
                d_ingr = {}
                n1, n2, n3 = file.readline().split("|")
                d_ingr['ingredient_name'] = n1.strip(' ')
                d_ingr['quantity'] = n2.strip(' ')
                d_ingr['measure'] = n3.strip(' \n')
                ingridients.append(d_ingr)
            book[name] = ingridients
            file.readline()
    return book
pprint(file_read(file_name))
print()

print('2 задание')
def get_shop_list_by_dishes(dishes, pers_c):
    dishes = ['Запеченный картофель', 'Омлет']
    pers_c = 2
    recipes_dict = {}
    for items in dishes:
        for keys, values in file_read(file_name).items():
            if keys == items:
                for elements in values:
                  elements['quantity'] = float(elements['quantity']) * pers_c   
    return pprint(get_shop_list_by_dishes(dishes, pers_c))
print()

print('Задание 3')
