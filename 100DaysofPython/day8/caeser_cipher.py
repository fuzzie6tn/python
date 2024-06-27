alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("type 'encode' to encrypt, and 'decode' to decrypt:\n")

text = input("type your message: \n").lower()
shift = int(input("type the shift number:\n"))

def caeser(text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        end_text += alphabet[new_position]
    print(f"The {direction} text  is {end_text}")        
caeser(text=text, shift=shift,direction=direction)    