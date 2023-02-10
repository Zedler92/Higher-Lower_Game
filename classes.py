# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def is_authenthicated_decorator(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_logged_in:
#             function(args[0])
#     return wrapper
#
# @is_authenthicated_decorator
# def create_blog_post(user):
#     print(f"This is {user.name}'s new blog post")
#
# new_user = User("Łukasz")
# new_user.is_logged_in = True
# create_blog_post(new_user)


def logging_decorator(function):
    def wrapper(*args, **kwargs):
        function(*args, **kwargs)
        print(f"You called function {function.__name__}")

        print(f"The arguments are {args}")
        print(f"The output is {function(*args, **kwargs)}")
        function(*args, **kwargs)
    return wrapper

@logging_decorator
def multiplier(num1, num2, num3):
    return num1 * num2 / num3

multiplier(1, 2, 3)




