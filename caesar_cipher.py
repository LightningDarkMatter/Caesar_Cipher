#A caesar cipher is a type of substitution cipher that uses a Caesar cipher to encrypt plaintext.
#The Caesar cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet
#so that the resulting alphabet is shifted by a fixed number of positions.
#For example, if the alphabet is rotated by 3, a becomes d, b becomes e, and so on.
#The Caesar cipher can be implemented using the following algorithm:
#
#1. Take each character in the input and encrypt it using the Caesar cipher.
#2. Concatenate the resulting characters into a single string.
#3. Print the string.

#!/usr/bin/env python3
# Path: caesar_cipher.py

alphabet = "abcdefghijklmnopqrstuvwxyz"

should_continue = True

while should_continue:

    direction = input("type 'e' to encrypt or 'd' to decrypt: \n")
    text = input("Enter a message: \n").lower()
    shift = int(input("Enter a shift value: \n"))

    def caesar_cipher(text, shift):
        new_text = ""
        for char in text:
            if char in alphabet:
                new_text += alphabet[(alphabet.find(char) + shift) % 26]
            else:
                new_text += char
        return new_text



    if direction == "e":
        print(caesar_cipher(text, shift))
    elif direction == "d":
        print(caesar_cipher(text, -shift))
    else:
        print("Invalid input")
    result= input("Continue? (y/n) \n")
    if result == "n":
        should_continue = False
        print("Goodbye")