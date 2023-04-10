from pprint import pprint
with open('files.txt', 'rt', encoding='utf-8') as file:
    cook_book = dict()
    for line in file:
        dep_name = line.strip()
        count_ingridients = int(file.readline().strip())
        bludo = []
        for _ in range(count_ingridients):
            ingridient_name, quantity, measure = file.readline().strip().split(' | ')
            bludo.append({
                'ingridient_name': ingridient_name,
                'quantity': int(quantity),
                'measure': measure
            })
        file.readline()
        cook_book[dep_name] = bludo
    def get_shop_list_by_dishes(dishes, person_count):
        dishes_dict = {}
        for c in dishes:
            for c1 in cook_book.keys():
                if c == c1:
                    for q in cook_book[c1]:
                        q['quantity'] *= person_count
                        dishes_dict[q['ingridient_name']] = q
                        del q['ingridient_name']
        pprint(dishes_dict)
        return dishes_dict
    get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)



