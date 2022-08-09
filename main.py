alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
  encoded_word = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in start_text:
    if letter == " ":
      encoded_word += letter
    else:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      if new_position > 25:
        new_position = new_position - 26
      elif new_position < -26:
        new_position = new_position + 26
      new_letter = alphabet[new_position]
      encoded_word += new_letter
  print(f"Your {cipher_direction} text is: {encoded_word}")



import art
print(art.logo)
game = "yes"
while game == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift % 26
  caesar(text, shift, direction)
  game = input("Do you want to restart the cipher program? Type Yes or No: ").lower()