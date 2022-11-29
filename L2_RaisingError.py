# def get_rainbow_color(color_number):
#     '''
#
#     :param color_number: Color number must be integer type and must be in range of integer from 1 to 7
#     :return: str
#     '''
#
#     if type(color_number) is not int:   # create a custom TypeError
#         raise TypeError('Color number must be integer type')
#
#     color_number_list = [i for i in range(1, 8)]  # create a custom ValueError
#     if color_number not in color_number_list:
#         raise ValueError('Color number must to be in range of integer from 1 to 7')
#
#     color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
#     return color_list[color_number - 1]
#
#
# color = get_rainbow_color(7)
# print(color)


def colorize_text(color_number, text):
    '''

    :param color_number: color_number must be integer type and must be in range of integer from 1 to 7
    :param text: text must be string type

    :return: str
    '''

    if type(color_number) is not int:  # create a custom TypeError
        raise TypeError('Parameter color number must be integer type')

    color_number_list = [i for i in range(1, 8)]  # create a custom ValueError
    if color_number not in color_number_list:
        raise ValueError('Color number must to be in range of integer from 1 to 7')

    if type(text) is not str:  # create a custom TypeError
        raise TypeError('Parameter text must be string type')

    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    print(f'{text} is {color_list[color_number - 1]}')


color = colorize_text(5, 'Vlad')
