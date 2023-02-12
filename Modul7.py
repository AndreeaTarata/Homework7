try:

    my_list = [1, 2, 3]
    print(my_list[3])
except IndexError:
    print('Index out of range')
finally:
    print('Astazi suntem in februarie')


try:
    print(x)
except NameError:
    print('X is not defined')