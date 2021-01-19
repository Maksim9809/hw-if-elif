cities = ['Москва', 'Париж', 'Лондон']

users = [{'name': 'Иван', 'age': 35},
         {'name': 'Мария', 'age': 22},
         {'name': 'Соня', 'age': 20}]

tourists = [{'user': users[0], 'city': cities[2]},
            {'user': users[1], 'city': cities[0]},
            {'user': users[2], 'city': cities[1]}]

city = input('Введите город: ')
cities_reg = city.capitalize()





if cities_reg not in cities:
    print('Здесь пока нет туристов')
elif cities_reg in tourists[0]['city']:
    name = tourists[0]['user']['name']
    his_age = tourists[0]['user']['age']
    
    print(f'Турист {name} возраст {his_age} посетил город {cities_reg}')
elif cities_reg in tourists[1]['city']:
    name = tourists[1]['user']['name']
    his_age = tourists[1]['user']['age']
    
    print(f'Турист {name} возраст {his_age} посетил город {cities_reg}')
elif cities_reg in tourists[2]['city']:
    name = tourists[2]['user']['name']
    his_age = tourists[2]['user']['age']
    
    print(f'Турист {name} возраст {his_age} посетил город {cities_reg}')

else:
    print('В этом городе пока не было туристов)')