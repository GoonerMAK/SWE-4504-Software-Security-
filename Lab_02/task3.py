import sys
import re

class MoreThanFiveCharacter(Exception):
    pass

class MoreThanTwentyCharacter(Exception):
    pass

class EmptyStringError(Exception):
    pass

try:
    if len(sys.argv) != 3:
        raise ValueError(f"{sys.argv[0]}: Incorrect number of arguments")

    substring = sys.argv[1]
    output_filename = sys.argv[2]

    if len(substring) > 5:
        raise MoreThanFiveCharacter(f"{sys.argv[0]}: The First argument: Input string is more than 5 characters")

    elif not substring or not re.match(r'^[a-zA-Z0-9~`!@#$%^&*()?;\'":\[\]{}\\|<>,./?_-]*$', substring):
        raise EmptyStringError(f"{sys.argv[0]}: The First argument: Input string is not valid")

    elif len(output_filename) > 20 or not re.match(r'^[a-zA-Z0-9~`!@#$%^&*()?;\'":\[\]{}\\|<>,.?_-]*$', output_filename):
        raise MoreThanTwentyCharacter(f"{sys.argv[0]}: The Second argument: Filename must have a valid name with at most 20 characters")

except ValueError as e:
    print(e)
    sys.exit(1)
except MoreThanFiveCharacter as e:
    print(e)
    sys.exit(1)
except MoreThanTwentyCharacter as e:
    print(e)
    sys.exit(1)
except EmptyStringError as e:
    print(e)
    sys.exit(1)
except Exception as e:
    print(f"{sys.argv[0]}: An unexpected error occurred: {e}")
    sys.exit(1)

matching_passwords = []

with open('top-100k-password-list.txt', 'r') as file:
    for line in file:
        password = line.strip()
        if password.endswith(substring):
            matching_passwords.append(password)

if matching_passwords:
    with open(output_filename, 'w') as output_file:
        for password in matching_passwords:
                output_file.write(password + '\n')
else:
    print("No password ends with the provided substring")
