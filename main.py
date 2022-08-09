alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt (text_plain, shift_amount):
  encoded_word = ""
  for letter in text_plain:
    if letter == " ":
      encoded_word += letter
    else:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position > 25:
        new_position = new_position - 26
      new_letter = alphabet[new_position]
      encoded_word += new_letter
  print(f"Your encoded text is: {encoded_word}")

def decrypt (text_plain, shift_amount):
  encoded_word = ""
  for letter in text_plain:
    if letter == " ":
      encoded_word += letter
    else:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      if new_position < -26:
        new_position = new_position + 26
      new_letter = alphabet[new_position]
      encoded_word += new_letter
  print(f"Your decoded text is: {encoded_word}")

if direction == "encode":
  encrypt(text, shift)
elif direction == "decode":
  decrypt(text, shift)
