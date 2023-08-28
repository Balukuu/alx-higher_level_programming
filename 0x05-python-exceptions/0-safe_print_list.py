#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        printed_count = 0
        for i in range(x):
            print(my_list[i], end="")
            printed_count += 1
        print()
        return printed_count
    except IndexError:
        print()
        return printed_count

my_list = [1, 2, 3, 4, 5]

nb_print = safe_print_list(my_list, 2)
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))



