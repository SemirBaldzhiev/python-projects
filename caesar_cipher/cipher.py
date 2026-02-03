from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(logo)


def caesar_cipher(original_text, shift_num, option):
    
    output_text = ""
    
    if option == "d":
        shift_num *= -1  
    
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_pos = alphabet.index(letter) + shift_num
            shifted_pos %= len(alphabet)
            output_text += alphabet[shifted_pos]
    
    return output_text


while True:
    user_input_text = input("Please enter text for encoding/decoding: ").lower()
    user_choice = input("Please enter e (for encoding) or d (for decoding): ").lower()
    shift = int(input("Please enter a shift amount (a whole number): "))

    if user_choice != "e" or user_choice != "d":
        pass

    output = caesar_cipher(user_input_text, shift, user_choice)
    
    if user_choice == "e":
        print(f"Encoded text is: {output}")
    elif user_choice == "d":
        print(f"Decoded text is: {output}")
    
    next = input("Type yes if you want to go again. Otherwise type no: ").lower()
    
    if next == "yes":
        continue
    else:
        break
    
        