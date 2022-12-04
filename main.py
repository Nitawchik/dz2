with open('data.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        ing_count = int(file.readline().strip())
        ingredient_list = []
        for _ in range(ing_count):
            nqm = file.readline().strip().split(' | ')
            name, quantity, measure = nqm
            ingredient_list.append({'ing': name, 'quantity': quantity, 'measure': measure})

        file.readline()
        cook_book[dish] = ', '.join(repr(e) for e in ingredient_list)

print(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    incode()
    cook_book_persone = {}
    lst = list()
    for dish in dishes:
        lst += cook_book.get(dish)

    new_dict = {}
    for old_dict in lst:
        key = old_dict.pop('ingredient_name')
        if key not in new_dict.keys():
            new_dict[key] = old_dict
        else:
            new_dict[key]: old_dict['quantity']

    for key, value in new_dict.items():
        print(f"{key}: {int(value['quantity']) * person_count} {value['measure']}")


print(dish)





