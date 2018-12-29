def checker(check_index):
    if check_index < 7:
        print("too low")
        return False
    elif check_index > 7:
        print("oops")
        return False
    else:
        print("found it!")
        return True

gues_me = 7
start = 0
#
# while(True):
#     needBreak = checker(check_index = start)
#     start+=1
#     if needBreak:
#         break

def good():
    return ('Henry', 'Ron', 'Hermione')

generator = (number for number in range(10) if number %2 == 0)
# print(generator)
# for number in range(3):
#     list_ = list(generator)
#     print(list_)

def decorator(func):
    def new_func(*args):
        print("Args",*args)
        result = func(*args)
        print("Result", result)
        return result
    return new_func

def rude_decorator(func):
    def new_func(*args):
        result = func(*args)
        print("Take it", result)
        return result
    return new_func


def add_int(first, second):
    return first + second

# print(add_int(1, 2))
# decorated_add_ints = decorator(add_int)
# decorated_add_ints(3, 4)


@decorator
@rude_decorator
def multiply(first, second):
    return first * second

# multiply(2, 3)

class CustomException(Exception):
    pass

# try:
#     raise CustomException()
# except CustomException as ecx:
#     print("got it", CustomException, ecx)

titles = ['Creatur of Habit', 'Crewel Fate']
plots =['Anun turns into a monster','A haunted yarn shop']

result = zip(titles, plots)
print(result)
print(set(result))