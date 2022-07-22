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