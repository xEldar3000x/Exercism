def encode(plain_text):
    
    plain_text = plain_text.replace(" ", "")
    
    encoded_text = ""

    for char in plain_text:

        if char.isalpha():

            char = char.lower()
            
            encoded_text += (chr(122 - ord(char) + 97))
            
        if char.isnumeric():
            
            encoded_text += char

        continue 

    return " ".join(encoded_text[i:i+5] for i in range(0, len(encoded_text), 5))


def decode(ciphered_text):

    decoded_text = ""

    ciphered_text = ciphered_text.replace(" ", "")

    for char in ciphered_text:

        if char.isalpha():

            decoded_text += (chr(122 - ord(char) + 97))

        else:
            
            decoded_text += char

    return decoded_text
            

        
            
