def encrypt_vigenere(plaintext, key):
  ciphertext = ""
  key = key.upper()
  for i in range(len(plaintext)):
    char = plaintext[i]
    if char.isalpha():
      shift = ord(key[i % len(key)]) - 65
      if char.isupper():
        ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
      else:
        ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
    else:
      ciphertext += char
  return ciphertext


def decrypt_vigenere(ciphertext, key):
  plaintext = ""
  key = key.upper()
  for i in range(len(ciphertext)):
    char = ciphertext[i]
    if char.isalpha():
      shift = ord(key[i % len(key)]) - 65
      if char.isupper():
        plaintext += chr((ord(char) - shift - 65) % 26 + 65)
      else:
        plaintext += chr((ord(char) - shift - 97) % 26 + 97)
    else:
      plaintext += char
  return plaintext


a = input('Voce gostaria de C para criptografar ou D para descriptografar: ')

if (a == 'C'):
  x = input('Digite sua mensagem: ')
  y = input('Digite a palavra chave: ')

  plaintext = x
  key = y
  ciphertext = encrypt_vigenere(plaintext, key)
  print(ciphertext)

if (a == 'D'):
  x = input('Digite sua mensagem: ')
  y = input('Digite a palavra chave: ')

  ciphertext = x
  key = y
  plaintext = decrypt_vigenere(ciphertext, key)
  print(plaintext)
