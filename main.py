
from src.people import People
from src.teacher import Teacher


def print_hi(name):
    print(f'Hi, {name}')


def pop(items):
    items.pop()


if __name__ == '__main__':

    # start up
    print_hi('PyCharm'.title())
    # chapter2
    space_line = "I\'m learning Python."
    print(2 ** 10)
    print(0.2 + 0.1)
    # chapter3
    bicycle = ['bike1', 'bike2', 'bike3']
    bicycle.insert(0, 'bike0')
    del bicycle[0]
    popped_bicycle = bicycle.pop()
    print(popped_bicycle)
    print(bicycle)
    print(len(bicycle))
    bicycle.sort(reverse=True)
    print(bicycle)
    # chapter4
    for item in bicycle:
        print(item)
    my_list = list(range(1, 10, 2))
    print(my_list)
    [print(value) for value in range(1, 10)]

    # chapter6 dictionary
    dictionary = {
        'username': 'lollipop',
        'password': '10010'
    }
    for key, value in dictionary.items():
        print('Key: ' + key + " value: " + value)

    animal = ['cat', 'cat']
    while 'cat' in animal:
        print('flag')
        animal.remove('cat')

    origin_list = ['1', '2']
    now_list = origin_list
    origin_list = ['0']
    print(now_list)

    people = People('lollipop', 'man')
    people.say()

    teacher = Teacher('Mike', 'women')
    teacher.say()
    teacher.teach()

