# Problem 6
# Sang Park

word = input("Enter a word or phrase: ")
word_combine_one = word.replace(" ", "")

if word_combine_one == word_combine_one[::-1]:
    print("This is a palindrome.")

else:
    print("This is not a palindrome.")



