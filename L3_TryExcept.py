# my_list = [1, 2, 3]
# try:
#     print(my_list[3])
#     x = my_list + 3
#     print('hello'[5])
# except IndexError:
#     print('IndexError')
# except TypeError:
#     print('TypeError')


def get_dictionary_values(dict, key):
    try:
        return dict[key]
    except KeyError:
        return None


user_dict = {'first_name': 'Jack', 'last_name': 'White', 'age': 23}
print(get_dictionary_values(user_dict, 'age'))
print(get_dictionary_values(user_dict, 'job'))
