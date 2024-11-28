# Problem 2
# Sang Park

grade = input("Enter a score: ")

if not grade.isdigit() or int(grade) > 100:
    print("That is not valid input.")
else: 
    if int(grade) >= 90:
        print("You received an A!")
    elif int(grade) >= 80:
        print("You received an B!")
    elif int(grade) >= 70:
        print("You received an C!")
    elif int(grade) >= 60:
        print("You received an D!")
    elif 0 <= int(grade) < 60:
        print("You received an F!")

    else:
        print("That is not valid input.")
