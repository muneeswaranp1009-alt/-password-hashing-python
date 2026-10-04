# Password Hashing

A simple python program demonstrating the working of password hashing using the python library hashlib.

## Features

- Password hashing using the SHA256 algorithm

- Conversion of password to hash

- Comparison of given password hash and stored hash

- Displaying the access status

- Demonstrating the basic concepts of hashing

## Technologies Used

- Python

- Hashlib

## Project Description

The program takes a password as input and then hashes it using the SHA256 algorithm in order to grant access.

The program performs the following steps:

1. Takes a desired password as input.

2. Converts the password into a hashed value.

3. Takes the user password as input.

4. The user password is also converted into a hashed value.

5. The two hashed values are compared.

6. The user is granted or denied access depending on whether the passwords match or not.

The program uses the hashlib.sha256() function to hash the passwords.

### Example Output

Welcome to Hashing

Enter Password: Munish

The Hashed Password is: f7df59e804478e88c7b465c2f8f745c1d764b6a3f7f0d5e7e5b9a4f5e7c4e8c5

Access Granted!

For wrong password:

Welcome to Hashing

Enter Password: WrongPassword

The Hashed Password is: 95584749e0e12c23187d4c84f05d486c39d5c6f2e1e5a7d1d9c8e7c5d3a9c5d9

Wrong Password!

## Practices Used

- Python Functions

- Taking user input

- Encoding a string

- Using the SHA256 hashing algorithm

- Using the hashlib library

- Using conditional statements

- Comparing the passwords and giving access

## How to Use

1. Install the Python Interpreter on your computer

2. Save the file in your computer as Hashing.py

3. Run the program using this command:

python Hashing.py

4. Enter the password when prompted

## Project Structure

password-hashing-python/

├── Hashing.py

└── README.md

## Why build it?

The project was built as a python user to develop an understanding of the concept of hashing by implementing the basic working of password verification using hashing.

## Future Scope

- Building the program further to include more users

- Adding functionalities such as log in, log out

- Storing the information of the users using a database

- Enhancing the security of the program

- Adding a sign-up function

## Author

This project was created as a python learning project.
