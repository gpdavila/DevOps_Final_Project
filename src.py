import gplib

try:
    print(gplib.get_user_age())
except ValueError:
    print("That's not a valid value for your age !")
