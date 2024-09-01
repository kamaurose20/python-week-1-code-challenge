def decorator_func(func):
    def wrapper():
        print("Decorator Applied")
        func()
    return wrapper

def apply_decorator(func):
    return decorator_func(func)


def greet():
    print("Hello, World!")

decorated_greet = apply_decorator(greet)
decorated_greet()
