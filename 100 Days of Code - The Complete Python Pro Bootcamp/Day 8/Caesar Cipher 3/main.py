# TODO-1: Import and print the logo from art.py when the program starts.
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(art.logo)


# TODO-2: What happens if the user enters a number/symbol/space?


def caesar():

    while True:
        output_text = ''
        direction = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'exit' to stop: \n").lower()
        if direction == 'exit':
            print('Goodbye')
            break
        original_text = input("Enter the text: \n").lower()
        shift_amount = int(input("Enter the shift amount: \n"))
        if direction not in ['encode', 'decode']:
            print("invalid entry. Please enter 'encode' or 'decode'.")
            continue
        if direction == "decode":
            shift_amount *= -1
        for character in original_text:
            if character not in alphabet:
                output_text += character
                continue
            shifted_position = alphabet.index(character) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        print(f"Here is the {direction}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?


caesar()



