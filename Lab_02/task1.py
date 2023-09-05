with open('top-100k-password-list.txt', 'r') as file:
    passwords = []

    for line in file:
        password = line.strip()
        if password.startswith('pass'):
            passwords.append(password)

output_filename = 'passwords_for_dummies.txt'
with open(output_filename, 'w') as output_file:
    if passwords:
        for password in passwords:
            output_file.write(password + '\n')
    else:
        output_file.write("No password starts with 'pass'\n")
