# Caesar Cipher Encoder/Decoder
def caesar_cipher(text, shift, encode=True):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = ord(char) - base
            if encode:
                new_offset = (offset + shift) % 26
            else:
                new_offset = (offset - shift) % 26
            result += chr(base + new_offset)
        else:
            result += char
    return result

if __name__ == "__main__":
    mode = input("Encode or Decode (e/d): ").lower()
    text = input("Enter text: ")
    shift = int(input("Enter shift: "))
    if mode == 'e':
        print("Encoded:", caesar_cipher(text, shift, True))
    else:
        print("Decoded:", caesar_cipher(text, shift, False))
