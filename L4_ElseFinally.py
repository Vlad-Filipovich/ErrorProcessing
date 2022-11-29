# If we have an error - except block fires and else block doesn't fire
# If we haven't an error - else block fires and except block doesn't fire
# Finally block fires anyway


while True:
    try:
        number = int(input('Enter some number: '))
        print()
        print(f'Result: {number / 2}')
        print()
    except ValueError:
        print('You have to enter a number')
    else:
        print('Good job! This is a number')
        break
    finally:
        print('Finally block')

print('See you!')

# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError as e:
#         print('You can\' divide by zero')
#         print(e)
#     except TypeError as e:
#         print('x and y must be numbers')
#         print(e)
#
#
# print(divide(4, 2))
