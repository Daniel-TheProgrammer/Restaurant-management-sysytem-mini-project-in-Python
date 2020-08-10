# Created by Daniel the programmer

List = [1, 5, 7, 87, 9, 0]
List_without_dupls = set(List)
if len(List) == len(List_without_dupls):
    print('No duplicates!')
else:
    print('There are duplicates')

my_list = [1, 2, 3, 4, 1, 2, 4, 2]
my_list_set = set(my_list)
dupls_count = len(my_list) - len(my_list_set)
print('List has', dupls_count, 'duplicates!')