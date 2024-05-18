# работа со списками
my_list=['Kiwi','Plum','Orange','Grape','Lemon','Lime','Papaya']
print(my_list)
print('Первый элемент: '+my_list[0])
print('Последний элемент: '+my_list[-1])
print(my_list[3:6])
my_list[3]='Banana'
print(my_list)
# работа со словарями
my_dict={'Kiwi':'Киви','Plum':'Слива','Orange':'Апельсин','Grape':'Виногдар'}
print(my_dict)
print('Translation: '+my_dict.get('Kiwi'))
my_dict['Kiwi']='неКИВИ'
print(my_dict)
my_dict.update({'Peach': 'Персик',
                'Mango':'Манго'})
print(my_dict)