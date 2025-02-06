

class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in=False

def is_authenticated_decorator(function):
    def wrapper(*args,**kwargs):
        if user.is_logged_in==True:
            function()
    return wrapper

@is_authenticated_decorator # decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")

new_user =User("Fazila")
create_blog_post(new_user)