#immutable_var = 1,2,3.0, True, 'text'
#print (immutable_var)
# immutable_var[2] = 3
# print(immutable_var)
# результат: TypeError: 'tuple' object does not support item assignment

mutable_list = [1,3,5,7.0,True,'text']
print(mutable_list)
mutable_list[3] = 7
print(mutable_list)