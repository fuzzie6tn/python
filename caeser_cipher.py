alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("type 'encode' to encrypt, and 'decode' to decrypt:\n")
text = input("type your message: \n").lower()
shift = int(input("type the shift number:\n"))

def encrypt(plain_text, shift_num):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_postition = position + shift_num
        new_letter = alphabet[new_postition]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text = text, shift_num = shift)
