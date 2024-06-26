alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("type 'encode' to encrypt, and 'decode' to decrypt:\n")

text = input("type your message: \n").lower()
shift = int(input("type the shift number:\n"))

def caeser(text, shift, direction):
    end_text = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "decode":
            shift *= -1
        new_position = position + shift
        end_text += alphabet[new_position]
    print(f"The {direction} text  is {end_text}")        
    def encrypt(plain_text, shift_num):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_postition = position + shift_num
            new_letter = alphabet[new_postition]
            cipher_text += new_letter
        print(f"The encoded text is {cipher_text}")
    def decrypt(cipher_text, shift_num):
        decipher_text = ""
        for letter in cipher_text:
            position = alphabet.index(letter)
            new_position = position - shift_num
            new_letter = alphabet[new_position]
            decipher_text += new_letter
        print(f"The decoded text is {decipher_text}")

if direction == "encode":
    encrypt(plain_text = text, shift_num = shift)
elif direction == "decode":
    
    decrypt(cipher_text = text, shift_num = shift)    
else:
    print("You typed a wrong option")    