class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in:
            function(args[0])  # Call the function if logged in
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    if len(user.name) == 5:
        print(f"This is {user.name}'s new blog post.")
    else:
        print(f"{user.name} cannot create a blog post because the name length is not 5.")

# Create users by taking input
user1_name = input("Enter name for User 1: ")
user2_name = input("Enter name for User 2: ")

user1 = User(user1_name)
user2 = User(user2_name)

# Setting login status
user1.is_logged_in = True  # User 1 is logged in
user2.is_logged_in = False  # User 2 is not logged in

# Try to create blog posts for both users
create_blog_post(user1)  # Should print blog post if name length is 5
create_blog_post(user2)  # Should not print anything as user2 is not logged in
