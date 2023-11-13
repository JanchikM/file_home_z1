from pprint import pprint


cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    while True:
        key = f.readline().strip()
        ingrid = f.readline()
        if ingrid == '':
            break
        counter = int(ingrid)
        for i in range(0, counter):
            meaning = f.readline().strip().split(' | ')
            value = {}
            value['ingredient_name'] = meaning[0]
            value['quantity'] = meaning[1]
            value['measure'] = meaning[2]
            if key in cook_book:
                cook_book[key].append(value)
            else:
                cook_book[key] = [value]
        f.readline()
#pprint(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    slov = {}
    for i in dishes:
        if i in cook_book:
            for x in cook_book.setdefault(i):
                values = {}
                if x['ingredient_name'] not in slov:
                    values.update([('measure', x['measure']), ('quantity', int(x['quantity']) * person_count)])
                    slov[x['ingredient_name']] = (values)
                else:
                    values.update([('measure', x['measure']), ('quantity', int(x['quantity']) * person_count + int(x['quantity']) * person_count)])
                    slov[x['ingredient_name']] = (values)
    pprint(slov)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
