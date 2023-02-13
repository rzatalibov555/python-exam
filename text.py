def test(func):
    def wrapper():
        return func().split()
    return wrapper


def test2(func):
    def wrapper():
        return func().upper()
    return wrapper




@test
@test2


def say_hello():
    return "Hello world"

print(say_hello())