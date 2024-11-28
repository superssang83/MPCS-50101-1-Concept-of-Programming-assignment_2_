# from fahrenhit to celsius formua - https://www.cuemath.com/fahrenheit-to-celsius-formula/
# Problem 1
# Sang Park

def fahrenhit_to_celsius(fahrenhit):
    if (fahrenhit >= 32):
        celsius = 5/9 * (fahrenhit - 32)
        return round(celsius,2)
    else: 
        print("fahrenhit should be more than or equal to 32")


fahrenhit = (input("Enter a temperature in Fahrenheit: "))

if fahrenhit.isdigit():
    print(fahrenhit_to_celsius(int(fahrenhit)))

else:
    print("Please enter a positive, whole number numeric temperature.")

    




