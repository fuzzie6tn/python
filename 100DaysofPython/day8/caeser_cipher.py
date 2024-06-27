alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def caeser(start_text, shift_num, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_num *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_num
            end_text += alphabet[new_position]
        else:
            end_text += char    
    print(f"The {cipher_direction} text  is {end_text}")        

from art import logo
print(logo)

should_continue = True
while should_continue:
    direction = input("type 'encode' to encrypt, and 'decode' to decrypt:\n")
    text = input("type your message: \n").lower()
    shift = int(input("type the shift number:\n"))
    shift = shift % 26
    caeser(start_text = text, shift_num = shift,cipher_direction = direction)     
    result = input("type 'y' to continue or 'n' to exit\n")
    if result == 'n':
        should_continue = False
        print("good bye\n")