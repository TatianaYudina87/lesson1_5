immutable_var = 1, 'car', 'a', 'Falce'
print(immutable_var)
# immutable_var[0] = 2       # кортеж не поддерживает обращение по элементам.
mutable_list = (['cat', 'True'], 2, 5)
mutable_list[0][0] = 'dog'
print(mutable_list)