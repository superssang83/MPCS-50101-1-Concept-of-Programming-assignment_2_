# Problem 3
# Sang Park

password = input("Enter a password: ")

characters = ["!", "@", "#", "$", "%"]
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"

# specials = False
# upper = False
# lower = False
# number = False

for c in characters:
    if c in password:
        specials = True

for u in uppercase:
    if u in password:
        upper = True

for l in lowercase:
    if l in password:
        lower = True

for n in numbers:
    if n in password:
        number = True

if len(password) >= 12 and specials and upper and lower and number:
    print("This is a strong password :)")
else:
    print("This is not a strong password :(")
