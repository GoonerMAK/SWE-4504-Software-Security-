import sys

class MoreThanFiveCharacter(Exception):
    pass

class EmptyStringError(Exception):
    pass

try:
    substring = input("Enter a string of maximum 5 characters: ")

    if len(substring) > 5:
        raise MoreThanFiveCharacter("The input string is more than 5 characters")
    elif not substring:
        raise EmptyStringError("The input string is empty")

except MoreThanFiveCharacter as e:
    print(e)
    sys.exit(1)
except EmptyStringError as e:
    print(e)
    sys.exit(1)

count=0

with open('top-100k-password-list.txt', 'r') as file:
    for line in file:
        password = line.strip()
        if substring in password:
            count+=1

if count==0:
    print("No password contains", substring)
else:
    print("The Count: ", count)

