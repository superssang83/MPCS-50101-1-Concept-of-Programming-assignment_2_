# Problem 5
# Sang Park

def is_divisible_by_11(number):
    if not isinstance(number, int):
        print("Invalid input. Please enter a valid integer.")
    
    num_str = str(abs(number))
    alternating_sum = 0
    
    for i, digit in enumerate(num_str):
        if i % 2 == 0:
            alternating_sum += int(digit)
        else:
            alternating_sum -= int(digit)

    if alternating_sum % 11 == 0:
        print(f"{number} is divisible by 11.")
    else:
        print(f"{number} is not divisible by 11.")

number = int(input("Enter a number: "))
is_divisible_by_11(number)

