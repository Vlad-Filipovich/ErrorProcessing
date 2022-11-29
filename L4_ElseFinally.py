# If we have an error - except block fires and else block doesn't fire
# If we haven't an error - else block fires and except block doesn't fire
# Finally block fires anyway


while True:
    try:
        number = int(input('Enter some number: '))
        print()
        print(f'Result: {number / 2}')
        print()
    except:
        print('You have to enter a number')
    else:
        print('Good job! This is a number')
        break
    finally:
        print('Finally block')

print('See you!')
