# Problem 4
# Sang Park

def max_of_three(a, b, c):
    if a > b and a > c:
        print(f"The largest number is {a}")
    elif b > a and b > c:
        print(f"The largest number is {b}")
    else:
        print(f"The largest number is {c}")

max_of_three(20,20,20)
max_of_three(10,30,20)
max_of_three(20,10,30)
max_of_three(10,10,10)
max_of_three(30,10,20)
